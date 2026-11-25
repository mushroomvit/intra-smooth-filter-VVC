All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.375377633 | 0.520325655 | 0.033295003 | 0.928998291 |
| logic | 0.815425503 | 0.941854984 | 0.04037853 | 1.79765902 |
| clock_sequential | 0.021135763 | 1.72531581 | 0.006369405 | 1.75282098 |
| clock_combinational | 0.258327556 | 0.0915439517 | 0.018538603 | 0.368410111 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal -1.30930497e-06, leakage -7.99707522e-15 µW. Verified tie cells are included in logic.
