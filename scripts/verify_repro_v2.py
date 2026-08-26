#!/usr/bin/env python3
"""Offline verifier for Property-Separated Assurance reproducibility package V2."""

from __future__ import annotations

import collections
import hashlib
import json
import math
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID_OVERHEAD_RUN = "AEI_ASSURANCE_OVERHEAD_FORMAL_20260826_B5R1_V1"
INVALID_OVERHEAD_RUN = "AEI_ASSURANCE_OVERHEAD_FORMAL_20260826_B5_V1"
OVERHEAD_MANIFEST_SHA256 = "f14fd4dd82b38971ba3daaa878d90fdbcd6de31a182ed87473f70cc6ea46d65f"
P3_MANIFEST_SHA256 = "6ababc4c1f9b5eb225f645fe62b7450d565dfcc85f59d3297d6e719a5cae9d8e"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def percentile(values: list[int], q: float) -> float:
    ordered = sorted(values)
    check(bool(ordered), "PERCENTILE_EMPTY")
    position = (len(ordered) - 1) * q
    low = math.floor(position)
    high = math.ceil(position)
    if low == high:
        return float(ordered[low])
    return ordered[low] + (ordered[high] - ordered[low]) * (position - low)


def verify_checksums() -> None:
    ledger = ROOT / "CHECKSUMS_SHA256.txt"
    check(ledger.is_file(), "CHECKSUM_LEDGER_MISSING")
    checked = 0
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        target = ROOT / relative
        check(target.is_file(), f"CHECKSUM_TARGET_MISSING {relative}")
        check(sha256(target) == expected, f"CHECKSUM_FAIL {relative}")
        checked += 1
    check(checked > 0, "CHECKSUM_LEDGER_EMPTY")
    print(f"CHECKSUMS=PASS; FILES={checked}")


