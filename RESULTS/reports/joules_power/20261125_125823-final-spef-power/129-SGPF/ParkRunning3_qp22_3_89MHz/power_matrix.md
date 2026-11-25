All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 2.5447365 | 2.82842793 | 0.125608454 | 5.49877288 |
| logic | 5.78703018 | 4.74991826 | 0.229205113 | 10.7661536 |
| clock_sequential | 0.027620782 | 8.32010097 | 0.005248121 | 8.35296987 |
| clock_combinational | 1.48172017 | 0.55440298 | 0.08778951 | 2.12391266 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.020434669, internal -1.08865528e-05, leakage 6.30051566e-14 µW. Verified tie cells are included in logic.
