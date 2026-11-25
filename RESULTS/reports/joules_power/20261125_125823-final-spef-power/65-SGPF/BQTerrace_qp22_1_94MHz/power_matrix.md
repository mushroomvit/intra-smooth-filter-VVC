All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.604703226 | 0.667830687 | 0.063578383 | 1.3361123 |
| logic | 1.20836728 | 1.35406505 | 0.086513735 | 2.64894607 |
| clock_sequential | 0.043295646 | 3.53204657 | 0.006408328 | 3.58175055 |
| clock_combinational | 0.538258955 | 0.185182944 | 0.035659543 | 0.759101442 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal 5.2292217e-06, leakage 9.00668429e-15 µW. Verified tie cells are included in logic.
