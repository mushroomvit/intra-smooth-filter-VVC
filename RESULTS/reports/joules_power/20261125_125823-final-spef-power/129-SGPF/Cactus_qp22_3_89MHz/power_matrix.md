All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.3831963 | 2.63039908 | 0.125822624 | 5.13941801 |
| logic | 5.36917783 | 4.42690128 | 0.230508006 | 10.0265871 |
| clock_sequential | 0.027587548 | 8.32194924 | 0.005247583 | 8.35478437 |
| clock_combinational | 1.4815327 | 0.554365888 | 0.08778951 | 2.1236881 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal 1.97433377e-05, leakage -2.59930966e-14 µW. Verified tie cells are included in logic.
