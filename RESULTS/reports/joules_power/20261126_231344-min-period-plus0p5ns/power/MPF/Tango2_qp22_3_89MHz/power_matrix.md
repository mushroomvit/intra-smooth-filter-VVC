All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 15.1543171 | 21.557874 | 0.033216891 | 36.745408 |
| logic | 35.111132 | 40.6399426 | 0.040374156 | 75.7914487 |
| clock_sequential | 0.964297838 | 79.1187859 | 0.006382732 | 80.0894664 |
| clock_combinational | 11.8770975 | 4.20562493 | 0.018563119 | 16.1012855 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal 0.000474771972, leakage -7.00134395e-15 µW. Verified tie cells are included in logic.
