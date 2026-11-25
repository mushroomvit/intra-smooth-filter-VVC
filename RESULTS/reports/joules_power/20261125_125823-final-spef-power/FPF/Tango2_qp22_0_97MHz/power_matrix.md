All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.385261369 | 0.224125697 | 0.25057343 | 0.859960496 |
| logic | 0.372830099 | 0.184523024 | 0.542910995 | 1.10026412 |
| clock_sequential | 0 | 10.8381779 | 0 | 10.8381779 |
| clock_combinational | 2.21436024 | 0.838177947 | 0.212127729 | 3.26466592 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal -8.80161e-07, leakage 0 µW. Verified tie cells are included in logic.
