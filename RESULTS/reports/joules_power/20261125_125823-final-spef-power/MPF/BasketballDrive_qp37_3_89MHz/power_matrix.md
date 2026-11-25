All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.783207379 | 1.12941479 | 0.033345544 | 1.94596771 |
| logic | 1.72900409 | 2.01461202 | 0.040378818 | 3.78399493 |
| clock_sequential | 0.042247696 | 3.4554161 | 0.006360941 | 3.50402473 |
| clock_combinational | 0.522670031 | 0.183941697 | 0.01854485 | 0.725156578 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal 2.3577744e-06, leakage -1.10016163e-14 µW. Verified tie cells are included in logic.
