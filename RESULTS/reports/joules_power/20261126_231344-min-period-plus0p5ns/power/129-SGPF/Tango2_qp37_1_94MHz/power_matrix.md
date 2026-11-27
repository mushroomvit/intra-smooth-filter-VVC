All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 66.0991388 | 73.4122559 | 0.125468375 | 139.636863 |
| logic | 151.984711 | 127.017397 | 0.228245819 | 279.230354 |
| clock_sequential | 0.595247069 | 181.006927 | 0.005271849 | 181.607446 |
| clock_combinational | 32.2361581 | 12.0828808 | 0.087972878 | 44.4070118 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal -6.96552001e-06, leakage 7.5994766e-14 µW. Verified tie cells are included in logic.
