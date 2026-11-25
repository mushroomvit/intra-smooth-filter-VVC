All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.78978736 | 1.03400759 | 0.250667015 | 3.07446197 |
| logic | 1.69353138 | 0.84708144 | 0.543158119 | 3.08377094 |
| clock_sequential | 0 | 43.4703215 | 0 | 43.4703215 |
| clock_combinational | 8.8802877 | 3.36148206 | 0.212127729 | 12.4538975 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 0.000118821374, leakage 0 µW. Verified tie cells are included in logic.
