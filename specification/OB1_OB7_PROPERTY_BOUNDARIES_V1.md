# OB1–OB7 property and boundary specification V1

| Obligation | Declared property |
|---|---|
| OB1 semantic admissibility | Only schema-, type-, range-, support-, and identity-valid events enter deterministic construction; failures reject closed. |
| OB2 schedule-authority exclusion | Non-optimizer layers have neither schedule-decision nor activation authority; `O` is the admitted selector. |
| OB3 deterministic instance construction | Authoritative state and an admitted event deterministically produce the optimization instance without selecting a schedule. |
| OB4 solver-independent feasibility | The exact selected schedule is checked against the exact instance without trusting optimizer status. |
| OB5-o exact artifact preservation | `Activated(t, pi) => pi = Out_O(t)`. |
| OB5-l lifecycle consistency | Parent, version, immutable persistence, and active-pointer transition remain consistent around the accepted artifact. |
| OB6 cross-artifact consistency | Identities, hashes, links, lineage, and recomputed deltas agree under the declared projection `R6`. |
| OB7 solver-evidence completeness | The required solver-evidence inventory `Complete(E_s)` is present and linked. |

OB1 owns semantic admissibility; OB2 owns schedule-authority exclusion. OB5-o and OB5-l are internal clauses, not an eighth obligation. OB6 consistency and OB7 completeness are non-substitutable: full repaired P3 conformance requires `R6(z)` and `Complete(E_s)`, but neither predicate is defined as the other. The obligations cover the complete declared property set of this methodology, not every requirement for trustworthy AI or manufacturing.
