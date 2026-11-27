All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.5850031 | 28.2559501 | 0.063578383 | 53.9045316 |
| logic | 51.12621 | 57.290698 | 0.086513735 | 108.503422 |
| clock_sequential | 1.83184315 | 149.441398 | 0.006408328 | 151.279649 |
| clock_combinational | 22.77379 | 7.83469689 | 0.035659543 | 30.6441464 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal -0.000190698782, leakage -6.99440506e-15 µW. Verified tie cells are included in logic.
