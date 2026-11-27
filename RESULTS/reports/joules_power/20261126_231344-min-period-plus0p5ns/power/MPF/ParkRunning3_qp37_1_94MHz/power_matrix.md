All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3837782 | 26.6070809 | 0.033262566 | 46.0241217 |
| logic | 41.0602456 | 48.2655295 | 0.040285698 | 89.3660608 |
| clock_sequential | 0.962251094 | 78.9299251 | 0.006378411 | 79.8985546 |
| clock_combinational | 11.8956264 | 4.19861907 | 0.018563059 | 16.1128085 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal 3.3105605e-05, leakage -6.30016872e-14 µW. Verified tie cells are included in logic.
