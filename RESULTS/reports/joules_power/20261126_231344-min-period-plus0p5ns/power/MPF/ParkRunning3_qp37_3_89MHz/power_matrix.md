All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3837913 | 26.6071866 | 0.033262566 | 46.0242405 |
| logic | 41.0602926 | 48.2655657 | 0.040285698 | 89.366144 |
| clock_sequential | 0.962251141 | 78.930184 | 0.006378411 | 79.8988136 |
| clock_combinational | 11.895627 | 4.19859831 | 0.018563059 | 16.1127883 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal 1.2139034e-05, leakage 3.30013794e-14 µW. Verified tie cells are included in logic.
