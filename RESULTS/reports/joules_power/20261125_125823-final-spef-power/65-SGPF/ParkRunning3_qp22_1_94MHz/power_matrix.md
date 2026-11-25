All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.718031195 | 0.845453701 | 0.063447487 | 1.62693238 |
| logic | 1.65096484 | 1.65933774 | 0.086532007 | 3.39683459 |
| clock_sequential | 0.04371097 | 3.51201511 | 0.006420727 | 3.5621468 |
| clock_combinational | 0.53542224 | 0.184285316 | 0.035648029 | 0.755355585 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal 4.682442e-07, leakage -6.30051566e-14 µW. Verified tie cells are included in logic.
