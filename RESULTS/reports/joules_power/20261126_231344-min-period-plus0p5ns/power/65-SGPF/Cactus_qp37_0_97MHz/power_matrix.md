All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.3089224 | 37.9738927 | 0.063545534 | 69.3463606 |
| logic | 73.1869972 | 71.853884 | 0.086728985 | 145.12761 |
| clock_sequential | 1.84844801 | 147.230483 | 0.006417376 | 149.085348 |
| clock_combinational | 22.496176 | 7.74864061 | 0.03563175 | 30.2804483 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal 0.00110534551, leakage 3.49997809e-14 µW. Verified tie cells are included in logic.
