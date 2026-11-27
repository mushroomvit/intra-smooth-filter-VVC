All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.341285 | 26.9775782 | 0.033280863 | 46.3521441 |
| logic | 41.1880249 | 48.8636348 | 0.040370569 | 90.0920303 |
| clock_sequential | 0.967931842 | 77.4470543 | 0.00636396 | 78.4213501 |
| clock_combinational | 11.7752256 | 4.12574369 | 0.01854552 | 15.9195148 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -4.6543136e-05, leakage 3.00107161e-15 µW. Verified tie cells are included in logic.
