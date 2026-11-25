All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.18060297 | 0.229170937 | 0.033251384 | 0.443025291 |
| logic | 0.356375137 | 0.463182316 | 0.040194786 | 0.859752239 |
| clock_sequential | 0.010886912 | 0.916397462 | 0.006402026 | 0.9336864 |
| clock_combinational | 0.136413145 | 0.048608138 | 0.018610353 | 0.203631636 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal -2.62202889e-06, leakage -8.00054467e-15 µW. Verified tie cells are included in logic.
