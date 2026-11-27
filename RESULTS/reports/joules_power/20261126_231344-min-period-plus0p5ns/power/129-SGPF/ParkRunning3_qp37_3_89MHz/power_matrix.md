All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 59.3412412 | 65.1327106 | 0.125621475 | 124.599573 |
| logic | 131.860156 | 109.405166 | 0.229947269 | 241.495269 |
| clock_sequential | 0.573775199 | 173.258121 | 0.005249566 | 173.837146 |
| clock_combinational | 30.8506595 | 11.5455905 | 0.08780599 | 42.484056 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal 0.00035221521, leakage 7.69939668e-14 µW. Verified tie cells are included in logic.
