# Plan Review — command-handoff: scale handoff detail proportionally to session depth

**Plan:** `08-command-handoff-scale-handoff-detail-proportionally-to-session-depth.md`
**Risk Level:** 🟢 Low

## Scope verification

The plan targets `src/commands/command-handoff.md` and claims it is symlinked to
`~/.claude/commands/command-handoff.md`. Verified:

- `~/.claude/commands` → `/Users/max/projects/skills/src/commands` (directory symlink).
- The target file and `~/.claude/commands/command-handoff.md` share inode `8959491380` —
  editing the `src/` copy is automatically live. The claim is accurate.
- No separate skill package exists (`src/skills/command-handoff/` is absent); the
  `command-handoff` entry in the skill list is just how Claude Code surfaces the command.
  There is **no second file to update** — the plan is complete on this axis.

## Line-reference accuracy

Every line anchor in the plan matches the current file:

- Task 1 — "skeleton intro (line ~41), before the skeleton fence" → line 41 is the
  "Use the skeleton below exactly…" paragraph; fence opens at line 43. ✅
- Task 2 — "after section 9 (Hard rules)" → section 9 ends at line 87, fence closes
  line 88. ✅ Also correctly flags the "Optional sections (7–9)" prose at line 41
  for update to 7–11.
- Task 3 — "section 6 (Error log)" → lines 77–78, including the "Empty → omit section"
  clause the plan preserves. ✅
- Task 4 — "after 'Populate every field…' (line ~90), before Step 3" → line 90 / Step 3
  starts line 94. ✅

## Spec fidelity

The plan implements all four items of spec note `18-task-command-handoff-scale-depth.md`
(proportional-depth mandate, two new sections, concrete error log, richness self-check)
and honors all three guard conditions (skeleton unchanged, note-trigger/persistence path
unchanged, proportional-not-maximal). The ROADMAP entry matches the plan one-to-one and is
properly linked to the spec note — roadmap alignment is satisfied.

The spec's Open Question (embed a sanitized few-shot fragment vs. describe the target depth)
is resolved implicitly: no task embeds an exemplar. This is a reasonable, defensible choice —
it keeps an already-substantial command file lean and matches its dense imperative tone.
Not a defect; noting it so the decision is explicit.

## Findings

### Critical
None.

### Minor (non-blocking)

1. **New section 10 vs. existing section 8 — overlap not disambiguated.** WARN.
   The plan carefully distinguishes new section 11 ("Per-unit map") from the existing flat
   "Current state" list (Task 2 says "Call out that it is distinct"). It does **not** apply
   the same treatment to new section 10 ("Cross-cutting contracts / invariants checklist")
   vs. existing section 8 ("Domain model spine"). Both concern "settled rules that must
   hold," so an agent filling the skeleton could double-write or hesitate over which slot a
   given item belongs in. The spec already implies the seam (10 = concrete names / types /
   signatures that must stay byte-identical; 8 = model concepts not to re-litigate), so a
   single clarifying clause in Task 2 — mirroring the 11-vs-3 distinction — would remove the
   ambiguity. Optional; the implementer can resolve this inline without a plan change.

### Positive notes

- Changes are strictly additive; the existing 9-section skeleton, section order/names, the
  `note`/`ноут` trigger, and the Step 3 note-persistence path are all explicitly preserved.
  No migration or breaking-change risk.
- Task dependencies (1 → 2 → 3 → 4) are correctly ordered and each task is independently
  verifiable.
- Task 4 correctly scopes the self-check to run before the Step 3 chat/note split, so it
  applies to both modes — a subtle sequencing point the plan got right.
- No security, performance, or data-migration surface (a single markdown command file).

The minor overlap note is a refinement, not a blocker. The plan is accurate, complete, and
faithful to its spec.

PLAN_REVIEW_PASS
