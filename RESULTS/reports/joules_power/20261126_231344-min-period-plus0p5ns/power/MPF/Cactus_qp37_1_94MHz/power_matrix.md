All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.6022646 | 24.676473 | 0.033308384 | 42.312046 |
| logic | 38.4366143 | 44.6134523 | 0.040469406 | 83.0905359 |
| clock_sequential | 0.953901138 | 77.9446987 | 0.006370336 | 78.9049702 |
| clock_combinational | 11.7138107 | 4.14017026 | 0.018544768 | 15.8725257 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal 0.000110771805, leakage -2.0997093e-14 µW. Verified tie cells are included in logic.
