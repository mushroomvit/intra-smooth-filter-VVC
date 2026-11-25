All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.199791576 | 0.275084924 | 0.03323877 | 0.50811527 |
| logic | 0.435721415 | 0.508340775 | 0.040310479 | 0.984372669 |
| clock_sequential | 0.010743846 | 0.883425874 | 0.006386459 | 0.900556179 |
| clock_combinational | 0.132637841 | 0.046948882 | 0.018570247 | 0.19815697 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 2.42400696e-06, leakage -8.00054467e-15 µW. Verified tie cells are included in logic.
