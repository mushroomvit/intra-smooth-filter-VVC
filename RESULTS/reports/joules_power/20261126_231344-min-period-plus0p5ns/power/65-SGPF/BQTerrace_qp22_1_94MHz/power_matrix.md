All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.5850553 | 28.2560441 | 0.063578383 | 53.9046778 |
| logic | 51.1263973 | 57.2908175 | 0.086513735 | 108.503729 |
| clock_sequential | 1.83184362 | 149.441184 | 0.006408328 | 151.279436 |
| clock_combinational | 22.7737959 | 7.83466302 | 0.035659543 | 30.6441184 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal -0.0002265832, leakage 9.00668429e-15 µW. Verified tie cells are included in logic.
