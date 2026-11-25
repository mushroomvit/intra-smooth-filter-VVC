All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.843428539 | 1.04993814 | 0.063511513 | 1.9568782 |
| logic | 1.98187087 | 1.96348455 | 0.086464722 | 4.03182015 |
| clock_sequential | 0.043485921 | 3.39205501 | 0.006400194 | 3.44194113 |
| clock_combinational | 0.521834681 | 0.179989619 | 0.03559041 | 0.73741471 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal -1.63250147e-05, leakage 7.70009057e-14 µW. Verified tie cells are included in logic.
