All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.43073216 | 0.765126226 | 0.251138727 | 2.44699711 |
| logic | 0.978542887 | 0.473020538 | 0.540552956 | 1.99211638 |
| clock_sequential | 0 | 21.6969408 | 0 | 21.6969408 |
| clock_combinational | 4.42872163 | 1.67634861 | 0.212127729 | 6.31719796 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal -9.477319e-06, leakage 0 µW. Verified tie cells are included in logic.
