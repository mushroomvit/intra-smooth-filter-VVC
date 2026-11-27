All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 16.2695829 | 20.6449465 | 0.033251384 | 36.9477808 |
| logic | 32.1043391 | 41.7259487 | 0.040194786 | 73.8704825 |
| clock_sequential | 0.9807437 | 82.5532513 | 0.006402026 | 83.540397 |
| clock_combinational | 12.2887292 | 4.37907341 | 0.018610353 | 16.686413 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -9.591588e-06, leakage 6.09998163e-14 µW. Verified tie cells are included in logic.