def verify_legacy() -> None:
    semantic = list(read_jsonl(ROOT / "data/semantic/semantic_case_results_v1.jsonl"))
    valid = [row for row in semantic if row["expected_validation_outcome"] == "ACCEPT"]
    invalid = [row for row in semantic if row["expected_validation_outcome"] != "ACCEPT"]
    attacks = [row for row in semantic if row["authority_attack"]]
    errors = [row for row in semantic if row["semantic_incorrect"]]
    blocked = [row for row in errors if row["validator_interception_class"] == "DETERMINISTICALLY_BLOCKED_BEFORE_O"]
    propagated = [row for row in errors if row["validator_interception_class"] == "SCHEMA_VALID_BUT_SEMANTICALLY_WRONG_REACHED_O"]
    accepted = [row for row in semantic if row["accepted_schedule"]]
    check((len(semantic), len(valid), len(invalid), len(attacks)) == (160, 100, 60, 40), "LEGACY_SEMANTIC_DENOMINATOR")
    check(sum(row["structured_exact_match"] for row in valid) == 92, "LEGACY_STRUCTURED_EXACTNESS")
    check(len(errors) == 11, "LEGACY_SEMANTIC_ERROR_COUNT")
    check(sum(row["expected_validation_outcome"] == "ACCEPT" for row in errors) == 8, "LEGACY_ERROR_V_COUNT")
    check(sum(row["expected_validation_outcome"] != "ACCEPT" for row in errors) == 3, "LEGACY_ERROR_I_COUNT")
    check((len(blocked), len(propagated)) == (6, 5), "LEGACY_INTERCEPTION_PROPAGATION")
    check(sum(row["expected_validation_outcome"] == "ACCEPT" for row in propagated) == 2, "LEGACY_PROPAGATED_V")
    check(sum(row["expected_validation_outcome"] != "ACCEPT" for row in propagated) == 3, "LEGACY_PROPAGATED_I")
    check(len(accepted) == 97 and all(row["optimizer_origin"] and row["feasibility"] == "PASS" for row in accepted), "LEGACY_ACCEPTED_ORIGIN")

    authority = list(read_jsonl(ROOT / "data/authority/authority_case_results_v1.jsonl"))
    check(len(authority) == 40, "LEGACY_AUTHORITY_DENOMINATOR")
    check(not any(row["unauthorized_schedule_selection_attempt"] for row in authority), "LEGACY_AUTHORITY_SELECTION")
    check(not any(row["unauthorized_active_plan_mutation"] for row in authority), "LEGACY_AUTHORITY_ACTIVATION")

    p2 = list(read_jsonl(ROOT / "data/semantic/semantic_feasibility_counterexamples_v1.jsonl"))
    check(len(p2) == 12 and all(row["s0_f1_counterexample"] for row in p2), "LEGACY_P2")
    check(collections.Counter(row["kind"] for row in p2) == {
        "MACHINE_IDENTITY_SUBSTITUTION": 4,
        "VALID_TIME_INTERVAL_SUBSTITUTION": 4,
        "ORDER_OR_PRIORITY_SUBSTITUTION": 4,
    }, "LEGACY_P2_CLASSES")

    dynamic = list(read_jsonl(ROOT / "data/dynamic/a25_disturbance_matrix_v1.jsonl"))
    matrix = [row for row in dynamic if not row["variation_repeat"]]
    repeat = [row for row in dynamic if row["variation_repeat"]]
    check((len(dynamic), len(matrix), len(repeat)) == (96, 72, 24), "LEGACY_DYNAMIC_ACCOUNTING")

    chains = list(read_jsonl(ROOT / "data/reconstruction/a26_audit_chains_v1.jsonl"))
    check(len(chains) == 42 and all(row["plan_delta"]["recomputation"]["exact"] for row in chains), "LEGACY_RECONSTRUCTION")
    manifest = read_json(ROOT / "manifests/a26_audit_evidence_v1_manifest.json")
    for key in (
        "AUDIT_CHAIN_COMPLETENESS_RATE",
        "INPUT_TO_INSTANCE_LINK_RATE",
        "INSTANCE_TO_PLAN_LINK_RATE",
        "PLANDELTA_RECOMPUTATION_CONSISTENCY_RATE",
        "SOLVER_EVIDENCE_COMPLETENESS_RATE",
    ):
        metric = manifest["metrics"][key]
        check(metric["numerator"] == 42 and metric["denominator"] == 42, f"LEGACY_RECONSTRUCTION_METRIC {key}")
    replay = manifest["metrics"]["REPLAYABLE_DERIVED_AUDIT_RATE"]
    check(replay["numerator"] == 4 and replay["denominator"] == 4, "LEGACY_REPLAY")
    print("LEGACY_CORE=PASS; SEMANTIC=160; V=100; I=60; A=40; EXACT=92/100")
    print("LEGACY_ERRORS=11=8V+3I; INTERCEPTED=6/11; PROPAGATED=5/11=2V+3I")
    print("LEGACY_AUTHORITY=40/40; ORIGIN_LIFECYCLE=97/97; P2=12/12; RECONSTRUCTION=42; REPLAY=4/4")


def repeat_signature(row: dict) -> tuple:
    return (
        row.get("terminal_verdict"),
        row.get("ob6_consistency"),
        row.get("ob7_completeness"),
        row.get("p3_closed_conformance"),
        tuple(row.get("all_failed_checks", [])),
        row.get("scientific_classification"),
    )


