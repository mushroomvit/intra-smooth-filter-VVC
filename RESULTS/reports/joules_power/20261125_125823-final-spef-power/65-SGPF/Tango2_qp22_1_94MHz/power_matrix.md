All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.613407336 | 0.741295124 | 0.063411633 | 1.41811409 |
| logic | 1.48772938 | 1.48135594 | 0.085953047 | 3.05503837 |
| clock_sequential | 0.043729756 | 3.51064818 | 0.006421169 | 3.56079911 |
| clock_combinational | 0.535272105 | 0.184231263 | 0.035647198 | 0.755150566 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal -6.7571182e-06, leakage 6.99440506e-15 µW. Verified tie cells are included in logic.
