All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.383752 | 26.6070615 | 0.033262566 | 46.0240761 |
| logic | 41.0601636 | 48.2654618 | 0.040285698 | 89.365911 |
| clock_sequential | 0.962250846 | 78.9302808 | 0.006378411 | 79.8989101 |
| clock_combinational | 11.8956233 | 4.19860673 | 0.018563059 | 16.1127931 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal 2.185346e-05, leakage -2.00187089e-15 µW. Verified tie cells are included in logic.
