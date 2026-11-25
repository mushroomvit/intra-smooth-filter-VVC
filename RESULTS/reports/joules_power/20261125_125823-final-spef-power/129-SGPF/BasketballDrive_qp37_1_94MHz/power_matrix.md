All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.41640463 | 1.60426715 | 0.125773585 | 3.14644537 |
| logic | 3.26146537 | 2.68234393 | 0.231063309 | 6.17487261 |
| clock_sequential | 0.013926523 | 4.20727071 | 0.005254745 | 4.22645198 |
| clock_combinational | 0.748910729 | 0.28035961 | 0.087839071 | 1.11710941 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -2.890506e-06, leakage 2.43013942e-13 µW. Verified tie cells are included in logic.
