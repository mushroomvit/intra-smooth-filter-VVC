All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.27665141 | 2.53421519 | 0.1257867 | 4.93665329 |
| logic | 5.15310563 | 4.31749359 | 0.230717712 | 9.70131694 |
| clock_sequential | 0.027577014 | 8.32226973 | 0.005247405 | 8.35509415 |
| clock_combinational | 1.48153271 | 0.554323869 | 0.08778951 | 2.12364608 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -2.22764179e-05, leakage 1.32005518e-13 µW. Verified tie cells are included in logic.
