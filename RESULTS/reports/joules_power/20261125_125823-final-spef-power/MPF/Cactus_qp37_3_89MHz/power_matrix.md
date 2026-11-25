All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.783604696 | 1.09852758 | 0.033308384 | 1.91544066 |
| logic | 1.71109006 | 1.98606611 | 0.040469406 | 3.73762558 |
| clock_sequential | 0.042465032 | 3.46988608 | 0.006370336 | 3.51872145 |
| clock_combinational | 0.521466339 | 0.18430409 | 0.018544768 | 0.724315197 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 1.326479e-07, leakage 4.50021964e-14 µW. Verified tie cells are included in logic.
