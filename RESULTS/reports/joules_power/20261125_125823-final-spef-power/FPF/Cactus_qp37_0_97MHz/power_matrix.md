All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.558306338 | 0.312728843 | 0.250891904 | 1.12192709 |
| logic | 0.469110194 | 0.230009567 | 0.542356625 | 1.24147639 |
| clock_sequential | 0 | 10.8428808 | 0 | 10.8428808 |
| clock_combinational | 2.21436024 | 0.838174718 | 0.212127729 | 3.26466269 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.010090478, internal -4.1089912e-06, leakage 0 µW. Verified tie cells are included in logic.
