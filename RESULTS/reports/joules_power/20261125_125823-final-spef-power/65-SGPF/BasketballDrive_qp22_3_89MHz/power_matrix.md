All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.18876252 | 1.47053693 | 0.063545337 | 2.72284479 |
| logic | 2.87936631 | 2.84353292 | 0.086624888 | 5.80952412 |
| clock_sequential | 0.087605996 | 6.98754436 | 0.006417911 | 7.08156826 |
| clock_combinational | 1.06737827 | 0.367566506 | 0.035634355 | 1.47057913 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 4.7895131e-06, leakage -9.20027943e-14 µW. Verified tie cells are included in logic.
