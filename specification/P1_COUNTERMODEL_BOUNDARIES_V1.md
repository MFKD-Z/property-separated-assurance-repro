# P1 countermodel and failure-boundary specification V1

Four finite constructions delimit the conditional P1 claim.

| Construction | Removed boundary | Consequence |
|---|---|---|
| CM1 base-state failure | optimizer-origin-base-state | The invariant fails at the included initial index. |
| CM2 unauthorized selector | exclusive-selector | A non-optimizer determines `Dec(pi)` while `O` merely serializes; metadata can look valid without establishing authorship. |
| CM3 activation substitution | origin-gated-activation | Lifecycle activates `pi_U != Out_O(t)`, so exact optimizer output is not preserved. |
| CM4 out-of-band bypass | no-bypass | The admitted trace remains valid, but a broader claim about every real active state fails after an unmodeled pointer write. |

These constructions establish necessity or scope boundaries only where stated. They do not prove that all seven assumptions are independent or minimal.
