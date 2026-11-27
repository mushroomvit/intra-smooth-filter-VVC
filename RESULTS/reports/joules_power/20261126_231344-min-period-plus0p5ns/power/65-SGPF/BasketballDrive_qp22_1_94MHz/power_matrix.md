All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.0836128 | 31.0292967 | 0.063545337 | 56.1764549 |
| logic | 60.7565303 | 60.0003841 | 0.086624888 | 120.843539 |
| clock_sequential | 1.84854194 | 147.441716 | 0.006417911 | 149.296676 |
| clock_combinational | 22.5223566 | 7.75524566 | 0.035634355 | 30.3132367 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal -0.000539003522, leakage 1.04000142e-13 µW. Verified tie cells are included in logic.
