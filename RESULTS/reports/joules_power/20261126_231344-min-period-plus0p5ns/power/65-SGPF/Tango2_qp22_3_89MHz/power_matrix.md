All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.9533546 | 31.3643546 | 0.063411633 | 57.3811208 |
| logic | 62.9463382 | 62.6765744 | 0.085953047 | 125.708866 |
| clock_sequential | 1.85021093 | 148.53622 | 0.006421169 | 150.392852 |
| clock_combinational | 22.6474231 | 7.79532612 | 0.035647198 | 30.4783964 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 0.000194757223, leakage 1.70002901e-14 µW. Verified tie cells are included in logic.
