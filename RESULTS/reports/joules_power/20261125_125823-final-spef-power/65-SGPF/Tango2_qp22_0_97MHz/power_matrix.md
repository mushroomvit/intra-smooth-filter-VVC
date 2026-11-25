All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.30670305 | 0.370645204 | 0.063411633 | 0.740759887 |
| logic | 0.743859465 | 0.740674367 | 0.085953047 | 1.57048688 |
| clock_sequential | 0.021864868 | 1.75532107 | 0.006421169 | 1.78360711 |
| clock_combinational | 0.267635941 | 0.092115473 | 0.035647198 | 0.395398612 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal -3.49804323e-06, leakage 6.69950206e-14 µW. Verified tie cells are included in logic.
