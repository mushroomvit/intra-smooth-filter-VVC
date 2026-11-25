All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 3.5567469 | 2.00797695 | 0.251973668 | 5.81669752 |
| logic | 3.30837609 | 1.59952155 | 0.552223512 | 5.46012115 |
| clock_sequential | 0 | 43.5368044 | 0 | 43.5368044 |
| clock_combinational | 8.8802877 | 3.36136466 | 0.212127729 | 12.4537801 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 1.422548e-06, leakage 0 µW. Verified tie cells are included in logic.
