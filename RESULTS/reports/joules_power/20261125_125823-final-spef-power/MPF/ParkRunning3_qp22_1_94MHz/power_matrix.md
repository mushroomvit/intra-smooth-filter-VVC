All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.399583782 | 0.550168346 | 0.03323877 | 0.982990898 |
| logic | 0.871447371 | 1.01668542 | 0.040310479 | 1.92844327 |
| clock_sequential | 0.021487702 | 1.76685238 | 0.006386459 | 1.79472655 |
| clock_combinational | 0.265275794 | 0.0938975078 | 0.018570247 | 0.377743549 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 4.55081811e-06, leakage 4.00374178e-15 µW. Verified tie cells are included in logic.
