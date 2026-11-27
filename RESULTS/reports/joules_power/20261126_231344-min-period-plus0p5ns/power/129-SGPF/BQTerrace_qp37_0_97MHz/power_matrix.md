All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 56.3281648 | 61.1027236 | 0.125831637 | 117.55672 |
| logic | 121.692791 | 99.8337393 | 0.231798516 | 221.758329 |
| clock_sequential | 0.572215926 | 172.963691 | 0.005248159 | 173.541156 |
| clock_combinational | 30.7826381 | 11.5187922 | 0.087798304 | 42.3892286 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -0.00025846888, leakage 5.90083538e-14 µW. Verified tie cells are included in logic.
