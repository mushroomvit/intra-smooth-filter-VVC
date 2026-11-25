All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.59285163 | 0.733376685 | 0.063545337 | 1.38977365 |
| logic | 1.4359752 | 1.41810565 | 0.086624888 | 2.94070574 |
| clock_sequential | 0.043690312 | 3.48478303 | 0.006417911 | 3.53489125 |
| clock_combinational | 0.532316185 | 0.183310395 | 0.035634355 | 0.751260935 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal 2.326409e-06, leakage 1.04000142e-13 µW. Verified tie cells are included in logic.
