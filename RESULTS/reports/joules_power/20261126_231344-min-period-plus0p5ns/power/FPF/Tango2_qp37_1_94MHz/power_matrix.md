All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 73.4222623 | 41.4510007 | 0.251973668 | 115.125237 |
| logic | 68.2953915 | 33.019213 | 0.552223512 | 101.866828 |
| clock_sequential | 0 | 898.736529 | 0 | 898.736529 |
| clock_combinational | 183.316996 | 69.3880395 | 0.212127729 | 252.917163 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal -0.00104271713, leakage 0 µW. Verified tie cells are included in logic.
