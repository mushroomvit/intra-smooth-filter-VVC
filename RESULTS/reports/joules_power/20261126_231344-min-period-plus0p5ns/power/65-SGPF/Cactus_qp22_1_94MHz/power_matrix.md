All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 27.0042641 | 32.2135097 | 0.063535483 | 59.2813092 |
| logic | 63.596433 | 63.8833303 | 0.086467002 | 127.56623 |
| clock_sequential | 1.85296833 | 149.07906 | 0.006423784 | 150.938453 |
| clock_combinational | 22.7096988 | 7.81508006 | 0.03565323 | 30.5604321 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal 0.00024597732, leakage 1.50018886e-14 µW. Verified tie cells are included in logic.
