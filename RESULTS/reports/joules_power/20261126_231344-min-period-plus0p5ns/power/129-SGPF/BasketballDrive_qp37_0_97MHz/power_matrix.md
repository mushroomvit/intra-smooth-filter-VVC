All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 58.8793595 | 66.6888017 | 0.125773585 | 125.693935 |
| logic | 135.578224 | 111.504272 | 0.231063309 | 247.31356 |
| clock_sequential | 0.578921135 | 174.894814 | 0.005254745 | 175.47899 |
| clock_combinational | 31.1319818 | 11.6545103 | 0.087839071 | 42.8743312 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638571, internal -7.014309e-05, leakage -1.54001811e-13 µW. Verified tie cells are included in logic.
