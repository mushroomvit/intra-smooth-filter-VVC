All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.677638183 | 0.953715864 | 0.033289599 | 1.66464365 |
| logic | 1.54665049 | 1.78748316 | 0.040373299 | 3.37450695 |
| clock_sequential | 0.042397711 | 3.46326469 | 0.006369712 | 3.51203211 |
| clock_combinational | 0.5170901 | 0.183640483 | 0.018537894 | 0.719268477 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 5.2941658e-06, leakage -1.21999633e-13 µW. Verified tie cells are included in logic.
