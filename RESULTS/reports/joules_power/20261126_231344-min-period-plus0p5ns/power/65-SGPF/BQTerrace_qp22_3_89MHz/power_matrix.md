All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.5850835 | 28.2560844 | 0.063578383 | 53.9047463 |
| logic | 51.1265028 | 57.29088 | 0.086513735 | 108.503897 |
| clock_sequential | 1.83184371 | 149.441388 | 0.006408328 | 151.27964 |
| clock_combinational | 22.773797 | 7.83495041 | 0.035659543 | 30.6444069 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 6.0423088e-05, leakage 8.59937122e-14 µW. Verified tie cells are included in logic.
