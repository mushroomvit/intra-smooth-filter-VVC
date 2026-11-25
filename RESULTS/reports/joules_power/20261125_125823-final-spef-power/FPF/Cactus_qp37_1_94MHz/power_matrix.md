All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.11662045 | 0.625465068 | 0.250891904 | 1.99297742 |
| logic | 0.938239683 | 0.460027354 | 0.542356625 | 1.94062366 |
| clock_sequential | 0 | 21.6857615 | 0 | 21.6857615 |
| clock_combinational | 4.42872163 | 1.67634944 | 0.212127729 | 6.31719879 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal -8.648993e-06, leakage 0 µW. Verified tie cells are included in logic.
