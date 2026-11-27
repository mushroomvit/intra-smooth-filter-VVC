All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.9981421 | 24.7809443 | 0.03323877 | 42.8123252 |
| logic | 39.2520613 | 45.7938947 | 0.040310479 | 85.0862665 |
| clock_sequential | 0.967855288 | 79.5830889 | 0.006386459 | 80.5573307 |
| clock_combinational | 11.9486288 | 4.22913739 | 0.018570247 | 16.1963365 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal -1.6324613e-05, leakage -8.00054467e-15 µW. Verified tie cells are included in logic.
