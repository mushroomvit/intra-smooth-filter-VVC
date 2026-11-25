All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.195396797 | 0.273924199 | 0.033308384 | 0.50262938 |
| logic | 0.426668494 | 0.495236238 | 0.040469406 | 0.962374138 |
| clock_sequential | 0.010588943 | 0.865239808 | 0.006370336 | 0.882199087 |
| clock_combinational | 0.130031164 | 0.0459574843 | 0.018544768 | 0.194533416 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 4.433724e-08, leakage -1.39992185e-14 µW. Verified tie cells are included in logic.
