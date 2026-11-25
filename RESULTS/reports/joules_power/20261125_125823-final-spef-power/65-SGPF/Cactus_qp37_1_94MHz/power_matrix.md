All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.739988236 | 0.897514477 | 0.063545534 | 1.70104825 |
| logic | 1.72977187 | 1.69826579 | 0.086728985 | 3.51476665 |
| clock_sequential | 0.043688102 | 3.47980734 | 0.006417376 | 3.52991282 |
| clock_combinational | 0.53169754 | 0.183119853 | 0.03563175 | 0.750449143 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal 6.7123832e-06, leakage 4.69971284e-14 µW. Verified tie cells are included in logic.
