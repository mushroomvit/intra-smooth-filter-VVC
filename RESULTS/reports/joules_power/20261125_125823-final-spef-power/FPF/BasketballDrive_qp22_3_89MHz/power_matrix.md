All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.71959907 | 0.924314341 | 0.250477949 | 2.89439136 |
| logic | 1.14231409 | 0.565978972 | 0.53817256 | 2.24646562 |
| clock_sequential | 0 | 43.4704938 | 0 | 43.4704938 |
| clock_combinational | 8.8802877 | 3.36140981 | 0.212127729 | 12.4538252 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 4.6565206e-05, leakage 0 µW. Verified tie cells are included in logic.
