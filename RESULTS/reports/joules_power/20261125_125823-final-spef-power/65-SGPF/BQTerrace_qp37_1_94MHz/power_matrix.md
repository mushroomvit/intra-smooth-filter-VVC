All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 0.727386236 | 0.854172852 | 0.063526827 | 1.64508592 |
| logic | 1.63163032 | 1.6317502 | 0.086837466 | 3.35021799 |
| clock_sequential | 0.043764424 | 3.50643742 | 0.006421771 | 3.55662362 |
| clock_combinational | 0.534733421 | 0.184046803 | 0.035644579 | 0.754424803 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.008308785, internal -2.33841182e-05, leakage -1.00003339e-13 µW. Verified tie cells are included in logic.
