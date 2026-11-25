All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.94876682 | 1.09385908 | 0.250605241 | 3.29323114 |
| logic | 1.61421018 | 0.793503826 | 0.540639036 | 2.94835305 |
| clock_sequential | 0 | 43.4713158 | 0 | 43.4713158 |
| clock_combinational | 8.8802877 | 3.36137881 | 0.212127729 | 12.4537942 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 1.5571176e-05, leakage 0 µW. Verified tie cells are included in logic.
