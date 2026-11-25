All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.22998003 | 1.48641786 | 0.063411633 | 2.77980953 |
| logic | 2.98314358 | 2.97036061 | 0.085953047 | 6.03945723 |
| clock_sequential | 0.087685088 | 7.03939061 | 0.006421169 | 7.13349687 |
| clock_combinational | 1.07330535 | 0.369481071 | 0.035647198 | 1.47843362 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 5.46615638e-05, leakage 1.70002901e-14 µW. Verified tie cells are included in logic.
