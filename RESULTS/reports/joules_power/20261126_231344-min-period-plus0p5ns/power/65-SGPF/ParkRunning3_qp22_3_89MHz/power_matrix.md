All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.3799999 | 35.7713524 | 0.063447487 | 66.2147997 |
| logic | 69.8528053 | 70.2069904 | 0.086532007 | 140.146328 |
| clock_sequential | 1.84941607 | 148.594138 | 0.006420727 | 150.449975 |
| clock_combinational | 22.6537753 | 7.79689341 | 0.035648029 | 30.4863167 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545589, internal -0.000219351217, leakage -2.50077736e-14 µW. Verified tie cells are included in logic.
