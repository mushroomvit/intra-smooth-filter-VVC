All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.594263903 | 0.655901773 | 0.125822624 | 1.3759883 |
| logic | 1.33882618 | 1.10386886 | 0.230508006 | 2.67320306 |
| clock_sequential | 0.006879138 | 2.07513456 | 0.005247583 | 2.08726128 |
| clock_combinational | 0.369429964 | 0.138228797 | 0.08778951 | 0.595448271 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal -1.0702998e-06, leakage -4.78006523e-13 µW. Verified tie cells are included in logic.
