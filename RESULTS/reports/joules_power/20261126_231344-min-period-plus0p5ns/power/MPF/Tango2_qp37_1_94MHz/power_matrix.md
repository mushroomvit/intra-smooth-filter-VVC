All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3412707 | 26.9774742 | 0.033280863 | 46.3520257 |
| logic | 41.1879606 | 48.8635899 | 0.040370569 | 90.0919211 |
| clock_sequential | 0.967931748 | 77.4471537 | 0.00636396 | 78.4214494 |
| clock_combinational | 11.775225 | 4.12571422 | 0.01854552 | 15.9194848 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal -7.5804469e-05, leakage -5.40019418e-14 µW. Verified tie cells are included in logic.
