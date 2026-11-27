#!/usr/bin/env python3
"""Compare full-workload VCD energy at normal and timing-safe maximum clocks."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import shutil
import statistics

DESIGNS=('FPF','129-SGPF','65-SGPF','MPF')
COMPONENTS=('switching','internal','leakage','dynamic','total')
CATEGORIES=('sequential','logic','clock_sequential','clock_combinational')


def close(a,b):
    return math.isclose(float(a),float(b),rel_tol=1e-8,abs_tol=1e-8)


def read_csv(path):
    with path.open() as f:return list(csv.DictReader(f))


def write_csv(path,rows):
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(root):
    rows=read_csv(root/'power_summary.csv')
    result={(r['design'],r['scenario']):r for r in rows}
    if len(result)!=120 or len(rows)!=120:raise ValueError('Expected exactly 120 unique cases')
    for r in rows:
        if (r['status']!='COMPLETE' or r['stage']!='postroute' or r['clock_tree']!='True'
                or float(r['spef_normal_annotation_pct'])!=100 or float(r['input_annotation_pct'])!=100):
            raise ValueError('Incomplete routed power analysis')
    details={}
    for r in read_csv(root/'power_detail.csv'):
        key=(r['design'],r['scenario'])
        if r['category'] in details.setdefault(key,{}):raise ValueError('Duplicate category')
        details[key][r['category']]=r
    if set(details)!=set(result):raise ValueError('Detailed cases do not match summary')
    for key,categories in details.items():
        if set(categories)!=set(CATEGORIES):raise ValueError('Missing energy category')
        for component in ('switching','internal','leakage','total'):
            if not close(sum(float(r[component+'_uW']) for r in categories.values()),result[key][component+'_uW']):
                raise ValueError('Category power does not conserve whole-design power')
    provenance=json.loads((root/'provenance.json').read_text())
    return result,details,{p['design']:p for p in provenance['designs']}


def aggregate(pairs,design,source_clock_ps=None):
    cases=[r for r in pairs if r['design']==design and (source_clock_ps is None or r['normal_clock_ps']==source_clock_ps)]
    blocks=sum(r['blocks'] for r in cases)
    row=dict(design=design,source_frequency_MHz='all three source rates' if source_clock_ps is None else 1e6/source_clock_ps,
             max_frequency_MHz=cases[0]['max_frequency_MHz'],cases=len(cases),total_blocks=blocks)
    for mode in ('normal','max'):
        energies=[r[mode+'_total_energy_nJ'] for r in cases]
        row[mode+'_mean_energy_per_VCD_nJ']=statistics.mean(energies)
        row[mode+'_sum_energy_nJ']=sum(energies)
        row[mode+'_weighted_energy_per_block_pJ']=1000*sum(energies)/blocks
        for component in ('switching','internal','leakage','dynamic'):
            row[mode+'_sum_'+component+'_energy_nJ']=sum(r[mode+'_'+component+'_energy_nJ'] for r in cases)
    row['energy_saving_pct']=100*(1-row['max_sum_energy_nJ']/row['normal_sum_energy_nJ'])
    return row


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--normal',type=Path,required=True)
    parser.add_argument('--max',dest='maximum',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    normal_root=args.normal.resolve();max_root=args.maximum.resolve();output=args.output.resolve()
    normal,normal_details,normal_plans=load(normal_root)
    maximum,max_details,max_plans=load(max_root)
    if set(normal)!=set(maximum):raise ValueError('Normal and maximum cases differ')
    timing=json.loads((max_root.parent/'summary.json').read_text())
    if len(timing)!=4 or any(t['scaled_setup_wns_ns']<0 or t['scaled_hold_wns_ns']<0 for t in timing):
        raise ValueError('Maximum clocks must pass routed setup and hold timing')
    for d in DESIGNS:
        n=normal_plans[d]['handoff_metadata'];m=max_plans[d]['handoff_metadata']
        for field in ('layout_run','netlist_sha256','spef_sha256','sdc_sha256','voltage_V','temperature_C','rc_view'):
            if n[field]!=m[field]:raise ValueError('Physical power inputs do not match: '+d+' '+field)
    cases=[];pairs=[];details=[]
    for key,n in normal.items():
        m=maximum[key]
        for field in ('layout_run','vcd','input_sha256','blocks','sample_divisor','corner'):
            if n[field]!=m[field]:raise ValueError('Mismatched workload: '+str(key)+' '+field)
        if not close(n['clock_ps'],m['source_clock_ps']) or not close(n['duration_ms'],m['source_duration_ms']):
            raise ValueError('Source clock or duration mismatch')
        if not close(float(n['duration_ms'])/float(m['frequency_scale_factor']),m['duration_ms']):
            raise ValueError('Effective duration does not match frequency scaling')
        pair=dict(design=key[0],scenario=key[1],blocks=int(n['blocks']),layout_run=n['layout_run'],
                  normal_clock_ps=float(n['clock_ps']),normal_frequency_MHz=1e6/float(n['clock_ps']),
                  max_clock_ps=float(m['clock_ps']),max_frequency_MHz=1e6/float(m['clock_ps']),
                  frequency_scale_factor=float(m['frequency_scale_factor']))
        for mode,r,category_rows in [('normal',n,normal_details[key]),('max',m,max_details[key])]:
            duration=float(r['duration_ms']);blocks=int(r['blocks'])
            if duration<=0 or blocks<=0:raise ValueError('Invalid workload duration or block count')
            row=dict(design=key[0],scenario=key[1],mode=mode,frequency_MHz=1e6/float(r['clock_ps']),
                     duration_ms=duration,blocks=blocks,layout_run=r['layout_run'])
            pair[mode+'_duration_ms']=duration
            for component in COMPONENTS:
                power=float(r[component+'_uW'])
                energy=power*duration  # 1 microwatt * 1 millisecond = 1 nanojoule.
                row[component+'_power_uW']=power;row[component+'_energy_nJ']=energy
                pair[mode+'_'+component+'_energy_nJ']=energy
            row['energy_per_block_pJ']=1000*row['total_energy_nJ']/blocks
            pair[mode+'_energy_per_block_pJ']=row['energy_per_block_pJ']
            if not close(row['total_energy_nJ'],r['energy_nJ']):raise ValueError('Source energy does not agree with power*time')
            if not close(sum(row[c+'_energy_nJ'] for c in ('switching','internal','leakage')),row['total_energy_nJ']):
                raise ValueError('Energy components do not conserve total energy')
            cases.append(row)
            for category in CATEGORIES:
                source=category_rows[category]
                detail=dict(design=key[0],scenario=key[1],mode=mode,category=category,
                            frequency_MHz=row['frequency_MHz'],duration_ms=duration,blocks=blocks)
                for component in ('switching','internal','leakage','total'):
                    detail[component+'_energy_nJ']=float(source[component+'_uW'])*duration
                detail['energy_per_block_pJ']=1000*detail['total_energy_nJ']/blocks
                details.append(detail)
        pair['energy_saved_nJ']=pair['normal_total_energy_nJ']-pair['max_total_energy_nJ']
        pair['energy_saving_pct']=100*pair['energy_saved_nJ']/pair['normal_total_energy_nJ']
        pairs.append(pair)
    summary=[aggregate(pairs,d) for d in DESIGNS]
    by_frequency=[aggregate(pairs,d,p) for d in DESIGNS for p in sorted({r['normal_clock_ps'] for r in pairs if r['design']==d},reverse=True)]
    output.mkdir(parents=True,exist_ok=False)
    for name,rows in [('energy_cases.csv',cases),('energy_comparison.csv',pairs),('energy_detail.csv',details),
                      ('summary_by_design.csv',summary),('summary_by_source_frequency.csv',by_frequency)]:
        write_csv(output/name,rows)
    (output/'energy_comparison.json').write_text(json.dumps(dict(energy_unit='nJ',per_block_unit='pJ',cases=pairs,summary=summary,summary_by_source_frequency=by_frequency),indent=2)+'\n')
    sources={}
    for label,root in [('normal',normal_root),('max',max_root)]:
        sources[label]={name:dict(path=str(root/name),sha256=sha256(root/name)) for name in ('power_summary.csv','power_detail.csv','provenance.json')}
    provenance=dict(formula='energy_nJ = average_power_uW * effective_duration_ms',
                    max_definition='Minimum passing clock period + 0.5 ns; routed setup/hold validated',
                    sources=sources,timing_summary=str(max_root.parent/'summary.json'),
                    comparisons=len(pairs),energy_cases=len(cases),category_records=len(details),
                    native_power_rerun_required=False)
    (output/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    shutil.copy2(__file__,output/'report_vcd_energy.py')
    text=['VCD energy consumption: normal versus timing-safe maximum frequency','',
          '120 matched VCD workloads, each evaluated at two operating points: 240 energy records.',
          'Normal = each bench original clock (approximately 0.97, 1.94 or 3.89 MHz).',
          'Maximum = the last validated clock: minimum passing period + 0.5 ns, not the zero-slack limit.',
          'Both sets use the same final Innovus netlists, actual buffers/CTS and detailed SPEF at TT_25, 0.8 V, 25 C.',
          'Energy [nJ] = average power [uW] * effective VCD duration [ms]. Per-block energy [pJ] = 1000 * energy [nJ] / blocks.',
          'Normal uses the original VCD duration. Maximum uses original duration / Joules frequency scaling factor.',
          'These are energies for the same complete workloads, including reset/startup and trailing time within each VCD, not for equal wall-clock durations.',
          'No Joules rerun is needed: the average powers were already computed over these same activity windows.',
          'Activity is RTL VCD activity propagated through routed netlists; it is not an SDF gate simulation.', '',
          'Averages below cover the same 30 matched benches per design; they include all three source rates.',
          'The source rates are separate runs. Aggregate sums are benchmark-suite totals, not a single video energy.', '',
          'Design       Max MHz   Normal mean nJ   Max mean nJ   Saving %   Normal pJ/block   Max pJ/block']
    for r in summary:
        text.append('{design:12} {max_frequency_MHz:7.3f} {normal_mean_energy_per_VCD_nJ:16.6f} {max_mean_energy_per_VCD_nJ:13.6f} {energy_saving_pct:10.3f} {normal_weighted_energy_per_block_pJ:17.6f} {max_weighted_energy_per_block_pJ:14.6f}'.format(**r))
    text+=['','Per-block summary is block-weighted: sum(energy)/sum(blocks), including VCD overhead.',
           'Dynamic energy is nearly frequency-independent for the same uniformly scaled workload: higher dynamic power is offset by shorter execution time. Leakage energy decreases with the shorter duration.', '',
           'Files:',
           '  energy_comparison.csv: 120 paired normal/max cases with nJ by mechanism, durations, frequencies, savings and pJ/block.',
           '  energy_cases.csv: 240 records with average power in uW and energy in nJ.',
           '  energy_detail.csv: 960 records; switching/internal/leakage x sequential/logic/clock-sequential/clock-combinational.',
           '  summary_by_design.csv: four aggregate design comparisons.',
           '  summary_by_source_frequency.csv: twelve comparisons keeping the three normal rates separate.',
           '  energy_comparison.json: machine-readable paired cases and summaries.',
           '  provenance.json: source reports, hashes, units and maximum-frequency definition.', '']
    (output/'REPORT.txt').write_text('\n'.join(text))
    print('\n'.join(text[:21]))


if __name__=='__main__':main()
