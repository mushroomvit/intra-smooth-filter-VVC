All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.363692496 | 0.427084739 | 0.063526827 | 0.854304062 |
| logic | 0.815810128 | 0.815871369 | 0.086837466 | 1.71851896 |
| clock_sequential | 0.021882202 | 1.75321871 | 0.006421771 | 1.78152268 |
| clock_combinational | 0.2673666 | 0.0920234014 | 0.035644579 | 0.39503458 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal -1.16535581e-05, leakage 6.99995617e-14 µW. Verified tie cells are included in logic.
