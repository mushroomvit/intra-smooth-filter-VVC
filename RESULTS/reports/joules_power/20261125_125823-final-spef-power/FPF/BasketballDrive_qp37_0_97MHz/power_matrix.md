All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.715362374 | 0.382563113 | 0.251138727 | 1.34906421 |
| logic | 0.489262513 | 0.236506219 | 0.540552956 | 1.26632169 |
| clock_sequential | 0 | 10.8484343 | 0 | 10.8484343 |
| clock_combinational | 2.21436024 | 0.83821043 | 0.212127729 | 3.2646984 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal 3.16034798e-05, leakage 0 µW. Verified tie cells are included in logic.
