All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 35.6855768 | 44.4232289 | 0.063511513 | 80.1723172 |
| logic | 83.8535789 | 83.0755055 | 0.086464722 | 167.015549 |
| clock_sequential | 1.83989429 | 143.51783 | 0.006400194 | 145.364125 |
| clock_combinational | 22.0788845 | 7.61607024 | 0.03559041 | 29.7305451 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal -1.66119399e-06, leakage -3.49997809e-14 µW. Verified tie cells are included in logic.
