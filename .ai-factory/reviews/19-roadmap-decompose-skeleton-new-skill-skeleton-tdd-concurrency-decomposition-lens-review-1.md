# Code Review: roadmap-decompose-skeleton (plan 19)

**Plan:** `.ai-factory/plans/19-roadmap-decompose-skeleton-new-skill-skeleton-tdd-concurrency-decomposition-lens.md`
**Changes reviewed:** `git diff HEAD` — new `src/skills/roadmap-decompose-skeleton/SKILL.md`, `CLAUDE.md` (registration), plus incidental changes to `roadmap-decompose/SKILL.md`, `roadmap-engine/SKILL.md`, notes 27/31/32, and `ROADMAP.md`.
**Risk Level:** 🟢 Low — no runtime/correctness bugs. Two minor findings, both non-blocking.

## Scope note

The staged diff bundles changes from adjacent milestones (roadmap-engine → `Read`-only, notes 31/32 hygiene, roadmap-decompose load-once wording). These are consistent with plan 19 and do not conflict with it — in particular, `roadmap-engine` becoming `allowed-tools: Read` confirms plan-review-1's central point: the engine cannot write, so this skill must carry its own `Write Edit`. It does. Verified consistent; not re-reviewed as their own deliverables.

## Verification of the plan's requirements

- **Frontmatter `name` = directory name** — ✅ `roadmap-decompose-skeleton`.
- **`argument-hint` brackets quoted** — ✅ `"[phase/slug or task description]"`.
- **`disable-model-invocation: true`** — ✅.
- **Tool grant includes `Write Edit`** (plan's correction to note 27) — ✅ `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`. The skill renders contract lines into `ROADMAP.md` itself (`roadmap-engine` is `Read`-only, `aif-note` only writes note files), so the grant is now sufficient and no out-of-band permission prompt will fire. Matches sibling `roadmap-decompose`.
- **Description ≤ 1024 chars** — ✅ 715 chars.
- **Body ≤ 500 lines** — ✅ 127 body lines.
- **Uses `test-engine` (not `test-philosophy`)** with alias noted — ✅ lines 7, 39, 46, 84, 134.
- **Renders to `ROADMAP.md`, never `ROADMAP_TESTS.md`** — ✅ Step 4 (lines 122–128).
- **Does not call `roadmap-decompose` at runtime; does not touch orchestrator or closed `[x]` tasks** — ✅ Critical Rules 3, 4, 6.
- **CLAUDE.md registration** — ✅ both the "Custom skills — never overwrite" list and the Repository Structure tree updated.

## Findings

### 1. Skill fails the repo's own validator — frontmatter word count (LOW)

`bash ~/.claude/skills/aif-skill-generator/scripts/validate.sh src/skills/roadmap-decompose-skeleton` reports:

```
ERROR: Frontmatter exceeds 100 tokens (~words): 113
Validation FAILED
```

The repo workflow (`CLAUDE.md` → "Workflow for Skill Development" → step 2, `/aif-skill-generator validate`) runs this validator, so the new skill will report FAILED there. It counts words across the whole frontmatter block (`validate.sh:56–58`), a stricter heuristic than the actual Agent Skills spec limit (1024-char description, which passes at 715).

Severity is low because (a) the skill loads and functions correctly in Claude Code — the 100-word rule is a lint heuristic, not a spec constraint — and (b) a shipped sibling, `roadmap-test-coverage`, already fails the same check (101 words), so the rule is tolerated in practice. Still worth a one-time fix: trim ~13 words from the `description` (e.g. shorten the trigger-phrase list or the "aka test-philosophy" parenthetical) to bring the frontmatter under 100 and get a clean validate run.

### 2. Step 0 never explicitly reads the roadmap to enumerate open tasks (NIT)

Step 0 (`SKILL.md:62–70`) says "Operate only on **open** `- [ ]` tasks in the target roadmap," and Targeting (53–58) says to infer the target from context — but no step explicitly instructs reading `ROADMAP.md` (via `Read`/`Grep`) to obtain the open-`[ ]` set the lenses run over. The skill has the tools, and an agent will almost certainly do this implicitly, but a one-line "Read the target roadmap and collect its open `- [ ]` tasks" in Step 0 would remove the ambiguity and mirror `roadmap-decompose`'s explicit "always read it before modifying" discipline. Non-blocking.

## Positive notes

- Engine/philosophy separation is clean: the skill treats `roadmap-engine` as format-only and does its own `ROADMAP.md` writes; it never asks the `Read`-only engine to write. Consistent with the engine's revised grant in the same diff.
- Load-once discipline for `roadmap-engine` and `test-engine` is stated at each seam (lines 33–34, 84–85, 124–126) and never re-invoked per task.
- The `test-engine` vs `test-philosophy` naming discrepancy from note 27 is handled exactly as the plan promised — invoke `test-engine`, note the alias.
- Restraint clauses (skeleton 79–81, concurrency 96–100, Critical Rule 5) and the m36/m37 canon are carried faithfully from the spec note.
- CLAUDE.md tree line is alphabetically reasonable and the "never overwrite" list entry is correct.

## Conclusion

No correctness, security, or runtime-breaking issues. Finding 1 (validator FAIL on frontmatter word count) is the only actionable item and is cosmetic/lint-level; finding 2 is a nit. Safe to proceed; recommend trimming the description to pass the repo validator.
