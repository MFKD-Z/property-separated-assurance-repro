# AEI P3 Controlled-Corruption Negative-Control Results V1

## Formal identity and claim boundary

- Formal run ID: `AEI_P3_FORMAL_20260826T034308Z_9b5f3c2bdfbe`.
- Paper authority: `7abc1e876f185dc17213376c2a0b7a82a00f0679`.
- Frozen SUT authority: `7ff79ee8ca81ea976c3791a5064772dbfb126082`.
- Scientific population: 42 retained accepted A26 realization chains in frozen lexicographic order.
- Checker repetition is a reproducibility execution and is not treated as a new scientific observation.

The bounded result concerns only the preregistered paper-side reconstruction checker, the specified controlled corruptions, the declared reconstruction relation, and the retained accepted realization set. It is not evidence of tamper-proofing, cryptographic security, arbitrary-corruption detection, cyberattack resistance, causal provenance, or a production security guarantee.

## Clean controls

- Pass 1: 42/42 PASS.
- Pass 2: 42/42 PASS.
- Exact repeated verdicts: 42/42.

## Family-specific scientific endpoints

| Family | Attempted | Preregistered detector | Incidental detector | Undetected | Unevaluable | Rejected proportion | Exact 95% CP interval | Reproducible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| M1 | 336 | 336 | 0 | 0 | 0 | 1.000000 | [0.989081, 1.000000] | 336/336 |
| M2 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M3 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M4 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M5 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M6 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M7 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M8 | 42 | 42 | 0 | 0 | 0 | 1.000000 | [0.915916, 1.000000] | 42/42 |
| M9 | 462 | 462 | 0 | 0 | 0 | 1.000000 | [0.992047, 1.000000] | 462/462 |

The frozen primary classification counts a unit as `DETECTED_AS_PREREGISTERED` whenever at least one observed check belongs to its expected-detector set. On that definition, no unit was rejected only by an outside detector. A separate raw-ledger audit found additional co-triggered checks in 168 pass-1 units: M1.08 (42 units; the 11 OB7 missing-field checks), M2.01 (42; `CHECK_AUDIT_CHAIN_ID` and `CHECK_INPUT_DELTA_RECOMPUTATION`), M3.01 (42; `CHECK_AUDIT_CHAIN_ID`), and M6.01 (42; `CHECK_LIFECYCLE_PROVENANCE_LINK`). These co-triggers are disclosed but do not convert an expected-detector hit into the frozen incidental-only category.

## M1 frozen subcases

| Subcase | Attempted | Preregistered detector | Incidental detector | Undetected | Unevaluable |
|---|---:|---:|---:|---:|---:|
| M1.01 | 42 | 42 | 0 | 0 | 0 |
| M1.02 | 42 | 42 | 0 | 0 | 0 |
| M1.03 | 42 | 42 | 0 | 0 | 0 |
| M1.04 | 42 | 42 | 0 | 0 | 0 |
| M1.05 | 42 | 42 | 0 | 0 | 0 |
| M1.06 | 42 | 42 | 0 | 0 | 0 |
| M1.07 | 42 | 42 | 0 | 0 | 0 |
| M1.08 | 42 | 42 | 0 | 0 | 0 |

## M9 frozen subcases

| Subcase | Attempted | Preregistered detector | Incidental detector | Undetected | Unevaluable |
|---|---:|---:|---:|---:|---:|
| M9.01 | 42 | 42 | 0 | 0 | 0 |
| M9.02 | 42 | 42 | 0 | 0 | 0 |
| M9.03 | 42 | 42 | 0 | 0 | 0 |
| M9.04 | 42 | 42 | 0 | 0 | 0 |
| M9.05 | 42 | 42 | 0 | 0 | 0 |
| M9.06 | 42 | 42 | 0 | 0 | 0 |
| M9.07 | 42 | 42 | 0 | 0 | 0 |
| M9.08 | 42 | 42 | 0 | 0 | 0 |
| M9.09 | 42 | 42 | 0 | 0 | 0 |
| M9.10 | 42 | 42 | 0 | 0 | 0 |
| M9.11 | 42 | 42 | 0 | 0 | 0 |

## Reproducibility and anomalies

- Unique mutated scientific units: 1092.
- Mutation checker executions: 2184.
- Clean checker executions: 84.
- Repeated mutation verdict mismatches: 0.
- Undetected controlled corruptions: 0.
- Unevaluable scientific units: 0.
- Incidental detector mismatches: 0.

## Gate result

`STRICT_SCIENTIFIC_GATE=PASS`

The preregistered paper-side reconstruction checker detected the specified controlled corruptions under the declared reconstruction relation over the retained accepted realization set.

Legacy intact-chain 42/42 results remain separate frozen evidence and are neither pooled with nor replaced by these negative controls.
