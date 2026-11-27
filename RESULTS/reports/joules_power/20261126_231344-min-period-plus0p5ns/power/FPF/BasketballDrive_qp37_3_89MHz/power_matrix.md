All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 59.2221448 | 31.6708923 | 0.251138727 | 91.1441758 |
| logic | 40.5052254 | 19.5799261 | 0.540552956 | 60.6257044 |
| clock_sequential | 0 | 898.094838 | 0 | 898.094838 |
| clock_combinational | 183.317005 | 69.3884647 | 0.212127729 | 252.917598 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal -0.00062095436, leakage 0 µW. Verified tie cells are included in logic.
