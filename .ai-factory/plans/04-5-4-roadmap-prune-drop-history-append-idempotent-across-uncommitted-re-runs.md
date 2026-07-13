# Plan: roadmap-prune: drop-history append idempotent across uncommitted re-runs

## Context
Make the Step 4.2 drop-history append idempotent so a prune re-run without an intervening commit does not append the same snapshot hash twice, upholding the "exactly one hash per prune" ledger contract.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Guard the append

- [x] **Task 1: Add the uncommitted-re-run guard to the drop-history append**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Edit the Step 4.2 drop-history append instruction at line 257 (`For the drop history row: find or create it at the bottom of the Features table and append exactly the Step-4.1 snapshot hash (one per prune run), comma-separated.`). Insert one guard **before** the append: when the drop-history row already exists and its **last** hash equals the current Step-4.1 snapshot hash, skip the append and report it — wording per the spec, e.g. "snapshot already ledgered — uncommitted re-run". State explicitly that the comparison is against the **last** hash only (not a full-row scan), because two distinct prunes always have a commit between them so their snapshots differ — mirror the spec's rationale so an implementer does not "improve" it into a whole-row dedup. Keep the rest of the sentence (find-or-create, comma-separated, one-per-prune) intact. Do not touch the self-heal pre-pass (4.2a), the versioned `## Features` header handling, the feature-row append rules, or Step 4.1's snapshot capture — every other line stays byte-identical. Note: this milestone runs after 5.3 on the same file; edit against the current on-disk text.

## Notes
- Single-task, single-file, doc-behavioral edit → one commit at the end; no commit plan needed.
- Guards (from spec `.ai-factory/specs/53-prune-ledger-append-idempotent.md`): never dedup older entries (that is the self-heal pre-pass's territory, untouched); ledger semantics, versioned Features header, self-heal, and snapshot capture stay byte-identical otherwise.
