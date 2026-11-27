All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 46.8417607 | 46.5353069 | 0.125877409 | 93.502945 |
| logic | 87.7486541 | 80.5393435 | 0.229837711 | 168.517835 |
| clock_sequential | 0.585591272 | 172.540902 | 0.005258355 | 173.131752 |
| clock_combinational | 30.7101 | 11.490659 | 0.087788488 | 42.2885475 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal -3.452318e-05, leakage -3.90007471e-13 µW. Verified tie cells are included in logic.
