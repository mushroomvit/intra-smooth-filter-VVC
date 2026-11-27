#!/usr/bin/env python3
"""Validate the requested clocks without modifying the routed implementations."""
import json
import os
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parent
output=Path(sys.argv[1]).resolve()
rows=json.loads((output/'clock_plan.json').read_text())
refine='--refine' in sys.argv[2:]
target_only='--target-only' in sys.argv[2:]
if refine and not (output/'initial_clock_plan.json').exists():
    (output/'initial_clock_plan.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:
    directory=output/('timing_validated' if refine or target_only else 'timing')/row['design']
    directory.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,SCALED_TIMING_DB=str(root.parent.parent/'lay/saves'/row['layout_run']/'finish'),
             SCALED_TIMING_PERIOD_NS=str(row['target_period_ns']),SCALED_TIMING_OUTPUT=str(directory))
    env['SCALED_TIMING_MINIMUM_NS']=str(row['estimated_minimum_period_ns'])
    print('TIMING_START '+row['design'],flush=True)
    with (directory/'console.log').open('w') as log:
        result=subprocess.run(['innovus','-stylus','-no_gui','-log',str(directory/'host'),
                               '-files',str(root/('refine_scaled_timing.tcl' if refine else 'check_scaled_timing.tcl'))],cwd=str(directory),env=env,stdout=log,stderr=subprocess.STDOUT)
    text=(directory/'console.log').read_text()
    if result.returncode or 'SCALED_TIMING_COMPLETE' not in text:
        print('TIMING_FAILED '+row['design'],flush=True)
        sys.exit(1)
    print('TIMING_COMPLETE '+row['design'],flush=True)
    if target_only:
        row['target_timing_passed']=True
        temporary=output/'clock_plan.json.tmp'
        temporary.write_text(json.dumps(rows,indent=2)+'\n')
        temporary.replace(output/'clock_plan.json')
    if refine:
        values={line.split()[1]:float(line.split()[2]) for line in (directory/'refined_period.tcl').read_text().splitlines()}
        row.update(minimum_passing_period_ns=values['MINIMUM_PERIOD_NS'],
                   minimum_passing_setup_wns_ns=values['MINIMUM_PASSING_SLACK_NS'],
                   target_period_ns=values['TARGET_PERIOD_NS'],
                   target_frequency_MHz=1000/values['TARGET_PERIOD_NS'],
                   refined_fmax_MHz=1000/values['MINIMUM_PERIOD_NS'],
                   target_timing_passed=True,margin_ns=0.5)
        temporary=output/'clock_plan.json.tmp'
        temporary.write_text(json.dumps(rows,indent=2)+'\n')
        temporary.replace(output/'clock_plan.json')
if refine or target_only:
    import csv
    with (output/'clock_plan.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
