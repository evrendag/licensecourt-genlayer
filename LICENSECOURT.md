# LICENSECOURT

LICENSECOURT turns open-source license review into a verifiable GenLayer workflow.

## What it does

1. A builder submits a repository, revision, allowed-license policy, and official GitHub evidence URLs.
2. Independent GenLayer validators reopen the same sources and inspect the repository metadata, license endpoint, license file, and revision.
3. Consensus requires agreement on the verdict, detected license, evidence quality, primary gap, and score band.
4. The contract issues an active on-chain License Compliance Passport.

The contract fails closed when sources are unavailable, the revision is not verifiable, or the license cannot be identified. It is a compliance evidence primitive, not legal advice.

## Example evidence URLs

For `owner/repository`, use:

- `https://api.github.com/repos/owner/repository`
- `https://api.github.com/repos/owner/repository/license`
- `https://api.github.com/repos/owner/repository/contents/LICENSE`

## Why GenLayer matters

License compliance is not a single deterministic lookup. Repositories expose metadata, files, and revision context across public sources. LICENSECOURT uses independent web-reading validators and an equivalence rule so one operator cannot silently decide the result.

## Contract

Deploy `contract.py` on GenLayer Studio Next, then connect the frontend to the resulting address. The contract exposes `submit_audit`, `run_audit`, `get_audit`, `get_passport`, and `get_counts`.
