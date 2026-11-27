All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 45.5998537 | 51.8544795 | 0.125465227 | 97.5797985 |
| logic | 108.620252 | 89.1774445 | 0.226646266 | 198.024343 |
| clock_sequential | 0.572160654 | 172.347223 | 0.005247699 | 172.924631 |
| clock_combinational | 30.7101015 | 11.4903905 | 0.087788488 | 42.2882805 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -0.0003036187, leakage -1.60996216e-13 µW. Verified tie cells are included in logic.
