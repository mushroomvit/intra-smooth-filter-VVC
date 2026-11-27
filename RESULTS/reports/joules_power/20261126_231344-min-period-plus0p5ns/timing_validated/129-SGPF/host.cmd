#######################################################
#                                                     
#  Innovus Command Logging File                     
#  Created on Thu Nov 26 23:15:41 2026                
#                                                     
#######################################################

#@(#)CDS: Innovus v26.10-p003_1 (64bit) 06/17/2026 14:23 (Linux 4.18.0-305.el8.x86_64)
#@(#)CDS: NanoRoute 26.10-p003_1 NR260416-2103/26_10-UB (database version 18.20.685) {superthreading v2.20}
#@(#)CDS: AAE 26.10-p004 (64bit) 06/17/2026 (Linux 4.18.0-305.el8.x86_64)
#@(#)CDS: CTE 26.10-p004_1 () May 14 2026 11:33:15 ( )
#@(#)CDS: SYNTECH 26.10-p001_1 () Apr 13 2026 10:40:29 ( )
#@(#)CDS: CPE v26.10-p002
#@(#)CDS: IQuantus/TQuantus 24.1.0-e481 (64bit) Fri Apr 3 12:57:29 PDT 2026 (Linux 4.18.0-305.el8.x86_64)

#@ source /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/syn/work/check_scaled_timing.tcl
#@ Begin verbose source (pre): source /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/syn/work/check_scaled_timing.tcl
#@ source [file join [file dirname [info script]] scaled_clock_constraints.tcl]
#@ Begin verbose source /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/syn/work/scaled_clock_constraints.tcl (pre)
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
#@ End verbose source /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/syn/work/scaled_clock_constraints.tcl
if {[catch {  set_multi_cpu_usage -local_cpu 4  read_db $::env(SCALED_TIMING_DB)  set_db extract_rc_engine post_route  set_db extract_rc_effort_level medium  extract_rc  set slack [setup_at_period $::env(SCALED_TIMING_PERIOD_NS) scaled_setup]  time_design -post_route -hold -report_dir $::env(SCALED_TIMING_OUTPUT) -report_prefix scaled_hold  set text [exec gzip -dc [file join $::env(SCALED_TIMING_OUTPUT) scaled_hold_hold.summary.gz]]  if {![regexp {WNS \(ns\):\|\s*([-0-9.]+)} $text -> hold_slack]} {error "Missing hold slack"}  if {$slack < 0 || $hold_slack < 0} {error "Target fails timing: setup=$slack hold=$hold_slack"}  puts "SCALED_TIMING_COMPLETE $::env(SCALED_TIMING_PERIOD_NS)"} detail options]} {...}
exit 0
