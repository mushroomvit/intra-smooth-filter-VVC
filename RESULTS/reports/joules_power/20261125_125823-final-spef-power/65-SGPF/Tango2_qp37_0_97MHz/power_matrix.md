All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.421713637 | 0.524967072 | 0.063511513 | 1.01019222 |
| logic | 0.990930057 | 0.981738439 | 0.086464722 | 2.05913322 |
| clock_sequential | 0.021742952 | 1.6960242 | 0.006400194 | 1.72416734 |
| clock_combinational | 0.260917227 | 0.0900043905 | 0.03559041 | 0.386512027 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 1.456458e-06, leakage 0 µW. Verified tie cells are included in logic.
