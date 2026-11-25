All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.359014937 | 0.422726851 | 0.063447487 | 0.845189275 |
| logic | 0.825477397 | 0.82966521 | 0.086532007 | 1.74167461 |
| clock_sequential | 0.021855475 | 1.75600755 | 0.006420727 | 1.78428376 |
| clock_combinational | 0.267711007 | 0.0921426581 | 0.035648029 | 0.395501694 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.004154392, internal 2.7112188e-07, leakage 9.79979986e-14 µW. Verified tie cells are included in logic.
