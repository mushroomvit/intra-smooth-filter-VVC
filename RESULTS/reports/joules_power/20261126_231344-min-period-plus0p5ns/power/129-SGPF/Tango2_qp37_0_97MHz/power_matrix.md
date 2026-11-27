All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 66.0990203 | 73.4121353 | 0.125468375 | 139.636624 |
| logic | 151.984413 | 127.017196 | 0.228245819 | 279.229854 |
| clock_sequential | 0.595246918 | 181.006685 | 0.005271849 | 181.607204 |
| clock_combinational | 32.23615 | 12.0833635 | 0.087972878 | 44.4074864 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal 0.00047878456, leakage -5.20000709e-14 µW. Verified tie cells are included in logic.
