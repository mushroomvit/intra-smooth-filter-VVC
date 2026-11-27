All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 56.7771081 | 62.5091196 | 0.125806251 | 119.412034 |
| logic | 126.322044 | 104.401661 | 0.23163212 | 230.955337 |
| clock_sequential | 0.572464974 | 173.090401 | 0.005248352 | 173.668114 |
| clock_combinational | 30.806612 | 11.5280664 | 0.087800241 | 42.4224787 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal -0.00018320378, leakage -2.49938958e-14 µW. Verified tie cells are included in logic.
