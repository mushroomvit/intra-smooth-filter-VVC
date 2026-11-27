All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.593313 | 25.3702539 | 0.033345544 | 42.9969124 |
| logic | 38.8389688 | 45.2546179 | 0.040378818 | 84.1339655 |
| clock_sequential | 0.949018746 | 77.6197355 | 0.006360941 | 78.5751152 |
| clock_combinational | 11.7408452 | 4.13181582 | 0.01854485 | 15.8912058 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal -5.167034e-05, leakage -5.39984724e-14 µW. Verified tie cells are included in logic.
