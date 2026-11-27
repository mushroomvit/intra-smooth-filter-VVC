All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 14.5069605 | 20.6469009 | 0.033295209 | 35.1871566 |
| logic | 32.8308588 | 38.4849041 | 0.040315794 | 71.3560787 |
| clock_sequential | 0.94655247 | 76.9988206 | 0.006363136 | 77.9517362 |
| clock_combinational | 11.5166341 | 4.08454639 | 0.018526583 | 15.6197071 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal -0.000318505325, leakage -4.20011248e-14 µW. Verified tie cells are included in logic.
