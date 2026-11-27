All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 47.3806295 | 26.8803129 | 0.250982614 | 74.511925 |
| logic | 42.0459224 | 20.7684256 | 0.544052421 | 63.3584004 |
| clock_sequential | 0 | 897.697038 | 0 | 897.697038 |
| clock_combinational | 183.317005 | 69.3887476 | 0.212127729 | 252.917881 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal -0.00033806252, leakage 0 µW. Verified tie cells are included in logic.
