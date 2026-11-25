All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.563411261 | 0.559722499 | 0.125877409 | 1.24901117 |
| logic | 1.05542546 | 0.968717603 | 0.229837711 | 2.25398077 |
| clock_sequential | 0.007043483 | 2.07532111 | 0.005258355 | 2.08762295 |
| clock_combinational | 0.36938062 | 0.138209234 | 0.087788488 | 0.595378342 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal -6.49553e-07, leakage 3.99957845e-14 µW. Verified tie cells are included in logic.
