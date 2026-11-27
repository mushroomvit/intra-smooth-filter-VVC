All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.6022389 | 24.6764444 | 0.033308384 | 42.3119917 |
| logic | 38.4365531 | 44.6133923 | 0.040469406 | 83.0904148 |
| clock_sequential | 0.953900893 | 77.9447243 | 0.006370336 | 78.9049955 |
| clock_combinational | 11.7138077 | 4.14016545 | 0.018544768 | 15.8725179 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal 0.000107030437, leakage -1.39992185e-14 µW. Verified tie cells are included in logic.
