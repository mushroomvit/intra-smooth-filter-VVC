All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 56.3283413 | 61.1029704 | 0.125831637 | 117.557143 |
| logic | 121.693232 | 99.8340301 | 0.231798516 | 221.759061 |
| clock_sequential | 0.5722161 | 172.964042 | 0.005248159 | 173.541506 |
| clock_combinational | 30.7826475 | 11.5186185 | 0.087798304 | 42.3890644 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -0.00043563768, leakage 1.38999923e-13 µW. Verified tie cells are included in logic.
