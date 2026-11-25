All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.09694849 | 1.24740733 | 0.125465227 | 2.46982105 |
| logic | 2.61295285 | 2.14524282 | 0.226646266 | 4.98484194 |
| clock_sequential | 0.013763888 | 4.14597912 | 0.005247699 | 4.1649907 |
| clock_combinational | 0.73876174 | 0.276420139 | 0.087788488 | 1.10297037 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal 1.755153e-07, leakage -1.04999343e-13 µW. Verified tie cells are included in logic.
