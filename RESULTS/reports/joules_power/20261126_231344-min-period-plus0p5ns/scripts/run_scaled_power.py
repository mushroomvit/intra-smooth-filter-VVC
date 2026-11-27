#!/usr/bin/env python3
"""Run all 120 cases at the independently verified per-design target periods."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

scripts=Path(__file__).resolve().parent
output=Path(sys.argv[1]).resolve()
if '--wait-for-timing' in sys.argv[2:]:
    print('Waiting for the four timing validations before launching power.',flush=True)
    deadline=time.monotonic()+3600
    while True:
        plans=json.loads((output/'clock_plan.json').read_text())
        if len(plans)==4 and all(p.get('target_timing_passed') for p in plans): break
        for log in (output/'timing_validated').glob('*/console.log'):
            if any(line.startswith('SCALED_TIMING_FAILED:') for line in log.read_text().splitlines()):
                raise ValueError('Timing validation failed: '+str(log))
        if time.monotonic()>deadline:raise TimeoutError('Timing validation did not complete')
        time.sleep(5)
plans=json.loads((output/'clock_plan.json').read_text())
if len(plans)!=4 or any(not p.get('target_timing_passed') for p in plans):
    raise ValueError('Complete all four timing refinements before running power')
command=[sys.executable,str(scripts/'run_joules_power.py'),'--design','all','--output',str(output/'power')]
for plan in plans:
    if abs(plan['target_period_ns']-plan['minimum_passing_period_ns']-0.5)>1e-8:
        raise ValueError('Target must be the passing minimum period plus 0.5 ns')
    command+=['--clock-period',plan['design']+'='+str(plan['target_period_ns']),
              '--layout-run',plan['design']+'='+plan['layout_run']]
(output/'command.json').write_text(json.dumps(command,indent=2)+'\n')
snapshot=output/'scripts';snapshot.mkdir(exist_ok=True)
for name in ('run_joules_power.py','script_joules.tcl','power_breakdown.py','export_power_metrics.tcl',
             'run_scaled_timing.py','refine_scaled_timing.tcl','scaled_clock_constraints.tcl',
             'check_scaled_timing.tcl','summarize_scaled_power.py','run_scaled_power.py'):
    shutil.copy2(scripts/name,snapshot/name)
result=subprocess.run(command)
if result.returncode:sys.exit(result.returncode)
sys.exit(subprocess.call([sys.executable,str(scripts/'summarize_scaled_power.py'),str(output)]))
