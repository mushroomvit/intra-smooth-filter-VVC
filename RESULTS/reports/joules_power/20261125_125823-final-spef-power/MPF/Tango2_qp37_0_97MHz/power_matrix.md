All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.214700921 | 0.299467276 | 0.033280863 | 0.54744906 |
| logic | 0.457210326 | 0.542415846 | 0.040370569 | 1.03999674 |
| clock_sequential | 0.010744692 | 0.859713578 | 0.00636396 | 0.87682223 |
| clock_combinational | 0.130712907 | 0.0457995635 | 0.01854552 | 0.195057991 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 5.2353368e-07, leakage -2.99760217e-15 µW. Verified tie cells are included in logic.
