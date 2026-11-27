All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 36.9462476 | 21.3448371 | 0.250667015 | 58.5417517 |
| logic | 34.9595146 | 17.4863163 | 0.543158119 | 52.988989 |
| clock_sequential | 0 | 897.364193 | 0 | 897.364193 |
| clock_combinational | 183.316949 | 69.3875272 | 0.212127729 | 252.916604 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal -0.00153733001, leakage 0 µW. Verified tie cells are included in logic.
