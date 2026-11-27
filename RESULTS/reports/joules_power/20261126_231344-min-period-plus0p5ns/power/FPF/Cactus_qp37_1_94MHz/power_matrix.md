All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 46.2199902 | 25.8898305 | 0.250891904 | 72.3607126 |
| logic | 38.8367947 | 19.0420272 | 0.542356625 | 58.4211785 |
| clock_sequential | 0 | 897.63332 | 0 | 897.63332 |
| clock_combinational | 183.316996 | 69.3911297 | 0.212127729 | 252.920254 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal 0.00204753252, leakage 0 µW. Verified tie cells are included in logic.
