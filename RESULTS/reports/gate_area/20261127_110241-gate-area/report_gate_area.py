#!/usr/bin/env python3
"""Count final routed leaf cells and their actual standard-cell areas."""
import argparse
from collections import Counter
import csv
import datetime
from decimal import Decimal
import gzip
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT=Path(__file__).resolve().parent
BACKEND=next(parent for parent in (ROOT,*ROOT.parents)
             if (parent/'syn/scripts/TECH/tsmc22.cfg.tcl').is_file())
DESIGNS=('FPF','129-SGPF','65-SGPF','MPF')
GROUPS=('mux','full_adder','half_adder','flip_flop','latch','clock_gating',
        'buffer','inverter','delay','tie','and_nand','or_nor','xor_xnor','compound_logic')


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def classify(name,cell):
    if name.startswith('MUX'):return 'mux'
    if re.match(r'FA\d',name):return 'full_adder'
    if re.match(r'HA\d',name):return 'half_adder'
    if cell['clock_gating']:return 'clock_gating'
    if cell['sequential']=='ff':return 'flip_flop'
    if cell['sequential']=='latch':return 'latch'
    if name.startswith(('BUFF','CKB')):return 'buffer'
    if name.startswith(('INV','CKNS')):return 'inverter'
    if name.startswith('DEL'):return 'delay'
    if name.startswith('TIE'):return 'tie'
    if re.match(r'(AN|ND|IND|CKAN|CKND)\d',name):return 'and_nand'
    if re.match(r'(OR|NR|INR)\d',name):return 'or_nor'
    if name.startswith(('XOR','XNR')):return 'xor_xnor'
    if name.startswith(('AO','OA','MAOI','MOAI')):return 'compound_logic'
    raise ValueError('Unclassified cell: '+name)


def libraries():
    script='source {'+str(BACKEND/'syn/scripts/common/message.tcl')+'}\nset CORNER TYPICAL\nsource {'+str(BACKEND/'syn/scripts/TECH/tsmc22.cfg.tcl')+'}\nforeach l $TECH(LIB_FILES_TYPICAL) {puts "GATE_LIBRARY [file join $TECH(LIB_PATH) $l]"}\n'
    result=subprocess.run(['tclsh'],input=script,universal_newlines=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    paths=[Path(line[len('GATE_LIBRARY '):]) for line in result.stdout.splitlines() if line.startswith('GATE_LIBRARY ')]
    if not paths:raise ValueError('No configured Liberty libraries')
    cells={};sources=[]
    for path in paths:
        sources.append(dict(path=str(path),sha256=digest(path)))
        text=gzip.open(path,'rt').read() if path.suffix=='.gz' else path.read_text()
        matches=list(re.finditer(r'^\s*cell\s*\(\s*"?([\w$]+)"?\s*\)\s*\{',text,re.M))
        for i,m in enumerate(matches):
            body=text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)]
            a=re.search(r'^\s*area\s*:\s*([\d.eE+-]+)\s*;',body,re.M)
            if not a:raise ValueError('Missing area for '+m.group(1))
            seq=re.search(r'^\s*(ff|latch)\s*\(',body,re.M)
            cell=dict(area=Decimal(a.group(1)),functions=re.findall(r'\bfunction\s*:\s*"([^"]*)"',body),
                      sequential=seq.group(1) if seq else '',
                      clock_gating=bool(re.search(r'\bclock_gating_integrated_cell\s*:',body)),library=str(path))
            name=m.group(1)
            if name in cells:
                if cells[name]['area']!=cell['area']:raise ValueError('Duplicate cell with different area: '+name)
            else:cells[name]=cell
    return cells,sources


