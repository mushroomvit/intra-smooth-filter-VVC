All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.390595989 | 0.563255749 | 0.033345544 | 0.987197282 |
| logic | 0.86227642 | 1.00471296 | 0.040378818 | 1.9073682 |
| clock_sequential | 0.021069505 | 1.72326289 | 0.006360941 | 1.75069334 |
| clock_combinational | 0.260662714 | 0.0917344268 | 0.01854485 | 0.370941991 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 1.35781501e-06, leakage 6.9978745e-15 µW. Verified tie cells are included in logic.
