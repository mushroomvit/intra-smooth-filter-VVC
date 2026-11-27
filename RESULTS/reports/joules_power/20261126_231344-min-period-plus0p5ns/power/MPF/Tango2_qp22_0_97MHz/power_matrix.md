All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 15.1542781 | 21.5577739 | 0.033216891 | 36.7452689 |
| logic | 35.1110445 | 40.6398525 | 0.040374156 | 75.7912711 |
| clock_sequential | 0.964297545 | 79.1190062 | 0.006382732 | 80.0896865 |
| clock_combinational | 11.8770939 | 4.20519475 | 0.018563119 | 16.1008517 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal 4.587977e-05, leakage 6.09998163e-14 µW. Verified tie cells are included in logic.