def leaf_instances(netlist,top,known_cells):
    text=re.sub(r'/\*.*?\*/|//[^\n]*','',netlist.read_text(),flags=re.S)
    modules={}
    for name,body in re.findall(r'\bmodule\s+(\w+)\s*\((.*?)\bendmodule',text,re.S):
        if name in modules:raise ValueError('Duplicate module '+name)
        body=body.split(';',1)[1]
        modules[name]=re.findall(r'^\s*(\w+)\s+(\\\S+|[\w$]+)\s*\(',body,re.M)
    def walk(module,prefix,ancestors):
        if module in ancestors:raise ValueError('Recursive module hierarchy')
        if module not in modules:raise ValueError('Missing module '+module)
        for master,instance in modules[module]:
            path=prefix+'/'+instance
            if master in modules:yield from walk(master,path,ancestors+(module,))
            elif master in known_cells:yield master,path
            else:raise ValueError('Unknown leaf master '+master)
    return list(walk(top,top,()))


def write_csv(path,rows):
    with path.open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    output=args.output.resolve()
    cells,library_sources=libraries()
    reference='ND2SGD1BWP7T40P140';nand_area=cells[reference]['area']
    runs=json.loads((BACKEND/'lay/reports/summary/current_runs.json').read_text())['current_layouts']
    summaries=[];categories=[];masters=[];instances=[];inputs=[];functions=[]
    for design in DESIGNS:
        run=runs[design];handoff=BACKEND/'lay/deliverables'/run/'postroute_power_handoff.json'
        metadata=json.loads(handoff.read_text());netlist=Path(metadata['netlist'])
        if metadata['physical_checks_passed'] is not True or metadata['clock_tree'] is not True:
            raise ValueError('Expected checked routed design with clock tree')
        if digest(netlist)!=metadata['netlist_sha256']:raise ValueError('Netlist does not match routed handoff')
        leaves=leaf_instances(netlist,metadata['top'],cells)
        counts=Counter(master for master,path in leaves)
        groups={g:dict(count=0,area=Decimal(0)) for g in GROUPS}
        for master,count in sorted(counts.items()):
            cell=cells[master];group=classify(master,cell);area=count*cell['area']
            if group in ('mux','full_adder','half_adder') and not cell['functions']:
                raise ValueError('Arithmetic/mux master has no library function')
            groups[group]['count']+=count;groups[group]['area']+=area
            masters.append(dict(design=design,category=group,cell=master,count=count,unit_area_um2=cell['area'],
                                total_area_um2=area,library=cell['library']))
            if group in ('mux','full_adder','half_adder'):
                functions.append(dict(design=design,category=group,cell=master,count=count,
                                      unit_area_um2=str(cell['area']),total_area_um2=str(area),
                                      liberty_functions=cell['functions'],library=cell['library']))
        area=sum((v['area'] for v in groups.values()),Decimal(0))
        report=BACKEND/'lay/reports'/run/'final_cell_area.rpt'
        match=re.search(r'^'+re.escape(metadata['top'])+r'\s+(\d+)\s+([\d.]+)\s*$',report.read_text(),re.M)
        if not match or int(match.group(1))!=len(leaves) or abs(Decimal(match.group(2))-area)>Decimal('0.0005'):
            raise ValueError('Inventory does not match native Innovus count/area: '+design)
        summary=dict(design=design,layout_run=run,total_cells=len(leaves),cell_area_um2=area,
                     nand2_equivalent_gates=area/nand_area,nand2_equivalent_kgates=area/nand_area/1000)
        for group in GROUPS:
            count=groups[group]['count'];a=groups[group]['area']
            summary[group+'_count']=count;summary[group+'_area_um2']=a
            categories.append(dict(design=design,category=group,count=count,area_um2=a,
                                   area_percent=100*a/area,cell_count_percent=100*Decimal(count)/len(leaves)))
        summary['adder_count']=summary['full_adder_count']+summary['half_adder_count']
        summary['adder_area_um2']=summary['full_adder_area_um2']+summary['half_adder_area_um2']
        summaries.append(summary)
        for master,path in leaves:
            instances.append(dict(design=design,instance=path,cell=master,category=classify(master,cells[master]),area_um2=cells[master]['area']))
        inputs.append(dict(design=design,layout_run=run,netlist=str(netlist),netlist_sha256=digest(netlist),
                           area_report=str(report),area_report_sha256=digest(report),
                           validated_leaf_count=len(leaves),validated_area_um2=str(area)))
    output.mkdir(parents=True,exist_ok=False)
    for name,rows in [('summary.csv',summaries),('categories.csv',categories),('cells.csv',masters),('instances.csv',instances)]:
        write_csv(output/name,rows)
    (output/'mux_adder_functions.json').write_text(json.dumps(functions,indent=2)+'\n')
    provenance=dict(created=datetime.datetime.now().isoformat(),stage='final routed Innovus netlists',
                    area_unit='um2',nand2_reference=reference,nand2_area_um2=str(nand_area),
                    validation='Counts and summed Liberty area match native Innovus final_cell_area.rpt for every design',
                    libraries=library_sources,designs=inputs,
                    scope='All logical leaf cells including buffers, clock cells, sequential cells and ties; excludes physical-only filler/tap/boundary cells omitted from the routed logical netlist',
                    interpretation='Mux/adder counts are dedicated mapped one-bit standard cells. RTL multi-bit operator counts and decomposed selection/arithmetic logic cannot be inferred uniquely from these totals.')
    (output/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    text=['Final routed gate counts and cell area','',
          'Absolute counts are leaf standard-cell instances in the final Innovus netlists, including the clock tree and inserted buffers.',
          'Area is sum(instance count x Liberty cell area), in um^2. Every design count and area was checked against native Innovus final_cell_area.rpt.',
          'Physical-only filler, tap and boundary cells are outside this logical-cell inventory.',
          'NAND2 equivalents = logical cell area / {:.3f} um^2 ({}). This is an area equivalent, not the actual instance count.'.format(nand_area,reference),'',
          'Definitions:',
          '  Mux: a multiplexer selects one data input using a select signal. MUX2 implements Z = (!S & I0) | (S & I1); MUX2N inverts that output.',
          '  Full adder: adds one-bit A, B and carry-in CI; SUM = A XOR B XOR CI, carry-out = AB | ACI | BCI.',
          '  Half adder: adds two one-bit inputs without carry-in; SUM = A XOR B, carry-out = AB.',
          'Counts below refer to dedicated mapped one-bit mux/full-adder/half-adder cells. They are not counts of buses or RTL arithmetic operators.',
          'For example, a multi-bit adder can contain many FA cells plus other gates. Selection and addition can also map to ordinary logic gates.',
          'FPF contains zero dedicated MUX cells; this does not mean it has no selection logic. Its selection functions have been mapped to ordinary logic.', '',
          'Design        Cells   Area um^2   NAND2 kGE   Mux count   Mux um^2   FA count    FA um^2   HA count   HA um^2']
    for r in summaries:
        text.append('{design:12} {total_cells:6d} {cell_area_um2:11.3f} {nand2_equivalent_kgates:10.3f} {mux_count:11d} {mux_area_um2:10.3f} {full_adder_count:10d} {full_adder_area_um2:10.3f} {half_adder_count:10d} {half_adder_area_um2:9.3f}'.format(**r))
    for design in DESIGNS:
        text+=['','Gate categories: '+design,'Category                Absolute count       Area um^2      Area %']
        for r in categories:
            if r['design']==design:text.append('{category:24} {count:14d} {area_um2:15.3f} {area_percent:11.3f}'.format(**r))
    text+=['','Files:',
           '  summary.csv: absolute total, mux, full-adder and half-adder counts/areas; all other gate classes; NAND2 equivalents.',
           '  categories.csv: exclusive gate-class totals and area/count percentages.',
           '  cells.csv: absolute count, unit area and total area for every library cell used by each design.',
           '  instances.csv: every flattened logical leaf instance, master, category and area.',
           '  mux_adder_functions.json: the actual Liberty functions and areas of all used mux/adder masters.',
           '  provenance.json: exact netlist/library hashes, native area reports, scope and counting definitions.', '']
    (output/'REPORT.txt').write_text('\n'.join(text))
    shutil.copy2(__file__,output/'report_gate_area.py')
    print('\n'.join(text[:22]))


if __name__=='__main__':main()