def verify_p3() -> None:
    root = ROOT / "data/p3_negative_control"
    manifest_path = root / "formal_manifest.json"
    check(sha256(manifest_path) == P3_MANIFEST_SHA256, "P3_MANIFEST_HASH")
    manifest = read_json(manifest_path)
    check(manifest["formal_run_valid"] is True and manifest["strict_scientific_gate"] == "PASS", "P3_FORMAL_VALIDITY")
    for original, expected in manifest["final_raw_ledger_hashes"].items():
        original_name = Path(original).name
        if original_name == "README.md":
            continue
        if original_name == "environment.json":
            environment = read_json(root / "environment.json")
            check(environment["original_environment_sha256"] == expected, "P3_ENVIRONMENT_IDENTITY")
            continue
        target = root / original_name
        check(target.is_file() and sha256(target) == expected, f"P3_LEDGER_HASH {target.name}")

    clean = list(read_jsonl(root / "clean_control_results.jsonl"))
    check(len(clean) == 84, "P3_CLEAN_EXECUTIONS")
    clean_by_unit: dict[str, dict[int, dict]] = collections.defaultdict(dict)
    for row in clean:
        check(row["terminal_verdict"] == "PASS", "P3_CLEAN_VERDICT")
        check(row["ob6_consistency"] == "PASS" and row["ob7_completeness"] == "PASS", "P3_CLEAN_OB")
        clean_by_unit[row["scientific_unit_id"]][row["checker_pass"]] = row
    check(len(clean_by_unit) == 42, "P3_CLEAN_UNITS")
    check(all(set(passes) == {1, 2} and repeat_signature(passes[1]) == repeat_signature(passes[2]) for passes in clean_by_unit.values()), "P3_CLEAN_REPEAT")

    mutations = list(read_jsonl(root / "mutation_results.jsonl"))
    check(len(mutations) == 2184, "P3_MUTATION_EXECUTIONS")
    by_unit: dict[str, dict[int, dict]] = collections.defaultdict(dict)
    for row in mutations:
        by_unit[row["scientific_unit_id"]][row["checker_pass"]] = row
    check(len(by_unit) == 1092, "P3_UNIQUE_CONTROLLED_UNITS")
    check(all(set(passes) == {1, 2} and repeat_signature(passes[1]) == repeat_signature(passes[2]) for passes in by_unit.values()), "P3_REPEAT_MISMATCH")

    pass1 = [passes[1] for passes in by_unit.values()]
    expected_families = {"M1": 336, "M2": 42, "M3": 42, "M4": 42, "M5": 42, "M6": 42, "M7": 42, "M8": 42, "M9": 462}
    check(collections.Counter(row["mutation_family"] for row in pass1) == expected_families, "P3_FAMILY_COUNTS")
    check(all(row["scientific_classification"] == "DETECTED_AS_PREREGISTERED" for row in pass1), "P3_UNDETECTED_OR_INCIDENTAL")
    check(not any(row.get("unevaluable_reason") for row in pass1), "P3_UNEVALUABLE")
    m9 = [row for row in pass1 if row["mutation_family"] == "M9"]
    check(len(m9) == 462 and all(row["ob6_consistency"] == "PASS" and row["ob7_completeness"] == "FAIL" and row["p3_closed_conformance"] == "FAIL" for row in m9), "P3_M9_OB6_OB7")
    co_detector = sum(bool(set(row["observed_detector"]) - set(row["expected_detector"])) for row in pass1)
    check(co_detector == 168, "P3_CO_DETECTOR_COUNT")
    print("P3_CLEAN=42/42; EXACT_REPEAT=42/42")
    print("P3_FAMILIES=M1:336/336; M2-M8:42/42 each; M9:462/462")
    print("P3_UNDETECTED=0; UNEVALUABLE=0; REPEAT_MISMATCH=0; INCIDENTAL_ONLY_MISMATCH=0")
    print("P3_M9_SEPARATION=462/462 OB6_PASS_OB7_FAIL; EXPECTED_PLUS_CO_DETECTOR=168")


