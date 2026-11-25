All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.567696583 | 0.631918294 | 0.1257867 | 1.32540158 |
| logic | 1.28494762 | 1.0765875 | 0.230717712 | 2.59225283 |
| clock_sequential | 0.006876511 | 2.07520963 | 0.005247405 | 2.08733355 |
| clock_combinational | 0.369429964 | 0.138232707 | 0.08778951 | 0.595452181 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal 2.8397878e-06, leakage -2.86992652e-13 µW. Verified tie cells are included in logic.
