All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.168222761 | 0.2393054 | 0.033216891 | 0.440745052 |
| logic | 0.389753869 | 0.451127631 | 0.040374156 | 0.881255656 |
| clock_sequential | 0.010704353 | 0.878274273 | 0.006382732 | 0.895361358 |
| clock_combinational | 0.131843753 | 0.0466807507 | 0.018563119 | 0.197087623 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 7.6172917e-07, leakage 6.09998163e-14 µW. Verified tie cells are included in logic.
