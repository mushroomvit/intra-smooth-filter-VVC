All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.48379474 | 1.7996639 | 0.063545534 | 3.34700417 |
| logic | 3.46848035 | 3.40530032 | 0.086728985 | 6.96050965 |
| clock_sequential | 0.087601568 | 6.97754583 | 0.006417376 | 7.07156478 |
| clock_combinational | 1.0661378 | 0.367183308 | 0.03563175 | 1.46895285 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.016660429, internal 1.24531928e-05, leakage -2.00534034e-15 µW. Verified tie cells are included in logic.
