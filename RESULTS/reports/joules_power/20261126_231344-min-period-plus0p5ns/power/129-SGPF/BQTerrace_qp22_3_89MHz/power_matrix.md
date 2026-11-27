All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 46.8418143 | 46.5353963 | 0.125877409 | 93.503088 |
| logic | 87.748805 | 80.5394204 | 0.229837711 | 168.518063 |
| clock_sequential | 0.585591302 | 172.541068 | 0.005258355 | 173.131918 |
| clock_combinational | 30.7101015 | 11.4904421 | 0.087788488 | 42.2883321 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -0.00025197187, leakage 1.99840144e-15 µW. Verified tie cells are included in logic.
