All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.428791423 | 0.230482191 | 0.250477949 | 0.909751563 |
| logic | 0.284834652 | 0.141126942 | 0.53817256 | 0.964134154 |
| clock_sequential | 0 | 10.8396763 | 0 | 10.8396763 |
| clock_combinational | 2.21436024 | 0.8381914 | 0.212127729 | 3.26467937 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal 1.25733008e-05, leakage 0 µW. Verified tie cells are included in logic.
