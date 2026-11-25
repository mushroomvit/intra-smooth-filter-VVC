All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.48212903 | 0.844448867 | 0.250343323 | 2.57692122 |
| logic | 1.2913787 | 0.642820338 | 0.539893734 | 2.47409277 |
| clock_sequential | 0 | 43.460542 | 0 | 43.460542 |
| clock_combinational | 8.8802877 | 3.36141583 | 0.212127729 | 12.4538313 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 5.2585574e-05, leakage 0 µW. Verified tie cells are included in logic.
