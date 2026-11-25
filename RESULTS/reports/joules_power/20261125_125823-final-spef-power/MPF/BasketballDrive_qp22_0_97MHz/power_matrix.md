All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.161037092 | 0.229193178 | 0.033295209 | 0.423525479 |
| logic | 0.36444191 | 0.427205955 | 0.040315794 | 0.831963659 |
| clock_sequential | 0.01050737 | 0.854736336 | 0.006363136 | 0.871606842 |
| clock_combinational | 0.127842403 | 0.0453459139 | 0.018526583 | 0.1917149 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 1.15890179e-06, leakage -4.20011248e-14 µW. Verified tie cells are included in logic.
