All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 47.198102 | 52.5379405 | 0.1257867 | 99.8618292 |
| logic | 106.831186 | 89.5077076 | 0.230717712 | 196.569612 |
| clock_sequential | 0.571709306 | 172.531726 | 0.005247405 | 173.108683 |
| clock_combinational | 30.7142038 | 11.4923407 | 0.08778951 | 42.294334 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -1.474791e-05, leakage 1.32005518e-13 µW. Verified tie cells are included in logic.
