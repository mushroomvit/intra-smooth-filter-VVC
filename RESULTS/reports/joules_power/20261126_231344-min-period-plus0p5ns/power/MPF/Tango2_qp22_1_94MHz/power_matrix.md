All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 15.1543044 | 21.5578694 | 0.033216891 | 36.7453908 |
| logic | 35.1111004 | 40.6399122 | 0.040374156 | 75.7913867 |
| clock_sequential | 0.964297794 | 79.119129 | 0.006382732 | 80.0898095 |
| clock_combinational | 11.8770969 | 4.20504606 | 0.018563119 | 16.1007061 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal -0.000103897735, leakage -2.90011071e-14 µW. Verified tie cells are included in logic.
