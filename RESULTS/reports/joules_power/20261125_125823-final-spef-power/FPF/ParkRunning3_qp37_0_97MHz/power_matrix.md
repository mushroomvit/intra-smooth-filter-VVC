All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.572324289 | 0.32469089 | 0.250982614 | 1.14799779 |
| logic | 0.50787392 | 0.25086353 | 0.544052421 | 1.30278987 |
| clock_sequential | 0 | 10.8436286 | 0 | 10.8436286 |
| clock_combinational | 2.21436024 | 0.838171464 | 0.212127729 | 3.26465944 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal -7.3626288e-06, leakage 0 µW. Verified tie cells are included in logic.
