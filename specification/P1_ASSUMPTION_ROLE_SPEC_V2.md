# P1 assumption-role specification V2 — manuscript synchronization

This documentation-only specification synchronizes the public repository with the scientific-argument-closed manuscript. It does not replace or mutate the archived v2.0.0 evidence release.

For admitted transition `t`, `Out_O(t)` is the exact schedule artifact returned by the admitted invocation of `O`. The activation condition is:

`Activated(t, pi) -> pi == Out_O(t)`

`E_origin(t,pi)` denotes machine-checkable evidence linking the optimizer invocation, the exact returned artifact, and the lifecycle transition.

| ID | Canonical assumption | Role |
|---|---|---|
| A1 | enumerated-path | Limits the invariant to the declared scheduling/lifecycle path. |
| A2 | fixed-transition-semantics | Holds transition, mapping, activation, and equality semantics fixed over the analyzed sequence. |
| A3 | optimizer-origin-base-state | Supplies the induction base. |
| A4 | authority-closure | Excludes schedule authorship/activation capability from `E`, `V_map`, and `K`; excludes substitution by `F`; excludes lifecycle selection of `Dec(pi)`. |
| A5 | exclusive-selector | Makes `O` the sole admitted selector of machine, mode, start, and end decisions. |
| A6 | exact-artifact-activation | Requires the activated artifact to equal `Out_O(t)` exactly. |
| A7 | no-bypass | Excludes out-of-band active-state mutation from the system-level claim. |

A4 is stronger than type-range separation. The implementation-facing authority restriction is expressed through negative `MayAuthor(c,Pi)` and `MayActivate(c)` capabilities. The seven assumptions are sufficient, not claimed minimal or mutually independent.

Historical relation: archived `P1_ASSUMPTION_ROLE_SPEC_V1.md` used the shorthand labels `range-closure` and `origin-gated-activation`. The V2 wording makes the same intended boundary explicit and does not change any empirical result.
