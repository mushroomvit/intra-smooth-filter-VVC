All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.368737413 | 0.474803139 | 0.063599861 | 0.907140413 |
| logic | 0.911781873 | 0.868051145 | 0.086873623 | 1.86670664 |
| clock_sequential | 0.021784469 | 1.71490332 | 0.006408084 | 1.74309587 |
| clock_combinational | 0.263047399 | 0.0906764575 | 0.035608195 | 0.389332051 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 1.1434991e-06, leakage -2.19962937e-14 µW. Verified tie cells are included in logic.
