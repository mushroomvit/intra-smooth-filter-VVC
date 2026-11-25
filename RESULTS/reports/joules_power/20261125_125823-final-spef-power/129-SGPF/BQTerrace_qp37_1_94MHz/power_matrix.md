All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.355033 | 1.46988464 | 0.125831637 | 2.95074928 |
| logic | 2.92743356 | 2.40159678 | 0.231798516 | 5.56082885 |
| clock_sequential | 0.013765222 | 4.16082788 | 0.005248159 | 4.17984127 |
| clock_combinational | 0.740506914 | 0.277071926 | 0.087798304 | 1.10537714 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -3.02679993e-05, leakage -1.43995926e-13 µW. Verified tie cells are included in logic.
