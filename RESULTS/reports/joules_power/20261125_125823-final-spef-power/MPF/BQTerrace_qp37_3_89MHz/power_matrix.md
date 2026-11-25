All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.752692127 | 1.04334024 | 0.033295003 | 1.82932737 |
| logic | 1.63506159 | 1.88857241 | 0.04037853 | 3.56401252 |
| clock_sequential | 0.042380554 | 3.45953249 | 0.006369405 | 3.50828245 |
| clock_combinational | 0.517987672 | 0.183559829 | 0.018538603 | 0.720086104 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal -2.921053e-06, leakage -3.46944695e-18 µW. Verified tie cells are included in logic.
