All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 45.5996733 | 51.8541644 | 0.125465227 | 97.579303 |
| logic | 108.619789 | 89.1771411 | 0.226646266 | 198.023577 |
| clock_sequential | 0.57216048 | 172.346862 | 0.005247699 | 172.92427 |
| clock_combinational | 30.7100921 | 11.490652 | 0.087788488 | 42.2885326 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -3.857828e-05, leakage 7.50094431e-14 µW. Verified tie cells are included in logic.
