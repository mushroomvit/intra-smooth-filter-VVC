All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 73.4224106 | 41.4510206 | 0.251973668 | 115.125405 |
| logic | 68.2956511 | 33.0193079 | 0.552223512 | 101.867182 |
| clock_sequential | 0 | 898.734598 | 0 | 898.734598 |
| clock_combinational | 183.317005 | 69.3908508 | 0.212127729 | 252.919984 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal 0.00176511757, leakage 0 µW. Verified tie cells are included in logic.
