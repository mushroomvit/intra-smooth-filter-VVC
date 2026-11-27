All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 47.1979253 | 52.537629 | 0.1257867 | 99.861341 |
| logic | 106.83075 | 89.5074226 | 0.230717712 | 196.56889 |
| clock_sequential | 0.57170913 | 172.531818 | 0.005247405 | 173.108775 |
| clock_combinational | 30.7141944 | 11.4924903 | 0.08778951 | 42.2944743 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal 0.00013839453, leakage -2.86992652e-13 µW. Verified tie cells are included in logic.
