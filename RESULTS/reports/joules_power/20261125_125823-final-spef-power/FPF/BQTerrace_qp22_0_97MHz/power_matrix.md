All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.233330523 | 0.143454237 | 0.250104346 | 0.626889106 |
| logic | 0.284402341 | 0.14506113 | 0.5414948 | 0.970958271 |
| clock_sequential | 0 | 10.8341994 | 0 | 10.8341994 |
| clock_combinational | 2.21436024 | 0.83818333 | 0.212127729 | 3.2646713 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal 4.5028709e-06, leakage 0 µW. Verified tie cells are included in logic.
