# P1 assumption-role specification V1

For an admitted transition `t`, `Out_O(t)` is the exact schedule artifact actually returned by optimizer `O`. The activation premise is exact artifact preservation: `Activated(t, pi) => pi = Out_O(t)` under the declared canonical identity/content/hash equality.

| ID | Canonical assumption | Role |
|---|---|---|
| A1 | enumerated-path | Limits the theorem to the declared transition relation. |
| A2 | fixed-transition-semantics | Holds mapping, activation, equality, and transition meanings fixed over the sequence. |
| A3 | optimizer-origin-base-state | Discharges the base case when the invariant includes the initial state. |
| A4 | range-closure | Excludes schedule artifacts and activation capability from semantic, validation, and construction mappings. |
| A5 | exclusive-selector | Makes `O` the only admitted component that determines schedule decisions. |
| A6 | origin-gated-activation | Requires the activated artifact to equal `Out_O(t)` exactly. |
| A7 | no-bypass | Excludes active-pointer changes outside the admitted transition relation for the system-level reading. |

The set is sufficient and declared. It is not claimed minimal, mutually independent, or individually necessary for every alternative formulation.
