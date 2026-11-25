All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.86238876 | 3.14174039 | 0.125621475 | 6.12975062 |
| logic | 6.36040408 | 5.27726877 | 0.229947269 | 11.8676201 |
| clock_sequential | 0.027676664 | 8.35729192 | 0.005249566 | 8.39021815 |
| clock_combinational | 1.48811478 | 0.556895149 | 0.08780599 | 2.13281592 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -1.8534824e-06, leakage 7.69939668e-14 µW. Verified tie cells are included in logic.
