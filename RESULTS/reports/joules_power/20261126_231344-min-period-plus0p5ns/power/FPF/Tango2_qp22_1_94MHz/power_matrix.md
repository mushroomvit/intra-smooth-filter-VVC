All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.8943545 | 18.5546066 | 0.25057343 | 50.6995345 |
| logic | 30.8657193 | 15.2761992 | 0.542910995 | 46.6848295 |
| clock_sequential | 0 | 897.246346 | 0 | 897.246346 |
| clock_combinational | 183.316996 | 69.3892198 | 0.212127729 | 252.918344 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal 0.00013762384, leakage 0 µW. Verified tie cells are included in logic.
