All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 35.6855491 | 44.4231317 | 0.063511513 | 80.1721923 |
| logic | 83.8534935 | 83.0754461 | 0.086464722 | 167.015404 |
| clock_sequential | 1.8398942 | 143.517915 | 0.006400194 | 145.364209 |
| clock_combinational | 22.0788834 | 7.61599613 | 0.03559041 | 29.7304699 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal -7.5386486e-05, leakage 7.70009057e-14 µW. Verified tie cells are included in logic.
