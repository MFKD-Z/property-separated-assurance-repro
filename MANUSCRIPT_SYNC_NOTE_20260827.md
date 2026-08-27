# Manuscript synchronization note — 2026-08-27

The archived reproducibility package `v2.0.0` and Zenodo record `10.5281/zenodo.22110943` remain the immutable empirical-evidence release for the manuscript.

After publication of v2.0.0, the manuscript underwent a scientific-argument closure that clarified formal terminology without changing retained data, outputs, denominators, or numerical results. The main clarifications are:

1. `K_eng` (authoritative engineering knowledge) and `S_op` (operational state) are represented separately in the formal constructor;
2. P1 distinguishes type closure from **authority closure** using negative `MayAuthor` / `MayActivate` capability predicates;
3. the earlier shorthand labels `range-closure` and `origin-gated-activation` are refined to `authority-closure` and `exact-artifact-activation`;
4. semantic truth, request-to-activation operational assurance, and post-acceptance reconstruction/audit are represented as three evidence planes;
5. P3 is explicitly post-acceptance and is not part of the definition of operational activation.

No v2.0.0 evidence file should be rewritten to incorporate these clarifications. Repository documentation may point readers to synchronized V2 specifications while preserving the archived V1 specification files as historical release evidence.

## Historical terminology note

The published v2.0.0 GitHub release description used the shorthand `preregistered P3 controlled negative-control evidence`. The manuscript-synchronized terminology is **pre-specified** (or protocol-frozen before execution where the freeze is explicitly documented). The release description is retained as historical metadata; the clarification does not alter the mutation registry, checker, results, or any scientific unit.
