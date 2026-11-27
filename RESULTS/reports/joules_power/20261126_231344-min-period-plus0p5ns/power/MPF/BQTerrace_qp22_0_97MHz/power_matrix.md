All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 16.2695426 | 20.6448795 | 0.033251384 | 36.9476735 |
| logic | 32.1042173 | 41.7258394 | 0.040194786 | 73.8702515 |
| clock_sequential | 0.980743396 | 82.5533976 | 0.006402026 | 83.540543 |
| clock_combinational | 12.2887254 | 4.37905698 | 0.018610353 | 16.6863928 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal -2.4658167e-05, leakage -8.00054467e-15 µW. Verified tie cells are included in logic.
