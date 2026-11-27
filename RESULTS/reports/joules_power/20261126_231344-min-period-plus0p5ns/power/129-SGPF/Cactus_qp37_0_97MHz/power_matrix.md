All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 56.7769932 | 62.5087915 | 0.125806251 | 119.411591 |
| logic | 126.321639 | 104.401445 | 0.23163212 | 230.954716 |
| clock_sequential | 0.572464827 | 173.089811 | 0.005248352 | 173.667524 |
| clock_combinational | 30.8066042 | 11.5280823 | 0.087800241 | 42.4224867 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -0.00016434076, leakage -9.80049375e-14 µW. Verified tie cells are included in logic.
