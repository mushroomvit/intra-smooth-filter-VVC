All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.737476067 | 0.949610819 | 0.063599861 | 1.75068675 |
| logic | 1.8235757 | 1.73611036 | 0.086873623 | 3.64655968 |
| clock_sequential | 0.043568958 | 3.42981118 | 0.006408084 | 3.47978822 |
| clock_combinational | 0.526095022 | 0.181348374 | 0.035608195 | 0.743051591 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal -2.328204e-06, leakage 5.99520433e-15 µW. Verified tie cells are included in logic.
