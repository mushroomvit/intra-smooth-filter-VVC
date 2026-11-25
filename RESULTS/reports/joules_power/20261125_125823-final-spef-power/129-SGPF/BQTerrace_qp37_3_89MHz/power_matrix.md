All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.71705833 | 2.94736356 | 0.125831637 | 5.79025353 |
| logic | 5.86999146 | 4.81559483 | 0.231798516 | 10.9173848 |
| clock_sequential | 0.02760146 | 8.34309267 | 0.005248159 | 8.37594229 |
| clock_combinational | 1.48483416 | 0.55564241 | 0.087798304 | 2.12827488 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal 8.4234602e-06, leakage 1.38999923e-13 µW. Verified tie cells are included in logic.
