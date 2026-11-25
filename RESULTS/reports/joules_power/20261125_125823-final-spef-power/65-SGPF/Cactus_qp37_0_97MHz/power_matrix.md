All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.369993463 | 0.448754714 | 0.063545534 | 0.882293711 |
| logic | 0.86487948 | 0.849128604 | 0.086728985 | 1.80073707 |
| clock_sequential | 0.021844042 | 1.73990367 | 0.006417376 | 1.76816509 |
| clock_combinational | 0.265848659 | 0.0915599267 | 0.03563175 | 0.393040336 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 3.39569111e-06, leakage 3.49997809e-14 µW. Verified tie cells are included in logic.
