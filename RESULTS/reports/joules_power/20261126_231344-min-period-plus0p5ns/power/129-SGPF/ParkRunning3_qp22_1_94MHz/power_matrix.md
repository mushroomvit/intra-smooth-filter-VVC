All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 52.7558118 | 58.6372421 | 0.125608454 | 111.518662 |
| logic | 119.973179 | 98.4723708 | 0.229205113 | 218.674755 |
| clock_sequential | 0.572616667 | 172.487147 | 0.005248121 | 173.065012 |
| clock_combinational | 30.7180886 | 11.4938604 | 0.08778951 | 42.2997386 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal 0.00010152441, leakage 2.39003262e-13 µW. Verified tie cells are included in logic.
