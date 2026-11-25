All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.548472831 | 0.623700075 | 0.125465227 | 1.29763813 |
| logic | 1.30646552 | 1.07261518 | 0.226646266 | 2.60572697 |
| clock_sequential | 0.00688194 | 2.07298956 | 0.005247699 | 2.0851192 |
| clock_combinational | 0.36938062 | 0.138210069 | 0.087788488 | 0.595379177 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal 1.852581e-07, leakage 7.50094431e-14 µW. Verified tie cells are included in logic.
