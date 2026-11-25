# Final routed power and area summary

**120/120 cases completed** across all four designs. Floorplan target: 65%; outer ring-to-die clearance: 0.2 µm. Power uses the actual implemented buffers/clock trees, matched detailed SPEF and the updated full-workload RTL VCDs. Corner: TT/0.8 V/25 °C.

| Design | Logical cell area (µm²) | NAND2 kGates | Total power min / mean / max (µW) |
|---|---:|---:|---:|
| FPF | 17441.844 | 59.326 | 15.696718 / 36.857121 / 67.267403 |
| 129-SGPF | 8283.940 | 28.177 | 6.185993 / 15.919488 / 31.531964 |
| 65-SGPF | 4233.600 | 14.400 | 4.259023 / 10.752263 / 20.195662 |
| MPF | 2203.530 | 7.495 | 2.318811 / 5.721420 / 10.395475 |

Cell area includes the implemented logical cells and CTS/optimization buffers, excluding physical-only filler/tap cells. kGates = cell area / 0.294 / 1000, using the PDK’s ND2SGD1BWP7T40P140 NAND2 cell. The mean is unweighted across the 30 cases per design; the maximum is a workload-average maximum, not an instantaneous current peak.

Detailed switching/internal/leakage matrices for all 120 cases are in `POWER_BREAKDOWN_ALL_CASES.md`, `power_detail.csv`, and `power_detail_wide.csv`. Per-case native reports and reconciliation provenance are retained in the Joules results directory.

Activity is propagated from RTL VCDs through the routed netlist. It is not SDF-backannotated gate-level simulation.
