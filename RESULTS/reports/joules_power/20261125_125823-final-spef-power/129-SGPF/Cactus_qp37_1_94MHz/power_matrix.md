All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.36582994 | 1.50371142 | 0.125806251 | 2.99534761 |
| logic | 3.0387885 | 2.5114783 | 0.23163212 | 5.78189891 |
| clock_sequential | 0.013771209 | 4.16386629 | 0.005248352 | 4.18288585 |
| clock_combinational | 0.741083441 | 0.27732026 | 0.087800241 | 1.10620394 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -3.1550058e-06, leakage -2.49938958e-14 µW. Verified tie cells are included in logic.
