All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 15.2218902 | 21.423422 | 0.033289599 | 36.6786018 |
| logic | 34.7426765 | 40.1525638 | 0.040373299 | 74.9356136 |
| clock_sequential | 0.95238857 | 77.7961039 | 0.006369712 | 78.7548622 |
| clock_combinational | 11.615502 | 4.12518293 | 0.018537894 | 15.7592228 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal 0.00014763229, leakage 7.00134395e-15 µW. Verified tie cells are included in logic.
