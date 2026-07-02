## Plan Review Summary

**Plan:** `33-roadmap-engine-absorb-the-shared-roadmap-maintenance-flow.md`
**Target file:** `src/skills/roadmap-engine/SKILL.md` (single-file change)
**Risk Level:** 🟢 Low

The plan faithfully implements its governing spec (note 43) and honors the boundary
rule from note 38. Scope is correct: engine-only, callers untouched (notes 44–45 own
the slim-down). File paths, tool references, and the mode/hook model all match the
actual codebase. No blocking issues found.

### Context Gates

- **Roadmap linkage — PASS.** The plan's heading maps to ROADMAP.md line 77
  (`roadmap-engine: absorb the shared roadmap-maintenance flow`), whose `Spec:` tag
  points at `.ai-factory/notes/43-roadmap-engine-maintenance-flow.md`. Governing spec
  read and cross-checked; the plan's Tasks 1–3 mirror note 43's Step 0 / mode /
  hook-point / critical-rules breakdown almost 1:1.
- **Architecture — PASS.** `.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs
  policy" mandates that engines hold the shared *how* and philosophies hold the
  *what/whether*. The plan moves only mechanism (Step 0, modes, dialogs, finalize,
  check scan, mechanism-tier rules) into the engine and explicitly leaves the
  atomicity gate / 5–15 rule / granularity as caller-supplied hooks. Directionally
  correct and load-once discipline is restated (Task 1). The engine already
  anticipates this — its intro says "never re-invoke it per task or per mode."
- **Rules — WARN (N/A).** No `.ai-factory/RULES.md` present. No
  `.ai-factory/skill-context/aif-review/SKILL.md` present. Nothing to enforce.

### Critical Issues

None. No missing migrations (Testing: no, Docs: no, Logging: none — all appropriate
for a skill-text change). No security surface. No incorrect file paths or API usage —
`AskUserQuestion`, `Glob`, `Grep`, `Bash(git *)`, `Write`, `Edit`, `Skill` are the
tools the callers already declare, and the engine correctly describes them as
caller-executed mechanism.

### Non-blocking Observations

1. **`allowed-tools` decision is sound (Task 4).** Leaving `allowed-tools: Read`
   despite the flow text naming `Write`/`Edit`/`Glob`/`Grep`/`Bash(git *)`/
   `AskUserQuestion` is correct and consistent with note 38's boundary model: the
   engine is *content the caller executes*, not an executor. Both callers already
   declare the full tool set. Good call not to widen.

2. **"rewrite" action drops from built-in to hook (WARN, spec-level, not a plan
   defect).** Both current callers list **rewrite** as a built-in update-menu action
   (outline option 4, decompose option 5). The plan's generic menu — per note 43 line
   19 — is "review progress / add / reprioritize / save", so "rewrite" (and
   decompose's "decompose existing") become caller-supplied extra actions (hook d).
   The plan follows the spec exactly, so this is not a plan error. Flagging only so
   the downstream authors of notes 44–45 remember to **register "rewrite" as an extra
   action** in each caller, or behavior will silently regress in update mode. Worth a
   one-line note in the engine's hook-(d) description that common extras like
   "rewrite" live with the caller.

3. **Banned-words grep will false-positive (Task 4 verification).** The word
   `milestone` already appears in the *existing, out-of-scope* sections ("The two-tier
   artifact" line 25; "Roadmap File Format" `## Milestones` header + `**Name**` lines
   46–50), and "tasks" appears at line 34. A whole-file `grep milestone` will hit
   these. The plan already scopes the check to "the new section" — to make that
   deterministic, suggest scoping the grep to the appended block, e.g.
   `sed -n '/## Roadmap maintenance flow/,$p' src/skills/roadmap-engine/SKILL.md | grep -nE 'milestone|atomic|strategic|roadmap-outline|roadmap-decompose'`.
   Minor; the reviewer-agent can scope mentally.

4. **H1 title / intro stay artifact-only (optional).** After the flow lands, the H1
   "Roadmap Engine — Shared Two-Tier Artifact Format" and the intro's "This is the
   shared explanation of the roadmap artifacts … not any decomposition philosophy"
   describe only the format tier, not the new maintenance flow. Note 43 constrains
   changes to the format sections ("no changes … beyond linking"), so leaving them is
   defensible, and Task 4 does broaden the frontmatter `description`. Consider a
   one-clause widening of the intro sentence so the section header isn't misleading —
   optional, not required by the spec.

5. **Line budget is comfortable.** Current engine is 60 lines; the generalized flow
   (distilled from ~229 + ~281 caller lines with the duplication removed) lands well
   under the ≤500 ceiling — realistically ~230–260 total. Task 4's `wc -l` gate is the
   right guard.

### Positive Notes

- Hook points (a)–(d) are enumerated identically to note 43's list, and the plan
  repeatedly restates "the engine holds none of these" — exactly the mechanism/policy
  separation the architecture requires.
- Finalization ordering is preserved verbatim from both callers: draft in memory →
  `` Spec: `<note pending>`. `` placeholders → confirm → write notes only for the
  confirmed set → replace placeholders → write `$TARGET_FILE`. The "removed/rewritten
  entries get no note" invariant is carried through (Task 2).
- Caller-agnostic discipline is enforced end-to-end ("entry" not "milestone/task",
  `$TARGET_FILE` not a literal path, no caller skill names), and `roadmap-prune` is
  correctly identified as a permitted reference (a downstream pruner, not a caller) —
  matching the existing callers' critical-rule 4 wording.
- Dependency structure is untouched and correct: `loads: note` stays (the flow's
  note-writing already routes through it); no new `loads` edge is introduced.

PLAN_REVIEW_PASS
