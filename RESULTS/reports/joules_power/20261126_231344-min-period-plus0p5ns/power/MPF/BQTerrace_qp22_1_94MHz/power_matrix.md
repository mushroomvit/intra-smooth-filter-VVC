All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 16.2695697 | 20.6448767 | 0.033251384 | 36.9476978 |
| logic | 32.1043024 | 41.7259154 | 0.040194786 | 73.8704126 |
| clock_sequential | 0.980743647 | 82.5532136 | 0.006402026 | 83.5403592 |
| clock_combinational | 12.2887285 | 4.37886507 | 0.018610353 | 16.686204 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.43218452, internal -0.000217688573, leakage -4.00027234e-14 µW. Verified tie cells are included in logic.
