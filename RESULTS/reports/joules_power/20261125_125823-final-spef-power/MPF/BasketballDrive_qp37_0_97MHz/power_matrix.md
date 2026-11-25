All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.195297706 | 0.281625933 | 0.033345544 | 0.510269183 |
| logic | 0.431136162 | 0.502354577 | 0.040378818 | 0.973869557 |
| clock_sequential | 0.010534748 | 0.861631447 | 0.006360941 | 0.878527136 |
| clock_combinational | 0.1303313 | 0.0458652719 | 0.01854485 | 0.194741422 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal -1.24414392e-06, leakage -5.39984724e-14 µW. Verified tie cells are included in logic.
