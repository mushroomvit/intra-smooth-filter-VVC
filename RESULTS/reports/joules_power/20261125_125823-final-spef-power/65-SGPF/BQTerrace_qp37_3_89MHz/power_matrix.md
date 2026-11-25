All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.45852571 | 1.71275581 | 0.063526827 | 3.23480835 |
| logic | 3.27168897 | 3.27192508 | 0.086837466 | 6.63045152 |
| clock_sequential | 0.087754602 | 7.03095085 | 0.006421771 | 7.12512722 |
| clock_combinational | 1.07222521 | 0.369110036 | 0.035644579 | 1.47697983 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 2.01541941e-05, leakage -3.09960391e-14 µW. Verified tie cells are included in logic.
