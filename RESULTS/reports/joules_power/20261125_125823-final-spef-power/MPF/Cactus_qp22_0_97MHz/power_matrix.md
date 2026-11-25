All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.168973313 | 0.237813377 | 0.033289599 | 0.440076289 |
| logic | 0.385664146 | 0.445718057 | 0.040373299 | 0.871755502 |
| clock_sequential | 0.010572155 | 0.863589473 | 0.006369712 | 0.88053134 |
| clock_combinational | 0.128939905 | 0.0457920495 | 0.018537894 | 0.193269849 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.00479754, internal 1.3765166e-06, leakage 7.00134395e-15 µW. Verified tie cells are included in logic.
