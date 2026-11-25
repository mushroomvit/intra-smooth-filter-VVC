All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.21252692 | 1.3391101 | 0.063578383 | 2.61521541 |
| logic | 2.42297892 | 2.71512222 | 0.086513735 | 5.22461488 |
| clock_sequential | 0.08681463 | 7.08232374 | 0.006408328 | 7.1755467 |
| clock_combinational | 1.07929445 | 0.371304375 | 0.035659543 | 1.48625837 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal -6.2720456e-06, leakage 8.59937122e-14 µW. Verified tie cells are included in logic.
