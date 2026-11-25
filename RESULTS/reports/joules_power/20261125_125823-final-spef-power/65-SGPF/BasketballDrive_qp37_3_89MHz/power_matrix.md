All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.47875748 | 1.90412493 | 0.063599861 | 3.44648227 |
| logic | 3.65656996 | 3.48118389 | 0.086873623 | 7.22462747 |
| clock_sequential | 0.087362656 | 6.87730832 | 0.006408084 | 6.97107906 |
| clock_combinational | 1.05490378 | 0.363640503 | 0.035608195 | 1.45415248 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 3.64164e-06, leakage -2.99760217e-15 µW. Verified tie cells are included in logic.
