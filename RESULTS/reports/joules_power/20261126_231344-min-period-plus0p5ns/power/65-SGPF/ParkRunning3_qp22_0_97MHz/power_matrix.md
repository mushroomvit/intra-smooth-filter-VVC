All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.3799164 | 35.7713383 | 0.063447487 | 66.2147022 |
| logic | 69.8526238 | 70.2068273 | 0.086532007 | 140.145983 |
| clock_sequential | 1.84941549 | 148.593852 | 0.006420727 | 150.449688 |
| clock_combinational | 22.6537683 | 7.79697223 | 0.035648029 | 30.4863885 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal -0.000138124116, leakage 9.79979986e-14 µW. Verified tie cells are included in logic.
