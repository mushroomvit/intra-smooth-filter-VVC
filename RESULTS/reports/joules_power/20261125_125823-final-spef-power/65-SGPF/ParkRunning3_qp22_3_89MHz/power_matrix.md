All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.43976734 | 1.69527804 | 0.063447487 | 3.19849286 |
| logic | 3.31045381 | 3.32724149 | 0.086532007 | 6.72422731 |
| clock_sequential | 0.087647418 | 7.04214668 | 0.006420727 | 7.13621482 |
| clock_combinational | 1.0736064 | 0.369520603 | 0.035648029 | 1.47877503 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 2.897934e-07, leakage -2.50077736e-14 µW. Verified tie cells are included in logic.
