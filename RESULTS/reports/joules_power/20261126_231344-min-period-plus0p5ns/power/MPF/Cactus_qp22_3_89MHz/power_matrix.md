All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 15.2219298 | 21.4235204 | 0.033289599 | 36.6787398 |
| logic | 34.7428043 | 40.1526674 | 0.040373299 | 74.935845 |
| clock_sequential | 0.952388863 | 77.796218 | 0.006369712 | 78.7549766 |
| clock_combinational | 11.6155056 | 4.12499579 | 0.018537894 | 15.7590393 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -4.0767179e-05, leakage -1.21999633e-13 µW. Verified tie cells are included in logic.
