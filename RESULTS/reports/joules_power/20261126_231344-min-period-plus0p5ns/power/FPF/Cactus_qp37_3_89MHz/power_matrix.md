All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 46.2201105 | 25.8898716 | 0.250891904 | 72.360874 |
| logic | 38.8368596 | 19.0420553 | 0.542356625 | 58.4212715 |
| clock_sequential | 0 | 897.635348 | 0 | 897.635348 |
| clock_combinational | 183.317005 | 69.3853384 | 0.212127729 | 252.914471 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal -0.00374725361, leakage 0 µW. Verified tie cells are included in logic.
