All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 58.8795388 | 66.6890205 | 0.125773585 | 125.694333 |
| logic | 135.578742 | 111.504582 | 0.231063309 | 247.314388 |
| clock_sequential | 0.578921313 | 174.895014 | 0.005254745 | 175.47919 |
| clock_combinational | 31.1319914 | 11.6549237 | 0.087839071 | 42.8747542 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal 0.00033962911, leakage -3.20021787e-14 µW. Verified tie cells are included in logic.
