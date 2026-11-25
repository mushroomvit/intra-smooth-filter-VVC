All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.713754165 | 0.783407909 | 0.125621475 | 1.62278355 |
| logic | 1.58599251 | 1.31591318 | 0.229947269 | 3.13185296 |
| clock_sequential | 0.006901359 | 2.08394682 | 0.005249566 | 2.09609774 |
| clock_combinational | 0.371071255 | 0.138865794 | 0.08780599 | 0.597743039 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal -1.490709e-07, leakage -1.10994547e-13 µW. Verified tie cells are included in logic.
