All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 36.9468225 | 21.3451441 | 0.250667015 | 58.5426336 |
| logic | 34.9599858 | 17.4864854 | 0.543158119 | 52.9896293 |
| clock_sequential | 0 | 897.363942 | 0 | 897.363942 |
| clock_combinational | 183.317005 | 69.3898926 | 0.212127729 | 252.919026 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal 0.00080697306, leakage 0 µW. Verified tie cells are included in logic.
