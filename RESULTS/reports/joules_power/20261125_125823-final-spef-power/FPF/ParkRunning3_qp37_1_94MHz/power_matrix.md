All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.14465654 | 0.64939224 | 0.250982614 | 2.04503139 |
| logic | 1.01576861 | 0.50173516 | 0.544052421 | 2.06155619 |
| clock_sequential | 0 | 21.6872352 | 0 | 21.6872352 |
| clock_combinational | 4.42872163 | 1.67644229 | 0.212127729 | 6.31729165 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal 8.420715e-05, leakage 0 µW. Verified tie cells are included in logic.
