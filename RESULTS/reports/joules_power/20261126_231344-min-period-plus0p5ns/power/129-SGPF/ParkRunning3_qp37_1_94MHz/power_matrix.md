All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 59.3411804 | 65.1326491 | 0.125621475 | 124.599451 |
| logic | 131.860008 | 109.40507 | 0.229947269 | 241.495026 |
| clock_sequential | 0.573775171 | 173.2578 | 0.005249566 | 173.836825 |
| clock_combinational | 30.850658 | 11.5453803 | 0.08780599 | 42.4838443 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.423638679, internal 0.00014258618, leakage -4.8699933e-13 µW. Verified tie cells are included in logic.
