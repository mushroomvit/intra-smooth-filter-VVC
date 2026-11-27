All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3163832 | 11.8761403 | 0.250104346 | 31.4426279 |
| logic | 23.5448242 | 12.0091888 | 0.5414948 | 36.0955078 |
| clock_sequential | 0 | 896.914478 | 0 | 896.914478 |
| clock_combinational | 183.316949 | 69.3895933 | 0.212127729 | 252.91867 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal 0.00052879338, leakage 0 µW. Verified tie cells are included in logic.
