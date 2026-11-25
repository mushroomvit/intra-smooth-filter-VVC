All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.26909365 | 1.41057324 | 0.125608454 | 2.80527534 |
| logic | 2.88606039 | 2.36884309 | 0.229205113 | 5.48410859 |
| clock_sequential | 0.013774858 | 4.14934739 | 0.005248121 | 4.16837037 |
| clock_combinational | 0.738953916 | 0.276487869 | 0.08778951 | 1.10323129 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -5.8320119e-06, leakage 2.39003262e-13 µW. Verified tie cells are included in logic.
