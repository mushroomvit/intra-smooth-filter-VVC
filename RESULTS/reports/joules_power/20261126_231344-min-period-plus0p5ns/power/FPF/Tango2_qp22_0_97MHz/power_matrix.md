All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.8940497 | 18.5544391 | 0.25057343 | 50.6990622 |
| logic | 30.8655598 | 15.2761226 | 0.542910995 | 46.6845934 |
| clock_sequential | 0 | 897.243953 | 0 | 897.243953 |
| clock_combinational | 183.316949 | 69.3892198 | 0.212127729 | 252.918297 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal 0.00015533766, leakage 0 µW. Verified tie cells are included in logic.
