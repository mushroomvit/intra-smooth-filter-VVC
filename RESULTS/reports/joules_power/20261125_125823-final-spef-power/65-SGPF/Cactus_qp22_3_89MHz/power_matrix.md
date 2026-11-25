All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.27978595 | 1.52665891 | 0.063535483 | 2.86998034 |
| logic | 3.01395573 | 3.02755364 | 0.086467002 | 6.12797637 |
| clock_sequential | 0.087815771 | 7.06516568 | 0.006423784 | 7.15940524 |
| clock_combinational | 1.07625676 | 0.370353548 | 0.03565323 | 1.48226354 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal -6.6294524e-06, leakage -1.27002575e-13 µW. Verified tie cells are included in logic.
