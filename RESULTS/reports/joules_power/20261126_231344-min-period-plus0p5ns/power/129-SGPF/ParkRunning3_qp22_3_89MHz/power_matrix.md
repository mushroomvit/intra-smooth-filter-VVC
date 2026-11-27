All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 52.7558726 | 58.6373806 | 0.125608454 | 111.518862 |
| logic | 119.973317 | 98.4724661 | 0.229205113 | 218.674988 |
| clock_sequential | 0.572616696 | 172.486669 | 0.005248121 | 173.064533 |
| clock_combinational | 30.7180902 | 11.4944607 | 0.08778951 | 42.3003404 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.4236387, internal 0.00070129984, leakage 6.30051566e-14 µW. Verified tie cells are included in logic.
