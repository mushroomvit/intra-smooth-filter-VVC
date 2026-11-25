All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.322074786 | 0.458389589 | 0.033295209 | 0.813759584 |
| logic | 0.728888033 | 0.854416061 | 0.040315794 | 1.62361989 |
| clock_sequential | 0.02101475 | 1.70948288 | 0.006363136 | 1.73686077 |
| clock_combinational | 0.255684921 | 0.0906915463 | 0.018526583 | 0.36490305 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 1.99731901e-06, leakage 8.20003787e-14 µW. Verified tie cells are included in logic.
