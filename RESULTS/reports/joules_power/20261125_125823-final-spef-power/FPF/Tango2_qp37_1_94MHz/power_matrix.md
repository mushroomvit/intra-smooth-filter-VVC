All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.77379514 | 1.00140349 | 0.251973668 | 3.0271723 |
| logic | 1.64991577 | 0.797697389 | 0.552223512 | 2.99983667 |
| clock_sequential | 0 | 21.7123879 | 0 | 21.7123879 |
| clock_combinational | 4.42872163 | 1.67635505 | 0.212127729 | 6.3172044 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal -3.039071e-06, leakage 0 µW. Verified tie cells are included in logic.
