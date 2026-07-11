## Plan Review Summary

**Plan:** 3.1 — roadmap-prune: drop-history is a prune-snapshot ledger — versioned Features header + legacy self-heal
**Files Reviewed:** plan + `src/skills/roadmap-prune/SKILL.md`, `src/skills/temporal-tree/SKILL.md`, spec note `.ai-factory/notes/59-prune-drop-history-snapshot-ledger-versioned-selfheal.md`, ROADMAP.md:197, ARCHITECTURE.md
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap** (`.ai-factory/ROADMAP.md:197`): the milestone line resolves cleanly to the plan title and to `Spec:` note 59. The plan's tasks are a faithful decomposition of the spec's five edits + assumption + retirement path. Linkage intact. **OK.**
- **Governing spec** (note 59): every task traces to a spec clause — Edit 1 → Tasks 2/3, Edit 2 → Tasks 1/5, Edit 3 → Task 4, Edit 4 (retirement) → Task 4's legacy-removable note, Edit 5 (coupling) → Tasks 5/6, force-push assumption → Task 1. No spec clause is orphaned; no task invents scope beyond the spec. **OK.**
- **Architecture** (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy" + repo CLAUDE.md cross-file-invariant rule): the header string is a cross-file invariant shared by `roadmap-prune` (writer) and `temporal-tree` (reader). The plan declares the coupling sentence on **both** sides (Task 5 + Task 6), exactly as the repo CLAUDE.md requires. `aif-architecture`'s template is correctly left unmarked (an unmarked header *is* v1; the first prune self-heals it). No engine content is inlined. **OK.**
- RULES.md / skill-context aif-review: not present — no gate to apply. **WARN (informational only).**

### Correctness verification
All line-number references in the plan were checked against ground truth and are **exact**:
- Task 1 → Step 2 read at `SKILL.md:82` ✓
- Task 2's five routing sites — `103` (Internal-only outcome row), `107` (refactor-enables-future bullet), `109` (Internal-only items line), `129` (Step 2.2 rule), `198` (Step 4.2 rule) — all verified verbatim ✓
- Task 2 → `## What NOT to do` at `288–301` ✓ (the two new What-NOT-to-do lines are genuinely absent today and correctly marked "add", not "keep")
- Task 6 → temporal-tree locate step at `SKILL.md:26` ✓

Semantic checks:
- **Self-heal / current-run composition is ordered correctly.** Self-heal (4.2a) rebuilds the ledger from *committed* past prune commits and discards old hashes; the current run's snapshot is not yet a committed prune commit, so it is not double-counted, and Step 4.2's append (Task 3) adds it afterward. Replace-then-append ordering is what makes this work, and the plan places self-heal as the *opening* sub-step of 4.2. Correct.
- **Version marker doubles as migrated-flag.** Marker current → self-heal skips; absent/older → rebuild. Step 4.2 re-stamps every run, making the whole thing idempotent on subsequent runs. Consistent with the spec's deterministic/idempotent guarantee.
- **`<prune>^` = parent = snapshot** matches Step 4.1's `git rev-parse --short HEAD` construction; both produce short hashes, so no dedup length mismatch. The off-by-one against the prune commit is by-construction correct (commit is on-request/later, so at write time only HEAD exists).
- **Message set** (`Roadmap prune`, `Remove complete plans`, `Rmove complete plans`) — the intentional `Rmove` typo is preserved; content-verify (diff must delete `[x]` lines from ROADMAP.md) and current-branch-only enumeration match the spec and its validation dry-run. The reliance on the pinned `Roadmap prune` message from the "Commit (on request only)" section is called out with a do-not-alter guard.
- **Guard** (self-heal edits only the drop-history row + header marker) is carried into Task 4 verbatim from the spec.
- **Commit plan** respects the task dependency chain (2→3→4→5→6) and matches repo commit-message style (sentence case, no type prefix, no period).

### Critical Issues
None.

### Positive Notes
- The plan does the hard work of enumerating **all five** routing sites with a grep-count sanity check and surgical boundaries ("this sentence stays, only that clause changes") — this is exactly the precision needed for prose-contract edits where a blanket rewrite would over-delete.
- The single-source version constant (Task 1) with two named use sites (self-heal read + Step 4.2 write) avoids the drift that a duplicated version string would cause.
- Prefix-matching is applied at **every** read site of the `## Features` header (Step 2 read, self-heal marker read, Step 4.2 find-or-create), not just the new write — so a legacy unmarked header still resolves everywhere. This is the subtle failure mode most plans would miss.
- The cross-file coupling is declared on both sides per the repo's cross-file-invariant rule, not just on the writer.

## Deferred observations
- Affects: future roadmap-prune idempotency work (outside this milestone) — Running the prune twice **without committing between runs** re-appends the same Step-4.1 snapshot (HEAD is unchanged and the previous run's snapshot is not yet a committed prune commit, so self-heal cannot dedup it). The result is two identical snapshot hashes in the ledger, which technically violates the new "exactly one hash per prune" contract. This is pre-existing behavior (the old skill also appended per run) and this milestone's scope is the ledger *semantics* and *legacy self-heal*, not run idempotency, so it is not a defect in this plan — noting it in case a later milestone hardens the append against uncommitted re-runs. [routed → .ai-factory/specs/53-prune-ledger-append-idempotent.md]

PLAN_REVIEW_PASS
