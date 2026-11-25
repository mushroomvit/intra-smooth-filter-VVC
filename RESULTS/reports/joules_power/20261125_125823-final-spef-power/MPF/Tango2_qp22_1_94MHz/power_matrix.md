All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.336446111 | 0.478614648 | 0.033216891 | 0.84827765 |
| logic | 0.779511781 | 0.902259031 | 0.040374156 | 1.72214497 |
| clock_sequential | 0.021408715 | 1.75655127 | 0.006382732 | 1.78434272 |
| clock_combinational | 0.263687619 | 0.0933585419 | 0.018563119 | 0.37560928 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.009595083, internal -1.47612184e-06, leakage -2.90011071e-14 µW. Verified tie cells are included in logic.
