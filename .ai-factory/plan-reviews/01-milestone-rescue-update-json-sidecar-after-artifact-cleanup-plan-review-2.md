# Plan Review 2: milestone-rescue — update JSON sidecar after artifact cleanup

**Plan file:** `.ai-factory/plans/01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.md`
**Target skill:** `.claude/skills/milestone-rescue/SKILL.md`
**Source note:** `.ai-factory/notes/08-milestone-rescue-sidecar-update.md`
**Prior review:** `plan-review-1.md` (🔴 High risk — required changes listed)

## Code Review Summary

**Files Reviewed:** 1 plan + target skill + source note + sidecar sample
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** not present in repo — WARN (no boundary check possible, but this repo is a meta-repo of skills and does not require ARCHITECTURE.md).
- **Rules (`.ai-factory/RULES.md`):** not present — WARN (no explicit rule violations checkable).
- **Roadmap (`.ai-factory/ROADMAP.md`):** not inspected for milestone linkage; this plan is a skill-internal refinement explicitly chartered by `notes/08`, so milestone linkage is satisfied via the note.
- **Project CLAUDE.md:** skill-authoring conventions (frontmatter, `argument-hint` quoting, ≤500 lines, relative paths) — plan respects all of these. ✅

### Resolution of plan-review-1 findings

| # | Issue | Status |
|---|---|---|
| 1 | `allowed-tools` not updated | ✅ Resolved — Task 0 adds `Write` after `Read` on line 11. Plan correctly chooses Option B (tool-agnostic prose, no `Bash(python3 *)` grant). |
| 2 | `json.load`/`json.dump` wording leaks Python | ✅ Resolved — Design decisions explicitly forbid these tokens; Task 1 instructions 3 and 7 use "parse it as JSON" / "serialize the result back as JSON with 2-space indentation". |
| 3 | Step 5.5 interaction unspecified | ✅ Resolved — Task 1 preamble explicitly states "inside Step 5 and therefore **before** Step 5.5 — do not insert it after Step 5.5 or at the top of Step 5". |
| 4 | Recursive "sidecar doesn't exist" row | ✅ Resolved — Task 1 instruction 6 adds the clarifying sentence with a concrete example (`{ "step": "planned" }`) so the agent does not write a literal string or recurse infinitely. |
| 5 | "Reviews exist and pass" case | ✅ Resolved — Task 1 instruction 9 adds the fall-through, and instruction 10 explicitly skips the confirmation line in that case. |
| 6 | Intentional duplication between Task 1 instr 8 and Task 2 | ✅ Resolved — both Task 1 instr 8 and Task 2 now explicitly label the duplication as defense-in-depth. |
| 7 | What counts as "exists" for the sidecar | ✅ Resolved — Design decision "Existence means working tree" + Task 1 instruction 2 explicitly mention checking the working tree via `Read` or `Glob`. |

All four "Required Changes Before PASS" items from plan-review-1 are addressed.

### Cross-checks against the codebase

- **Frontmatter line number.** Plan references SKILL.md line 11. Verified: line 11 is `allowed-tools: Read Edit Glob Grep Bash(git *) AskUserQuestion`. ✅
- **Insertion point.** Plan inserts after the artifact deletion block (SKILL.md lines 185–194 with the "Do NOT delete committed files…" paragraph at 193–194) and before the "Show the user the list of deleted files…" line (SKILL.md line 196). This sits inside Step 5 (174–196), before Step 5.5 (200+). ✅
- **Slug derivation.** Plan refers to "the same `<NN>-<slug>` prefix identified in Step 1" — SKILL.md Step 1 (lines 44–46) does extract this prefix from artifact filenames. ✅ The sidecar lives at `.ai-factory/plans/{seq}-{slug}.json`, which matches the actual on-disk pattern (verified: `01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.json`).
- **Preserved keys.** The actual sidecar contains `planner`, `step`, `elapsed`. Plan instructs to preserve `planner`, `implementer`, `elapsed` (implementer would appear in later pipeline stages) — superset of what is present, correctly conservative. ✅
- **Tool-agnostic style consistency.** Confirmed by reading the existing Step 5: "use Edit to modify…", "`git status --short`" — no `python3`, no `json.load`. The new sub-step's prose ("parse it as JSON", "serialize the result back as JSON") matches. ✅
- **Mapping table verbatim requirement.** The note (line 44) requires verbatim inclusion. The plan reproduces the table exactly as it appears in `notes/08-milestone-rescue-sidecar-update.md` lines 14–20. ✅
- **`argument-hint` quoting.** Plan does not touch `argument-hint` — current value `"[path/to/ROADMAP.md | ROADMAP_TESTS.md]"` is already quoted. ✅
- **Order of `allowed-tools` tokens.** Plan inserts `Write` immediately after `Read`, preserving the existing whitespace-separated single-line format. No risk to YAML parsing. ✅

### Critical Issues
None.

### Medium Issues
None.

### Minor Issues / Suggestions

1. **(Optional, non-blocking) Existence-check phrasing for `Glob`.** Task 1 instruction 2 offers "attempting to read it, or listing with `Glob`" as ways to check existence. `Glob` returns an empty list for non-matching patterns, which is well-defined; a failed `Read` is also clear-cut. Either path is fine. No change required.

2. **(Optional, non-blocking) Confirmation line emoji/format.** Plan mandates the exact form `Sidecar updated: step set to "{value}"`. This matches the source note (line 30). The braces around `{value}` are template syntax, not literal — the implementer should be aware to substitute. The plan's prose contextualizes this clearly enough that misinterpretation is unlikely. No change required.

3. **(Observation, not a defect) Sidecar key written when starting from `{}`.** When the sidecar does not exist and the agent creates one with only `{"step": "<value>"}`, no other keys are written. The orchestrator will later add `planner`/`implementer`/`elapsed` on its own — consistent with the note's intent. The plan does not need to mention this.

### Positive Notes

- Design-decisions block at the top of the plan cleanly explains *why* each prior-review concern is resolved, before the task list. This format makes the iteration auditable.
- Task 0 isolates the frontmatter mutation from the body change — small, reviewable diff per task.
- Defense-in-depth duplication (in-flow forbiddance + "What NOT to do" bullet) is explicitly justified rather than left as accidental redundancy.
- All file paths use the correct `.claude/skills/milestone-rescue/SKILL.md` form (not the upstream-style `milestone-rescue/SKILL.md`), respecting this repo's actual layout.
- Plan correctly preserves Step numbering — adds a sub-step, not a new top-level step.
- The fall-through case (instruction 9) handles manual rescue invocation against a green pipeline — a real edge case worth covering.

### Verdict

The plan addresses every required change from plan-review-1 and survives cross-checking against the actual SKILL.md, the source note, and the on-disk sidecar shape. The scope is tight (one frontmatter token + one sub-step + one "What NOT to do" bullet), the prose style matches the existing skill, and the tool-permission story is internally consistent (only `Write` added; no Python; no `Bash(python3 *)`).

PLAN_REVIEW_PASS
