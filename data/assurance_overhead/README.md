# Bounded assurance implementation-cost evidence

Only the valid formal run `AEI_ASSURANCE_OVERHEAD_FORMAL_20260826_B5R1_V1` contributes scientific timing rows. It contains 656 registered component/artifact pairs, 65,600 component rows, 65,600 paired H0 rows, 131,200 total rows, 656 allocation rows, zero failed or replacement blocks, and zero unevaluable measurements.

The 138 MB `raw_timings.jsonl` is release-ZIP-only to keep the ordinary Git tree compact. The V2 release ZIP includes the complete ledger; the offline verifier checks its frozen SHA-256 and independently recomputes row counts, medians, H8 quartiles, and H8 p95. Process-block JSON duplicates the row evidence and is omitted; its original frozen hashes remain in `formal_manifest.json`.

The first run contributes zero timing rows. See `../../provenance/INVALID_RUN_NOTE.md`. Reported scaling relations are descriptive over the observed artifact range and are not asymptotic or extrapolative claims.
