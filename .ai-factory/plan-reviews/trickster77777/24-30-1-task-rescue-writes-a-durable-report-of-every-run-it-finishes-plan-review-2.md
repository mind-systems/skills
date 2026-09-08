# Plan review: 30.1 — task-rescue writes a durable report of every run it finishes

## Code Review Summary

**Files Reviewed:** 1 plan + the target it edits (`src/skills/task-rescue/SKILL.md`, 581 lines), plus `src/skills/note/SKILL.md`, `src/commands/command-handoff.md`, `.ai-factory/ARCHITECTURE.md`, the contract line (`.ai-factory/roadmaps/trickster77777.md:144`), the task spec (`.ai-factory/specs/trickster77777/105-rescue-report-persisted.md`), the three reports in `.ai-factory/rescue-reports/skills/`, and plan-review round 1.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md:30-39`, "Composition: mechanism vs policy") — aligned. `task-rescue` stays policy and drives `note` (engine) through its three declared hooks, keeping control; the edge is declared in the caller's `loads:` only, and `note` already carries its reverse-graph marker (`src/skills/note/SKILL.md:21-23`), so no engine-side edit is owed. The plan's explicit refusal to restate `note`'s mechanics (numbering, `mkdir -p`, folder style) keeps that mechanism in one home.
- **Rules** (`.ai-factory/RULES.md`) — **WARN**: absent in this repo. Non-blocking; conventions live in `CLAUDE.md` and `ARCHITECTURE.md`. The ≤ 500-line body constraint is waived explicitly by the spec's guard and the plan repeats the waiver rather than silently ignoring it.
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md:140-144`) — aligned. The plan title matches the contract line verbatim, and each of the line's pins (the `note` edge, the four facts snapshotted at Step 1 before deletion, one write at the end, the `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` destination under `.ai-factory/rescue-reports/<project>/`, never stored/cached, `Bash(mkdir *)`) is carried. The `Spec:` tag resolves and the spec was read; Phase 30's header names no `Governing spec:` and no `Phase note:` (its intro is prose only), so the reference chain ends at the task spec.

### Round-1 findings — both closed

- **Step 1 placement.** Round 1 showed `$TARGET_FILE` is first determined not after `**Identify the task slug.**` but by the next sub-block (`src/skills/task-rescue/SKILL.md:58-59`, "Determine `$TARGET_FILE` (the same resolution Step 4 determines)"). The plan now pins the insertion **after `**Read the phase's governing spec and phase note.**` and before `**Read every artifact file found**`**, states that placement as load-bearing, and states that the new sub-block *reads* `$TARGET_FILE` rather than resolving it a third time. Verified against the file: `:58-59` is exactly the sub-block named, and nothing in Step 1 before it touches `$TARGET_FILE`. Closed correctly, and by the option the round-1 review recommended.
- **`<project>` specified two ways.** The destination bullet now states both halves are resolved at write time inside Step 5.7 — `git rev-parse --show-toplevel` in the rescued project (last segment → `<project>`) and `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` (→ skills repo root) — and disambiguates the Step 1 fact explicitly: "The Step 1 project fact is not this address: it fills the report's `**Project:**` line, and the path is re-resolved here regardless." That is the spec's reading (item 3, "both run at this moment and neither stored or cached"), and it makes the "neither stored nor cached" sentence true as written. The verification count is restated to match (`rev-parse --show-toplevel` ≥ 2, with the clause "Step 5.7 alone must carry two"), so the exact confusion that killed round 3 of the previous run is now checkable rather than merely asserted.

### Verified ground truth

