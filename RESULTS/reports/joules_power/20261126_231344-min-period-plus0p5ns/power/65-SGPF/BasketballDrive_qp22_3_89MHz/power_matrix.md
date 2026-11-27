All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.0836394 | 31.0292577 | 0.063545337 | 56.1764424 |
| logic | 60.7566092 | 60.0004431 | 0.086624888 | 120.843677 |
| clock_sequential | 1.84854204 | 147.441592 | 0.006417911 | 149.296552 |
| clock_combinational | 22.5223579 | 7.75590035 | 0.035634355 | 30.3138926 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 0.000115272917, leakage -9.20027943e-14 µW. Verified tie cells are included in logic.
