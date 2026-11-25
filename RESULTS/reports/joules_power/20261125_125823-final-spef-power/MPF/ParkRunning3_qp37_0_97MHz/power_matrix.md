All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.215172798 | 0.295356852 | 0.033262566 | 0.543792216 |
| logic | 0.455792693 | 0.535776936 | 0.040285698 | 1.03185533 |
| clock_sequential | 0.010681633 | 0.876177828 | 0.006378411 | 0.893237872 |
| clock_combinational | 0.132049442 | 0.0466077667 | 0.018563059 | 0.197220268 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 6.42688e-07, leakage -2.00187089e-15 µW. Verified tie cells are included in logic.
