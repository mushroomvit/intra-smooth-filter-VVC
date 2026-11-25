All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.857585894 | 0.460964383 | 0.250477949 | 1.56902823 |
| logic | 0.56968256 | 0.282259784 | 0.53817256 | 1.3901149 |
| clock_sequential | 0 | 21.6793525 | 0 | 21.6793525 |
| clock_combinational | 4.42872163 | 1.6763828 | 0.212127729 | 6.31723216 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020180962, internal 2.4715611e-05, leakage 0 µW. Verified tie cells are included in logic.
