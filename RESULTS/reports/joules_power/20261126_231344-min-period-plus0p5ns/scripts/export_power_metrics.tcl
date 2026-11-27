# Export measured Joules report values as native Unified Metrics snapshots.
proc measured_power_metric {field unit} {
  global measurement
  return [list $measurement($field) $unit]
}
if {[catch {
  source $::env(POWER_METRICS_MANIFEST)
  set definitions {
    {joules.power.leakage leakage_uW uW}
    {joules.power.internal internal_uW uW}
    {joules.power.switching switching_uW uW}
    {joules.power.dynamic dynamic_uW uW}
    {joules.power.total total_uW uW}
    {joules.energy.total energy_nJ nJ}
    {joules.trace.duration duration_ms ms}
    {joules.trace.clock_period clock_ps ps}
    {joules.annotation.inputs input_annotation_pct %}
    {joules.annotation.outputs output_annotation_pct %}
    {joules.annotation.flops flop_annotation_pct %}
  }
  foreach definition $definitions {
    lassign $definition metric field unit
    define_metric -name $metric -units $unit -precision 6
  }
  file mkdir $POWER_METRICS_DIRECTORY
  foreach row $POWER_METRICS_ROWS {
    array unset measurement
    array set measurement $row
    set name $measurement(design)_$measurement(scenario)
    foreach definition $definitions {
      lassign $definition metric field unit
      set_metric -name $metric -value [list $measurement($field) $unit]
    }
    create_snapshot joules.* -name $name -categories flow
    write_metric -format json -names [list $name] -out_file \
      [file join $POWER_METRICS_ROOT $measurement(design) $measurement(scenario) power_metrics.json]
  }
  write_metric -format json -out_file [file join $POWER_METRICS_DIRECTORY power_metrics.json]
  write_metric -format csv -out_file [file join $POWER_METRICS_DIRECTORY power_metrics.csv]
  report_metric -format html -out_file [file join $POWER_METRICS_DIRECTORY power_metrics.html]
  puts POWER_METRICS_COMPLETE
} detail options]} {
  puts stderr "POWER_METRICS_FAILED: $detail"
  puts stderr [dict get $options -errorinfo]
  exit 1
}
exit 0
