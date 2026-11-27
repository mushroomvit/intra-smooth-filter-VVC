All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.5957157 | 17.4320137 | 0.250343323 | 48.2780727 |
| logic | 26.6581132 | 13.2698643 | 0.539893734 | 40.4678712 |
| clock_sequential | 0 | 897.16469 | 0 | 897.16469 |
| clock_combinational | 183.316996 | 69.3889373 | 0.212127729 | 252.918061 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345638, internal -0.0001448694, leakage 0 µW. Verified tie cells are included in logic.
