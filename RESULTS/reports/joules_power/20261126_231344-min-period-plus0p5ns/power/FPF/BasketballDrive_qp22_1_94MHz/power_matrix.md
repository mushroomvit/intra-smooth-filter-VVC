All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 35.4978416 | 19.0807655 | 0.250477949 | 54.829085 |
| logic | 23.5810804 | 11.6836367 | 0.53817256 | 35.8028896 |
| clock_sequential | 0 | 897.364055 | 0 | 897.364055 |
| clock_combinational | 183.316996 | 69.3901969 | 0.212127729 | 252.919321 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal 0.00111471259, leakage 0 µW. Verified tie cells are included in logic.
