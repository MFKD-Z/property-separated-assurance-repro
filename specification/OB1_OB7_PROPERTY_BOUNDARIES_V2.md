# OB1–OB7 property and boundary specification V2 — manuscript synchronization

| Obligation | Synchronized declared property |
|---|---|
| OB1 semantic admissibility | Only supported schema-, type-, range-, and identity-valid events enter construction. |
| OB2 schedule decision-authority exclusion | Upstream semantic/validation/construction components have negative `MayAuthor(·,Pi)` and `MayActivate(·)` capability; `O` exclusively determines `Dec(pi)`. |
| OB3 deterministic instance construction | `K(r,K_eng,S_op)` deterministically constructs `X` from the admitted event, authoritative engineering knowledge, and operational state. |
| OB4 solver-independent deterministic feasibility | The exact selected artifact is checked against the exact constructed instance independently of optimizer status. |
| OB5-o exact artifact preservation | `Activated(t,pi) -> pi == Out_O(t)`. |
| OB5-l lifecycle consistency | Parent/version, immutable persistence, and active-pointer transition remain consistent. |
| OB6 cross-artifact consistency | `R6` checks identities, hashes, links, lineage, and recomputed deltas. |
| OB7 solver-evidence completeness | `Complete(E_s)` checks the required solver-evidence inventory and links. |

OB5-o and OB5-l remain clauses of OB5. OB6 and OB7 remain non-substitutable. These are the seven declared conformance obligations exercised by the methodology; they are not claimed to exhaust trustworthy AI-enabled manufacturing requirements.

The synchronized manuscript further separates semantic truth, operational assurance, and post-acceptance audit evidence. That clarification changes no frozen empirical result.
