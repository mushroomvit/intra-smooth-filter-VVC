All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.886894152 | 0.500696767 | 0.251973668 | 1.63956459 |
| logic | 0.824941737 | 0.398842288 | 0.552223512 | 1.77600754 |
| clock_sequential | 0 | 10.8561939 | 0 | 10.8561939 |
| clock_combinational | 2.21436024 | 0.838177523 | 0.212127729 | 3.26466549 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal -1.3040377e-06, leakage 0 µW. Verified tie cells are included in logic.
