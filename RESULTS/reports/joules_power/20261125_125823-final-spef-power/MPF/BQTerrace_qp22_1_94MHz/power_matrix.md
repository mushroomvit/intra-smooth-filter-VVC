All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.361206538 | 0.458344217 | 0.033251384 | 0.852802139 |
| logic | 0.712755134 | 0.926368909 | 0.040194786 | 1.67931883 |
| clock_sequential | 0.021773835 | 1.83279565 | 0.006402026 | 1.86097151 |
| clock_combinational | 0.272826403 | 0.0972158555 | 0.018610353 | 0.388652612 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal -5.7064742e-06, leakage -4.00027234e-14 µW. Verified tie cells are included in logic.
