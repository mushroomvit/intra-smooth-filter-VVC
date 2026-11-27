All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 30.3799726 | 35.7713383 | 0.063447487 | 66.2147584 |
| logic | 69.8527543 | 70.2069412 | 0.086532007 | 140.146227 |
| clock_sequential | 1.84941598 | 148.593542 | 0.006420727 | 150.449379 |
| clock_combinational | 22.6537742 | 7.79728182 | 0.035648029 | 30.486704 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.351545572, internal 0.00016943791, leakage -6.30051566e-14 µW. Verified tie cells are included in logic.
