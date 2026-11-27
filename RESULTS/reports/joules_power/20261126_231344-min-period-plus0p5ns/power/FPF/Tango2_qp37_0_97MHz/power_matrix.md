All values in µW.

| Category | Switching | Internal | Leakage | Total |
|---|---:|---:|---:|---:|
| sequential | 73.4219816 | 41.4506689 | 0.251973668 | 115.124624 |
| logic | 68.2949891 | 33.019067 | 0.552223512 | 101.86628 |
| clock_sequential | 0 | 898.736529 | 0 | 898.736529 |
| clock_combinational | 183.316949 | 69.3880395 | 0.212127729 | 252.917117 |

Clock-combinational = native aggregate clock minus native clock_seq. Signed native clock partition difference beyond cell-only clock_comb: switching 0.835345426, internal -0.00102500331, leakage 0 µW. Verified tie cells are included in logic.
