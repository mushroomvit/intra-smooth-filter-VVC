All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 49.4069244 | 54.5320611 | 0.125822624 | 104.064808 |
| logic | 111.31064 | 91.7758726 | 0.230508006 | 203.31702 |
| clock_sequential | 0.57192769 | 172.525703 | 0.005247583 | 173.102878 |
| clock_combinational | 30.7142038 | 11.4923485 | 0.08778951 | 42.2943418 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -6.98469999e-06, leakage -2.59930966e-14 µW. Verified tie cells are included in logic.
