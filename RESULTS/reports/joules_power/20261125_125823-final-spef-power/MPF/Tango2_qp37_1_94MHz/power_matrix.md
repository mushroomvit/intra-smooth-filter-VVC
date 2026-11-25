All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.429402459 | 0.598936902 | 0.033280863 | 1.06162022 |
| logic | 0.914426204 | 1.08483588 | 0.040370569 | 2.03963266 |
| clock_sequential | 0.021489394 | 1.71942968 | 0.00636396 | 1.74728304 |
| clock_combinational | 0.261425926 | 0.0915992617 | 0.01854552 | 0.371570708 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 1.14368016e-06, leakage -5.40019418e-14 µW. Verified tie cells are included in logic.
