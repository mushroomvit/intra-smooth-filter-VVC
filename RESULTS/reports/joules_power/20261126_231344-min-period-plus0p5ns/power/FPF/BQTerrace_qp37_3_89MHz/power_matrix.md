All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 40.2286587 | 22.5807217 | 0.250605241 | 63.0599856 |
| logic | 33.3225593 | 16.3804874 | 0.540639036 | 50.2436857 |
| clock_sequential | 0 | 897.384846 | 0 | 897.384846 |
| clock_combinational | 183.317005 | 69.387426 | 0.212127729 | 252.916559 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345679, internal -0.00165965603, leakage 0 µW. Verified tie cells are included in logic.
