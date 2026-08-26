# P3 repaired checker specification V1

The frozen checker evaluates three non-equivalent relations over 42 retained accepted bundles:

- `OB6_CONSISTENCY = R6(z)`: cross-artifact equality, linkage, lineage, canonicalization, artifact identity, and delta reconstruction agree.
- `OB7_COMPLETENESS = Complete(E_s)`: eleven required solver-evidence fields are present and nonempty.
- `P3_CLOSED_CONFORMANCE = OB6_CONSISTENCY AND OB7_COMPLETENESS`.

Every clean or mutated unit starts from a fresh verified copy. The checker receives no mutation-family metadata, returns every failed check in deterministic order, and distinguishes `PASS`, `FAIL:<CHECK_ID>`, and `UNEVALUABLE:<REASON>`. Crashes, skipped rows, and unevaluable rows are never detections.

Frozen identities:

- checker specification SHA-256: `13bc79cd08375983ab5d8200995c6c7003f0e42dc939f97b285d1a7e20cfef18`
- checker implementation SHA-256: `c0fa4957e18ab5b403df99628b77d5236f9dc8fcef18ff1ab809f941e5651f4a`
- mutation registry SHA-256: `5874fdb1b9267878db38598a764134bb37bc8cef890abbfcf30dd7a8fb4dca4f`
- source-bundle manifest SHA-256: `e5b62f6f428255892b217f176a9d166369653d0f33343a6e57801fd1d170dd51`

This is a controlled negative-control specification. It does not establish arbitrary-corruption detection, security, tamper-proof provenance, or unseen-mutation generalization.
