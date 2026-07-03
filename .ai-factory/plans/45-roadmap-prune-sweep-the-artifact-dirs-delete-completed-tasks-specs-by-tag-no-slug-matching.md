# Plan: roadmap-prune: sweep the artifact dirs; delete completed tasks' specs by tag — no slug matching

## Context
Rework `src/skills/roadmap-prune/SKILL.md` so a prune also frees the dead weight completed work leaves at HEAD. The mechanism is the user's manual workflow, encoded: **plain `rm`, then `git add -A` once at commit time — no `git rm` anywhere** (a prior attempt used `git rm` and failed three review rounds over its staging split and abort modes; that mechanism is rejected). The skill carries **instructions only, no rationale prose** — no counter-reset claims, no git-semantics or safety explanations. All changes are to one skill file; behavior is defined by the spec note (`.ai-factory/notes/56-prune-deletes-pruned-specs.md`).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Add the sweep to the prune execution

- [x] **Task 1: Insert the sweep step — capture tags, rm the artifact dirs, rm the specs**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Add a new step in the execution flow, placed **after** Step 4 (ARCHITECTURE.md update; the Step 4.1 snapshot is captured before any changes) and **before** the ROADMAP.md line deletion — tags must be read off the roadmap lines before any line is removed. The step performs, in order:
  1. **Capture** the `Spec:` tag path of **every** `[x]` line (both the lines being pruned and any `[x]` lines kept as recent context). An `[x]` line with no `Spec:` tag contributes nothing — skip it, never synthesize a path. Paths are literal from the tag (works across the lazy `notes/`→`specs/` migration).
  2. `rm -rf` the four artifact dirs: `plans/`, `plan-reviews/`, `reviews/`, `patches/`. `-f` makes a missing dir a non-event — no existence checks, no guards.
  3. `rm -f` each captured spec path.
  **Path base (load-bearing — this is the sole safety under `rm`):** derive the target repo root from the skill's ROADMAP.md argument — the parent of the `.ai-factory/` the skill reads ROADMAP.md from — and anchor every deletion there. The four dirs sit directly under `<target>/.ai-factory/` (`plans/`, `plan-reviews/`, `reviews/`, `patches/`). The captured tag paths are **repo-root-relative** — they already begin with `.ai-factory/` — so join them onto the **target repo root**, not onto `.ai-factory/` (joining onto `.ai-factory/` would double the segment). Both share one base: the target repo root. Never run `rm` against a bare `plans/` (or a fixed top-level `.ai-factory/`) from an arbitrary cwd: for a monorepo sub-repo roadmap at `<subrepo>/.ai-factory/ROADMAP.md` the sweep targets `<subrepo>/.ai-factory/*` and `<subrepo>/.ai-factory/notes|specs/...`, never the repo root's. This matters more than it did under the rejected `git rm`: plain `rm -rf` also deletes untracked files, and a mis-pointed base is unrecoverable — so a wrong base is catastrophic, and correct derivation from the argument is mandatory.
  State the single invariant as an instruction, not an explanation: spec deletion goes **only** through `[x]` lines' tags — no spec directory is ever scanned or swept, so open `[ ]` tasks' specs are never touched. Write **no rationale prose** around any of this (no tracked-vs-untracked reasoning, no counter-reset claims). `allowed-tools` already grants `Bash(git *)` for the commit; add `Bash(rm *)` for the sweep.

- [x] **Task 2: Sequence the ROADMAP.md update after tag capture** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In the existing "Update ROADMAP.md" step, add a one-line ordering constraint: the pruned `[x]` lines may only be deleted after Task 1's tag capture has run. No other change to that step's grouping/retention rules.

### Phase 2: Rules, commit policy, report, parity

- [x] **Task 3: Replace the What-NOT-to-do notes rule and refresh the description** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In `## What NOT to do`, replace the line `Do not delete the notes/ directory or individual note files — they are referenced by commit hash and must stay in the repo` with the sweep-model rules: spec deletion goes only through `[x]` lines' `Spec:` tags — never scan or sweep a spec directory, never touch a path an open `[ ]` line's tag names; `handoffs/` is never touched; no `git rm` — deletion is plain `rm`, staging happens once at commit time via `git add -A`; no per-task resolution (no slug derivation, no discovery, no orphan report, no extended verify); no rationale/explanation prose in the skill; never auto-commit. Update the frontmatter `description` so it reflects that prune now also sweeps completed artifacts and specs (keep it within the field's length norm).

- [x] **Task 4: Add commit policy, the summary report, and the parity rule** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  - **Commit policy (on request, never automatic):** the run ends with all changes in the working tree — **no commit is made**; the user reviews first. When the user says to commit (any wording): `git add -A` scoped to the target repo, then **one** commit with the message exactly `Roadmap prune` — no body, no prefixes, no co-author line, no per-file commits, and never ask about the message.
  - **Summary report:** a new **additive** closing step placed **after** the existing "Verify" step (renumber the whole tail consistently once the sweep step is inserted — sweep, Update ROADMAP.md, Verify, Summary report), listing the swept dirs and the deleted spec files — information, not verification; no cross-checks against the roadmap. The Verify step's existing checks (feature-row hash resolution, no-orphaned-`[x]`, coherence) stay **untouched** — "no extended verify" applies only to the new sweep, never to Verify.
  - **`ROADMAP_TESTS.md` parity:** when pruning that file, the same sweep applies, and `test-runs/` joins the swept dirs **in that mode only**.

## Commit Plan
- Do not auto-commit. The change is a single cohesive edit to one skill file; the user commits when ready.
