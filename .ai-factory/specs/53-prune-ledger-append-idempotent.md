# roadmap-prune: drop-history append is idempotent across uncommitted re-runs

Source observation: `plan-reviews/87-3-1-roadmap-prune-drop-history-…-plan-review-1.md:38`, re-verified live 2026-07-12 — the Step 4.2 append ("append exactly the Step-4.1 snapshot hash, one per prune run") is unconditional.

## Current state

Running the prune twice **without committing between runs** captures the same Step-4.1 snapshot (HEAD is unchanged) and appends it to the `Roadmap drop history` row twice. Two identical hashes violate the "exactly one hash per prune" ledger contract, and the self-heal pre-pass cannot dedup them — the previous run is not yet a committed prune commit, so it never enters the candidate set. Pre-existing behavior, deliberately left out of 3.1's scope (ledger semantics, not run idempotency).

## Change

One guard before the Step 4.2 append: when the drop-history row's **last** hash already equals the current Step-4.1 snapshot hash, skip the append and report ("snapshot already ledgered — uncommitted re-run"). Comparing against the last hash only is correct by construction: two distinct prunes always have a commit between them, so their snapshots differ.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` only (Step 4.2 / the drop-history append instruction). Runs after 5.3 (same file, serial).

## Guards

- Never dedup older entries — history repair is the self-heal pre-pass's territory, untouched.
- Ledger semantics, versioned Features header, self-heal, snapshot capture byte-identical otherwise.

## Verification

- Dry-read: run → re-run without commit → the row gains one hash; run → commit → run → two hashes.