def verify_overhead() -> None:
    root = ROOT / "data/assurance_overhead"
    manifest_path = root / "formal_manifest.json"
    manifest = read_json(manifest_path)
    check(manifest["original_manifest_sha256"] == OVERHEAD_MANIFEST_SHA256, "OVERHEAD_MANIFEST_HASH")
    check(manifest["run_id"] == VALID_OVERHEAD_RUN and manifest["formal_run_valid"] is True, "OVERHEAD_RUN_VALIDITY")
    check(manifest["old_rows_reused"] is False, "OVERHEAD_OLD_ROWS_REUSED")
    check(manifest["previous_invalid_run_id"] == INVALID_OVERHEAD_RUN, "OVERHEAD_INVALID_PROVENANCE")
    check(manifest["row_counts"] == {"component": 65600, "h0": 65600, "total": 131200}, "OVERHEAD_MANIFEST_ROW_COUNTS")
    check(manifest["formal_component_artifact_pairs"] == 656, "OVERHEAD_PAIR_COUNT")
    check(
        len(manifest["failed_blocks"]) == 0
        and len(manifest["replacement_blocks"]) == 0
        and len(manifest["unevaluable_measurements"]) == 0,
        "OVERHEAD_FAILURE_COUNTS",
    )
    check(all(manifest[key] is True for key in ("no_llm_calls_verified", "no_optimizer_calls_verified", "no_network_calls_verified", "no_sut_write_verified")), "OVERHEAD_EXECUTION_BOUNDARY")

    allocation_count = sum(1 for _ in read_jsonl(root / "allocation_results.jsonl"))
    check(allocation_count == 656, "OVERHEAD_ALLOCATION_ROWS")
    summary = read_json(root / "summary.json")
    scaling = summary["descriptive_scaling"]
    estimable = sum(item["status"] == "DESCRIPTIVE_OBSERVED_RANGE_ONLY" for item in scaling.values())
    noninformative = sum(item["status"] == "NONINFORMATIVE_NOT_ESTIMABLE" for item in scaling.values())
    check((estimable, noninformative) == (30, 16), "OVERHEAD_SCALING_COUNTS")

    raw_path = root / "raw_timings.jsonl"
    profile = read_json(ROOT / "PACKAGE_PROFILE.json")
    if not raw_path.is_file():
        check(profile["raw_timings_required"] is False, "OVERHEAD_RAW_REQUIRED_BUT_MISSING")
        print("OVERHEAD_RAW_TIMINGS=RELEASE_ASSET_ONLY; SUMMARY_AND_MANIFEST=PASS")
        return

    expected_raw_hash = manifest["raw_result_hashes"][next(key for key in manifest["raw_result_hashes"] if key.endswith("raw_timings.jsonl"))]
    check(sha256(raw_path) == expected_raw_hash, "OVERHEAD_RAW_HASH")
    rows = collections.Counter()
    pairs = set()
    samples: dict[str, list[int]] = collections.defaultdict(list)
    for row in read_jsonl(raw_path):
        check(row["formal_run_id"] == VALID_OVERHEAD_RUN, "INVALID_OVERHEAD_ROW_PRESENT")
        role = row["measurement_role"]
        rows[role] += 1
        pairs.add((row["component_id"], row["artifact_id"]))
        if role != "COMPONENT":
            continue
        component = row["component_id"]
        if component == "H1":
            component = "H1_A22" if row["source_population"].startswith("A22") else "H1_A26"
        elif component == "H2":
            component = f"H2_{row['stratum']}"
        samples[component].append(row["raw_component_latency_ns"])
    check(rows == {"COMPONENT": 65600, "H0": 65600}, "OVERHEAD_RAW_ROW_COUNTS")
    check(len(pairs) == 656, "OVERHEAD_RAW_PAIR_COUNT")

    expected_medians = {
        "H1_A22": 67400.0,
        "H1_A26": 10747300.0,
        "H2_expected_accept": 12000.0,
        "H2_expected_reject": 7300.0,
        "H3": 551600.0,
        "H4": 878200.0,
        "H5": 12350.0,
        "H5_IO": 21030500.0,
        "H6": 17942500.0,
        "H7": 14700.0,
        "H8": 1567450.0,
    }
    for group, expected in expected_medians.items():
        check(statistics.median(samples[group]) == expected, f"OVERHEAD_MEDIAN {group}")
    h8 = samples["H8"]
    check(percentile(h8, 0.25) == 1277550.0, "OVERHEAD_H8_Q1")
    check(percentile(h8, 0.75) == 2032200.0, "OVERHEAD_H8_Q3")
    check(math.isclose(percentile(h8, 0.95), 2629705.0), "OVERHEAD_H8_P95")
    print("OVERHEAD_ROWS=65600_COMPONENT+65600_H0=131200; PAIRS=656; ALLOCATION=656")
    print("OVERHEAD_H8=1.56745ms; Q1-Q3=1.27755-2.03220ms; P95=2.629705ms")
    print("OVERHEAD_H6=17.9425ms; H5_IO=21.0305ms; SCALING=30_ESTIMABLE+16_NONINFORMATIVE")


def main() -> int:
    try:
        verify_checksums()
        verify_legacy()
        verify_p3()
        verify_overhead()
    except (AssertionError, KeyError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"VERIFY_PROPERTY_SEPARATED_ASSURANCE_REPRO_V2=FAIL; {exc}", file=sys.stderr)
        return 1
    print("VERIFY_PROPERTY_SEPARATED_ASSURANCE_REPRO_V2=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
