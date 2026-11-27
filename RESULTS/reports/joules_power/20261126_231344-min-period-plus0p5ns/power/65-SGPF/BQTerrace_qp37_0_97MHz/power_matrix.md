All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.7757337 | 36.1401455 | 0.063526827 | 66.979406 |
| logic | 69.0345804 | 69.0396073 | 0.086837466 | 138.161025 |
| clock_sequential | 1.85167713 | 148.357243 | 0.006421771 | 150.215342 |
| clock_combinational | 22.6246244 | 7.78799698 | 0.035644579 | 30.4482659 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal -3.0986009e-05, leakage 6.99995617e-14 µW. Verified tie cells are included in logic.