- `src/skills/task-rescue/SKILL.md:11` is `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill` and `:12` is `loads: orchestrator-artifacts roadmap-engine` — the plan's target strings add exactly `Bash(mkdir *)` and `note` and drop nothing.
- `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` executed here returns `/Users/max/projects/sakshi/skills` (exit 0) through the double symlink hop `~/.claude/skills` → `active/skills` → `../../src/skills/task-rescue`. The mechanism holds with no `readlink`, inside the existing `Bash(git *)` grant.
- The `Bash(mkdir *)` grant is genuinely required and correctly justified: `note` issues `mkdir -p <destination>` unconditionally (`src/skills/note/SKILL.md:63`, inside the block the plan cites as `:60-63`), and `src/commands/command-handoff.md:9` carries the same grant for the identical delegation. Omitting `Bash(ls *)` is right — `note`'s numbering step is written as a `[0-9][0-9]-*.md` file-match scan, which the already-granted `Glob` serves.
- `note`'s three hooks are at `src/skills/note/SKILL.md:31-33` exactly as cited, and the caller-supplied verbosity directive does replace Rules 1 and 2 as the plan says (`:33`).
- Every branch the plan names as reaching Step 5.7 does fall through sequentially: non-convergence options 1–3 ("Proceed directly to Step 5.5.", `:339`), escalation options 1–3 (option 3: "no Step 5 procedure runs … Proceed directly to Step 5.5.", `:353-356`), and all four depths including plan-ratified. The scope-overload flag (`:279-283`) does "Skip the depth menu in this case" with no repair procedure, so naming it as the exit that writes nothing is accurate.
- The insertion point exists as described: `## Step 5.6` at `:515`, `## What NOT to do` at `:541`, with `---` rules between neighboring steps.
- The template shape is drawn from the folder, not invented: `01…`/`02…`/`03…` each open with `# <task number> — <phrase>` followed by `**Project:**`, `**Date:**` (ISO), `**Stopped at:**`, `**Elapsed before the rescue:**`, and each ends in a "what was done" section. The slug convention `30-1-<phrase>` (with `note` supplying the `NN` prefix) matches the files on disk. `.ai-factory/rescue-reports/` is tracked and not git-ignored, so the phase's "under version control" intent holds.
- `:373` (deleting the sidecar loses `elapsed`), `:387` and `:424` (the two flat sidecar paths left outside the edit set) and `:32-38` (the two load-protocol paragraphs) all resolve to what the plan claims.

### Critical Issues

None.

### Positive Notes

- Writing once, at the end, is the correct collapse of the two-part write that cost this task its two previous runs (`03-30-1-…`): with no mid-run file identity to re-resolve, the recovery branch that generated three rounds of findings has no reason to exist.
- The plan is grounded citation by citation — every line reference checked resolves to what it claims, in both the edited file and the two skills it depends on.
- Naming the scope-overload exit as the branch that writes nothing turns an implicit control-flow fact into a stated, checkable one, which is what makes the "every terminating branch" claim verifiable at all.
- Carrying "what Step 3 actually emitted" for the escalation branch — instead of demanding a root-cause section that branch structurally cannot produce (`:183-189`, `:201-203`) — closes a hole that would otherwise force the implementer to invent a section.
- The failure clause refuses silent degradation in the right shape: name both ways it fails, say so plainly, complete the rescue anyway, no fallback path inside the rescued project, no deferral to a later run.

## Deferred observations
- Affects: Phase 30 — `src/skills/task-rescue/SKILL.md:387` and `:424` still locate the sidecar at the flat `.ai-factory/plans/{seq}-{slug}.json`, which is wrong for any named roadmap (this very run's sidecar lives at `.ai-factory/plans/trickster77777/24-…json`). Task 30.1 correctly leaves them alone — its spec pins them outside the edit set, and the new Step 1 sub-block names `orchestrator-artifacts` § 1 as the locator for its own read — but the result is one file holding two different answers to "where is the sidecar", and Step 5 still writes the rollback `step` through the flat one. A follow-up task in this phase should route both write sites through the same locator.
- Affects: Phase 30 — neither `CLAUDE.md` (§ "Repository Structure", which lists `.ai-factory/` as "Roadmap, specs, notes, handoffs, architecture, plans") nor `docs/sakshi-harness/skill-cycle.md` mentions the durable rescue-report artifact this task makes the mechanism produce. The plan is right not to touch them — the task's Settings say `Docs: no` and its verification pins the diff to one file — but once the capability lands, the cross-project report folder is a system fact with no home in the docs tree.

PLAN_REVIEW_PASS
