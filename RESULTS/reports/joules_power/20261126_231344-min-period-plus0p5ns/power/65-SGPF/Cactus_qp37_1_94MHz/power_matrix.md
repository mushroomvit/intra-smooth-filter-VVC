All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.3089778 | 37.9740189 | 0.063545534 | 69.3465422 |
| logic | 73.1871712 | 71.8540141 | 0.086728985 | 145.127914 |
| clock_sequential | 1.84844849 | 147.230987 | 0.006417376 | 149.085853 |
| clock_combinational | 22.4961818 | 7.74763085 | 0.03563175 | 30.2794444 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal 9.3585098e-05, leakage 4.69971284e-14 µW. Verified tie cells are included in logic.
