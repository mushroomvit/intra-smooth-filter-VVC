All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.935740126 | 0.575310969 | 0.250104348 | 1.76115544 |
| logic | 1.14057663 | 0.581756746 | 0.541494803 | 2.26382818 |
| clock_sequential | 0 | 43.4485825 | 0 | 43.4485825 |
| clock_combinational | 8.8802877 | 3.36138151 | 0.212127729 | 12.4537969 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.040466022, internal 1.826566e-05, leakage 0 µW. Verified tie cells are included in logic.
