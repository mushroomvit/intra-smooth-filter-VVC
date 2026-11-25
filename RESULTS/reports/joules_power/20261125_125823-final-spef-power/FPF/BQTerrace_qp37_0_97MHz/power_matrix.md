All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.485935536 | 0.272756301 | 0.250605241 | 1.00929708 |
| logic | 0.40250356 | 0.197861046 | 0.540639036 | 1.14100364 |
| clock_sequential | 0 | 10.8398615 | 0 | 10.8398615 |
| clock_combinational | 2.21436024 | 0.838182145 | 0.212127729 | 3.26467012 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal 3.3180207e-06, leakage 0 µW. Verified tie cells are included in logic.
