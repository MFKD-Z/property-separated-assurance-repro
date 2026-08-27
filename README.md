# Property-Separated Assurance — Reproducibility Package V2

This versioned package supports the final manuscript evidence for property-separated assurance in semantic-to-optimization manufacturing scheduling.

## Versions

- `v1.0.0` is the historical legacy minimal reproducibility package for semantic, authority, P2, dynamic accounting, reconstruction, and replay evidence.
- `v2.0.0` carries that evidence forward and adds the exact-artifact P1/OB specification, controlled P3 negative controls, and bounded assurance implementation-cost evidence.
- 
## Manuscript-synchronized formal clarification

The archived `v2.0.0` release and Zenodo DOI `10.5281/zenodo.22110943` remain the frozen empirical-evidence package. A later scientific-argument closure refined formal terminology without changing any retained output, denominator, or numerical result.

For the manuscript-synchronized formulation, see:

- `specification/P1_ASSUMPTION_ROLE_SPEC_V2.md`;
- `specification/OB1_OB7_PROPERTY_BOUNDARIES_V2.md`;
- `MANUSCRIPT_SYNC_NOTE_20260827.md`.

The V2 clarification distinguishes type closure from authority closure, separates authoritative engineering knowledge (`K_eng`) from operational state (`S_op`), uses `authority-closure` and `exact-artifact-activation` in P1, and treats reconstruction as post-acceptance evidence rather than an activation prerequisite. The historical V1 specification files are retained for release provenance.

## Verify

Requirements: Python 3 and the standard library. No network, language-model call, optimizer, SUT checkout, or experiment rerun is required.

```bash
python scripts/verify_repro_v2.py
```

Expected terminal status:

```text
VERIFY_PROPERTY_SEPARATED_ASSURANCE_REPRO_V2=PASS
```

The Git tree verifies all compact evidence and records the timing ledger as a versioned release-only asset. The V2 release ZIP includes the complete timing ledger and additionally recomputes the frozen latency statistics from its 131,200 rows.

## Evidence classes

- fixed semantic evidence and validator outcomes;
- authority exclusion and retained optimizer-origin/lifecycle witnesses;
- P2 non-implication witnesses;
- legacy accepted-chain reconstruction and bounded replay;
- controlled P3 clean and M1–M9 negative controls;
- bounded component-only latency, allocation, and observed-range descriptive scaling evidence.

## Archival record

The final-manuscript reproducibility package `v2.0.0` is archived on Zenodo under the version-specific DOI:

https://doi.org/10.5281/zenodo.22110943

The corresponding GitHub release is:

https://github.com/MFKD-Z/property-separated-assurance-repro/releases/tag/v2.0.0

## Claim boundary

The package verifies finite frozen evidence from one reference implementation and declared environment. It does not prove universal trustworthiness, security, tamper-proof provenance, real-time capability, industrial scalability, or production readiness. External language-model outputs are archived fixed realizations; a new provider call would create a different realization.
