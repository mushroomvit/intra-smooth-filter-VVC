All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.645811498 | 0.919144143 | 0.033295209 | 1.59825085 |
| logic | 1.46154068 | 1.71324345 | 0.040315794 | 3.21509993 |
| clock_sequential | 0.042137904 | 3.42778549 | 0.006363136 | 3.47628653 |
| clock_combinational | 0.512688781 | 0.181850997 | 0.018526583 | 0.713066361 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 4.081695e-06, leakage -5.99867378e-15 µW. Verified tie cells are included in logic.
