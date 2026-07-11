# Code Review — 3.1 roadmap-prune: drop-history is a prune-snapshot ledger

**Artifact reviewed:** implemented changes for milestone 3.1
**Files changed (code):** `src/skills/roadmap-prune/SKILL.md`, `src/skills/temporal-tree/SKILL.md`
**Other diff content:** planning artifacts only (ROADMAP.md contract line, note 59, plan + plan-reviews, handoff) — not a runtime surface.
**Reviewed against:** plan `87-3-1…md`, spec note `59-…md`, ROADMAP.md `3.1`, both target files in full at ground truth.

## What was verified

- `git diff HEAD` + `git status` — the only code edits are the two SKILL.md files; everything else is planning artifacts.
- Both skill files read in full (not just the diff) to check for surviving contradictions.
- `grep` for every `drop history` / `drop-history` reference in `roadmap-prune/SKILL.md` — all nine sites now describe the snapshot-ledger semantics; no residual "maintenance work goes here as hashes" routing survives.

## Conformance to spec + plan

All six plan tasks land, matching note 59 word-for-word where the note pins wording:

1. **Format-version constant** (SKILL.md:16–22) — single source above `## Step 0`, referenced by both the 4.2a marker read and the 4.2 write; prefix-match rule stated for all three in-skill read sites (Step 2, 4.2a, 4.2). ✓
2. **Internal-only routing removed** — all four flagged sites plus the table row are edited: `:117` (table), `:121` (bullet), `:123` (first sentence kept, routing clause removed), `:143` (Step 2.2 row), `:247` (Step 4.2 rule). Each now reads "writes no hash anywhere — captured by the nearest prune snapshot." No self-contradiction remains. ✓
3. **Drop-history = prune-snapshot ledger** — Step 2.2 (`:143`) and Step 4.2 (`:240`, `:247`) state "exactly one hash per prune — the Step-4.1 snapshot … `<prune-commit>^`." ✓
4. **Self-heal pre-pass 4.2a** (`:200–228`) — current-branch-only enumeration (never `--all`), message set (`Roadmap prune` / `Remove complete plans` / `Rmove complete plans`), content-verify of `[x]` deletions with artifact-sweep-twin skip, entry = `<prune>^`, wholesale replace (never repair-in-place), zero-found → stamp only, guard limiting edits to the ledger row + header, legacy-removable marker, and the explicit "do not alter the Commit section" dependency. ✓
5. **Versioned header stamp + temporal-tree coupling** (`:230–235`) — `## Features (roadmap-prune v2)`, restamped every run, with the prefix-match coupling sentence. ✓
6. **temporal-tree mirror** (`temporal-tree/SKILL.md:27–29`) — prefix-match sentence at the locate step. ✓
7. **Two new What-NOT-to-do lines** (`:339–340`). ✓
8. **Force-push out-of-scope assumption** (`:24–28`). ✓

## Correctness analysis (runtime behaviour when an LLM executes the skill)

The load-bearing ordering was traced for a double-count / omission bug and is **correct**:

- The current prune run is uncommitted at execution time, so 4.2a's `git log` enumeration finds only *past committed* prunes. Self-heal rebuilds those parents wholesale, then the 4.2 write appends the current HEAD snapshot. Result = {all past prune snapshots} ∪ {current}. No duplication.
- Idempotent forward: once the run's prune is committed as `Roadmap prune`, its parent equals the appended HEAD, so a later self-heal (or a v2 skip) reproduces the same value — dedup absorbs it.
- The `<prune>^` = snapshot invariant is exactly what makes `git show <snapshot>:.ai-factory/ROADMAP.md` reconstruct the pre-prune roadmap, including internal-only lines (they lived in that snapshot before being pruned) — so dropping their per-task hashes loses no navigational reach. The "captured by the nearest prune snapshot" claim holds.

No blocking correctness, security, or type/contract defect found in the changes.

## Non-blocking observations (informational — not defects in this change)

- **Uncommitted re-run double-appends the snapshot.** If the user runs the prune, does *not* commit, then re-runs before committing, the 4.2 write appends the current HEAD snapshot a second time (self-heal is skipped once the header is v2, and the append step has no "already present" guard). This behaviour is **pre-existing** — the old Step 4.2 appended unconditionally too — and unchanged by this milestone; normal use commits between prunes. Noted only for completeness, not a regression.
- **Path shorthand in What-NOT-to-do (`:340`).** `git show <hash>:ROADMAP.md` omits the `.ai-factory/` prefix that the real path carries (correctly spelled at `:143`, `:173`). It is illustrative prose and matches the spec note's own shorthand (note 59:71), so it is intentional shorthand, not an error.

REVIEW_PASS
