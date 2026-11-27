All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 25.953328 | 31.364323 | 0.063411633 | 57.3810627 |
| logic | 62.9462576 | 62.6765171 | 0.085953047 | 125.708728 |
| clock_sequential | 1.85021083 | 148.536026 | 0.006421169 | 150.392658 |
| clock_combinational | 22.647422 | 7.7952466 | 0.035647198 | 30.4783158 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal 0.000115622393, leakage 6.99440506e-15 µW. Verified tie cells are included in logic.
