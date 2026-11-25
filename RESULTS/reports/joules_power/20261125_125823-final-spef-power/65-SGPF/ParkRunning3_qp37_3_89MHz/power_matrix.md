All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.57842725 | 1.88515841 | 0.063473202 | 3.52705887 |
| logic | 3.61043838 | 3.59235046 | 0.086758095 | 7.28954693 |
| clock_sequential | 0.087549738 | 6.97135519 | 0.006416425 | 7.06532135 |
| clock_combinational | 1.06548127 | 0.366962849 | 0.035630348 | 1.46807446 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 2.6694306e-06, leakage 3.40005801e-14 µW. Verified tie cells are included in logic.
