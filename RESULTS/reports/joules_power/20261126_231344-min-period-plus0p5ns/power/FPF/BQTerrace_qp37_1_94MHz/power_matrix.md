All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 40.2285365 | 22.5806085 | 0.250605241 | 63.0597503 |
| logic | 33.3225869 | 16.3804915 | 0.540639036 | 50.2437174 |
| clock_sequential | 0 | 897.384953 | 0 | 897.384953 |
| clock_combinational | 183.316996 | 69.3876779 | 0.212127729 | 252.916802 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal -0.0014043455, leakage 0 µW. Verified tie cells are included in logic.
