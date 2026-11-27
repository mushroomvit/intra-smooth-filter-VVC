All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 46.8416457 | 46.5351337 | 0.125877409 | 93.5026568 |
| logic | 87.7483192 | 80.5391334 | 0.229837711 | 168.51729 |
| clock_sequential | 0.585591124 | 172.540902 | 0.005258355 | 173.131751 |
| clock_combinational | 30.7100921 | 11.490659 | 0.087788488 | 42.2885396 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -3.158218e-05, leakage 3.99957845e-14 µW. Verified tie cells are included in logic.
