All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.2594655 | 2.2446853 | 0.125877409 | 4.63002821 |
| logic | 4.23264658 | 3.8848992 | 0.229837711 | 8.34738349 |
| clock_sequential | 0.028246626 | 8.3227077 | 0.005258355 | 8.35621268 |
| clock_combinational | 1.48133482 | 0.554263653 | 0.087788488 | 2.12338697 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -2.3566008e-06, leakage 1.99840144e-15 µW. Verified tie cells are included in logic.
