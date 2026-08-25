# System Under Test Baseline

Captured: 2026-08-24T19:57:01.2535418+08:00

## Repository authority

- `SYSTEM_ROOT=C:\Users\WM\Desktop\ILLM\SCHEDULING_SYSTEM_POST_MVP`
- `CURRENT_HEAD=7ff79ee8ca81ea976c3791a5064772dbfb126082`
- `EXPECTED_HEAD=7ff79ee`
- `EXPECTED_HEAD_MATCH=true`
- `SUT_MODIFIED=false` (this goal did not modify the SUT)

The worktree was already dirty at intake. Therefore the current checked-out
source—not old documentation—is the architectural authority, while the HEAD
identity still matches the requested commit. Pre-existing changes were:

```text
 M PROJECT_HANDOFF.md
 M README.md
 M src/scheduling_system_post_mvp/__init__.py
 M src/scheduling_system_post_mvp/services/data_driven_rescheduling_demo.py
 M src/scheduling_system_post_mvp/services/execution_progress_rescheduling.py
 M tests/test_mes_execution_ingress.py
?? acceptance/results/s6_quantity_semantics_diagnostic/
?? data/public/brandimarte/mk11.json ... mk15.json
?? data/public/brandimarte/raw/mk11.txt ... mk15.txt
?? docs/INDUSTRIAL_CLOSED_LOOP_ACCEPTANCE_V1.md
?? docs/PUBLIC_FJSP_CLOSED_LOOP_VALIDATION_V1.md
?? examples/public_benchmark_validation/{derived,raw,runtime_diagnostic_runs}/
?? examples/public_benchmark_validation/manifests/validation_result.json
?? runtime/
?? scripts/run_public_fjsp_closed_loop_validation.py
?? src/scheduling_system_post_mvp/services/public_fjsp_closed_loop_validation.py
?? src/scheduling_system_post_mvp/validation/
?? tests/test_public_fjsp_closed_loop_validation.py
?? tests/test_system_validation_campaign.py
?? tests/test_system_validation_protocol.py
```

## Implemented architecture

| Concern | Current implementation |
|---|---|
| Optimizer authority | `optimizer/profile_aware_cp_sat.py::solve_profile`; ID `PROFILE_AWARE_CP_SAT_OPTIMIZER_V1`; dispatched by `services/unified_scheduling.py::schedule` |
| NL event ingress | `services/natural_language_event_ingress.py::reschedule_from_natural_language` |
| Provider interfaces | `services/llm_provider_interface.py::LLMProvider`; S5 uses the same abstract interface with `RuleBasedNaturalLanguageEventProvider` |
| Rule/mock/external providers | `RuleBasedLLMProvider`, `MockLLMProvider`, `ExternalLLMProvider`; S5 also has `RuleBasedNaturalLanguageEventProvider` |
| Deterministic semantic validation | `validate_natural_language_event` and `validate_structured_extraction` |
| Product/master-data construction | `resolve_product_route` and `materialize_new_order_from_product_template`; provider route generation is disabled |
| Business-event construction | `BusinessEvent.from_mapping`, `MachineFailureEvent.from_mapping`, `apply_business_event` |
| ERP ingress | `ErpOrderIngress.from_mapping` → `ingest_erp_order`; accepts business header only |
| MES ingress | `MesExecutionIngress.from_mapping` → `ingest_mes_execution_state`; exact identifier/status mapping into S9/S4 |
| Independent feasibility | `acceptance/benchmark/reference/feasibility_validator.py::validate_schedule`; no OR-Tools dependency |
| PlanDelta | `_dynamic_delta` produces V1/S3 forms; `_progress_delta` produces `S4PlanDelta`; persisted by `accept_plan` |
| Active plan lifecycle | `ActivePlanStore`, `accept_plan`, `schedule_and_accept`; immutable versions plus atomic active pointer |
| Solver evidence | optimizer ID/backend/method, schedule source/hash, objective vector, profile score/encoding, model hashes, cap phase, search configuration, native status, optimality, phase timings/conflicts/branches, feasibility |

## Provider reality

- `RULE_BASED_PROVIDER=true`
- `MOCK_PROVIDER=true`
- `REAL_LLM_PROVIDER=true`
- `EXTERNAL_PROVIDER_INTERFACE=true`
- `ACTIVE_PROVIDER=RULE_BASED`
- `LIVE_EXTERNAL_CONFIGURATION_PRESENT=true` at capture (values were not read or recorded)
- `LIVE_EXTERNAL_CALL_EXECUTED=false`

The external provider is a real OpenAI-compatible JSON-over-HTTP implementation
and is credential-gated. Its mere availability does not make rule-based or mock
runs probabilistic LLM evidence.

## Relevant source hashes (current worktree bytes)

| File | SHA-256 |
|---|---|
| `natural_language_event_ingress.py` | `a37024f7185ac8b01f7aa8ffab051e226f979991d09112f6590ffe170734c3a9` |
| `llm_provider_interface.py` | `107edc1ec493a9cc373989f45499e4ad24918ad5b8ec1c8afa1ba72396c4f7c2` |
| `business_event_rescheduling.py` | `ca9ebac48477be1ee9859a573e64ed13b3547a4a0c334f452a388c99b6aee4db` |
| `active_plan_lifecycle.py` | `487cde61e9f8a17ca21b45ea2c9a764770a993a75e12ea1f1267bd14bf59d5a1` |
| `erp_order_ingress.py` | `f02641d1568056bf53f8100154a5b522f87ed197cc23878935fc81e9aff51fda` |
| `mes_execution_ingress.py` | `3951dd165dc53b163d32f6609d6714524a379a3b0f501358abe523cd20dc372b` |
| `industrial_dataset_loader.py` | `7e53e1d1ab7c2095983a0edd3e715db70f75885066e97bac4b10437362914e2c` |
| `unified_scheduling.py` | `800f84e971bcb0fc4210f2fc3576f6400029e5adc917f09e51f74a50f0ed9e75` |
| `profile_aware_cp_sat.py` | `b5ebd0ef1ca15cc267b7ce9e001e31114f87aae0fb81e1ee80fed2762c0dbb01` |
| `feasibility_validator.py` | `dd57998f0df86a99062c2ef62fa8f120deab10bd3d1aa4a85ab11ba128cf3b0e` |
