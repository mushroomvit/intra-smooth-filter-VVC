All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.770529984 | 0.4482557 | 0.25057343 | 1.46935911 |
| logic | 0.745671906 | 0.369051277 | 0.542910995 | 1.65763418 |
| clock_sequential | 0 | 21.6763559 | 0 | 21.6763559 |
| clock_combinational | 4.42872163 | 1.67640374 | 0.212127729 | 6.3172531 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal 4.5656717e-05, leakage 0 µW. Verified tie cells are included in logic.
