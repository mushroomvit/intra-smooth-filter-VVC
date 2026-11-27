All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 59.3410599 | 65.1325735 | 0.125621475 | 124.599255 |
| logic | 131.859642 | 109.404848 | 0.229947269 | 241.494438 |
| clock_sequential | 0.57377502 | 173.258178 | 0.005249566 | 173.837203 |
| clock_combinational | 30.8506498 | 11.5450024 | 0.08780599 | 42.4834582 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -0.00023229129, leakage -1.10994547e-13 µW. Verified tie cells are included in logic.
