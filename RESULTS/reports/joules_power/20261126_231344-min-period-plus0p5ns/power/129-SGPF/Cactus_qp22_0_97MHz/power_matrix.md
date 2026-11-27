All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 49.4067157 | 54.5317516 | 0.125822624 | 104.06429 |
| logic | 111.310252 | 91.7755896 | 0.230508006 | 203.316349 |
| clock_sequential | 0.571927515 | 172.525722 | 0.005247583 | 173.102897 |
| clock_combinational | 30.7141944 | 11.4923169 | 0.08778951 | 42.2943008 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -3.504787e-05, leakage -4.78006523e-13 µW. Verified tie cells are included in logic.
