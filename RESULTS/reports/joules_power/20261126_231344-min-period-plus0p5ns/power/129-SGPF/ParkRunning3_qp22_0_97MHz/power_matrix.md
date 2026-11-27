All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 52.7556936 | 58.6371733 | 0.125608454 | 111.518475 |
| logic | 119.972776 | 98.4721493 | 0.229205113 | 218.67413 |
| clock_sequential | 0.572616521 | 172.487059 | 0.005248121 | 173.064923 |
| clock_combinational | 30.7180808 | 11.4935753 | 0.08778951 | 42.2994456 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -0.00018063089, leakage -7.99360578e-15 µW. Verified tie cells are included in logic.
