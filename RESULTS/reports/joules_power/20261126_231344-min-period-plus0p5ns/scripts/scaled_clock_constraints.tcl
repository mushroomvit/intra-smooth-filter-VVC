# Re-evaluate SI timing while solving for a zero-slack period. No DB is written.
proc setup_at_period {period prefix} {
  # Update the mode SDC in place and retain each view's CTS source latencies.
  set modes [glob -directory [file join $::env(SCALED_TIMING_DB) mmmc modes] *]
  if {[llength $modes] != 1} {error "Expected one functional constraint mode"}
  set mode [file tail [lindex $modes 0]]
  set original [file join [lindex $modes 0] ${mode}.sdc]
  set f [open $original r]; set constraints [read $f]; close $f
  set replacement [format {create_clock -name clk -period %.12g [get_ports {clk}]} $period]
  if {[regsub -line {^create_clock[^\n]*$} $constraints $replacement constraints] != 1} {
    error "Expected exactly one source clock"
  }
  set path [file join $::env(SCALED_TIMING_OUTPUT) ${prefix}.sdc]
  set f [open $path w]; puts $f $constraints; close $f
  update_constraint_mode -name $mode -sdc_files [list $path]
  foreach latency [glob -directory [file join $::env(SCALED_TIMING_DB) mmmc views] */latency.sdc] {
    update_analysis_view -name [file tail [file dirname $latency]] -latency_file $latency
  }
  extract_rc
  time_design -post_route -report_dir $::env(SCALED_TIMING_OUTPUT) -report_prefix $prefix
  set report [file join $::env(SCALED_TIMING_OUTPUT) ${prefix}.summary.gz]
  set text [exec gzip -dc $report]
  if {![regexp {WNS \(ns\):\|\s*([-0-9.]+)} $text -> slack]} {error "Missing setup slack in $report"}
  return $slack
}
