All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 14.5069866 | 20.6469144 | 0.033295209 | 35.1871962 |
| logic | 32.8309336 | 38.4849744 | 0.040315794 | 71.3562238 |
| clock_sequential | 0.946552716 | 76.998892 | 0.006363136 | 77.9518078 |
| clock_combinational | 11.5166371 | 4.08484408 | 0.018526583 | 15.6200078 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal -2.1865843e-05, leakage 8.20003787e-14 µW. Verified tie cells are included in logic.
