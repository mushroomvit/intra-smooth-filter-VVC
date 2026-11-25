All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.337947222 | 0.475630353 | 0.033289599 | 0.846867174 |
| logic | 0.771333503 | 0.891440513 | 0.040373299 | 1.70314731 |
| clock_sequential | 0.02114432 | 1.72717895 | 0.006369712 | 1.75469298 |
| clock_combinational | 0.257879923 | 0.091584099 | 0.018537894 | 0.368001916 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 2.71203337e-06, leakage 9.39977263e-14 µW. Verified tie cells are included in logic.
