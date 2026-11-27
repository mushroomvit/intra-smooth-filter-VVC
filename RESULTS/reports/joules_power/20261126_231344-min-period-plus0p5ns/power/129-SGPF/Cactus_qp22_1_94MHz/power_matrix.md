All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 49.40685 | 54.5318736 | 0.125822624 | 104.064546 |
| logic | 111.310522 | 91.7757753 | 0.230508006 | 203.316805 |
| clock_sequential | 0.57192766 | 172.525112 | 0.005247583 | 173.102287 |
| clock_combinational | 30.7142023 | 11.4923169 | 0.08778951 | 42.2943087 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal -3.7993e-05, leakage 1.19904087e-14 µW. Verified tie cells are included in logic.
