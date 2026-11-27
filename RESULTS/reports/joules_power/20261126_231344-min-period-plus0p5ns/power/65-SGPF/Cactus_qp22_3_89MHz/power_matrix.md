All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 27.0042912 | 32.2134912 | 0.063535483 | 59.2813178 |
| logic | 63.596504 | 63.88339 | 0.086467002 | 127.566361 |
| clock_sequential | 1.85296842 | 149.079495 | 0.006423784 | 150.938887 |
| clock_combinational | 22.7096998 | 7.81490929 | 0.03565323 | 30.5602623 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 7.4854199e-05, leakage -1.27002575e-13 µW. Verified tie cells are included in logic.
