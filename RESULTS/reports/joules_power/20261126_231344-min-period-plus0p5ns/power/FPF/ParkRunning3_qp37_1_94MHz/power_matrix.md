All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 47.3804828 | 26.8801741 | 0.250982614 | 74.5116396 |
| logic | 42.045917 | 20.7684116 | 0.544052421 | 63.3583811 |
| clock_sequential | 0 | 897.696496 | 0 | 897.696496 |
| clock_combinational | 183.316996 | 69.3890874 | 0.212127729 | 252.918211 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534564, internal 5.19666993e-06, leakage 0 µW. Verified tie cells are included in logic.
