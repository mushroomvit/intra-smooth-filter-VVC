All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 27.0042106 | 32.2133732 | 0.063535483 | 59.2811193 |
| logic | 63.596251 | 63.8832063 | 0.086467002 | 127.565924 |
| clock_sequential | 1.85296785 | 149.079301 | 0.006423784 | 150.938693 |
| clock_combinational | 22.7096928 | 7.81506143 | 0.03565323 | 30.5604074 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.35154548, internal 0.000229406621, leakage -1.99840144e-15 µW. Verified tie cells are included in logic.
