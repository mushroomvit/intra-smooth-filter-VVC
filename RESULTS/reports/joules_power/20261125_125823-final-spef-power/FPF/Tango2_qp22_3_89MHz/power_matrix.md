All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.54503838 | 0.898827582 | 0.25057343 | 2.69443939 |
| logic | 1.49520156 | 0.74001203 | 0.542910995 | 2.77812459 |
| clock_sequential | 0 | 43.4645828 | 0 | 43.4645828 |
| clock_combinational | 8.8802877 | 3.36134857 | 0.212127729 | 12.453764 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal -1.4672977e-05, leakage 0 µW. Verified tie cells are included in logic.
