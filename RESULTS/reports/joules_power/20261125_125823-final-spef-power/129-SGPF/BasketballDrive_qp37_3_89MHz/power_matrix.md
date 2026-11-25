All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.84011811 | 3.21681285 | 0.125773585 | 6.18270454 |
| logic | 6.53977483 | 5.37853649 | 0.231063309 | 12.1493746 |
| clock_sequential | 0.027924891 | 8.43624563 | 0.005254745 | 8.46942526 |
| clock_combinational | 1.50168512 | 0.562164085 | 0.087839071 | 2.15168827 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -7.3186306e-06, leakage -3.20021787e-14 µW. Verified tie cells are included in logic.
