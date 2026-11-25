All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.69120897 | 2.10529858 | 0.063511513 | 3.86001906 |
| logic | 3.97397637 | 3.93710494 | 0.086464722 | 7.99754603 |
| clock_sequential | 0.087196167 | 6.80160264 | 0.006400194 | 6.895199 |
| clock_combinational | 1.04636125 | 0.36094656 | 0.03559041 | 1.44289822 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 6.1093453e-06, leakage -3.49997809e-14 µW. Verified tie cells are included in logic.
