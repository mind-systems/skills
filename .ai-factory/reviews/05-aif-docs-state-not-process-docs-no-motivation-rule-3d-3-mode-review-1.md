# Code Review: aif-docs state-not-process docs (no-motivation rule + `3d`/`3д` mode)

**Reviewed:** `git diff HEAD` on branch `master`
**Files changed:** `.claude/skills/aif-docs/SKILL.md`, `.claude/skills/aif-docs/references/REVIEW-CHECKLISTS.md`, `CLAUDE.md` (plus plan/sidecar/plan-review artifacts under `.ai-factory/`)
**Risk Level:** 🟢 Low

## Summary

This is a text-only change to one skill plus a one-line registration in `CLAUDE.md`. No executable code, no migrations, no type or schema surface, no security implications. "Runtime" here means how a model reads the instructions, so the review focuses on internal consistency, contradictory directives, and faithfulness to the plan.

The implementation is faithful to the plan and the spec note. All nine tasks landed: Core Principle 7 added, no-motivation review pass wired into Step 4 and the Technical Checklist, `3d`/`3д` MODE detection in Step 0.1, the 3D explanation block, the three branched points (Step 1, Step 2.1 audit, Step 4 accuracy carve-out), the printed conformance pointer, and the `CLAUDE.md` divergence registration. Markdown structure is intact — no broken headers, no orphaned fenced blocks, the State A/B/C block correctly follows the `MODE = normal` branch, and `CLAUDE.md` has exactly one `aif-docs` entry (no duplicate from the pre-existing in-flight edit).

Findings are all non-blocking nits.

## Findings

### NIT-1: `argument-hint` omits the Cyrillic `3д` variant
`argument-hint: "[--web] [3d]"` (SKILL.md line 4) advertises only `3d`, while the skill body fully supports `3д` (line 92, 96). Hints are illustrative, not parsed, so this is cosmetic — but since the Russian token is a first-class trigger, `"[--web] [3d|3д]"` would be more honest. Optionally the `description` field could mention 3D mode, since that is what the skill loader surfaces. Low impact.

### NIT-2: Two no-motivation phrase lists drifted slightly
The Step 4 no-motivation pass (SKILL.md line ~506) lists: `we changed, was added, was replaced, this replaces, previously, because we, this milestone, was introduced, has been`. The matching Technical Checklist item (REVIEW-CHECKLISTS.md line ~18) lists: `we changed / was replaced / previously / because we / this milestone / was added / was introduced` — it omits `this replaces` and `has been`. The lists are illustrative heuristics for a model rather than exact matchers, so the drift is harmless, but aligning them avoids the appearance of a deliberate distinction.

Separately, `has been` is the most over-broad entry in the SKILL.md list — present-perfect phrasing can legitimately describe state in some docs. Because the agent applies judgment rather than a literal regex, this is acceptable; flagging only so it is a conscious choice.

### NIT-3: Step 1 (3D branch) points at a ROADMAP the skill never loads
The 3D branch in Step 1 (line 123) instructs the agent to gather target state "from the ROADMAP milestone, spec note, or stated user intent." Step 0 only resolves and reads `paths.description`, `paths.architecture`, and `paths.docs` — the skill never resolves a roadmap path or opens `ROADMAP.md`. So "the ROADMAP milestone" is a soft, unresolved reference. This was raised in plan-review WARN-3 and not tightened during implementation. It is low impact because "spec note / stated user intent" are also offered and the agent can open `ROADMAP.md` opportunistically if present, but the cleanest fix is to phrase it as "if a ROADMAP milestone or spec note is provided/available" so it does not read as a dangling instruction to consult a file the skill never loads.

## Pre-existing observations (not introduced by this change)

- **Checklist name mismatch.** Step 4 prose (SKILL.md line ~504) calls the two checklists "Technical Accuracy" and "Readability & Completeness", while the reference file headers are `## Technical Checklist` and `## Readability Checklist — "New User Eyes"`. The new 3D carve-out correctly targets the actual checklist *item text*, so it lands in the right place regardless — but the prose-vs-header naming gap predates this change and could mislead a future editor.
- **Internal-link checking is correctly preserved in 3D.** The Step 4 carve-out skips "broken-reference checks against the live codebase" (code/files that don't exist yet), while the Technical Checklist's "All internal links work" item is *not* annotated as skipped — doc-to-doc links are still verified in 3D. This is the correct distinction; calling it out only to confirm it was handled deliberately, not by omission.

## Verification performed

- Read all three changed files in full around the edits; confirmed no malformed markdown, no duplicated/renumbered headers, and the `MODE = normal` branch flows correctly into the State A/B/C block.
- Confirmed `CLAUDE.md` has a single `aif-docs` divergence entry and that it is placed in the "Intentionally diverged" list above the "All other skills — safe to overwrite" line, so a future sync will no longer treat it as overwrite-safe.
- Confirmed Change A (Principle 7 + no-motivation pass) is unconditional across modes, and the 3D carve-outs explicitly preserve the no-history rule — matching the spec's "drops current-state and verify, keeps no-history" constraint.
- No secrets, no shell/exec changes, no dependency or permission (`allowed-tools`) changes.

None of the findings block merge.
