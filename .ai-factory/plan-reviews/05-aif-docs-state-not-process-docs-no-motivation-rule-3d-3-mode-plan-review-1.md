# Plan Review: aif-docs state-not-process docs (no-motivation rule + `3d`/`3д` mode)

**Plan reviewed:** `.ai-factory/plans/05-aif-docs-state-not-process-docs-no-motivation-rule-3d-3-mode.md`
**Files targeted:** `.claude/skills/aif-docs/SKILL.md`, `.claude/skills/aif-docs/references/REVIEW-CHECKLISTS.md`, `CLAUDE.md`
**Risk Level:** 🟢 Low

## Summary

This is a text-only edit to one skill plus a one-line registration in `CLAUDE.md`. No code, no migrations, no security surface. I verified every line-number reference, section header, and file path the plan cites against the live files — they are all accurate. The task decomposition is coherent, dependencies are correct, and the commit plan is sensible.

The plan is solid. Findings below are non-blocking recommendations the implementing agent should fold in.

## Verification of plan claims (all correct)

| Plan claim | Actual | Status |
|---|---|---|
| Core Principles: 6 numbered items, ~lines 17-24 | 6 items, lines 19-24 | ✓ |
| Step 0.1 Parse Flags, ~lines 87-91 | lines 87-91 | ✓ |
| Step 1 Determine Current State, ~line 93 | line 93 | ✓ |
| State C "Stale content" check, ~lines 404-413 | line 409 (audit block 404-413) | ✓ |
| Step 4 Documentation Review, ~lines 468-476 | lines 468-476 | ✓ |
| Checklist lines "Code examples..." / "Installation instructions..." | REVIEW-CHECKLISTS.md lines 14-15 | ✓ |
| CLAUDE.md "Intentionally diverged" list | lines 103-105; "All other skills safe to overwrite" at 107 | ✓ |
| `--web` is the only existing flag | confirmed (line 90) | ✓ |
| Source of truth is `.claude/skills/...` (symlinked from `~/.claude/skills`) | confirmed in CLAUDE.md | ✓ |

## Findings (non-blocking)

### WARN-1: `argument-hint` frontmatter not updated for the new `3d`/`3д` token
The plan adds a new standalone invocation token (`3d`/`3д`) in Task 3, but no task updates the frontmatter `argument-hint: "[--web]"` (SKILL.md line 4). A new user-facing invocation parameter that is never surfaced in the hint is a discoverability gap. Recommend Task 3 (or a sub-step) also update it to something like `argument-hint: "[--web] [3d|3д]"`. Optionally mention 3D mode in the `description` field, since that is what the skill loader shows.

### WARN-2: Checklist naming inconsistency the implementer must navigate
Tasks 2 and 7 say to edit the "Technical Checklist". The reference file header is indeed `## Technical Checklist` (REVIEW-CHECKLISTS.md line 3) — so the plan's wording matches the file. However, SKILL.md Step 4 (line 474) refers to the two checklists as **"Technical Accuracy"** and **"Readability & Completeness"**, which do not match the reference-file headers (`## Technical Checklist`, `## Readability Checklist — "New User Eyes"`). This mismatch is pre-existing, not introduced by the plan, but the implementer should target the actual header text in the reference file and not get confused by the Step 4 prose. No plan change required; flagging so the edit lands in the right place.

### WARN-3: Task 5 references a ROADMAP milestone the skill never loads
Task 5 says the 3D content source is "the ROADMAP milestone / spec note / user intent." But Step 0 only resolves and reads `paths.description`, `paths.architecture`, and `paths.docs` — there is no roadmap read anywhere in the skill, and `config.yaml`'s roadmap path is not resolved. As written, the 3D branch could instruct the agent to consult a ROADMAP it never opened. Mitigation: "user intent" is also a listed source, so 3D is still functional. Recommend Task 5 either (a) add a step to resolve/read the roadmap path when present, or (b) downgrade the roadmap to "if the user points to one" and lean on user-provided intent as the primary source. Low impact, but worth tightening so the instruction isn't a dangling reference.

### WARN-4: "Spec: tag rhythm" analogy in Task 8(b) may be opaque to the executor
Task 8(b) tells the agent to print the conformance pointer "mirroring the `Spec:` tag rhythm." That convention lives in the roadmap/planning skills, not in aif-docs, so an agent executing only this skill has no local referent. The intent (print a copy-pasteable line, never auto-write to ROADMAP) is clear enough on its own — recommend dropping or briefly inlining the analogy so it doesn't read as a missing reference.

## Architectural / consistency checks

- **Mode isolation is sound.** Every 3D task explicitly preserves normal-mode behavior ("Leave normal-mode path unchanged"), and Task 3 states absence of the token is byte-identical to today plus Change A. This keeps the always-on rule (Change A) cleanly separate from the opt-in mode (Change B). Good.
- **Change A correctly spans both modes.** Tasks 2 and 7 both reaffirm the no-motivation rule stays active in 3D — consistent and explicitly called out. Good.
- **Upstream-sync registration (Task 9) is necessary and correctly placed.** Without it, `aif-docs` falls under "All other skills — safe to overwrite," so a sync would wipe both changes. The plan caught this. This aligns with the existing divergence-tracking pattern in CLAUDE.md.
- **Project-convention note (no plan defect):** the global doc-style rule says "No prev/next navigation links," yet the aif-docs skill mandates prev/next nav (Core Principle 4) and Task 8(a) reaffirms it as unchanged. This conflict is pre-existing in the skill and out of scope for this plan; the plan correctly leaves the skill's own behavior intact rather than silently changing it.

## Positive notes

- Line references are precise and current — rare and appreciated; reduces implementer guesswork.
- Dependency graph is correct (Tasks 2→1, 4→3, 5/6/7→3, 8→4).
- Commit plan groups the always-on rule, the mode, and the registration into three logically independent commits, matching the repo's single-concern commit convention.
- The plan correctly identifies that suppressing the staleness/technical-accuracy checks in 3D must be surgical (it enumerates exactly which checks stay active), avoiding an over-broad "skip review" carve-out.

PLAN_REVIEW_PASS
