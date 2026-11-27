All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 16.9078689 | 23.4367497 | 0.033295003 | 40.3779136 |
| logic | 36.728766 | 42.4234224 | 0.04037853 | 79.1925669 |
| clock_sequential | 0.952003414 | 77.7121045 | 0.006369405 | 78.6704773 |
| clock_combinational | 11.6356673 | 4.1233539 | 0.018538603 | 15.7775598 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal -5.5257328e-05, leakage -7.99707522e-15 µW. Verified tie cells are included in logic.
