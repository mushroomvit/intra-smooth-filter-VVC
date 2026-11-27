All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.9981688 | 24.7809859 | 0.03323877 | 42.8123934 |
| logic | 39.252103 | 45.7939453 | 0.040310479 | 85.0863587 |
| clock_sequential | 0.967855536 | 79.5834175 | 0.006386459 | 80.5576595 |
| clock_combinational | 11.9486319 | 4.22912585 | 0.018570247 | 16.196328 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal -2.8943682e-05, leakage 4.00374178e-15 µW. Verified tie cells are included in logic.
