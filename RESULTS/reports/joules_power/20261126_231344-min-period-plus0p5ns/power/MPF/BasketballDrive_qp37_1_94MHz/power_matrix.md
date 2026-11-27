All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.5933391 | 25.3702927 | 0.033345544 | 42.9969774 |
| logic | 38.839029 | 45.2546821 | 0.040378818 | 84.1340899 |
| clock_sequential | 0.949018989 | 77.6197355 | 0.006360941 | 78.5751154 |
| clock_combinational | 11.7408481 | 4.13200997 | 0.01854485 | 15.891403 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal 0.000141439819, leakage 6.9978745e-15 µW. Verified tie cells are included in logic.
