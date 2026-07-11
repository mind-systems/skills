# Plan: 3.1 — roadmap-prune: drop-history is a prune-snapshot ledger — versioned Features header + legacy self-heal

## Context
Redefine `roadmap-prune`'s `Roadmap drop history` row as a prune-snapshot ledger (exactly one snapshot hash per prune, internal-only tasks write no hash anywhere), add a versioned `## Features` header plus a git-grounded legacy self-heal pre-pass, and pin the header-string coupling with `temporal-tree`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Drop-history semantics

- [x] **Task 1: Declare the Features-table format-version constant and document the force-push assumption** — DEVIATION: plan's sentence template cited "Step 2's classification read (line 82)"; that literal line number goes stale the instant a body edit shifts content (it moved to line 96 within this same task), so the added line names the read site by step ("Step 2's classification read") without a hardcoded line number.
  Files: `src/skills/roadmap-prune/SKILL.md`
  Add one line in the skill body **above the steps** (after `# Roadmap Prune`, before `## Step 0`) declaring the format version, e.g. `**Features-table format version:** \`roadmap-prune v2\` — the version stamped into the \`## Features\` header; an unmarked/legacy \`## Features\` header is v1.` This single line is the source both the self-heal pre-pass (Task 4) and the Step-4.2 header write (Task 5) reference. State in the same line that every read of the `## Features` header inside this skill — Step 2's classification read (line 82), the self-heal marker read (4.2a), and Step 4.2's find-or-create — matches the stable base `## Features` **by prefix**, tolerating an optional ` (roadmap-prune vN)` suffix, never by exact `^## Features$`, so both a versioned header and an unmarked legacy header resolve at every read site. In the same location (or the nearest existing assumptions/note spot), add one sentence documenting the out-of-scope assumption per the spec: a force-push / shared-history rewrite invalidates every hash in the Features table (feature rows and ledger alike); defending against it is out of scope (repo policy: shared history is not rewritten), and recovery is to delete the version marker from the header and re-run the prune so self-heal rebuilds from the rewritten history.

- [x] **Task 2: Remove the internal-only → drop-history routing**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Delete every rule that routes internal-only task hashes into drop history — **all five sites** (a `grep` for the routing wording returns five; the enumeration below is the complete worklist):
  - `SKILL.md:103` — Step 2.1's outcome table: change the **Internal only** row's Action from "Hash goes to drop history only — no feature row" to "No feature row and no hash recorded anywhere — captured by the nearest prune snapshot".
  - `SKILL.md:107` — the Step 2.1 bullet ("A refactor that enables a future feature is still internal — record it in drop history, not as a feature"): reword so the refactor writes no hash.
  - `SKILL.md:109` — "Refactors, renames, cleanups, doc fixes, migration changes, and dependency updates **all go to the drop history hash only**." Surgical boundary: the **first** sentence ("Internal-only items never get a named row in the Features table") is correct and stays; only "all go to the drop history hash only" is removed/reworded so internal-only work writes no hash.
  - `SKILL.md:129` — the Step 2.2 rule ("all maintenance work (refactors, cleanups, dep fixes, renames, doc changes) goes here as hashes, never as named rows"): reword so this work writes no hash.
  - `SKILL.md:198` — Step 4.2's additional rule ("All maintenance work (refactors, arch cleanup, dep fixes, renames, doc changes) **is absorbed into that row's hashes only** — never as a named row."). Surgical boundary: the row's last-position rule stays; only "absorbed into that row's hashes only" is reworded so internal/maintenance work writes no hash (the drop-history row now holds only prune snapshots).

  Internal-only classification still affects the Features table only by producing no named row — it never writes a hash. **Add** a new line to the skill's `## What NOT to do` section (lines 288–301, which does not currently contain it): "Do not write internal-only task hashes anywhere — they belong to no feature row and to no ledger entry." (This reinforcement text lives only in the spec note's own What-NOT-to-do today, not in the skill — it must be added, not "kept".)

