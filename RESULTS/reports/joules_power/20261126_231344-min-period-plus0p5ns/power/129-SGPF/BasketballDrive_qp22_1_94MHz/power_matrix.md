All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 47.1980447 | 52.5377056 | 0.1257867 | 99.861537 |
| logic | 106.831036 | 89.5076113 | 0.230717712 | 196.569365 |
| clock_sequential | 0.571709276 | 172.532347 | 0.005247405 | 173.109303 |
| clock_combinational | 30.7142023 | 11.4924718 | 0.08778951 | 42.2944636 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal 0.00011689937, leakage -1.23998034e-13 µW. Verified tie cells are included in logic.
