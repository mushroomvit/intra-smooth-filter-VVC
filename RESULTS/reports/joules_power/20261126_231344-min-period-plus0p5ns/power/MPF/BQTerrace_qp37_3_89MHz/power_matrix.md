All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 16.9078822 | 23.4367867 | 0.033295003 | 40.377964 |
| logic | 36.7288007 | 42.4234562 | 0.04037853 | 79.1926354 |
| clock_sequential | 0.952003465 | 77.7120445 | 0.006369405 | 78.6704174 |
| clock_combinational | 11.635668 | 4.12348821 | 0.018538603 | 15.7776948 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal 7.8830363e-05, leakage -3.46944695e-18 µW. Verified tie cells are included in logic.
