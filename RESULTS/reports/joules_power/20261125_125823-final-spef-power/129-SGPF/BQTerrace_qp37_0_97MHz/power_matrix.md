All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.677515073 | 0.734940549 | 0.125831637 | 1.53828726 |
| logic | 1.46370712 | 1.20079245 | 0.231798516 | 2.89629808 |
| clock_sequential | 0.006882607 | 2.08041394 | 0.005248159 | 2.09254471 |
| clock_combinational | 0.370253205 | 0.138535963 | 0.087798304 | 0.596587472 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal -1.50389998e-05, leakage 5.90083538e-14 µW. Verified tie cells are included in logic.
