All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 16.907843 | 23.4366899 | 0.033295003 | 40.377828 |
| logic | 36.7287101 | 42.4233653 | 0.04037853 | 79.192454 |
| clock_sequential | 0.952003173 | 77.712068 | 0.006369405 | 78.6704406 |
| clock_combinational | 11.6356644 | 4.12352419 | 0.018538603 | 15.7777272 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184409, internal 0.000116074861, leakage -1.79994908e-14 µW. Verified tie cells are included in logic.
