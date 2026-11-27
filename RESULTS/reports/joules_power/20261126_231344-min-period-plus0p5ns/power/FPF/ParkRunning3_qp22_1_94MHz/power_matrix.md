All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 36.9466527 | 21.3450518 | 0.250667015 | 58.5423715 |
| logic | 34.959774 | 17.4864083 | 0.543158119 | 52.9893405 |
| clock_sequential | 0 | 897.368489 | 0 | 897.368489 |
| clock_combinational | 183.316996 | 69.3832315 | 0.212127729 | 252.912355 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal -0.00585068736, leakage 0 µW. Verified tie cells are included in logic.
