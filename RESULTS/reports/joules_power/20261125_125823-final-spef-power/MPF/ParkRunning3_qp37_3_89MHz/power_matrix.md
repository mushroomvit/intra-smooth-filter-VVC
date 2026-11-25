All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.862912744 | 1.18447533 | 0.033262566 | 2.08065064 |
| logic | 1.82788779 | 2.148647 | 0.040285698 | 4.01682049 |
| clock_sequential | 0.042836753 | 3.51375299 | 0.006378411 | 3.56296816 |
| clock_combinational | 0.529560318 | 0.186912034 | 0.018563059 | 0.735035411 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 2.6246332e-06, leakage 3.30013794e-14 µW. Verified tie cells are included in logic.
