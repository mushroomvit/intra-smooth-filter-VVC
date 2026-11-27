All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 19.3165121 | 11.8762558 | 0.250104346 | 31.4428722 |
| logic | 23.5451059 | 12.0092874 | 0.5414948 | 36.0958881 |
| clock_sequential | 0 | 896.916788 | 0 | 896.916788 |
| clock_combinational | 183.316996 | 69.3884385 | 0.212127729 | 252.917562 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345639, internal -0.00064368197, leakage 0 µW. Verified tie cells are included in logic.
