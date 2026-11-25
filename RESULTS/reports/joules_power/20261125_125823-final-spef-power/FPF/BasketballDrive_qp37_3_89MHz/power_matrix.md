All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.86885422 | 1.53421323 | 0.251138727 | 4.65420618 |
| logic | 1.96215015 | 0.948489545 | 0.540552956 | 3.45119265 |
| clock_sequential | 0 | 43.5057879 | 0 | 43.5057879 |
| clock_combinational | 8.8802877 | 3.36134332 | 0.212127729 | 12.4537587 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal -1.992166e-05, leakage 0 µW. Verified tie cells are included in logic.
