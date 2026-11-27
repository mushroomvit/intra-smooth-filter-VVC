All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.9981821 | 24.780995 | 0.03323877 | 42.8124158 |
| logic | 39.252148 | 45.7939829 | 0.040310479 | 85.0864413 |
| clock_sequential | 0.967855586 | 79.5832394 | 0.006386459 | 80.5574815 |
| clock_combinational | 11.9486325 | 4.22910015 | 0.018570247 | 16.1963029 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -5.4872847e-05, leakage -5.50011425e-14 µW. Verified tie cells are included in logic.
