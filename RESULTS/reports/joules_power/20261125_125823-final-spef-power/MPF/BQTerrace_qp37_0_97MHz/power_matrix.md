All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.187688537 | 0.260161618 | 0.033295003 | 0.481145158 |
| logic | 0.407710461 | 0.470925508 | 0.04037853 | 0.919014499 |
| clock_sequential | 0.010567876 | 0.86265768 | 0.006369405 | 0.879594961 |
| clock_combinational | 0.129163721 | 0.0457720507 | 0.018538603 | 0.193474375 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal -5.6029369e-07, leakage -1.79994908e-14 µW. Verified tie cells are included in logic.
