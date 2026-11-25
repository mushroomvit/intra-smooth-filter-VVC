All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.18853107 | 1.31181575 | 0.125822624 | 2.62616944 |
| logic | 2.67767302 | 2.2077507 | 0.230508006 | 5.11593173 |
| clock_sequential | 0.013758283 | 4.15026912 | 0.005247583 | 4.16927499 |
| clock_combinational | 0.738860428 | 0.276469798 | 0.08778951 | 1.10311974 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal 9.871494e-06, leakage 1.19904087e-14 µW. Verified tie cells are included in logic.