- [x] **Task 3: Redefine the drop-history row as a prune-snapshot ledger** (depends on Task 2)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 2.2 and Step 4.2, restate the `Roadmap drop history` row's semantics per the spec (user wording): the row holds **exactly one hash per prune** — the Step-4.1 snapshot, the last known intact roadmap before that prune (the commit before which the prune deleted roadmap lines; equivalently `<prune-commit>^`). Storing the snapshot is what makes `git show <hash>:.ai-factory/ROADMAP.md` reconstruct the pre-prune roadmap directly. Update Step 4.2's drop-history instruction to "append exactly the Step-4.1 snapshot hash (one per prune run), comma-separated". **Add** a new line to the skill's `## What NOT to do` section (it is not present today): "Do not store the prune/deletion commit in drop history — store its parent (the snapshot), so `git show <hash>:.ai-factory/ROADMAP.md` yields the pre-prune roadmap."

### Phase 2: Legacy self-heal and versioned header

- [x] **Task 4: Add the legacy self-heal pre-pass with retirement marker** (depends on Task 3)
  Files: `src/skills/roadmap-prune/SKILL.md`
  Add a self-heal pre-pass that runs before Step 4.2 writes features (as Step 4.2's opening sub-step, e.g. a new **4.2a**). Read the `## Features (...)` header marker and branch: (a) marker == current version → nothing to migrate, proceed; (b) marker absent or older → rebuild the drop-history row wholesale from git ground truth. Rebuild procedure per the spec: enumerate the repo's prune commits on the **current branch only** (never `--all`) via `git log --format='%h %s' -- .ai-factory/ROADMAP.md` filtered to the prune-message set — `Roadmap prune`, `Remove complete plans`, `Rmove complete plans`; **content-verify each candidate** (its diff must actually delete `[x]` lines from `.ai-factory/ROADMAP.md`; artifact-sweep twins that touch no roadmap line are skipped and reported, never ledgered); each verified entry = its parent (`<prune>^`); **replace** the drop-history hashes with this reconstructed, de-duplicated, chronological set (old polluting hashes discarded); zero prune commits found → stamp only. Guard: self-heal edits only the drop-history row and the header marker — never feature rows, never ROADMAP.md, never specs; the rebuild is authoritative from git — do not repair existing hashes in place. Note that this pre-pass relies on the pinned `Roadmap prune` commit message from the "Commit (on request only)" section and must not alter that section. Mark the self-heal block **legacy-removable** with a one-line note: once every consuming repo's header shows the current version, this block is dead code and can be deleted (the version constant and per-run stamping stay).

- [x] **Task 5: Stamp the versioned header at Step 4.2 with the temporal-tree coupling sentence** (depends on Task 4)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 4.2, where the `## Features` section is found/created, instruct writing the header as `## Features (roadmap-prune v2)` using the version from the Task-1 constant, and state that every run (re)stamps the current version. Add the coupling sentence next to the header write: `temporal-tree` matches this header **by prefix** (`## Features (roadmap-prune vN)`), so the version suffix must not break prefix-matching. This is the second use site of the Task-1 constant.

### Phase 3: temporal-tree coupling

- [x] **Task 6: Add the prefix-match coupling sentence in temporal-tree** (depends on Task 5)
  Files: `src/skills/temporal-tree/SKILL.md`
  At the `## Before you start` locate step (around line 26, "locate the `## Features` table"), add one sentence: the header may carry a version suffix (`## Features (roadmap-prune vN)`) written by `roadmap-prune`, so match it **by prefix**, not by exact string. This mirrors the coupling sentence added on the `roadmap-prune` side in Task 5.

## Commit Plan
- **Commit 1** (after tasks 1-3): "Make roadmap-prune drop history a prune-snapshot ledger"
- **Commit 2** (after tasks 4-6): "Add roadmap-prune versioned Features header and legacy self-heal"
