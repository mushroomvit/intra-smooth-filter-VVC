All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.7758133 | 36.1402429 | 0.063526827 | 66.979583 |
| logic | 69.034849 | 69.0397862 | 0.086837466 | 138.161473 |
| clock_sequential | 1.85167771 | 148.357068 | 0.006421771 | 150.215167 |
| clock_combinational | 22.6246314 | 7.78811352 | 0.035644579 | 30.4483895 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 8.3146317e-05, leakage -3.09960391e-14 µW. Verified tie cells are included in logic.
