All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.682913603 | 0.751852604 | 0.125806251 | 1.56057246 |
| logic | 1.51938215 | 1.25573256 | 0.23163212 | 3.00674683 |
| clock_sequential | 0.0068856 | 2.0819222 | 0.005248352 | 2.09405616 |
| clock_combinational | 0.370541472 | 0.138660322 | 0.087800241 | 0.597002035 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal -1.2864071e-06, leakage -9.80049375e-14 µW. Verified tie cells are included in logic.
