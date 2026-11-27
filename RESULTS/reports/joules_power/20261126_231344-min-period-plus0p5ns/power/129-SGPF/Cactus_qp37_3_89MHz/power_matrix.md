All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 56.7771682 | 62.5090047 | 0.125806251 | 119.411979 |
| logic | 126.32224 | 104.401771 | 0.23163212 | 230.955643 |
| clock_sequential | 0.572465007 | 173.09018 | 0.005248352 | 173.667893 |
| clock_combinational | 30.8066138 | 11.5281888 | 0.087800241 | 42.4226028 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -6.153208e-05, leakage 4.26006452e-13 µW. Verified tie cells are included in logic.
