All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.971873994 | 0.545522063 | 0.250605241 | 1.7680013 |
| logic | 0.805024687 | 0.39572931 | 0.540639036 | 1.74139303 |
| clock_sequential | 0 | 21.6797703 | 0 | 21.6797703 |
| clock_combinational | 4.42872163 | 1.67631698 | 0.212127729 | 6.31716634 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal -4.1100439e-05, leakage 0 µW. Verified tie cells are included in logic.
