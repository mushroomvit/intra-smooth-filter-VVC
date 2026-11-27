All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 35.4977131 | 19.0806364 | 0.250477949 | 54.8288275 |
| logic | 23.580822 | 11.6835492 | 0.53817256 | 35.8025437 |
| clock_sequential | 0 | 897.365131 | 0 | 897.365131 |
| clock_combinational | 183.316949 | 69.3891209 | 0.212127729 | 252.918198 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal 5.64428101e-05, leakage 0 µW. Verified tie cells are included in logic.
