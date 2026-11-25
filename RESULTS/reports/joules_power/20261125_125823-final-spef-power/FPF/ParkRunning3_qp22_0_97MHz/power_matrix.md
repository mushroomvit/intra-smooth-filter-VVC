All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.446288917 | 0.257831817 | 0.250667015 | 0.954787749 |
| logic | 0.422281261 | 0.211220769 | 0.543158119 | 1.17666015 |
| clock_sequential | 0 | 10.8396265 | 0 | 10.8396265 |
| clock_combinational | 2.21436024 | 0.838165932 | 0.212127729 | 3.2646539 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal -1.28948824e-05, leakage 0 µW. Verified tie cells are included in logic.
