All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.42751125 | 1.56683093 | 0.125621475 | 3.11996366 |
| logic | 3.17201144 | 2.6318406 | 0.229947269 | 6.03379931 |
| clock_sequential | 0.013802727 | 4.16789364 | 0.005249566 | 4.18694593 |
| clock_combinational | 0.742143008 | 0.277731588 | 0.08780599 | 1.10768059 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -4.891418e-07, leakage -4.8699933e-13 µW. Verified tie cells are included in logic.
