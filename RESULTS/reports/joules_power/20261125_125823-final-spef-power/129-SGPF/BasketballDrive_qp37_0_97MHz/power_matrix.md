All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.708200872 | 0.802128729 | 0.125773585 | 1.63610319 |
| logic | 1.63072239 | 1.34116583 | 0.231063309 | 3.20295154 |
| clock_sequential | 0.006963256 | 2.10363239 | 0.005254745 | 2.11585039 |
| clock_combinational | 0.374455112 | 0.140182117 | 0.087839071 | 0.6024763 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.005095524, internal 9.618464e-07, leakage -1.54001811e-13 µW. Verified tie cells are included in logic.
