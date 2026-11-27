"""Conserve native Joules power while exporting the requested four groups."""
import csv,json,math,re
from pathlib import Path
NUMBER=r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'
GROUPS={'register':'sequential','latch':'sequential','logic':'logic','clock_seq':'clock_sequential','clock_comb':'clock_combinational'}
CATEGORIES=('sequential','logic','clock_sequential','clock_combinational')
MECHANISMS=('switching','internal','leakage','total')
def native_rows(path,order=MECHANISMS):
 text=Path(path).read_text()
 if not re.search(r'Power Unit:\s*uW\b',text):raise ValueError('Detailed power must be in uW: '+str(path))
 entries={};pattern=r'^\s*(\w+)\s+('+NUMBER+r')\s+('+NUMBER+r')\s+('+NUMBER+r')\s+('+NUMBER+r')(?:\s|$)'
 for m in re.finditer(pattern,text,re.M):
  name=m.group(1)
  if name in entries:raise ValueError('Duplicate power category: '+name)
  values=dict(zip(order,map(float,m.groups()[1:])))
  if not all(math.isfinite(v) and v>=-1e-10 for v in values.values()):raise ValueError('Invalid native category power')
  if not math.isclose(sum(values[k] for k in MECHANISMS[:3]),values['total'],rel_tol=1e-8,abs_tol=1e-9):raise ValueError('Category mechanisms do not sum: '+name)
  entries[name]=values
 if 'Subtotal' not in entries:raise ValueError('Missing detailed-power subtotal')
 for k in MECHANISMS:
  if not math.isclose(sum(v[k] for c,v in entries.items() if c!='Subtotal'),entries['Subtotal'][k],rel_tol=1e-8,abs_tol=1e-9):raise ValueError('Native subtotal mismatch: '+k)
 return entries

def validate_spef_annotation(path):
 text=Path(path).read_text()
 match=re.search(r'^Normal\s+(\d+)\s+(\d+)\s+([\d.]+)\s+(\d+)',text,re.M)
 if not match:raise ValueError('Missing normal-net SPEF annotation summary')
 count,annotated,percent,unannotated=match.groups()
 if int(count)==0 or int(annotated)!=int(count) or int(unannotated)!=0:raise ValueError('SPEF annotation is incomplete for normal nets')
 return dict(spef_normal_nets=int(count),spef_annotated_normal_nets=int(annotated),spef_normal_annotation_pct=float(percent))

def verified_ties(path,pad):
 if not any(v>1e-9 for v in pad.values()):return []
 if path is None:raise ValueError('Nonzero pad power needs leaf-level tie-cell verification')
 text=Path(path).read_text();values={k:0.0 for k in MECHANISMS};cells=[]
 pattern=r'^\s*('+NUMBER+r')\s+('+NUMBER+r')\s+('+NUMBER+r')\s+('+NUMBER+r')\s+(\S+)\s+(/\S+)'
 for m in re.finditer(pattern,text,re.M):
  leakage,internal,switching,total=map(float,m.groups()[:4]);cell,instance=m.groups()[4:]
  if not cell.startswith('TIE'):raise ValueError('Non-tie pad/bbox cell requires an additional group: '+cell)
  cells.append(dict(cell=cell,instance=instance))
  for k,v in zip(('leakage','internal','switching','total'),(leakage,internal,switching,total)):values[k]+=v
 if not cells or any(not math.isclose(values[k],pad[k],rel_tol=1e-5,abs_tol=1e-10) for k in MECHANISMS):raise ValueError('Tie-cell leaf power does not match native pad power')
 return cells

def parse_matrix(path,reference_total=None,aggregate_path=None,special_path=None,return_metadata=False):
 detailed=native_rows(path);entries=detailed
 for name in ('register','latch','logic','clock_seq','clock_comb'):
  if name not in detailed:raise ValueError('Missing native power category: '+name)
 if aggregate_path is not None:
  entries=native_rows(aggregate_path,('leakage','internal','switching','total'))
  if 'clock' not in entries:raise ValueError('Missing aggregate clock power')
 matrix={c:{k:0.0 for k in MECHANISMS} for c in CATEGORIES}
 ties=[]
 for name,values in entries.items():
  if name=='Subtotal' or (aggregate_path is not None and name=='clock'):continue
  if name=='pad' and any(v>1e-9 for v in values.values()):
   ties=verified_ties(special_path,values);category='logic'
  elif name in GROUPS:category=GROUPS[name]
  else:
   if any(v>1e-9 for v in values.values()):raise ValueError('Nonzero power outside the requested groups: '+name)
   continue
  for k in MECHANISMS:matrix[category][k]+=values[k]
 boundary={k:0.0 for k in MECHANISMS}
 if aggregate_path is not None:
  matrix['clock_sequential']=dict(detailed['clock_seq'])
  for name in ('register','latch','logic'):
   for k in MECHANISMS:
    if not math.isclose(entries[name][k],detailed[name][k],rel_tol=1e-8,abs_tol=1e-9):raise ValueError('Clock reassignment changed non-clock category: '+name)
  for k in MECHANISMS:
   value=entries['clock'][k]-detailed['clock_seq'][k]
   if value < -1e-9:raise ValueError('Clock sequential exceeds aggregate clock power')
   matrix['clock_combinational'][k]=max(0.0,value)
   boundary[k]=value-detailed['clock_comb'][k]
 for k in MECHANISMS:
  if not math.isclose(sum(matrix[c][k] for c in CATEGORIES),entries['Subtotal'][k],rel_tol=1e-8,abs_tol=1e-9):raise ValueError('Matrix does not reconcile with whole-design '+k)
 if reference_total is not None and not math.isclose(entries['Subtotal']['total'],reference_total,rel_tol=1e-5,abs_tol=1e-7):raise ValueError('Detailed total differs from whole-design power')
 metadata=dict(tie_cells_classified_as_logic=ties,clock_partition_difference_uW=dict(boundary),native_clock_comb=detailed['clock_comb'],clock_definition='Clock-sequential is native clock_seq; clock-combinational is aggregate clock minus clock_seq, including clock-network contributions omitted by the cell-only clock_comb category.')
 return (matrix,metadata) if return_metadata else matrix

