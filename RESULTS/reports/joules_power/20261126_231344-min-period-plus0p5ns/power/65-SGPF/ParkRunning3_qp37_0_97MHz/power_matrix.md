All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 33.3057292 | 39.7778489 | 0.063473202 | 73.1470514 |
| logic | 76.1823993 | 75.8007691 | 0.086758095 | 152.069926 |
| clock_sequential | 1.84735439 | 147.10002 | 0.006416425 | 148.95379 |
| clock_combinational | 22.4823227 | 7.74292178 | 0.035630348 | 30.2608749 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal -0.000168096587, leakage -1.10002285e-13 µW. Verified tie cells are included in logic.
