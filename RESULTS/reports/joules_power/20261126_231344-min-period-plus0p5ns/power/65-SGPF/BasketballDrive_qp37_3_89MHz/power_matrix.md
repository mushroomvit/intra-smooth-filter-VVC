All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.2027165 | 40.1782918 | 0.063599861 | 71.4446081 |
| logic | 77.1560913 | 73.4552821 | 0.086873623 | 150.698247 |
| clock_sequential | 1.84340757 | 145.115644 | 0.006408084 | 146.965459 |
| clock_combinational | 22.2591399 | 7.67255509 | 0.035608195 | 29.9673032 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal -0.000413706808, leakage -2.99760217e-15 µW. Verified tie cells are included in logic.
