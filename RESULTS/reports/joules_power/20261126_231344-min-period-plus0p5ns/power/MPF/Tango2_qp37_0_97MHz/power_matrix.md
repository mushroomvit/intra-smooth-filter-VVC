All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3412441 | 26.977508 | 0.033280863 | 46.352033 |
| logic | 41.1878855 | 48.8635248 | 0.040370569 | 90.0917809 |
| clock_sequential | 0.967931388 | 77.4470399 | 0.00636396 | 78.4213352 |
| clock_combinational | 11.775222 | 4.12585511 | 0.01854552 | 15.9196226 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal 6.6160786e-05, leakage -2.99760217e-15 µW. Verified tie cells are included in logic.
