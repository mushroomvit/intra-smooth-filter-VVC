All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.393590744 | 0.470073993 | 0.063473202 | 0.927137939 |
| logic | 0.900277693 | 0.895770937 | 0.086758095 | 1.88280673 |
| clock_sequential | 0.021831118 | 1.73835274 | 0.006416425 | 1.76660028 |
| clock_combinational | 0.265684947 | 0.0915047532 | 0.035630348 | 0.392820048 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 7.5624797e-07, leakage -1.10002285e-13 µW. Verified tie cells are included in logic.
