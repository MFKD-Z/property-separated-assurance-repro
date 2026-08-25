#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, collections, sys

ROOT=Path(__file__).resolve().parents[1]

EXPECTED={
"data/semantic/semantic_benchmark_v1.jsonl":"bc9a675c1ebbb5d131e98ba3ba1a113622889866194424f748dd463fa747c867",
"data/semantic/real_llm_outputs_v1.jsonl":"48530bd11e1266128f9e8ab1324349272dbfc8c11903bfa20e7bdb57f0ad1e2e",
"data/semantic/semantic_case_results_v1.jsonl":"ed741343815f13f5e4222a72eb5043da43040074882bb5315f327094b9ed71d1",
"data/semantic/semantic_feasibility_counterexamples_v1.jsonl":"0a21e6d43066c4c081f5a8bd34930e5a8190a150cc44a76d962426e2349ee5f3",
"data/authority/authority_case_results_v1.jsonl":"e43791b83b6a4e7cf15fa3c347c4b8cc61eae28b9714fbbac39a97ce8f3f7650",
"data/dynamic/a25_disturbance_matrix_v1.jsonl":"4ccb6130e22fd87675939f75d8ffe8167927d46c612260257e771cb7d3f8b5e9",
"data/reconstruction/a26_audit_chains_v1.jsonl":"6736aa25d2729de8aa2ad8761b9597a734a20a05ec7e1a4a3dc6a3284bff2e92",
}

def h(p):
    x=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): x.update(b)
    return x.hexdigest()

def jl(rel):
    return [json.loads(x) for x in (ROOT/rel).read_text(encoding="utf-8").splitlines() if x.strip()]

for rel,exp in EXPECTED.items():
    got=h(ROOT/rel)
    assert got==exp, f"HASH_FAIL {rel}: {got}"

sem=jl("data/semantic/semantic_case_results_v1.jsonl")
V=[r for r in sem if r["expected_validation_outcome"]=="ACCEPT"]
I=[r for r in sem if r["expected_validation_outcome"]!="ACCEPT"]
A=[r for r in sem if r["authority_attack"]]
err=[r for r in sem if r["semantic_incorrect"]]
blk=[r for r in err if r["validator_interception_class"]=="DETERMINISTICALLY_BLOCKED_BEFORE_O"]
pro=[r for r in err if r["validator_interception_class"]=="SCHEMA_VALID_BUT_SEMANTICALLY_WRONG_REACHED_O"]
acc=[r for r in sem if r["accepted_schedule"]]
assert (len(sem),len(V),len(I),len(A))==(160,100,60,40)
assert sum(r["structured_exact_match"] for r in V)==92
assert len(err)==11 and sum(r["expected_validation_outcome"]=="ACCEPT" for r in err)==8
assert len(blk)==6 and len(pro)==5
assert sum(r["expected_validation_outcome"]=="ACCEPT" for r in pro)==2
assert sum(r["expected_validation_outcome"]!="ACCEPT" for r in pro)==3
assert all(r["optimizer_reached"] and r["feasibility"]=="PASS" and r["optimizer_origin"] for r in pro)
assert len(acc)==97 and all(r["optimizer_origin"] and r["feasibility"]=="PASS" for r in acc)

auth=jl("data/authority/authority_case_results_v1.jsonl")
assert len(auth)==40
assert not any(r["unauthorized_schedule_selection_attempt"] for r in auth)
assert not any(r["unauthorized_active_plan_mutation"] for r in auth)

p2=jl("data/semantic/semantic_feasibility_counterexamples_v1.jsonl")
assert len(p2)==12 and all(r["s0_f1_counterexample"] for r in p2)
assert collections.Counter(r["kind"] for r in p2)=={
"MACHINE_IDENTITY_SUBSTITUTION":4,
"VALID_TIME_INTERVAL_SUBSTITUTION":4,
"ORDER_OR_PRIORITY_SUBSTITUTION":4,
}
assert all(r["semantic_correctness_S"]==0 and r["feasibility_F"]==1 for r in p2)

llm=jl("data/semantic/real_llm_outputs_v1.jsonl")
assert len(llm)==160 and all(len(r["attempts"])==1 and r["transport_status"]=="SUCCESS" for r in llm)

a25=jl("data/dynamic/a25_disturbance_matrix_v1.jsonl")
matrix=[r for r in a25 if not r["variation_repeat"]]
repeat=[r for r in a25 if r["variation_repeat"]]
assert (len(a25),len(matrix),len(repeat))==(96,72,24)
assert sum(r["execution_outcome"]=="ACCEPTED_SCHEDULE" for r in matrix)==30
assert sum(r["execution_outcome"]=="PRE_SOLVE_CONTRACT_BLOCK" for r in matrix)==42
assert sum(r["execution_outcome"]=="ACCEPTED_SCHEDULE" for r in repeat)==12
assert sum(r["execution_outcome"]=="PRE_SOLVE_CONTRACT_BLOCK" for r in repeat)==12

a26=jl("data/reconstruction/a26_audit_chains_v1.jsonl")
assert len(a26)==42 and all(r["plan_delta"]["recomputation"]["exact"] for r in a26)
ids25={(r["scenario_id"],r["profile_id"],r["variation_repeat"]) for r in a25 if r["execution_outcome"]=="ACCEPTED_SCHEDULE"}
ids26={(r["scenario_id"],r["profile_id"],r["variation_repeat"]) for r in a26}
assert ids25==ids26

m=json.loads((ROOT/"manifests/a26_audit_evidence_v1_manifest.json").read_text(encoding="utf-8"))
for k in ["AUDIT_CHAIN_COMPLETENESS_RATE","INPUT_TO_INSTANCE_LINK_RATE","INSTANCE_TO_PLAN_LINK_RATE",
          "PLANDELTA_RECOMPUTATION_CONSISTENCY_RATE","SOLVER_EVIDENCE_COMPLETENESS_RATE"]:
    assert m["metrics"][k]["numerator"]==42 and m["metrics"][k]["denominator"]==42
assert m["metrics"]["REPLAYABLE_DERIVED_AUDIT_RATE"]["numerator"]==4
assert m["metrics"]["REPLAYABLE_DERIVED_AUDIT_RATE"]["denominator"]==4

print("VERIFY_FROZEN_EVIDENCE=PASS")
print("SEMANTIC=160; V=100; I=60; A=40; STRUCTURED_EXACT=92/100")
print("SEMANTIC_ERRORS=11=8V+3I; INTERCEPTED=6; PROPAGATED=5=2V+3I")
print("ACCEPTED_OPTIMIZER_ORIGIN=97/97")
print("AUTHORITY_ATTACKS_BLOCKED=40/40")
print("P2_CONTROLLED_WITNESSES=12/12")
print("A25_MATRIX=72(30 accepted,42 blocked); REPEAT=24(12 accepted,12 blocked)")
print("A26=42 accepted chains; five checks=42/42; bounded replay=4/4")
