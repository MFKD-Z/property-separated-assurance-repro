# Property-Separated Assurance — Minimal Reproducibility Package V1

This package contains the frozen evidence needed to verify the principal reported results of a study on property-separated assurance for semantic-to-optimization manufacturing scheduling.

It intentionally excludes the manuscript, figures, supplementary submission files, revision reports, and historical internal artifacts.

## Verify the frozen evidence

Requirements: Python 3, standard library only.

From the package root, run:

```bash
python scripts/verify_frozen_evidence.py
```

Expected final status:

```text
VERIFY_FROZEN_EVIDENCE=PASS
```

The verifier checks the frozen file identities and recomputes the principal evidence counts, including:

- semantic cases: 160 total; V=100, I=60, A=40;
- structured exactness: 92/100;
- semantic errors: 11 = 8 V + 3 I;
- deterministic interception: 6/11;
- schema-valid propagation: 5/11 = 2 V + 3 I;
- accepted optimizer-origin schedules: 97/97;
- controlled authority challenges blocked: 40/40;
- controlled semantic–feasibility witnesses: 12/12;
- dynamic matrix accounting: 72 matrix units and 24 repeat units;
- accepted reconstruction chains: 42;
- five reconstruction checks: 42/42 each;
- bounded replay subset: 4/4.

## Package structure

```text
data/
  semantic/
  authority/
  dynamic/
  reconstruction/
manifests/
scripts/
source_identity/
CHECKSUMS_SHA256.txt
LICENSE.txt
README.md
```

## Reproducibility scope

The package is designed to verify the frozen evidence actually used in the study without rerunning the external language model or the scheduling experiments.

The archived language-model outputs are the fixed evidence realization. A new provider call would be a new realization and must not replace the archived evidence.

The package does not claim provider-general semantic accuracy, universal security, scheduling-performance superiority, global optimizer correctness, causal or tamper-proof provenance, industrial deployment, or cross-system empirical generality.

## Frozen implementation identity

- SUT evidence revision: `7ff79ee8ca81ea976c3791a5064772dbfb126082`
- recorded evidence-generation fingerprint: `36431f4b2fe7bcb58a3c571478d4eb7ed2698a39f1333df9c01ad7f5420e7571`
- external semantic model: `deepseek-v4-flash`
- temperature: `0`
- output format: JSON object
- semantic contract version: `A22_S5_EVENT_EXTRACTION_CONTRACT_V1`

No API key, token, password, or secret credential is included.

## Version

`v1.0.0`

## License

See `LICENSE.txt`.
