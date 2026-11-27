All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.083558 | 31.0292404 | 0.063545337 | 56.1763437 |
| logic | 60.7563801 | 60.0002636 | 0.086624888 | 120.843269 |
| clock_sequential | 1.84854147 | 147.44156 | 0.006417911 | 149.296519 |
| clock_combinational | 22.5223508 | 7.75586255 | 0.035634355 | 30.3138477 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal 7.98882e-05, leakage 7.5994766e-14 µW. Verified tie cells are included in logic.
