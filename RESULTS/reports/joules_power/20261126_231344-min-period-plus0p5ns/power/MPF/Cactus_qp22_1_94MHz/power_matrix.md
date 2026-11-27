All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 15.2219174 | 21.423482 | 0.033289599 | 36.678689 |
| logic | 34.7427668 | 40.1526366 | 0.040373299 | 74.9357767 |
| clock_sequential | 0.952388819 | 77.7961039 | 0.006369712 | 78.7548625 |
| clock_combinational | 11.6155051 | 4.12506298 | 0.018537894 | 15.7591059 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal 2.66023e-05, leakage 9.39977263e-14 µW. Verified tie cells are included in logic.
