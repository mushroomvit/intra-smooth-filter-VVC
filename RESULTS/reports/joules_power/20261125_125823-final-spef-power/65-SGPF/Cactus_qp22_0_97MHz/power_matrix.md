All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.319122475 | 0.380679928 | 0.063535483 | 0.763337886 |
| logic | 0.751542337 | 0.754935559 | 0.086467002 | 1.5929449 |
| clock_sequential | 0.021897455 | 1.76174495 | 0.006423784 | 1.79006619 |
| clock_combinational | 0.268371897 | 0.0923560234 | 0.03565323 | 0.39638115 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 4.21043888e-06, leakage -1.99840144e-15 µW. Verified tie cells are included in logic.
