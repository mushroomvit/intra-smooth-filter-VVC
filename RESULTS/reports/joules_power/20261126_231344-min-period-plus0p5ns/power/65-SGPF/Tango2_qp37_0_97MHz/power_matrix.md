All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 35.685496 | 44.423045 | 0.063511513 | 80.1720525 |
| logic | 83.8533761 | 83.0753406 | 0.086464722 | 167.015181 |
| clock_sequential | 1.83989372 | 143.51822 | 0.006400194 | 145.364514 |
| clock_combinational | 22.0788776 | 7.61598127 | 0.03559041 | 29.7304493 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal -8.8268597e-05, leakage 0 µW. Verified tie cells are included in logic.
