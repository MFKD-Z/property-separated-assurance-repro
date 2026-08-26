# AEI P3 Negative-Control Checker Specification V1

Status: **FROZEN FOR BATCH 2 / PREREGISTERED FOR BATCH 3**

Formal experiment executed: **false**

## 1. Authority and population

This paper-side experimental specification implements the definition repair authorized by Batch 1. Its source population is exactly the 42 accepted `AUDIT_CHAIN_V1` rows in `evidence/derived/a26_audit_chains_v1.jsonl`, as confirmed by `evidence/manifests/a26_audit_evidence_v1.json`. Population order is lexicographic `audit_chain_id`. A bundle is eligible only when its chain ID is unique, its linked paper-local raw artifact exists and matches `solver_evidence.schedule_artifact_sha256`, its retained instance fixture resolves, and the retained before/after canonical instance and schedule hashes agree with the chain. No directory scan adds units.

The retained source bundle comprises the chain row, linked raw artifact, and the scenario's retained `data/disturbance_matrix/instances/<instance_id>/<timing>_<duration>.json` fixture. The frozen machine-readable source manifest records the exact paths and SHA-256 values.

## 2. Three non-equivalent relations

### 2.1 `R_LEGACY`

`R_LEGACY` is the broad relation retained in the pre-closure P3 formalization. It combines request/event, instance, schedule, profile, solver-realization, lineage, and delta requirements. It is historical/current-definition context. This Batch-2 harness does not rewrite it and does not claim that the unchanged manuscript already contains the repaired split below.

### 2.2 `R6` / `OB6_CONSISTENCY`

`R6` is the repaired cross-artifact consistency projection. It checks only declared equality, linkage, lineage, canonicalization, artifact-identity, and reconstruction relations. A required OB7 solver field that is absent is not itself an `R6` failure; any present solver field participating in a cross-artifact relation must agree.

`R6` checks, in deterministic order:

1. `CHECK_REQUIRED_<ARTIFACT>`: availability of each frozen top-level artifact class: input/event, before instance, after instance, before schedule, after schedule, lifecycle/provenance, PlanDelta, and solver artifact.
2. `CHECK_SOURCE_RAW_ARTIFACT_DIGEST` and `CHECK_SOURCE_INSTANCE_ARTIFACT_DIGEST`: copied source identity metadata agrees with the frozen source manifest. Authoritative bytes are verified before copying.
3. `CHECK_REQUEST_EVENT_IDENTITY`: chain/InputDelta event identity, type, effective time, controlled source, and validated-request hash agree with the retained event. The frozen validated-request projection is exactly `event_id`, `event_type`, `effective_time`, `failed_machine_id`, `unavailable_start`, and `available_again_time`; runtime progress annotations in the raw event envelope are not part of that hash.
4. `CHECK_INPUT_DELTA_RECOMPUTATION`: recomputation using canonical JSON (UTF-8, `ensure_ascii=true`, sorted keys, compact separators, no trailing newline) equals the copied InputDelta, including `input_delta_hash`.
5. `CHECK_INSTANCE_LOCAL_DIGEST` and `CHECK_INSTANCE_DELTA_RECOMPUTATION`: canonical before/after instance hashes and the complete frozen InstanceDelta recomputation equal the copied local fields.
6. `CHECK_INSTANCE_PROVENANCE_LINK`, `CHECK_INSTANCE_LIFECYCLE_LINK`, and `CHECK_INSTANCE_SOLVER_LINK`: local instance hashes agree with independent provenance, lifecycle, and present solver references.
7. `CHECK_SCHEDULE_LOCAL_DIGEST`: schedule-local lifecycle digest uses the lifecycle canonicalization above; schedule-local solver digest uses UTF-8 JSON with `ensure_ascii=false`, sorted keys, compact separators, and one trailing newline.
8. `CHECK_SCHEDULE_PROVENANCE_LINK`, `CHECK_SCHEDULE_LIFECYCLE_LINK`, and `CHECK_SOLVER_SCHEDULE_LINK`: local schedule digests agree with independent provenance, lifecycle, and any present solver schedule hash.
9. `CHECK_PROFILE_LINK`: profile ID agrees across chain, InputDelta, lifecycle scheduling request/accepted-plan fields, and raw solver realization where present.
10. `CHECK_PARENT_SCHEDULE_HASH`, `CHECK_PARENT_VERSION`, and `CHECK_LIFECYCLE_VERSION_SEQUENCE`: the successor names the predecessor schedule, the successor parent version equals the predecessor version, and successor version equals predecessor version plus one. Chain provenance must agree with both lifecycle artifacts.
11. `CHECK_PLAN_DELTA_RECOMPUTATION`: the full paper-side conventional PlanDelta is recomputed from before/after schedules and the retained event/progress state; objective-component deltas are recomputed from retained lifecycle objectives; native S4 fields declared by the retained `recomputation.fields` map are independently reconstructed and equal.
12. `CHECK_SOLVER_ARTIFACT_LINK`: any present solver artifact path and digest agree with the bundle's frozen linked raw artifact identity.
13. `CHECK_AUDIT_CHAIN_ID`: the retained ID equals the canonical digest of the clean chain payload with `audit_chain_id` omitted. This check is evaluated last so a mutation's scientific failing surface remains explicit.

