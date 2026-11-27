# Routed power breakdown

120 cases with detailed switching, internal and leakage power in µW. Each case uses its routed Innovus netlist and matched detailed SPEF.

Sequential combines native register and latch power. Clock-sequential uses native `clock_seq`, with register/latch clock-pin power assigned to the clock network (`-assign2clk`). Clock-combinational is native aggregate `clock` minus `clock_seq`, retaining additional clock-network contributions omitted by cell-only `clock_comb`. Logic includes native `logic` and tie cells whose leaf reports verify their identity. Native category reports and per-case matrices are retained.

Activity comes from the updated RTL VCDs propagated through the routed netlist; this is not SDF-backannotated gate simulation.

The tables below show the case with the largest total average power for each design. All cases are in `power_detail.csv` and `power_detail_wide.csv`.

## 129-SGPF — Tango2_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 66.099202 | 73.412153 | 0.125468375 | 139.636823 |
| logic | 151.984857 | 127.017499 | 0.228245819 | 279.230602 |
| clock_sequential | 0.595247096 | 181.006814 | 0.005271849 | 181.607333 |
| clock_combinational | 32.2361597 | 12.0828332 | 0.087972878 | 44.4069658 |

## 65-SGPF — Tango2_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 35.6855768 | 44.4232289 | 0.063511513 | 80.1723172 |
| logic | 83.8535789 | 83.0755055 | 0.086464722 | 167.015549 |
| clock_sequential | 1.83989429 | 143.51783 | 0.006400194 | 145.364125 |
| clock_combinational | 22.0788845 | 7.61607024 | 0.03559041 | 29.7305451 |

## FPF — Tango2_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 73.4224106 | 41.4510206 | 0.251973668 | 115.125405 |
| logic | 68.2956511 | 33.0193079 | 0.552223512 | 101.867182 |
| clock_sequential | 0 | 898.734598 | 0 | 898.734598 |
| clock_combinational | 183.317005 | 69.3908508 | 0.212127729 | 252.919984 |

## MPF — ParkRunning3_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 19.3837913 | 26.6071866 | 0.033262566 | 46.0242405 |
| logic | 41.0602926 | 48.2655657 | 0.040285698 | 89.366144 |
| clock_sequential | 0.962251141 | 78.930184 | 0.006378411 | 79.8988136 |
| clock_combinational | 11.895627 | 4.19859831 | 0.018563059 | 16.1127883 |

