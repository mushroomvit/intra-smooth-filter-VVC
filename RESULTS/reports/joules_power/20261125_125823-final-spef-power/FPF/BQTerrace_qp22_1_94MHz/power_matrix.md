All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.466664143 | 0.286914247 | 0.250104346 | 1.00368274 |
| logic | 0.568815711 | 0.290128029 | 0.5414948 | 1.40043854 |
| clock_sequential | 0 | 21.6683988 | 0 | 21.6683988 |
| clock_combinational | 4.42872163 | 1.67636666 | 0.212127729 | 6.31721602 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal 8.574732e-06, leakage 0 µW. Verified tie cells are included in logic.
