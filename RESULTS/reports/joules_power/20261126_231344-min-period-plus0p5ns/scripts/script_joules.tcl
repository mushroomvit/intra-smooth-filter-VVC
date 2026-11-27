# Gate-level power using standalone Joules Common UI (or integrated Genus).
# Run through run_joules_power.py, which writes POWER_MANIFEST with validated
# netlist/VCD provenance. No synthesis or layout optimization is performed.
if {[catch {
  source $::env(POWER_MANIFEST)
  source [file join $PWR(syn) scripts common message.tcl]
  set CORNER TYPICAL
  source [file join $PWR(syn) scripts TECH tsmc22.cfg.tcl]
  set_db max_cpus_per_server $PWR(cpus)
  if {$PWR(engine) eq "joules"} {
    set libraries {}
    foreach library $TECH(LIB_FILES_TYPICAL) {
      lappend libraries [file join $TECH(LIB_PATH) $library]
    }
    read_libs $libraries
    read_netlist $PWR(netlist) -top $PWR(top)
    set_db power_unit uW
    if {$PWR(stage) eq "postroute"} {
      read_sdc $PWR(sdc)
      set spef_result [read_spef $PWR(spef) -detailed_parasitics -max_fanout 1000000]
      puts "POWER_SPEF_READ_RESULT <$spef_result>"
      report_spef_annotation -net_category all -show_details unannotated \
        -out [file join $PWR(output) spef_annotation.rpt]
    }
  } else {
    set_db power_engine joules
    set_db lp_power_unit uW
    if {[get_db power_engine] ne "joules"} {error "Joules power engine is not active"}
    read_mmmc $PWR(mmmc)
    read_physical -lef $TECH(LEF_FILES)
    set_db cap_table_file [file join $TECH(CapT_PATH) $TECH(CapT_TYPICAL)]
    read_netlist $PWR(netlist) -top $PWR(top)
    init_design
  }
  set status [open [file join $PWR(output) status.tsv] w]
  puts $status "design\tscenario\tstatus"
  flush $status

  foreach scenario $PWR(cases) {
    lassign $scenario name vcd scope period_ps frequency_scale
    if {$frequency_scale eq ""} {set frequency_scale 1.0}
    set directory [file join $PWR(output) $name]
    file mkdir $directory
    puts "POWER_CASE_START $PWR(design) $name"
    if {[catch {
      # Clear prior assertions so cases never inherit activity from one another.
      set DESIGN(CLOCK_PERIOD_NS) [expr {$period_ps / 1000.0}]
      if {$PWR(stage) eq "postroute"} {
        set sdc $PWR(sdc)
      } else {
        set sdc [file join $PWR(syn) scripts $PWR(design) $PWR(design).sdc]
      }
      if {$PWR(engine) eq "joules"} {
        delete_sdb
        reset_pin_activity -activity_type user -all
        reset_pin_activity -activity_type system -global
        if {$PWR(stage) eq "postroute"} {
          # SDC commands run in read_sdc's timing context, not the Joules shell.
          set original [open $sdc r]; set constraints [read $original]; close $original
          # Replace the clock in place: appending create_clock after latency,
          # uncertainty and I/O constraints can reset clock properties.
          set replacement [format {create_clock -name clk -period %.12g [get_ports {clk}]} $DESIGN(CLOCK_PERIOD_NS)]
          if {[regsub -line {^create_clock[^\n]*$} $constraints $replacement constraints] != 1} {
            error "Expected exactly one source clock in routed SDC"
          }
          set sdc [file join $directory workload.sdc]
          set f [open $sdc w]
          puts $f $constraints
          puts $f {set_units -time ns -capacitance pF}
          puts $f {set_propagated_clock [all_clocks]}
          close $f
        }
        read_sdc $sdc
        set dut /[string map {. /} $scope]
        read_stimulus -file $vcd -format vcd -dut_instance $dut \
          -stim_annotation_report_file [file join $directory annotation_import.rpt]
        if {$PWR(stage) eq "postroute"} {
          puts "POWER_ACTIVITY_SCALE period_ps=$period_ps global_factor=$frequency_scale"
          compute_power -mode average -post_cts_clock -clock_network_slew propagate \
            -frequency_scale_factor $frequency_scale
        } else {
          compute_power -mode average
        }
        report_power -unit uW -by_category -assign2clk {register latch} -format %.12e -cols {leakage internal switching total} \
          -out [file join $directory power.rpt]
        report_power -unit uW -by_category -assign2clk {register latch} -format %.12e -cols {leakage internal switching total} \
          -csv -out [file join $directory power.csv]
        report_power -unit uW -by_leaf_instance -rtl_type {tie pad bbox} \
          -cols {instances leakage internal switching total cell} \
          -out [file join $directory special_cell_power.rpt]
        report_power -unit uW -by_category -assign2clk {register latch} \
          -category {register latch logic clock_seq clock_comb memory bbox pad pm physical_only_cells} \
          -cols {switching internal leakage total} -format %.12e \
          -out [file join $directory power_breakdown.rpt]
        report_power -unit uW -by_category -assign2clk {register latch} \
          -category {register latch logic clock_seq clock_comb memory bbox pad pm physical_only_cells} \
          -cols {switching internal leakage total} -format %.12e -csv \
          -out [file join $directory power_breakdown.csv]
        report_power -unit uW -by_hierarchy -levels all -out [file join $directory hierarchy.rpt]
      } else {
        set_activity -reset
        read_sdc -view TT_25 $sdc
        read_vcd -static -vcd_scope $scope $vcd
        report_power -view TT_25 -unit uW > [file join $directory power.rpt]
        report_power -view TT_25 -unit uW -by_hierarchy -levels all > [file join $directory hierarchy.rpt]
      }
      report_sdb_annotation -out [file join $directory annotation.rpt]
      if {[llength [info commands create_snapshot]] && [llength [info commands write_metric]]} {
        create_snapshot -name $PWR(design)_$name -categories {flow design power}
        write_metric -format json -names [list $PWR(design)_$name] \
          -out_file [file join $directory metrics.json]
      }
      foreach report {power.rpt hierarchy.rpt annotation.rpt} {
        set path [file join $directory $report]
        if {![file exists $path] || [file size $path] == 0} {
          error "Required export is missing or empty: $path"
        }
      }
      puts $status "$PWR(design)\t$name\tCOMPLETE"
      puts "POWER_CASE_COMPLETE $PWR(design) $name"
    } detail options]} {
      set failure [open [file join $directory error.txt] w]
      puts $failure [dict get $options -errorinfo]
      close $failure
      puts $status "$PWR(design)\t$name\tFAILED"
      puts stderr "POWER_CASE_FAILED $PWR(design) $name: $detail"
    }
    flush $status
  }
  close $status
  if {[llength [info commands write_metric]]} {
    write_metric -format json -out_file [file join $PWR(output) metrics.json]
  }
  if {[llength [info commands report_metric]]} {
    report_metric -format html -out_file [file join $PWR(output) metrics.html]
  }
  puts "POWER_DESIGN_FINISHED $PWR(design)"
} detail options]} {
  puts stderr "POWER_FLOW_FAILED: $detail"
  puts stderr [dict get $options -errorinfo]
  exit 1
}
exit 0
