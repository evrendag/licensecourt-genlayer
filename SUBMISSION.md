# Portal submission
## Project name
LICENSECOURT
## One-line summary
A consensus-based release passport that verifies open-source license compatibility against pinned repository and package evidence.
## Description (under 1000 characters)
LICENSECOURT issues evidence-backed license passports for software releases. A developer submits a public repository, immutable commit, exact package version and intended distribution model. The GenLayer contract fetches the pinned LICENSE, manifest and registry metadata, then checks SPDX expressions, obligations and policy conflicts through independent validator analysis. Verdict and primary risk must match; confidence must remain in the same band and differ by at most 10 points. Deterministic guards reject moving branches, contradictory fields and unsupported results. COMPATIBLE releases receive an ACTIVE passport; CONDITIONAL results list required actions; INCOMPATIBLE releases are blocked; missing or conflicting evidence fails closed. Passports are versioned and challengeable, preventing later releases from overwriting earlier evidence. Includes source, tests, architecture and a live consensus workflow. This is a technical evidence tool, not legal advice.
## Suggested tags
Developer Tools · AI Verification · Governance
