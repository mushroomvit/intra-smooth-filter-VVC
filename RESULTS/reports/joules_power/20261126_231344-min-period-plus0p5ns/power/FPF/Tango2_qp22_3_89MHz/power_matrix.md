All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.8944347 | 18.5546249 | 0.25057343 | 50.6996331 |
| logic | 30.8657738 | 15.2762254 | 0.542910995 | 46.6849102 |
| clock_sequential | 0 | 897.245488 | 0 | 897.245488 |
| clock_combinational | 183.317005 | 69.3856796 | 0.212127729 | 252.914813 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345679, internal -0.00340605958, leakage 0 µW. Verified tie cells are included in logic.
