All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 47.3801536 | 26.8799992 | 0.250982614 | 74.5111354 |
| logic | 42.0455356 | 20.7682682 | 0.544052421 | 63.3578563 |
| clock_sequential | 0 | 897.694372 | 0 | 897.694372 |
| clock_combinational | 183.316949 | 69.3911787 | 0.212127729 | 252.920256 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal 0.00211418497, leakage 0 µW. Verified tie cells are included in logic.
