# Solve for the minimum passing period with the original routed constraints.
source [file join [file dirname [info script]] scaled_clock_constraints.tcl]
if {[catch {
  set_multi_cpu_usage -local_cpu 4
  read_db $::env(SCALED_TIMING_DB)
  set_db extract_rc_engine post_route
  set_db extract_rc_effort_level medium
  extract_rc
  set period $::env(SCALED_TIMING_MINIMUM_NS)
  set converged 0
  set f [open [file join $::env(SCALED_TIMING_OUTPUT) period_search.tsv] w]
  puts $f "iteration\tperiod_ns\tsetup_wns_ns"
  set history {}
  for {set i 0} {$i < 20} {incr i} {
    set slack [setup_at_period $period search_$i]
    puts $f "$i\t$period\t$slack"; flush $f
    puts "PERIOD_SEARCH $i $period $slack"
    if {abs($slack) <= 0.002} {set converged 1; break}
    lappend history [list $period $slack]
    set next [expr {$period-$slack}]
    if {[llength $history] >= 2} {
      lassign [lindex $history end-1] previous previous_slack
      if {abs($slack-$previous_slack)>0.0001} {
        set next [expr {$period-$slack*($period-$previous)/($slack-$previous_slack)}]
      }
    }
    set low {}; set high {}
    foreach pair $history {
      lassign $pair p s
      if {$s < 0 && ($low eq "" || $p > $low)} {set low $p}
      if {$s > 0 && ($high eq "" || $p < $high)} {set high $p}
    }
    # Before both signs are known, keep moving toward the missing bracket.
    # SI timing windows can make two nearby same-sign samples non-monotonic.
    if {$low eq "" && $high ne ""} {set next [expr {$high-max(0.1,abs($slack))}]}
    if {$high eq "" && $low ne ""} {set next [expr {$low+max(0.1,abs($slack))}]}
    if {$low ne "" && $high ne "" && ($next <= $low || $next >= $high)} {
      set next [expr {($low+$high)/2.0}]
    }
    set period [expr {round($next*1000.0)/1000.0}]
    if {$period <= 1.0} {error "Nonphysical period during timing search"}
  }
  close $f
  if {!$converged} {error "Zero-slack period search did not converge"}
  # Keep the minimum passing candidate slightly above the 1 ps report resolution.
  set minimum [expr {round(($period-$slack+0.003)*1000.0)/1000.0}]
  set passing_slack [setup_at_period $minimum minimum_passing_setup]
  if {$passing_slack < 0} {error "Refined minimum candidate does not pass setup"}
  set target [expr {round(($minimum+0.5)*1000.0)/1000.0}]
  set target_slack [setup_at_period $target scaled_setup]
  time_design -post_route -hold -report_dir $::env(SCALED_TIMING_OUTPUT) -report_prefix scaled_hold
  set hold_text [exec gzip -dc [file join $::env(SCALED_TIMING_OUTPUT) scaled_hold_hold.summary.gz]]
  if {![regexp {WNS \(ns\):\|\s*([-0-9.]+)} $hold_text -> hold_slack]} {error "Missing hold slack"}
  if {$target_slack < 0 || $hold_slack < 0} {error "Margin target does not pass setup/hold"}
  set f [open [file join $::env(SCALED_TIMING_OUTPUT) refined_period.tcl] w]
  puts $f [list set MINIMUM_PERIOD_NS $minimum]
  puts $f [list set MINIMUM_PASSING_SLACK_NS $passing_slack]
  puts $f [list set TARGET_PERIOD_NS $target]
  puts $f [list set TARGET_SETUP_SLACK_NS $target_slack]
  close $f
  puts "SCALED_TIMING_COMPLETE minimum=$minimum target=$target setup=$target_slack"
} detail options]} {
  puts stderr "SCALED_TIMING_FAILED: $detail"
  puts stderr [dict get $options -errorinfo]
  exit 1
}
exit 0
