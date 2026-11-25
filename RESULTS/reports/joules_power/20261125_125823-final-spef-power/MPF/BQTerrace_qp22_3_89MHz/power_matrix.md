All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.724276801 | 0.919053912 | 0.033251384 | 1.6765821 |
| logic | 1.42919308 | 1.85752113 | 0.040194786 | 3.32690899 |
| clock_sequential | 0.04365999 | 3.6750398 | 0.006402026 | 3.72510182 |
| clock_combinational | 0.547060155 | 0.194951145 | 0.018610353 | 0.760621653 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 6.5121495e-06, leakage 6.09998163e-14 µW. Verified tie cells are included in logic.
