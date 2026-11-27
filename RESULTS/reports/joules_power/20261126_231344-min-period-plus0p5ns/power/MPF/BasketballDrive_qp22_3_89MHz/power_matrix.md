All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 14.5070002 | 20.6469651 | 0.033295209 | 35.1872605 |
| logic | 32.8309631 | 38.4850067 | 0.040315794 | 71.3562857 |
| clock_sequential | 0.946552764 | 76.9988362 | 0.006363136 | 77.9517521 |
| clock_combinational | 11.5166377 | 4.08480156 | 0.018526583 | 15.6199659 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -6.4590656e-05, leakage -5.99867378e-15 µW. Verified tie cells are included in logic.
