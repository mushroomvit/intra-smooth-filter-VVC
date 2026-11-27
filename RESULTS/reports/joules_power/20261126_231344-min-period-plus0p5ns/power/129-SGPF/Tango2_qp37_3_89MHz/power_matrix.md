All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 66.099202 | 73.412153 | 0.125468375 | 139.636823 |
| logic | 151.984857 | 127.017499 | 0.228245819 | 279.230602 |
| clock_sequential | 0.595247096 | 181.006814 | 0.005271849 | 181.607333 |
| clock_combinational | 32.2361597 | 12.0828332 | 0.087972878 | 44.4069658 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal -5.508552e-05, leakage 1.46993528e-13 µW. Verified tie cells are included in logic.
