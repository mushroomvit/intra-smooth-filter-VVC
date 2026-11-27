All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 46.2196699 | 25.8895352 | 0.250891904 | 72.360097 |
| logic | 38.8365009 | 19.0419272 | 0.542356625 | 58.4207848 |
| clock_sequential | 0 | 897.63332 | 0 | 897.63332 |
| clock_combinational | 183.316949 | 69.3892842 | 0.212127729 | 252.918361 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal 0.00021973783, leakage 0 µW. Verified tie cells are included in logic.
