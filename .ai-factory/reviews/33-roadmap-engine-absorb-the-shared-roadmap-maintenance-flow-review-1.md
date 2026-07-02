# Code Review: roadmap-engine — absorb the shared roadmap-maintenance flow

**Scope:** `git diff HEAD` — only `src/skills/roadmap-engine/SKILL.md` is a code change (the `.json` / plan / plan-review files are planning artifacts, out of review scope).

**Nature of the change:** this file is agent-runtime instruction content, so "correctness" means: does the absorbed flow behave the same as what the two callers currently do, does it stay caller-agnostic, and does it leak any philosophy? Reviewed against the plan, note 43, note 38, and the two callers' current text.

## Constraint checks (all pass)

- **Single code file:** only `src/skills/roadmap-engine/SKILL.md` modified. `roadmap-outline` / `roadmap-decompose` untouched. ✓
- **Line budget:** 242 lines ≤ 500. ✓
- **Caller-agnostic:** grep of the new section (lines 63–242) for `milestone|atomic|strategic|roadmap-outline|roadmap-decompose|roadmap-decompose-skeleton` → none. `roadmap-prune` appears only as the downstream pruner in critical rule 3 (not a caller — matches the callers' existing rule 4 wording). ✓
- **No philosophy leaked:** no atomicity gate, no 5–15 rule, no granularity definition. Granularity / per-entry gate / target-file routing / extra actions are all named as caller hooks only (lines 71–80). ✓
- **Load-once restated** for the new section (lines 68–69). ✓
- **Two-tier format + Roadmap File Format sections unchanged** (diff confirms only an append + the description edit). ✓
- **Register:** prose + the callers' existing `AskUserQuestion` blocks — same register as the rest of the file, not rigid pseudo-code. ✓
- **Frontmatter `allowed-tools: Read` left as-is:** correct — the engine is *loaded* (Read) by callers that already declare Write/Edit/Glob/Grep/Bash/AskUserQuestion/Skill; it does not execute the flow itself. Consistent with the plan's Task 4 note. ✓

## Findings

### 1. (Medium) The shared update-mode "Rewrite" action was not absorbed

The absorbed **Update mode** action menu (lines 165–172) offers only:

```
1. Review progress
2. Add new entries
3. Reprioritize
```

But **both** callers' current update menus include a fourth shared action — "Rewrite — major revision of the roadmap":

- `roadmap-outline/SKILL.md:125` — `4. Rewrite — major revision of the roadmap`
- `roadmap-decompose/SKILL.md:154` — `5. Rewrite — major revision of the roadmap`

This is generic mechanism, identical in both callers — exactly the "shared roadmap-maintenance flow" this milestone is chartered to absorb. `Decompose existing` (decompose-only) was correctly left out as a caller-specific hook-(d) action, but `Rewrite` is common to both and belongs in the engine's built-in menu.

Consequence: it surfaces at notes 44/45, whose contract is "behavior-identical for the user in every mode." With `Rewrite` absent from the engine menu, the slimmed callers either (a) silently drop a user-facing update action — a behavior regression — or (b) each re-register `Rewrite` as a hook-(d) extra, re-duplicating the very action this task was meant to centralize.

Note the inconsistency this creates within the same file: the **Create-mode** confirm menu *keeps* its Rewrite option (line 147, `4. Rewrite — let me give better input`), while the **Update-mode** menu drops its Rewrite. The absorption kept one and dropped the other.

Caveat: the plan's Task 2 itself specified the update menu as "review progress / add / reprioritize / save" and omitted Rewrite, so the implementation faithfully followed the plan — the gap originates in the plan, not a coding slip. Flagging it here because it defeats the milestone's stated goal and will require a fix (in this engine, ideally) before notes 44/45 can honor "behavior-identical." Suggested fix: add `Rewrite — major revision` as option 4 in the engine's update menu (lines 168–172), with a one-line description that it re-runs the create-mode draft→confirm cycle over the existing file.

## Notes (non-blocking, no action needed)

- Check-mode summary shows only `Completed: X/N` + `Next up` (no `Total entries`), unlike update mode — this matches both callers' current check-mode summaries, so it is intentional and consistent, not a regression.
- The finalize step (lines 150–154) says "write each confirmed entry's spec note" without restating "ensure `note` is loaded"; the two-tier section above (line 30) already carries the load-once rule for `note`, and the flow references "two-tier artifact per the format above," so this is covered.
