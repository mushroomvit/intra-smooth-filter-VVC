# Read-only analysis of a finished routed checkpoint at the requested clock.
source [file join [file dirname [info script]] scaled_clock_constraints.tcl]
if {[catch {
  set_multi_cpu_usage -local_cpu 4
  read_db $::env(SCALED_TIMING_DB)
  set_db extract_rc_engine post_route
  set_db extract_rc_effort_level medium
  extract_rc
  set slack [setup_at_period $::env(SCALED_TIMING_PERIOD_NS) scaled_setup]
  time_design -post_route -hold -report_dir $::env(SCALED_TIMING_OUTPUT) -report_prefix scaled_hold
  set text [exec gzip -dc [file join $::env(SCALED_TIMING_OUTPUT) scaled_hold_hold.summary.gz]]
  if {![regexp {WNS \(ns\):\|\s*([-0-9.]+)} $text -> hold_slack]} {error "Missing hold slack"}
  if {$slack < 0 || $hold_slack < 0} {error "Target fails timing: setup=$slack hold=$hold_slack"}
  puts "SCALED_TIMING_COMPLETE $::env(SCALED_TIMING_PERIOD_NS)"
} detail options]} {
  puts stderr "SCALED_TIMING_FAILED: $detail"
  puts stderr [dict get $options -errorinfo]
  exit 1
}
exit 0
