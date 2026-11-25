All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.12682526 | 1.11945366 | 0.125877409 | 2.37215633 |
| logic | 2.11086996 | 1.9374471 | 0.229837711 | 4.27815477 |
| clock_sequential | 0.014086976 | 4.15064222 | 0.005258355 | 4.16998755 |
| clock_combinational | 0.73876174 | 0.276418469 | 0.087788488 | 1.1029687 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -1.4941059e-06, leakage -3.90007471e-13 µW. Verified tie cells are included in logic.
