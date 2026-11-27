#!/usr/bin/env python3
"""Combine routed timing evidence and the newly computed Joules consumption."""
import csv
import gzip
import json
from pathlib import Path
import re
import statistics
import sys

root=Path(sys.argv[1]).resolve()
clock=json.loads((root/'clock_plan.json').read_text())
power=json.loads((root/'power/power_summary.json').read_text())
if len(power)!=120 or any(r['status']!='COMPLETE' for r in power):
    raise ValueError('All 120 cases must complete before reporting consumption')
with (root/'baseline_power_summary.csv').open() as f:
    baseline={(r['design'],r['scenario']):r for r in csv.DictReader(f)}
comparisons=[]
for r in power:
    b=baseline[(r['design'],r['scenario'])]
    item=dict(design=r['design'],scenario=r['scenario'],frequency_scale_factor=r['frequency_scale_factor'])
    for k in ('switching_uW','internal_uW','leakage_uW'):
        expected=float(b[k])*(1 if k=='leakage_uW' else r['frequency_scale_factor'])
        item[k]=r[k]
        item[k+'_baseline_scaled_reference']=expected
        item[k+'_relative_difference_pct']=100*(r[k]-expected)/expected
    comparisons.append(item)
with (root/'baseline_comparison.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(comparisons[0]));w.writeheader();w.writerows(comparisons)
tables=['# Detailed power for all 120 cases','',
        'Native Joules results at the verified minimum passing periods plus 0.5 ns. All values are in µW.', '']
for r in power:
    matrix=root/'power'/r['design']/r['scenario']/'power_matrix.md'
    tables+=['## '+r['design']+' — '+r['scenario'],'',matrix.read_text().strip(),'']
(root/'power/POWER_BREAKDOWN_ALL_CASES.md').write_text('\n'.join(tables)+'\n')

def wns(path):
    opener=gzip.open if path.suffix=='.gz' else open
    with opener(path,'rt') as f: text=f.read()
    return float(re.search(r'WNS \(ns\):\|\s*([-\d.]+)',text).group(1))

rows=[]
normalized=[]
for c in clock:
    directory=root/'timing_validated'/c['design']
    if 'SCALED_TIMING_COMPLETE' not in (directory/'console.log').read_text():
        raise ValueError('Missing native timing validation: '+c['design'])
    c['scaled_setup_wns_ns']=wns(directory/'scaled_setup.summary.gz')
    c['scaled_hold_wns_ns']=wns(directory/'scaled_hold_hold.summary.gz')
    if c['scaled_setup_wns_ns'] < 0 or c['scaled_hold_wns_ns'] < 0:
        raise ValueError('Selected target does not pass setup/hold: '+c['design'])
    with gzip.open(directory/'scaled_setup_all.tarpt.gz','rt') as f:
        critical=f.read(10000)
    for label,key in [('View','critical_setup_view'),('Group','critical_setup_group'),
                      ('Startpoint','critical_startpoint'),('Endpoint','critical_endpoint')]:
        match=re.search(r'^\s*'+label+r':\s*([^\n]+)',critical,re.M)
        c[key]=match.group(1).strip() if match else ''
    cases=[r for r in power if r['design']==c['design']]
    peak=max(cases,key=lambda r:r['total_uW'])
    row=dict(c,cases=len(cases),minimum_total_uW=min(r['total_uW'] for r in cases),
             mean_total_uW=statistics.mean(r['total_uW'] for r in cases),
             maximum_total_uW=peak['total_uW'],maximum_power_scenario=peak['scenario'])
    for k in ('switching_uW','internal_uW','leakage_uW'):
        row['mean_'+k]=statistics.mean(r[k] for r in cases)
    groups={}
    for case in cases:
        workload=re.sub(r'_(0_97|1_94|3_89)MHz$','',case['scenario'])
        groups.setdefault(workload,[]).append(case)
    if len(groups)!=10 or any(len(g)!=3 for g in groups.values()):
        raise ValueError('Expected all three source clocks for ten workloads per design')
    for workload,group in sorted(groups.items()):
        values=[r['total_uW'] for r in group]
        normalized.append(dict(design=c['design'],workload=workload,cases=len(group),
                               target_frequency_MHz=c['target_frequency_MHz'],
                               minimum_total_uW=min(values),maximum_total_uW=max(values),
                               relative_spread_pct=100*(max(values)-min(values))/statistics.mean(values)))
    rows.append(row)
with (root/'source_clock_comparison.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(normalized[0]));w.writeheader();w.writerows(normalized)
with (root/'summary.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(root/'summary.json').write_text(json.dumps(rows,indent=2)+'\n')
lines=['Routed timing and scaled-activity Joules power', '',
       'Requested operating point: refined minimum passing period PLUS 0.5 ns.',
       'Setup and hold must pass in fresh routed analysis at every selected period before power is launched.',
       'Initial minimum-period estimate = original routed SDC period - worst setup slack across all path groups (includes input/output paths).',
       'Refinement: fresh routed SI timing at successive periods until |setup WNS| <= 0.002 ns, then a passing candidate with 0.003 ns report-resolution margin. The target is this passing period plus 0.5 ns.',
       'Timing-report precision is 0.001 ns; these limits apply to the retained constraints and active MMMC views.', '',
       'Design       Tmin ns    Target ns   Target MHz  Setup ns  Hold ns   Mean uW   Max uW',]
for r in rows:
    lines.append('{design:12} {minimum_passing_period_ns:8.3f} {target_period_ns:10.3f} {target_frequency_MHz:11.3f} {scaled_setup_wns_ns:9.3f} {scaled_hold_wns_ns:8.3f} {mean_total_uW:9.3f} {maximum_total_uW:9.3f}'.format(**r))
lines+=['','All 120 cases were recomputed in standalone Joules using the final Innovus netlists, buffers, clock tree and matched detailed SPEF at TT_25, 0.8 V, 25 C.',
        'Frequency limits and reported setup/hold slack use the original active MMMC timing views; power uses TT_25.',
        'Joules compute_power -frequency_scale_factor scales the complete stimulus time base by source period / target period. The per-case SDC uses the target period. No second scale_to_sdc_frequency factor is applied.',
        'Source VCDs remain unchanged. source_clock_ps and source_duration_ms identify the raw waveform; clock_ps and duration_ms describe the scaled workload. Energy = total_uW * effective duration_ms (nJ).',
        'The three source clock rates remain as separate cases; all three are normalized to the same target frequency for each design.',
        'Largest total-power spread across the three normalized source rates for the same workload: {:.6g}%. See source_clock_comparison.csv.'.format(max(r['relative_spread_pct'] for r in normalized)),
        'Activity comes from RTL VCDs propagated through the routed netlist, not SDF gate-level simulation.', '',
        'Files:', '  clock_plan.csv/json: original timing, estimated minimum periods, requested clocks and report sources.',
        '  original_timing/<design>/: original setup/hold summaries.',
        '  limit_search/<design>/: SI-aware period search and verified passing minimum.',
        '  timing_validated/<design>/: fresh setup/hold reports at the final target, retaining original mode and latency constraints.',
        '  power/power_summary.csv/json: 120 cases, switching/internal/leakage/total in uW and effective energy.',
        '  power/power_detail.csv and power_detail_wide.csv: detailed sequential, logic, clock sequential and clock combinational power.',
        '  power/POWER_BREAKDOWN.md and POWER_BREAKDOWN_ALL_CASES.md: per-category tables.',
        '  power/<design>/<scenario>/: native reports, target workload SDC, annotation and conserved category matrices.',
        '  power/provenance.json: matched netlist/SPEF hashes, activity source and scaling factors.',
        '  summary.csv/json: one consumption and timing summary per design.',
        '  baseline_comparison.csv: fresh native power versus the old report after accounting for frequency scaling (a validation reference, not the source of new power values).',
        '  scripts/: reusable analysis scripts; native command logs are retained per design.', '']
(root/'REPORT.txt').write_text('\n'.join(lines))
print('\n'.join(lines[:17]))
