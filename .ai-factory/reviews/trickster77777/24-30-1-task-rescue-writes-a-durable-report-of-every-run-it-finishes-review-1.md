# Review: 30.1 — task-rescue writes a durable report of every run it finishes

## Code Review Summary

**Files Reviewed:** the full changed file `src/skills/task-rescue/SKILL.md` (693 lines, +114/−2), plus the artifacts it depends on and is judged against: `src/skills/note/SKILL.md`, `src/skills/orchestrator-artifacts/SKILL.md`, `src/commands/command-handoff.md` (the sibling caller of the same engine), the contract line (`.ai-factory/roadmaps/trickster77777.md:144`), the task spec (`.ai-factory/specs/trickster77777/105-rescue-report-persisted.md`), the plan, both plan-review rounds, and the three existing reports in `.ai-factory/rescue-reports/skills/`.
**Risk Level:** 🟢 Low

`git status` shows only the four artifact files of this run plus the one product file; `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/skills/task-rescue/SKILL.md` and nothing else, as the spec's verification requires. No symlink, no engine, and no doc was touched.

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy") — aligned. `task-rescue` stays policy and drives `note` (engine) through its three declared hooks, keeping control of structure and depth; the edge is declared only in the caller's `loads:`, and `note` already carries its reverse-graph marker (`src/skills/note/SKILL.md:21-23`), so no engine-side edit is owed. Step 5.7 explicitly refuses to restate `note`'s mechanics ("numbering, `mkdir -p`, folder style — are not restated here; they are reached through these hooks"), keeping one home per fact.
- **Rules** (`.ai-factory/RULES.md`) — **WARN**: absent in this repo. Non-blocking; conventions live in `CLAUDE.md` and `ARCHITECTURE.md`. The ≤ 500-line body constraint is waived by the spec's own guard, and the file grew 581 → 693 lines as that guard anticipated.
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md:144`) — aligned. Every pin on the contract line landed: the `note` edge, the four facts snapshotted at Step 1 before anything is deleted, one report per run written once through `note` at the end, the destination resolved by `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` under `.ai-factory/rescue-reports/<project>/`, never stored or cached, and `Bash(mkdir *)` as the one added grant. Phase 30's header names no `Governing spec:` and no `Phase note:`, so the reference chain ends at the task spec.

### Verification — spec checklist, taken on a whitespace-normalized read

Counts were taken by flattening newlines and collapsing runs of whitespace, never by a line-oriented `grep`, as the spec's verification section mandates:

- `loads:` reads `orchestrator-artifacts roadmap-engine note` — ✅ 1.
- `allowed-tools:` diffed against `git show HEAD:src/skills/task-rescue/SKILL.md` — exactly one entry added, `Bash(mkdir *)`; `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash(git *)`, `AskUserQuestion`, `Skill` all still present, nothing else new. `Bash(ls *)` correctly not added — `note`'s numbering is a `[0-9][0-9]-*.md` file-match scan served by the already-granted `Glob`. ✅
- `readlink` → 0; `rev-parse --show-toplevel` → 3 (Step 1's project fact, and Step 5.7's two halves of the address — Step 5.7 alone carries the required two). ✅
- `.ai-factory/rescue-reports/` → 1 (≥ 1). ✅
- Step 1 states the capture happens "now, at discovery, before anything is deleted" and names `orchestrator-artifacts` § 1 as the sidecar locator, with the named-roadmap subdirectory rule spelled out. ✅
- Step 5.7 names all three `note` hooks (destination directory, template, verbosity directive) plus the `$1` slug. ✅
- "written on every terminating branch, escalation and non-convergence included" ✅; scope-overload named as the one exit that does not reach the step ✅; "neither half is stored nor cached" ✅; "once, at the end… invoked exactly once per run… never reopened" ✅; both failure modes stated with the rescue completing anyway, and no second write permitted anywhere ✅.
- `description:`, `argument-hint:`, `name:`, `disable-model-invocation:` untouched — a durable side effect does not change when the skill is invoked. ✅

### Runtime correctness — what was checked and held

- **Placement dependency (round-1 plan finding).** The new `**Capture the report facts.**` sub-block sits at `:69`, after `**Read the phase's governing spec and phase note.**` (`:58-59`, the sub-block that first determines `$TARGET_FILE`) and before `**Read every artifact file found**`. It *reads* `$TARGET_FILE` rather than resolving it a third time, so the named-roadmap stem is available where the sub-block uses it — no unresolved-variable read, and the live named-roadmap branch (this very run's sidecar lives under `plans/trickster77777/`) is the one that works.
- **`<project>` double-resolution (round-2 plan finding).** Step 5.7 runs both git commands itself at write time and states the Step 1 fact "fills the report's `**Project:**` line only". The exact confusion that killed round 3 of the previous attempt is closed, and the ≥ 2 count is what makes it checkable.
- **Control flow to Step 5.7.** Every branch claimed to reach the step does, traced in the file: non-convergence options 1–3 (`:355-359`, "Proceed directly to Step 5.5."), escalation options 1 and 2 (route into the "Depth: spec" procedure, which falls through Step 5 → 5.5), escalation option 3 (`:373-377`, "no Step 5 procedure runs… Proceed directly to Step 5.5."), and all four repair depths. The scope-overload flag (`:299-303`) skips the depth menu with no repair procedure, so naming it as the exit that writes nothing is accurate rather than assumed.
- **The `<project>` resolution cannot fail in practice.** Step 1 opens with `git status --short -- .ai-factory/`, so the rescued project is a git repository by the time Step 5.7 runs; the two failure modes the step lists (skills root unresolvable, repository not writable in this session) are therefore the complete set, matching the spec's "both ways".
- **The mechanism resolves.** `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` returns the skills repo root through the double symlink hop (`~/.claude/skills` → `active/skills`, `task-rescue` → `../../src/skills/task-rescue`) via git's physical `getcwd()` — no `readlink`, inside the existing `Bash(git *)` grant. The `Bash(mkdir *)` grant is genuinely required: `note` issues `mkdir -p <destination>` unconditionally on every invocation (`src/skills/note/SKILL.md:60-63`), and `src/commands/command-handoff.md:9` carries the same grant for the identical delegation.
- **Template fidelity.** The fenced block is balanced (open/close pair) and its shape matches the three files already in `.ai-factory/rescue-reports/skills/`: `# <task number> — <phrase>`, the four facts as `**Project:**` / `**Date:**` / `**Stopped at:**` / `**Elapsed before the rescue:**`, the diagnosis, then `## What was done` — the outcome heading now pinned literally, which is what an earlier round of this task found missing. The `## What was done` line inside the fence is template content, not a file heading, and no program scans headings in a skill body, so it is inert.
- **No branch is asked for a part it cannot produce.** The escalation branch (`:203-209`, `:221-223`) ends in a restated decision with no root-cause sentence and no category; the step states the report carries what Step 3 actually emitted and invents no section. The title is pinned as a phrase naming what stopped the run, never a root-cause claim, so a branch with no root cause still has a title.
- **Absence is rendered, not guessed.** Step 1 records `step`/`elapsed` as absent when no sidecar is on disk, and the template renders absence as absence — the failure mode where a wrong path silently reads as "no sidecar" is called out at the place the path is chosen.
- **Nothing regressed.** Step 5.6, the marker grammar, the sidecar `step` closed set, the Diagnosis Report's chat mandate (still printed exactly as Step 3 requires; the file is additional and never read back), and the two flat sidecar paths the spec pinned outside the edit set are all byte-unchanged.

