# Review: roadmap-prune drop-history append idempotent across uncommitted re-runs

## Scope
Reviewed `git diff HEAD` and `git status`. The only code change in scope is a single-line edit to `src/skills/roadmap-prune/SKILL.md:257` (the Step 4.2 drop-history append instruction). The other staged changes are unrelated planning artifacts (specs 60/61 rename, ROADMAP, plan/plan-review files) and are not part of this milestone's implementation.

Read the full `SKILL.md` and cross-checked the edit against spec `.ai-factory/specs/53-prune-ledger-append-idempotent.md` and the file's own ledger-contract lines (135, 155, 169, 234, 240, 264, 394).

## The change
Line 257 now inserts an idempotency guard before the append: if the drop-history row already exists and its **last** hash equals the current Step-4.1 snapshot hash, skip and report ("snapshot already ledgered — uncommitted re-run"); otherwise append as before.

## Findings

### Correctness — clean
- **Spec fidelity.** The guard matches spec 53 verbatim in intent: last-hash-only comparison, the exact report wording, the explicit "never a whole-row scan" instruction, and the "two distinct prunes always have a commit between them" rationale that justifies comparing only the last hash.
- **First-ever prune preserved.** "if the row already exists" is false on a fresh table, so control falls through to the unchanged "Otherwise append" path — find-or-create behavior is intact; no regression for the no-row case.
- **No false skip against self-heal (4.2a).** Self-heal ledgers each committed prune's parent (`<prune>^`). The current snapshot is HEAD. On an uncommitted re-run after a legacy rebuild, HEAD equals the last *prune commit*, which differs from that commit's parent — so the guard cannot fire spuriously after self-heal. It fires only in the true target case: HEAD unchanged between runs ⇒ same snapshot ⇒ equals the last-appended hash.
- **Verification cases hold.** run → re-run (no commit): second run skips → one hash. run → commit → run: new snapshot = new prune commit ≠ previously-ledgered parent → appends → two hashes. Both match the spec's dry-read expectations.
- **Delimiter and contract intact.** "comma-separated" is retained; "last hash" is well-defined over the comma-separated cell. The guard now actually enforces the "exactly one hash per prune" contract asserted at lines 155/264 rather than leaving it aspirational.

### Guards respected
- Older ledger entries are never touched (last-hash-only, explicitly "never a whole-row scan") — self-heal's history-repair territory is untouched.
- Self-heal pre-pass, versioned `## Features` header, Step 4.1 snapshot capture, and feature-row append rules are all byte-identical; the diff is exactly one line.

### Security / runtime
No security surface (documentation/instruction text). No runtime, migration, type, or concurrency concerns.

REVIEW_PASS
