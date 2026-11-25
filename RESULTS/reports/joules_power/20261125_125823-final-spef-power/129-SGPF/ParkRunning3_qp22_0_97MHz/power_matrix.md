All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.634545434 | 0.705282451 | 0.125608454 | 1.46543634 |
| logic | 1.44301952 | 1.18441519 | 0.229205113 | 2.85663982 |
| clock_sequential | 0.006887425 | 2.07467071 | 0.005248121 | 2.08680626 |
| clock_combinational | 0.369476708 | 0.138247601 | 0.08778951 | 0.595513819 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal 8.43009e-07, leakage -7.99360578e-15 µW. Verified tie cells are included in logic.
