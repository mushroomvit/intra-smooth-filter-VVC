All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.795038937 | 0.882996645 | 0.125468375 | 1.80350396 |
| logic | 1.82805452 | 1.52775484 | 0.228245819 | 3.58405518 |
| clock_sequential | 0.007159623 | 2.17715348 | 0.005271849 | 2.18958495 |
| clock_combinational | 0.387736053 | 0.145331016 | 0.087972878 | 0.621039947 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal -1.7806605e-06, leakage -5.20000709e-14 µW. Verified tie cells are included in logic.
