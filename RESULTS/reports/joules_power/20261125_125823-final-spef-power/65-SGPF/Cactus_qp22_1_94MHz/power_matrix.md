All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.638246253 | 0.761364056 | 0.063535483 | 1.46314579 |
| logic | 1.50309555 | 1.50987864 | 0.086467002 | 3.0994412 |
| clock_sequential | 0.043794929 | 3.52349829 | 0.006423784 | 3.57371701 |
| clock_combinational | 0.536744017 | 0.184700565 | 0.03565323 | 0.757097812 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal -3.1390015e-06, leakage 1.50018886e-14 µW. Verified tie cells are included in logic.
