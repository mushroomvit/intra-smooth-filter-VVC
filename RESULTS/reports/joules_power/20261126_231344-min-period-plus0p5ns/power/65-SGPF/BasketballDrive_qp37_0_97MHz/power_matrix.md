All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.2026358 | 40.1782876 | 0.063599861 | 71.4445232 |
| logic | 77.1558461 | 73.4551058 | 0.086873623 | 150.697826 |
| clock_sequential | 1.84340699 | 145.115483 | 0.006408084 | 146.965298 |
| clock_combinational | 22.259133 | 7.67304251 | 0.035608195 | 29.9677837 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal 7.6112809e-05, leakage -2.19962937e-14 µW. Verified tie cells are included in logic.
