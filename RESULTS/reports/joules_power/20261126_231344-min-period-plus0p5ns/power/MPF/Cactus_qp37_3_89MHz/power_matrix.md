All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 17.6022778 | 24.6765231 | 0.033308384 | 42.3121093 |
| logic | 38.4366495 | 44.6134837 | 0.040469406 | 83.0906026 |
| clock_sequential | 0.953901186 | 77.9448447 | 0.006370336 | 78.9051162 |
| clock_combinational | 11.7138112 | 4.13990804 | 0.018544768 | 15.8722641 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.432184543, internal -0.000151647583, leakage 4.50021964e-14 µW. Verified tie cells are included in logic.
