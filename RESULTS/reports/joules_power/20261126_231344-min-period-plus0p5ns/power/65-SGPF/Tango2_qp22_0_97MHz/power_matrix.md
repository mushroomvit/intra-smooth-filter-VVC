All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.9532756 | 31.3643379 | 0.063411633 | 57.3810251 |
| logic | 62.9461057 | 62.6764068 | 0.085953047 | 125.708466 |
| clock_sequential | 1.85021034 | 148.536114 | 0.006421169 | 150.392746 |
| clock_combinational | 22.6474159 | 7.79506114 | 0.035647198 | 30.4781243 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal -6.7769124e-05, leakage 6.69950206e-14 µW. Verified tie cells are included in logic.
