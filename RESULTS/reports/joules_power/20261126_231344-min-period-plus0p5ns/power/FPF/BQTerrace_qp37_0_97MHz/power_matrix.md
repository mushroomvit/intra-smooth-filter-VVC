All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 40.2284132 | 22.5805376 | 0.250605241 | 63.059556 |
| logic | 33.3223418 | 16.3804142 | 0.540639036 | 50.2433951 |
| clock_sequential | 0 | 897.384953 | 0 | 897.384953 |
| clock_combinational | 183.316949 | 69.3876779 | 0.212127729 | 252.916755 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal -0.00138663149, leakage 0 µW. Verified tie cells are included in logic.
