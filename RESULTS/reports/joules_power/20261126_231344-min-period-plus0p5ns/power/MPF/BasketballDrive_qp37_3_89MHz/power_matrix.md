All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.5933529 | 25.3703127 | 0.033345544 | 42.9970111 |
| logic | 38.8390502 | 45.2547108 | 0.040378818 | 84.1341398 |
| clock_sequential | 0.949019039 | 77.6197521 | 0.006360941 | 78.5751321 |
| clock_combinational | 11.7408488 | 4.13168058 | 0.01854485 | 15.8910742 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -0.000188179947, leakage -1.10016163e-14 µW. Verified tie cells are included in logic.
