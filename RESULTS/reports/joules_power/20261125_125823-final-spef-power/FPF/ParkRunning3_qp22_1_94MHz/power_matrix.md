All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.892587509 | 0.515670507 | 0.250667015 | 1.65892503 |
| logic | 0.844577915 | 0.422446519 | 0.543158119 | 1.81018255 |
| clock_sequential | 0 | 21.6792529 | 0 | 21.6792529 |
| clock_combinational | 4.42872163 | 1.67633186 | 0.212127729 | 6.31718122 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal -2.6220772e-05, leakage 0 µW. Verified tie cells are included in logic.
