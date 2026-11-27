All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 33.3058116 | 39.7781046 | 0.063473202 | 73.1473894 |
| logic | 76.182694 | 75.8009671 | 0.086758095 | 152.070419 |
| clock_sequential | 1.84735496 | 147.099963 | 0.006416425 | 148.953735 |
| clock_combinational | 22.4823297 | 7.74355682 | 0.035630348 | 30.2615168 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 0.000464565618, leakage 3.40005801e-14 µW. Verified tie cells are included in logic.
