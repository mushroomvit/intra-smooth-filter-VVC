All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 31.3090056 | 37.9740633 | 0.063545534 | 69.3466144 |
| logic | 73.1872861 | 71.8540873 | 0.086728985 | 145.128102 |
| clock_sequential | 1.84844858 | 147.231193 | 0.006417376 | 149.086059 |
| clock_combinational | 22.4961829 | 7.74759817 | 0.03563175 | 30.2794128 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal 6.052769e-05, leakage -2.00534034e-15 µW. Verified tie cells are included in logic.