def write_case(directory,matrix,metadata=None):
 directory=Path(directory)
 with (directory/'power_matrix.csv').open('w') as f:
  w=csv.writer(f);w.writerow(['category']+[k+'_uW' for k in MECHANISMS])
  for c in CATEGORIES:w.writerow([c]+[matrix[c][k] for k in MECHANISMS])
 lines=['All values in µW.','', '| Category | Switching | Internal | Leakage | Total |','|---|---:|---:|---:|---:|']
 for c in CATEGORIES:lines.append('| {} | {} |'.format(c,' | '.join('{:.9g}'.format(matrix[c][k]) for k in MECHANISMS)))
 if metadata:
  (directory/'power_matrix_provenance.json').write_text(json.dumps(metadata,indent=2)+'\n')
  extra=metadata['clock_partition_difference_uW']
  lines+=['','Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching {:.9g}, internal {:.9g}, leakage {:.9g} µW. Verified tie cells are included in logic.'.format(extra['switching'],extra['internal'],extra['leakage'])]
 (directory/'power_matrix.md').write_text('\n'.join(lines)+'\n')

def write_summary(output,records):
 output=Path(output)
 fields=['design','scenario','layout_run','category']+[k+'_uW' for k in MECHANISMS]
 with (output/'power_detail.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(records)
 (output/'power_detail.json').write_text(json.dumps(dict(unit='uW',clock_combinational_definition='Aggregate native clock minus native clock_seq; raw clock_comb and signed partition differences are preserved per case',tie_policy='Pad power is included in logic only after leaf-level verification that all such cells are TIE cells',clock_accounting='Native Joules -assign2clk register latch; clock pin power assigned to clock_seq',records=records),indent=2)+'\n')
 cases={}
 for r in records:
  key=(r['design'],r['scenario'],r['layout_run']);cases.setdefault(key,{})[r['category']]=r
 wide_fields=['design','scenario','layout_run']+[c+'_'+k+'_uW' for c in CATEGORIES for k in MECHANISMS]
 with (output/'power_detail_wide.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=wide_fields);w.writeheader()
  for key,data in sorted(cases.items()):
   row=dict(zip(['design','scenario','layout_run'],key))
   for c in CATEGORIES:
    for k in MECHANISMS:row[c+'_'+k+'_uW']=data[c][k+'_uW']
   w.writerow(row)
 lines=['# Routed power breakdown','', '{} cases with detailed switching, internal and leakage power in µW. Each case uses its routed Innovus netlist and matched detailed SPEF.'.format(len(cases)), '', 'Sequential combines native register and latch power. Clock-sequential uses native `clock_seq`, with register/latch clock-pin power assigned to the clock network (`-assign2clk`). Clock-combinational is native aggregate `clock` minus `clock_seq`, retaining additional clock-network contributions omitted by cell-only `clock_comb`. Logic includes native `logic` and tie cells whose leaf reports verify their identity. Native category reports and per-case matrices are retained.','', 'Activity comes from the updated RTL VCDs propagated through the routed netlist; this is not SDF-backannotated gate simulation.','', 'The tables below show the case with the largest total average power for each design. All cases are in `power_detail.csv` and `power_detail_wide.csv`.','']
 for design in sorted({k[0] for k in cases}):
  key=max((k for k in cases if k[0]==design),key=lambda k:sum(r['total_uW'] for r in cases[k].values()))
  lines+=['## '+design+' — '+key[1],'','| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |','|---|---:|---:|---:|---:|']
  for c in CATEGORIES:lines.append('| {} | {} |'.format(c,' | '.join('{:.9g}'.format(cases[key][c][k+'_uW']) for k in MECHANISMS)))
  lines+=['']
 (output/'POWER_BREAKDOWN.md').write_text('\n'.join(lines)+'\n')
