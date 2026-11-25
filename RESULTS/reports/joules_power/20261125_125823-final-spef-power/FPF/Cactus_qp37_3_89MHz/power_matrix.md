All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.23900638 | 1.25416127 | 0.250891904 | 3.74405955 |
| logic | 1.88133234 | 0.922434139 | 0.542356625 | 3.3461231 |
| clock_sequential | 0 | 43.483403 | 0 | 43.483403 |
| clock_combinational | 8.8802877 | 3.36135884 | 0.212127729 | 12.4537743 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal -4.39953e-06, leakage 0 µW. Verified tie cells are included in logic.
