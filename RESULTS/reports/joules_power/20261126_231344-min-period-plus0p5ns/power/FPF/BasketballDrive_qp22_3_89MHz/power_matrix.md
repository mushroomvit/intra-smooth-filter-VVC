All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 35.4979185 | 19.0808119 | 0.250477949 | 54.8292084 |
| logic | 23.5811293 | 11.6836631 | 0.53817256 | 35.8029649 |
| clock_sequential | 0 | 897.366968 | 0 | 897.366968 |
| clock_combinational | 183.317005 | 69.3857121 | 0.212127729 | 252.914845 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.83534568, internal -0.0033736024, leakage 0 µW. Verified tie cells are included in logic.
