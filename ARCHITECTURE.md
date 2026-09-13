# Architecture
`Audit` pins repository, commit, release, ecosystem, manifest and distribution model. Validators derive canonical raw GitHub URLs themselves; users cannot inject arbitrary fetch targets.

Exact-consensus fields: verdict, primary risk, obligation bitmask and evidence gap. Evidence score differs by at most 10 within one band; blocker/condition counts differ by at most one. Contract guards enforce verdict consistency.

Security: full SHA only, bounded paths, no traversal, untrusted-file prompt boundary, one finalization per audit and fail-closed missing evidence.
