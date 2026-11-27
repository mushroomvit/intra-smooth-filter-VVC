All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 33.305784 | 39.7779874 | 0.063473202 | 73.1472446 |
| logic | 76.1825943 | 75.8009031 | 0.086758095 | 152.070256 |
| clock_sequential | 1.84735487 | 147.099857 | 0.006416425 | 148.953629 |
| clock_combinational | 22.4823286 | 7.74289512 | 0.035630348 | 30.260854 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal -0.000196753393, leakage -3.69981823e-14 µW. Verified tie cells are included in logic.
