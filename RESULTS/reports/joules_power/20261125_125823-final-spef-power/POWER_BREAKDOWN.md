# Routed power breakdown

120 cases with detailed switching, internal and leakage power in µW. Each case uses its routed Innovus netlist and matched detailed SPEF.

Sequential combines native register and latch power. Clock-sequential uses native `clock_seq`, with register/latch clock-pin power assigned to the clock network (`-assign2clk`). Clock-combinational is native aggregate `clock` minus `clock_seq`, retaining additional clock-network contributions omitted by cell-only `clock_comb`. Logic includes native `logic` and tie cells whose leaf reports verify their identity. Native category reports and per-case matrices are retained.

Activity comes from the updated RTL VCDs propagated through the routed netlist; this is not SDF-backannotated gate simulation.

The tables below show the case with the largest total average power for each design. All cases are in `power_detail.csv` and `power_detail_wide.csv`.

## 129-SGPF — Tango2_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 3.1883663 | 3.54112141 | 0.125468375 | 6.85495609 |
| logic | 7.33114032 | 6.1268183 | 0.228245819 | 13.6862044 |
| clock_sequential | 0.028712383 | 8.73107747 | 0.005271849 | 8.7650617 |
| clock_combinational | 1.55494578 | 0.58282357 | 0.087972878 | 2.22574223 |

## 65-SGPF — Tango2_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 1.69120897 | 2.10529858 | 0.063511513 | 3.86001906 |
| logic | 3.97397637 | 3.93710494 | 0.086464722 | 7.99754603 |
| clock_sequential | 0.087196167 | 6.80160264 | 0.006400194 | 6.895199 |
| clock_combinational | 1.04636125 | 0.36094656 | 0.03559041 | 1.44289822 |

## FPF — Tango2_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 3.5567469 | 2.00797695 | 0.251973668 | 5.81669752 |
| logic | 3.30837609 | 1.59952155 | 0.552223512 | 5.46012115 |
| clock_sequential | 0 | 43.5368044 | 0 | 43.5368044 |
| clock_combinational | 8.8802877 | 3.36136466 | 0.212127729 | 12.4537801 |

## MPF — ParkRunning3_qp37_3_89MHz

| Category | Switching (µW) | Internal (µW) | Leakage (µW) | Total (µW) |
|---|---:|---:|---:|---:|
| sequential | 0.862912744 | 1.18447533 | 0.033262566 | 2.08065064 |
| logic | 1.82788779 | 2.148647 | 0.040285698 | 4.01682049 |
| clock_sequential | 0.042836753 | 3.51375299 | 0.006378411 | 3.56296816 |
| clock_combinational | 0.529560318 | 0.186912034 | 0.018563059 | 0.735035411 |

