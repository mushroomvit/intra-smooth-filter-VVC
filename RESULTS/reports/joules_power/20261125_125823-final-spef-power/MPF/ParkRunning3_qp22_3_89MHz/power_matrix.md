All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.80122926 | 1.10317691 | 0.03323877 | 1.93764494 |
| logic | 1.7473945 | 2.03861916 | 0.040310479 | 3.82632413 |
| clock_sequential | 0.043086245 | 3.54282607 | 0.006386459 | 3.59229877 |
| clock_combinational | 0.531919964 | 0.188268815 | 0.018570247 | 0.738759026 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal -1.4316082e-06, leakage -5.50011425e-14 µW. Verified tie cells are included in logic.
