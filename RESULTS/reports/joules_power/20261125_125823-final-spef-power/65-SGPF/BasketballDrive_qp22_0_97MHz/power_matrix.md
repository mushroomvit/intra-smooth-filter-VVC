All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.296425138 | 0.36668572 | 0.063545337 | 0.726656195 |
| logic | 0.717982006 | 0.709048771 | 0.086624888 | 1.51365566 |
| clock_sequential | 0.021845146 | 1.74238926 | 0.006417911 | 1.77065232 |
| clock_combinational | 0.266157979 | 0.0916554699 | 0.035634355 | 0.393447804 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 1.47385662e-06, leakage 7.5994766e-14 µW. Verified tie cells are included in logic.
