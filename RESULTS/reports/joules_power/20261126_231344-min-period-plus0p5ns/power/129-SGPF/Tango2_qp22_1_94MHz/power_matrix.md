All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 45.5997933 | 51.8545233 | 0.125465227 | 97.5797818 |
| logic | 108.620167 | 89.1773534 | 0.226646266 | 198.024167 |
| clock_sequential | 0.572160625 | 172.346862 | 0.005247699 | 172.92427 |
| clock_combinational | 30.7101 | 11.490652 | 0.087788488 | 42.2885405 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal -4.151931e-05, leakage -1.04999343e-13 µW. Verified tie cells are included in logic.
