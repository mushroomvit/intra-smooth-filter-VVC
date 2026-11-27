All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3166089 | 11.8762793 | 0.250104348 | 31.4429925 |
| logic | 23.5451967 | 12.0093311 | 0.541494803 | 36.0960226 |
| clock_sequential | 0 | 896.917171 | 0 | 896.917171 |
| clock_combinational | 183.317005 | 69.3879725 | 0.212127729 | 252.917105 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal -0.00111319543, leakage 0 µW. Verified tie cells are included in logic.
