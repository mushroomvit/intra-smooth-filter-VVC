All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 3.1883663 | 3.54112141 | 0.125468375 | 6.85495609 |
| logic | 7.33114032 | 6.1268183 | 0.228245819 | 13.6862044 |
| clock_sequential | 0.028712383 | 8.73107747 | 0.005271849 | 8.7650617 |
| clock_combinational | 1.55494578 | 0.58282357 | 0.087972878 | 2.22574223 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -7.5235934e-06, leakage 1.46993528e-13 µW. Verified tie cells are included in logic.
