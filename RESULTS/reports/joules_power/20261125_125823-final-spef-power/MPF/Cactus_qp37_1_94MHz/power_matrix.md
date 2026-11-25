All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.390794158 | 0.547849033 | 0.033308384 | 0.971951575 |
| logic | 0.853342023 | 0.990476735 | 0.040469406 | 1.88428816 |
| clock_sequential | 0.021177895 | 1.7304793 | 0.006370336 | 1.75802753 |
| clock_combinational | 0.260062444 | 0.0919150753 | 0.018544768 | 0.370522287 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal 1.5533516e-07, leakage -2.0997093e-14 µW. Verified tie cells are included in logic.