The checker never receives mutation-family metadata. It returns all failed check IDs in deterministic order and uses the first as the terminal detector.

### 2.3 `Complete(E_s)` / `OB7_COMPLETENESS`

`Complete(E_s)` is independent of `R6`. A required field is complete only when the exact canonical field exists and its value is not `null`, the empty string, or `UNKNOWN`. The frozen field mapping is:

| Protocol name | Canonical `solver_evidence` field |
|---|---|
| solver version | `solver_version` |
| model hash | `model_hash` |
| instance hash | `instance_hash` |
| seed | `seed` |
| workers | `workers` |
| budget | `budget_seconds` |
| native status | `status` |
| objective | `objective_encoded` |
| solver schedule hash | `solver_schedule_hash` |
| schedule artifact link | `schedule_artifact` |
| schedule artifact digest | `schedule_artifact_sha256` |

The two artifact-link fields must also be jointly present to be sufficient. Their equality with retained artifacts is an `R6` consistency question when present. Missing fields produce `CHECK_OB7_REQUIRED_<CANONICAL_FIELD>` and `OB7_COMPLETENESS=FAIL` without being absorbed into `R6`.

### 2.4 Closed experimental conformance

`P3_CLOSED_CONFORMANCE = OB6_CONSISTENCY AND OB7_COMPLETENESS`.

This is a repaired/preregistered experimental conformance definition only. Manuscript integration and any revision of formal theory remain deferred.

## 3. Bundle and copying semantics

The loader verifies authoritative retained bytes, then materializes a deep in-memory copy with eight separately addressable artifact classes. Every trial starts from a fresh load or fresh deep copy of the verified clean bundle. Mutators may update local self-consistency material but never independent cross-artifact references unless their frozen operator explicitly attacks that reference. No mutation is applied to a prior mutation.

## 4. Verdicts

- `PASS`: every applicable `R6` and `Complete(E_s)` check passes.
- `FAIL:<CHECK_ID>`: at least one declared scientific check fails; the first deterministic failed check is the terminal detector and the full set is retained.
- `UNEVALUABLE:<REASON>`: malformed harness input, unresolved source identity, parser error, missing experimental precondition, or implementation defect prevents a scientific verdict.

Crashes, exceptions, skipped units, silent row drops, and `UNEVALUABLE` outcomes are never corruption detections. Every requested unit must produce exactly one ledger row.

## 5. Clean-control migration policy

A clean copy is checked without mutation and records `OB6_CONSISTENCY`, `OB7_COMPLETENESS`, `P3_CLOSED_CONFORMANCE`, and the terminal verdict. A future failure under this repaired specification is classified `CLEAN_CONTROL_SPEC_MIGRATION_FAILURE`; it does not silently rewrite any legacy `42/42` result.

## 6. Non-adaptivity and execution boundary

Checker order, IDs, canonicalization, equality relations, required fields, expected detectors, mutations, and denominators are frozen by this specification and `config/experiments/p3_mutation_registry_v1.json`. Batch 2 permits unit fixtures and a minimal non-formal real-bundle smoke only. It forbids the full 42-chain clean control, full mutation population, rates, LLM/provider calls, optimizer/scheduler calls, or real lifecycle activation.
