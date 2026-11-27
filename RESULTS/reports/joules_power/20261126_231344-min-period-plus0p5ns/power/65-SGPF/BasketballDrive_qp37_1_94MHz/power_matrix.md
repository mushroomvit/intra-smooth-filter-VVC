All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.2026882 | 40.1782422 | 0.063599861 | 71.4445302 |
| logic | 77.1559823 | 73.4552136 | 0.086873623 | 150.69807 |
| clock_sequential | 1.84340747 | 145.115483 | 0.006408084 | 146.965298 |
| clock_combinational | 22.2591388 | 7.67326957 | 0.035608195 | 29.9680166 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal 0.000301162811, leakage 5.99520433e-15 µW. Verified tie cells are included in logic.
