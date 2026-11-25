All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.861020461 | 1.20096536 | 0.033280863 | 2.09526668 |
| logic | 1.83357433 | 2.17527164 | 0.040370569 | 4.04921654 |
| clock_sequential | 0.043089643 | 3.44772614 | 0.00636396 | 3.49717974 |
| clock_combinational | 0.524200398 | 0.183670883 | 0.01854552 | 0.726416801 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 2.1424649e-06, leakage 3.00107161e-15 µW. Verified tie cells are included in logic.
