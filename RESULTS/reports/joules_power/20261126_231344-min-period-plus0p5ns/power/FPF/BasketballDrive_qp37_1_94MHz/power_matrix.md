All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 59.2219404 | 31.6707851 | 0.251138727 | 91.1438642 |
| logic | 40.5051366 | 19.5798901 | 0.540552956 | 60.6255796 |
| clock_sequential | 0 | 898.093958 | 0 | 898.093958 |
| clock_combinational | 183.316996 | 69.3920608 | 0.212127729 | 252.921185 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal 0.00297859433, leakage 0 µW. Verified tie cells are included in logic.
