All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.787182791 | 0.940151635 | 0.063473202 | 1.79080763 |
| logic | 1.80056874 | 1.79155047 | 0.086758095 | 3.6788773 |
| clock_sequential | 0.043662254 | 3.47670727 | 0.006416425 | 3.52678595 |
| clock_combinational | 0.531370117 | 0.183008876 | 0.035630348 | 0.750009341 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal 8.00371e-07, leakage -3.69981823e-14 µW. Verified tie cells are included in logic.
