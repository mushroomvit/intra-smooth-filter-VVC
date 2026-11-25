All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.29522449 | 1.3021368 | 0.250982614 | 3.8483439 |
| logic | 2.0367886 | 1.00606455 | 0.544052421 | 3.58690557 |
| clock_sequential | 0 | 43.4863575 | 0 | 43.4863575 |
| clock_combinational | 8.8802877 | 3.36153355 | 0.212127729 | 12.453949 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 0.000170309503, leakage 0 µW. Verified tie cells are included in logic.