### Critical Issues

None.

### Positive Notes

- The single write at the end is the correct collapse of the two-part write that cost this task its previous two runs: with no mid-run file identity to carry across a gap, the recovery branch that generated three rounds of findings has no reason to exist, and the step contains no rule that needs a further rule to disambiguate it.
- The failure clause refuses silent degradation in the right shape — name both ways it fails, say so plainly, complete the rescue anyway, no fallback path inside the rescued project, no deferral to a later run — and it states those bans at the spot where an agent would reach for them, rather than relying on a prohibition written elsewhere in the file.
- Step 5.7 reads in the voice of Steps 5.5/5.6 and delegates to `note` in the same register as `command-handoff` § "Delegate to `note`", so the two callers of the engine now present one consistent shape.
- The Step 1 sub-block explains *why* the sidecar locator is pinned (a wrong path and an absent sidecar record the same thing, with no signal) instead of only stating the rule — the reason is what survives a later edit.

## Deferred observations
- Affects: Phase 30 — `src/skills/task-rescue/SKILL.md:407` and `:444` still locate the sidecar at the flat `.ai-factory/plans/{seq}-{slug}.json`, wrong for any named roadmap (this run's own sidecar lives at `.ai-factory/plans/trickster77777/24-…json`). Task 30.1 correctly leaves them alone — its spec pins them outside the edit set — but the file now holds two different answers to "where is the sidecar": the new read site routes through `orchestrator-artifacts` § 1, while both rollback *write* sites still use the flat path. A follow-up task in this phase should route both write sites through the same locator.
- Affects: Phase 30 — neither `CLAUDE.md` § "Repository Structure" (which lists `.ai-factory/` as "Roadmap, specs, notes, handoffs, architecture, plans") nor `docs/sakshi-harness/skill-cycle.md` mentions the durable rescue-report artifact this capability now produces. Correctly out of scope here (`Docs: no`, diff pinned to one file), but the cross-project report folder is now a system fact with no home in the docs tree.
- Affects: Phase 30 — `task-rescue` grants `Write`, and Step 5.7, unlike its sibling `src/commands/command-handoff.md:95` ("do not mine, number, slug, `mkdir`, or `Write` yourself"), states the delegation without an explicit ban on composing the file by hand. The step is unambiguous as written — the report is written *through* `note`, whose hooks drive the numbering and the final path — so this is a hardening note for whenever the two callers are next touched together, not a defect in this task.

REVIEW_PASS
