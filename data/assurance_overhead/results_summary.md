# AEI assurance-overhead formal results V1

Formal run ID: `AEI_ASSURANCE_OVERHEAD_FORMAL_20260826_B5R1_V1`

The earlier run `AEI_ASSURANCE_OVERHEAD_FORMAL_20260826_B5_V1` remains `FORMAL_RUN_INVALID`; none of its timing rows are used here.

Primary latency is component-only `raw_component_latency_ns`. The paired component-minus-load difference is diagnostic only and is not an overhead estimate.

## Component-only latency

| Reporting group | Median (ns) | Q1 (ns) | Q3 (ns) | IQR (ns) | MAD (ns) | p95 (ns) | n | Artifact bootstrap median 95% CI (ns) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H1_A22 | 67400 | 56700 | 83100 | 26400 | 12100 | 173100 | 16000 | 65500–70050 |
| H1_A26 | 10747300 | 9549050 | 19997875 | 10448825 | 1814450 | 22304625 | 4200 | 9684859–19821450 |
| H2_expected_accept | 12000 | 7200 | 13600 | 6400 | 4000 | 19800 | 10000 | 11900–12350 |
| H2_expected_reject | 7300 | 5000 | 13300 | 8300 | 4100 | 18300 | 6000 | 5600–12625 |
| H3 | 551600 | 443775 | 708450 | 264675 | 125800 | 930890 | 4200 | 477575–700406 |
| H4 | 878200 | 731875 | 1149300 | 417425 | 208850 | 1384405 | 4200 | 762600–1149500 |
| H5 | 12350 | 4200 | 17100 | 12900 | 7650 | 21000 | 4200 | 11600–12550 |
| H5_IO | 21030500 | 15621600 | 27305175 | 11683575 | 5681200 | 53229685 | 4200 | 20208425–21874450 |
| H6 | 17942500 | 9191725 | 23007025 | 13815300 | 8407800 | 58099900 | 4200 | 10606575–19104900 |
| H7 | 14700 | 5700 | 19200 | 13500 | 7900 | 24800 | 4200 | 13450–15100 |
| H8 | 1567450 | 1277550 | 2032200 | 754650 | 364950 | 2629705 | 4200 | 1328250–1965425 |

## Direct and contextual results

- Direct H8 composite accepted-path latency: median 1567450 ns; Q1–Q3 1277550–2032200 ns; p95 2629705 ns; n=4200.
- Offline H6 reconstruction consistency latency: median 17942500 ns; Q1–Q3 9191725–23007025 ns; p95 58099900 ns; n=4200.
- Isolated H5_IO latency: median 21030500 ns; Q1–Q3 15621600–27305175 ns; p95 53229685 ns; n=4200.
- Among separately measured H3/H4/H5/H7 checks, `H4` had the largest median component-only latency in this environment.
- Negative paired component-minus-load diagnostic values were retained: 54457 observations.
- Composed-path summaries (`T_H0 + T_Hk`) and H0 summaries are retained in `component_summary.csv` and `summary.json`; they are derived isolated software-path quantities, not production end-to-end measurements.

## Allocation and bounded scaling

Peak traced Python allocation was measured in a separate pass and was not subtracted from H0. Component-level allocation summaries are retained in `summary.json`.

Descriptive observed-range scaling produced 30 estimable relationships and 16 non-informative relationships. No asymptotic fit or extrapolation was performed.

## Claim boundary

Supported only as bounded observations in this environment: measured component latency over the retained artifacts; measured derived load/parse-plus-component path latency; observed-range descriptive scaling; identification of the largest median H3/H4/H5/H7 component; and measured paper-local H5_IO latency.

Not supported: negligible or negative overhead, assurance speedup, real-time capability, industrial-scale or general/asymptotic scalability, production latency guarantees or readiness, cross-hardware generality, optimizer speedup, or LLM latency improvement.
