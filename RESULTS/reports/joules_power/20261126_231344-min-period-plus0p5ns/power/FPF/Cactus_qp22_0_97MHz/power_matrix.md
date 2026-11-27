All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.5955857 | 17.4319608 | 0.250343323 | 48.2778898 |
| logic | 26.6580507 | 13.2698336 | 0.539893734 | 40.4677781 |
| clock_sequential | 0 | 897.16615 | 0 | 897.16615 |
| clock_combinational | 183.316949 | 69.3857958 | 0.212127729 | 252.914873 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345425, internal -0.00326873573, leakage 0 µW. Verified tie cells are included in logic.
