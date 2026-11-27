All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 56.3282831 | 61.1029008 | 0.125831637 | 117.557016 |
| logic | 121.69304 | 99.8339256 | 0.231798516 | 221.758765 |
| clock_sequential | 0.572216071 | 172.963691 | 0.005248159 | 173.541156 |
| clock_combinational | 30.782646 | 11.5191466 | 0.087798304 | 42.3895909 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal 9.299569e-05, leakage -1.43995926e-13 µW. Verified tie cells are included in logic.
