All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 59.221633 | 31.6706767 | 0.251138727 | 91.1434485 |
| logic | 40.5050538 | 19.5798505 | 0.540552956 | 60.6254573 |
| clock_sequential | 0 | 898.093958 | 0 | 898.093958 |
| clock_combinational | 183.316949 | 69.3884481 | 0.212127729 | 252.917525 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal -0.00061635634, leakage 0 µW. Verified tie cells are included in logic.
