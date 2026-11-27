All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.775786 | 36.1403142 | 0.063526827 | 66.979627 |
| logic | 69.0347308 | 69.0397174 | 0.086837466 | 138.161286 |
| clock_sequential | 1.85167761 | 148.357243 | 0.006421771 | 150.215342 |
| clock_combinational | 22.6246303 | 7.78799698 | 0.035644579 | 30.4482718 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal -3.3016024e-05, leakage -1.00003339e-13 µW. Verified tie cells are included in logic.
