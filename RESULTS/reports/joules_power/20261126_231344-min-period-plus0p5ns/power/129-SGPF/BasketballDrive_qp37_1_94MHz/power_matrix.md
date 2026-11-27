All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 58.8794805 | 66.6887122 | 0.125773585 | 125.693966 |
| logic | 135.578515 | 111.504466 | 0.231063309 | 247.314044 |
| clock_sequential | 0.578921285 | 174.895015 | 0.005254745 | 175.479191 |
| clock_combinational | 31.1319899 | 11.6545416 | 0.087839071 | 42.8743706 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal -4.185321e-05, leakage 2.43013942e-13 µW. Verified tie cells are included in logic.
