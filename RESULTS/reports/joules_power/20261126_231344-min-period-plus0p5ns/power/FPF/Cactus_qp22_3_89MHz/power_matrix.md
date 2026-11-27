All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.595791 | 17.4320832 | 0.250343323 | 48.2782175 |
| logic | 26.6582554 | 13.2699105 | 0.539893734 | 40.4680596 |
| clock_sequential | 0 | 897.163907 | 0 | 897.163907 |
| clock_combinational | 183.317005 | 69.3883411 | 0.212127729 | 252.917474 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal -0.00074458104, leakage 0 µW. Verified tie cells are included in logic.
