All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.739156357 | 0.421135621 | 0.250343323 | 1.4106353 |
| logic | 0.644021286 | 0.320581476 | 0.539893734 | 1.5044965 |
| clock_sequential | 0 | 21.6744015 | 0 | 21.6744015 |
| clock_combinational | 4.42872163 | 1.67638674 | 0.212127729 | 6.31723609 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal 2.865231e-05, leakage 0 µW. Verified tie cells are included in logic.
