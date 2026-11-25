All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.19955816 | 2.5012556 | 0.125465227 | 4.82627899 |
| logic | 5.23940373 | 4.30156351 | 0.226646266 | 9.76761351 |
| clock_sequential | 0.027598785 | 8.31331803 | 0.005247699 | 8.34616452 |
| clock_combinational | 1.48133482 | 0.554264375 | 0.087788488 | 2.12338769 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -1.6353193e-06, leakage -1.60996216e-13 µW. Verified tie cells are included in logic.
