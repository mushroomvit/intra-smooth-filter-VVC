All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.430346188 | 0.59071544 | 0.033262566 | 1.05432419 |
| logic | 0.911589966 | 1.07155766 | 0.040285698 | 2.02343332 |
| clock_sequential | 0.021363275 | 1.75235493 | 0.006378411 | 1.78009661 |
| clock_combinational | 0.264098998 | 0.0932158073 | 0.018563059 | 0.375877864 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 1.51925695e-06, leakage -6.30016872e-14 µW. Verified tie cells are included in logic.
