All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.302350992 | 0.333913761 | 0.063578383 | 0.699843136 |
| logic | 0.604178206 | 0.677028832 | 0.086513735 | 1.36772077 |
| clock_sequential | 0.021647814 | 1.76602227 | 0.006408328 | 1.79407842 |
| clock_combinational | 0.269129364 | 0.0925918723 | 0.035659543 | 0.397380779 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 3.05027895e-06, leakage -6.99440506e-15 µW. Verified tie cells are included in logic.
