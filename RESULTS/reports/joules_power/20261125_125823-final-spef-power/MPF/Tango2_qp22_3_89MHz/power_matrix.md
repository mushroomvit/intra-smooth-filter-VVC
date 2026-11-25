All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.674628247 | 0.959699207 | 0.033216891 | 1.66754434 |
| logic | 1.56304766 | 1.80917546 | 0.040374156 | 3.41259728 |
| clock_sequential | 0.042927864 | 3.52216108 | 0.006382732 | 3.57147167 |
| clock_combinational | 0.52873543 | 0.187198865 | 0.018563119 | 0.734497414 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.019239659, internal -2.7534443e-06, leakage -7.00134395e-15 µW. Verified tie cells are included in logic.
