All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.73870797 | 3.01518879 | 0.125806251 | 5.87970302 |
| logic | 6.09327554 | 5.03592445 | 0.23163212 | 11.3608321 |
| clock_sequential | 0.027613466 | 8.34918155 | 0.005248352 | 8.38204336 |
| clock_combinational | 1.48599019 | 0.556072747 | 0.087800241 | 2.12986318 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -4.8213802e-06, leakage 4.26006452e-13 µW. Verified tie cells are included in logic.
