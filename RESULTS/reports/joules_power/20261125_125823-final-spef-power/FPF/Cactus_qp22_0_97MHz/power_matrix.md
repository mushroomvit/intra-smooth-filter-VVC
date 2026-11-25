All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.3695766 | 0.210564085 | 0.250343323 | 0.830484008 |
| logic | 0.32200566 | 0.16028814 | 0.539893734 | 1.02218753 |
| clock_sequential | 0 | 10.8372184 | 0 | 10.8372184 |
| clock_combinational | 2.21436024 | 0.838194733 | 0.212127729 | 3.2646827 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal 1.59056003e-05, leakage 0 µW. Verified tie cells are included in logic.
