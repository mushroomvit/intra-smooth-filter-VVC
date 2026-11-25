All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.13539606 | 1.26384585 | 0.1257867 | 2.5250286 |
| logic | 2.56991608 | 2.15318783 | 0.230717712 | 4.95382162 |
| clock_sequential | 0.01375303 | 4.15042871 | 0.005247405 | 4.16942914 |
| clock_combinational | 0.738860428 | 0.276448826 | 0.08778951 | 1.10309876 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -1.1100781e-05, leakage -1.23998034e-13 µW. Verified tie cells are included in logic.
