#!/usr/bin/env python3
"""Export testbench power from matched routed Innovus netlists and SPEF."""
import argparse
import csv
import datetime
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from power_breakdown import parse_matrix, write_case, write_summary, validate_spef_annotation

SCRIPT = Path(__file__).resolve().parent
BACKEND = SCRIPT.parent.parent
SYN = BACKEND/'syn'
FRONTEND = BACKEND.parent/'frontend'
DESIGNS = ('FPF', '129-SGPF', '65-SGPF', 'MPF')


def file_sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as channel:
        for block in iter(lambda: channel.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def completed_layout(design, run_id=None):
    base = BACKEND/'lay/deliverables'
    candidates = [base/run_id/'postroute_power_handoff.json'] if run_id else sorted(
        base.glob('*/postroute_power_handoff.json'), key=lambda path:path.stat().st_mtime, reverse=True)
    failures = []
    for manifest in candidates:
        if not manifest.is_file():
            continue
        metadata = json.loads(manifest.read_text())
        if metadata.get('design') != design:
            continue
        try:
            top = 'filtragem1x64_wrapper' if design == 'FPF' else 'wrapper'
            if (metadata.get('format_version') != 1 or metadata.get('stage') != 'postroute' or metadata.get('top') != top or
                    metadata.get('clock_tree') is not True or metadata.get('physical_checks_passed') is not True):
                raise ValueError('Handoff is not a checked, routed design with CTS')
            if metadata.get('rc_view') != 'TT_25' or metadata.get('voltage_V') != 0.8 or metadata.get('temperature_C') != 25:
                raise ValueError('Handoff corner must be TT_25, 0.8 V, 25 C')
            layout_run = metadata['layout_run']
            if layout_run != manifest.parent.name:
                raise ValueError('Layout run identity does not match its directory')
            checkpoint = BACKEND/'lay/saves'/layout_run/'finish/root.init'
            if not checkpoint.is_file():
                raise ValueError('Finished Innovus database is missing')
            for kind in ('netlist','spef','sdc','sdf'):
                path = Path(metadata[kind])
                if not path.is_file() or path.stat().st_size == 0 or path.parent.resolve() != manifest.parent.resolve():
                    raise ValueError('Missing or mismatched '+kind+' export')
                if file_sha256(path) != metadata.get(kind+'_sha256'):
                    raise ValueError(kind+' hash does not match the routed handoff')
            opener = gzip.open if metadata['spef'].endswith('.gz') else open
            spef_design = None
            capacitances = resistances = 0
            section = ''
            with opener(metadata['spef'], 'rt', errors='replace') as channel:
                for line in channel:
                    if re.match(r'^\*DESIGN\s',line):
                        spef_design = line.split(None,1)[1].strip().strip('"')
                    if line.startswith('*CAP'): section='cap'
                    elif line.startswith('*RES'): section='res'
                    elif line.startswith('*'): section=''
                    elif line.strip() and line.lstrip()[0].isdigit():
                        if section=='cap': capacitances+=1
                        elif section=='res': resistances+=1
            if spef_design != top or not capacitances or not resistances:
                raise ValueError('SPEF must match the top and contain detailed capacitances and resistances')
            return dict(design=design,top=top,stage='postroute',layout_run=layout_run,
                        syn_run=metadata['syn_run'],netlist=metadata['netlist'],spef=metadata['spef'],
                        sdc=metadata['sdc'],sdf=metadata['sdf'],rc_view=metadata['rc_view'],
                        clock_tree=True,timing_backannotated_activity=False,
                        sdf_usage='Export for timing simulation; Joules loads SPEF, not SDF',
                        handoff=str(manifest),handoff_metadata=metadata)
        except (KeyError,OSError,ValueError) as error:
            failures.append(str(manifest)+': '+str(error))
    detail='; '.join(failures) if failures else 'no completed routed handoff exists'
    raise ValueError('{}: {}. Complete Innovus through finish; synthesis inputs are not used as fallback.'.format(design,detail))


def tcl_list(values):
    # Double-quoted Tcl words: escape substitution characters and control chars.
    # No GUI/Tk dependency and no shell interpolation is involved.
    def quote(value):
        text = str(value)
        for before, after in [('\\','\\\\'),('$','\\$'),('[','\\['),(']','\\]'),
                              ('"','\\"'),('\n','\\n'),('\r','\\r')]:
            text = text.replace(before, after)
        return '"'+text+'"'
    return ' '.join(quote(value) for value in values)


def completed_synthesis(design):
    candidates = []
    for manifest in (SYN/'work/runs').glob('*/status.tsv'):
        with manifest.open() as channel:
            for row in csv.DictReader(channel, delimiter='\t'):
                if row.get('design') == design and row.get('status') == 'COMPLETE' and row.get('exit_code') == '0':
                    candidates.append(row['run_id'])
    top = 'filtragem1x64_wrapper' if design == 'FPF' else 'wrapper'
    for run in sorted(set(candidates), reverse=True):
        base = SYN/'save'/run/(top+'_map')
        if Path(str(base)+'.v').is_file() and Path(str(base)+'.mmmc.tcl').is_file():
            return run, top, base
    raise ValueError('No completed synthesis handoff for '+design)


def vcd_duration_ms(path):
    with path.open('rb') as channel:
        header = channel.read(4096)
        scale, unit = re.search(rb'\$timescale\s+(\d+)\s*(fs|ps|ns|us|ms|s)\s+\$end', header).groups()
        channel.seek(max(0, path.stat().st_size-65536))
        times = re.findall(rb'^#(\d+)\r?$', channel.read(), re.M)
    return int(times[-1])*int(scale)*{b'fs':1e-12,b'ps':1e-9,b'ns':1e-6,b'us':1e-3,b'ms':1,b's':1000}[unit]


def collect_cases(design, selection, activity_root=None):
    result = []
    for bench in sorted((FRONTEND/'testbench').glob('*MHz/*.vhd')):
        name = bench.stem
        if selection != 'all' and name != selection:
            continue
        pointer = FRONTEND/'build/active_vcd_root.txt'
        default_root = Path(pointer.read_text().strip()) if pointer.is_file() else FRONTEND/'build'
        directory = (activity_root or default_root)/design/name
        metadata = json.loads((directory/'activity.json').read_text())
        vcd = directory/'activity.vcd'
        if (metadata['design'] != design or metadata['scenario'] != name or
                metadata['max_blocks'] != 0 or metadata['sample_divisor'] not in (1, 4) or
                metadata['vcd'] != str(vcd) or not vcd.is_file()):
            raise ValueError('Missing or partial VCD completion record for '+str(directory))
        if 'input_sha256' in metadata and file_sha256(Path(metadata['input'])) != metadata['input_sha256']:
            raise ValueError('Sample changed since VCD generation: '+metadata['input'])
        result.append(dict(metadata, duration_ms=vcd_duration_ms(vcd)))
    if not result:
        raise ValueError('No matching testbench: '+selection)
    return result


def parse_power(path):
    source = path.read_text()
    line = re.search(r'^\s*Subtotal\s+([\d.eE+-]+)\s+([\d.eE+-]+)\s+([\d.eE+-]+)\s+([\d.eE+-]+)', source, re.M)
    if not line or 'Power Unit: uW' not in source:
        raise ValueError('Unrecognized power report: '+str(path))
    leakage, internal, switching, total = map(float, line.groups())
    if min(leakage, internal, switching, total) < 0:
        raise ValueError('Negative power in '+str(path))
    if abs(total-leakage-internal-switching) > max(1e-5, total*1e-4):
        raise ValueError('Inconsistent power subtotal in '+str(path))
    return dict(leakage_uW=leakage, internal_uW=internal, switching_uW=switching,
                dynamic_uW=internal+switching, total_uW=total)


def scale_case(case, period_ns):
    """Scale the complete stimulus time base inside Joules; preserve raw VCDs."""
    if not math.isfinite(period_ns) or period_ns <= 0:
        raise ValueError('Target clock period must be finite and positive')
    factor = case['clock_ps'] / (period_ns * 1000.0)
    return dict(case, source_clock_ps=case['clock_ps'], clock_ps=period_ns*1000.0,
                frequency_scale_factor=factor, source_duration_ms=case['duration_ms'],
                duration_ms=case['duration_ms']/factor)


def parse_coverage(path):
    source = path.read_text()
    # Asserted percentage is the final column for both annotation report forms.
    result = {}
    for label, column in [('Inputs','input_annotation_pct'),('Outputs','output_annotation_pct'),('Flop','flop_annotation_pct')]:
        match = re.search(r'^\s*'+label+r'\s+[^\n]*?([\d.]+)%\s*$', source, re.M)
        result[column] = float(match.group(1)) if match else ''
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--design', choices=DESIGNS+('all',), default='all')
    parser.add_argument('--bench', default='all')
    parser.add_argument('--activity-root', type=Path, help='Versioned VCD generation directory')
    parser.add_argument('--stage', choices=('postroute','synthesis'), default='postroute')
    parser.add_argument('--layout-run', action='append', default=[], metavar='DESIGN=RUN_ID')
    parser.add_argument('--clock-period', action='append', default=[], metavar='DESIGN=NS',
                        help='Scale all VCD activity to this design clock period inside Joules')
    parser.add_argument('--plan-only', action='store_true', help='Validate required routed handoffs without running Joules')
    parser.add_argument('--engine', choices=('joules','genus-joules'), default='joules')
    parser.add_argument('--host', default='/home/tools/cadence/installs/DDI261/RTLSTUDIO261/bin/joules',
                        help='Standalone Joules executable, or Genus when engine=genus-joules')
    parser.add_argument('--cpus', type=int, default=8)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--collect-only', action='store_true')
    parser.add_argument('--skip-metric-export', action='store_true', help='Collect tabular results without invoking Unified Metrics export')
    args = parser.parse_args()
    if args.cpus < 1:
        parser.error('cpus must be positive')
    if args.collect_only and args.output is None:
        parser.error('collect-only requires output')
    output = args.output.resolve() if args.output else BACKEND/'lay/reports/joules_power'/datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    designs = DESIGNS if args.design == 'all' else (args.design,)
    planned = []
    if args.collect_only:
        planned = json.loads((output/'provenance.json').read_text())['designs']
    else:
        overrides={}
        periods={}
        for value in args.clock_period:
            try:
                design,period=value.split('=',1)
                period=float(period)
                if design not in DESIGNS or not math.isfinite(period) or period <= 0:
                    raise ValueError()
                if design in periods: raise ValueError()
                periods[design]=period
            except ValueError:
                parser.error('clock-period requires unique DESIGN=positive_finite_NS')
        if periods and (args.stage != 'postroute' or args.engine != 'joules'):
            parser.error('Clock scaling requires standalone post-route Joules')
        for value in args.layout_run:
            if '=' not in value or value.split('=',1)[0] not in DESIGNS:
                parser.error('layout-run must have the form DESIGN=RUN_ID')
            design,run=value.split('=',1)
            overrides[design]=run
        errors=[]
        for design in designs:
            try:
                if args.stage=='postroute':
                    plan=completed_layout(design,overrides.get(design))
                else:
                    run,top,base=completed_synthesis(design)
                    plan=dict(design=design,stage='synthesis',syn_run=run,top=top,netlist=str(base)+'.v')
                plan['cases']=collect_cases(design,args.bench,args.activity_root.resolve() if args.activity_root else None)
                if design in periods:
                    plan['target_clock_period_ns']=periods[design]
                    plan['activity_scaling']='compute_power -frequency_scale_factor; complete stimulus time base'
                    plan['cases']=[scale_case(case,periods[design]) for case in plan['cases']]
                planned.append(plan)
            except (OSError,ValueError) as error:
                errors.append(str(error))
        if errors:
            parser.error('\n'.join(errors))
        if args.plan_only:
            print(json.dumps(planned,indent=2))
            return 0
        if args.stage=='postroute' and args.engine!='joules':
            parser.error('Post-route analysis requires standalone Joules for propagated clock-tree slew analysis')
        output.mkdir(parents=True, exist_ok=False)
    if not args.collect_only:
        (output/'provenance.json').write_text(json.dumps(dict(engine=args.engine,
            host=args.host, corner='TT_25: 0.8 V, 25 C',stage=args.stage,
            designs=planned), indent=2)+'\n')
        for plan in planned:
            design = plan['design']
            directory = output/design
            directory.mkdir()
            mmmc = directory/'synthesis.mmmc.tcl'
            if plan['stage']=='synthesis':
                mmmc.write_text(Path(plan['netlist'][:-2]+'.mmmc.tcl').read_text().replace('../save/', str(SYN/'save')+'/'))
            manifest = directory/'manifest.tcl'
            case_list = tcl_list([tcl_list([case['scenario'], case['vcd'], case['scope'], case['clock_ps'],
                                         case.get('frequency_scale_factor',1.0)]) for case in plan['cases']])
            settings = dict(syn=SYN,design=design,engine=args.engine,stage=plan['stage'],top=plan['top'],netlist=plan['netlist'],
                            mmmc=mmmc, cpus=args.cpus, output=directory)
            if plan['stage']=='postroute':
                settings.update(spef=plan['spef'],sdc=plan['sdc'],sdf=plan['sdf'])
            text = 'array set PWR [list '+tcl_list([item for pair in settings.items() for item in pair])+']\n'
            text += 'set PWR(cases) [list '+case_list+']\n'
            manifest.write_text(text)
            command = [args.host, '-no_gui', '-batch', '-log', str(directory/'host'),
                       '-files', str(SCRIPT/'script_joules.tcl')]
            if args.engine == 'joules':
                command += ['-work', str(directory/'joules_work')]
            print('START {}: {} testbenches'.format(design,len(plan['cases'])),flush=True)
            with (directory/'console.log').open('w') as channel:
                process = subprocess.run(command, cwd=str(BACKEND/'lay/work'),
                    env=dict(os.environ, POWER_MANIFEST=str(manifest)), stdout=channel, stderr=subprocess.STDOUT)
            print('FINISHED {}: host exit {}'.format(design,process.returncode),flush=True)

    rows = []
    detailed_rows = []
    failed = []
    for plan in planned:
        design = plan['design']
        status_file = output/design/'status.tsv'
        statuses = {}
        if status_file.exists():
            with status_file.open() as channel:
                statuses = {row['scenario']:row['status'] for row in csv.DictReader(channel,delimiter='\t')}
        for case in plan['cases']:
            name = case['scenario']
            row = dict(design=design, scenario=name, clock_ps=case['clock_ps'], blocks=case['blocks'],
                       duration_ms=case['duration_ms'], syn_run=plan['syn_run'], status=statuses.get(name,'NOT_COMPLETED'),
                       engine='joules',corner='TT_25',stage=plan.get('stage','synthesis'),
                       layout_run=plan.get('layout_run',''),spef=plan.get('spef',''),sdc=plan.get('sdc',''),
                       sdf=plan.get('sdf',''),clock_tree=plan.get('clock_tree',False),
                       timing_backannotated_activity=plan.get('timing_backannotated_activity',False),
                       activity='RTL VCD; propagated netlist activity',vcd=case['vcd'],netlist=plan['netlist'],
                       input_sha256=case.get('input_sha256',''),sample_divisor=case['sample_divisor'])
            row.update(source_clock_ps=case.get('source_clock_ps',case['clock_ps']),
                       frequency_MHz=1e6/case['clock_ps'],
                       frequency_scale_factor=case.get('frequency_scale_factor',1.0),
                       source_duration_ms=case.get('source_duration_ms',case['duration_ms']))
            try:
                if row['status'] != 'COMPLETE':
                    raise ValueError('Run not complete')
                if plan.get('stage')=='postroute': row.update(validate_spef_annotation(output/design/'spef_annotation.rpt'))
                row.update(parse_power(output/design/name/'power.rpt'))
                row.update(parse_coverage(output/design/name/'annotation.rpt'))
                if plan.get('stage') == 'postroute' or (output/design/name/'power_breakdown.rpt').is_file():
                    matrix,matrix_metadata=parse_matrix(output/design/name/'power_breakdown.rpt',row['total_uW'],aggregate_path=output/design/name/'power.rpt',special_path=output/design/name/'special_cell_power.rpt',return_metadata=True)
                    write_case(output/design/name,matrix,matrix_metadata)
                    for category,values in matrix.items():
                        detail=dict(design=design,scenario=name,layout_run=plan.get('layout_run',''),category=category)
                        detail.update({key+'_uW':value for key,value in values.items()})
                        detailed_rows.append(detail)
                row['energy_nJ'] = row['total_uW']*row['duration_ms']
                if row['input_annotation_pct'] != 100:
                    raise ValueError('Input-port annotation is below 100%')
            except (OSError, ValueError) as error:
                row['status'] = 'FAILED'
                row['error'] = str(error)
                failed.append((design,name,str(error)))
            rows.append(row)
    if detailed_rows: write_summary(output,detailed_rows)
    fields = ['design','scenario','status','clock_ps','source_clock_ps','frequency_MHz',
              'frequency_scale_factor','source_duration_ms','blocks','duration_ms','leakage_uW','internal_uW',
              'switching_uW','dynamic_uW','total_uW','energy_nJ','input_annotation_pct','output_annotation_pct',
              'flop_annotation_pct','engine','corner','stage','layout_run','spef','sdc','sdf','clock_tree',
              'spef_normal_nets','spef_annotated_normal_nets','spef_normal_annotation_pct','activity','timing_backannotated_activity','syn_run','netlist','vcd','input_sha256','sample_divisor','error']
    with (output/'power_summary.csv').open('w') as channel:
        writer=csv.DictWriter(channel,fieldnames=fields)
        writer.writeheader();writer.writerows(rows)
    (output/'power_summary.json').write_text(json.dumps(rows,indent=2)+'\n')
    print('Power summary: '+str(output/'power_summary.csv'))
    print('{} complete, {} failed'.format(len(rows)-len(failed),len(failed)))
    if not failed and not args.skip_metric_export:
        directory = output/'metrics'
        directory.mkdir(exist_ok=True)
        manifest = directory/'manifest.tcl'
        manifest.write_text('set POWER_METRICS_ROOT '+tcl_list([output])+'\n'+
            'set POWER_METRICS_DIRECTORY '+tcl_list([directory])+'\n'+
            'set POWER_METRICS_ROWS [list '+tcl_list([tcl_list([item for pair in row.items() for item in pair]) for row in rows])+']\n')
        command = [args.host,'-no_gui','-batch','-log',str(directory/'host'),
                   '-files',str(SCRIPT/'export_power_metrics.tcl')]
        if args.engine == 'joules':
            command += ['-work',str(directory/'joules_work')]
        with (directory/'console.log').open('w') as channel:
            process = subprocess.run(command,cwd=str(BACKEND/'lay/work'),
                env=dict(os.environ,POWER_METRICS_MANIFEST=str(manifest)),stdout=channel,stderr=subprocess.STDOUT)
        if process.returncode or 'POWER_METRICS_COMPLETE' not in (directory/'console.log').read_text():
            print('Unified Metrics export failed; see '+str(directory/'console.log'))
            return 1
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
