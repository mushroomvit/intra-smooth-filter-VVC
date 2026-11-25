All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 1.5900807 | 1.76600053 | 0.125468375 | 3.48154961 |
| logic | 3.65612852 | 3.05552209 | 0.228245819 | 6.93989643 |
| clock_sequential | 0.014319255 | 4.35430695 | 0.005271849 | 4.37389806 |
| clock_combinational | 0.775472604 | 0.290662033 | 0.087972878 | 1.15410751 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.01019105, internal -3.757321e-06, leakage 7.5994766e-14 µW. Verified tie cells are included in logic.
