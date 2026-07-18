# Code Review: 17.4 — Standalones: grep-audit and conform

## Code Review Summary

**Files Reviewed:** `src/skills/detangle/SKILL.md` (in full, 124 lines) + the six certified-clean files (by grep) + the plan + governing spec (`.ai-factory/specs/65-standalone-skills-conformance.md`) + contract line (ROADMAP 17.4) + reverse-graph consumers of `detangle`
**Risk Level:** 🟢 Low
**Code diff:** 1 file, 1 insertion, 1 deletion.

### What changed

`src/skills/detangle/SKILL.md:33` — one prose substitution inside the "Before you start — load project context" section:

```diff
-in-progress or planned roadmap milestone? That changes the impact analysis in Step 4.
+in-progress or planned task? That changes the impact analysis in Step 4.
```

Nothing else in the source tree changed. The remaining four files in `git status` are the pipeline's own artifacts for this task (plan, its `.json`, two plan-reviews) — expected bookkeeping, correctly excluded by the plan's path-scoped gate.

### Every plan gate re-run independently

Each of the plan's Task 3 gates was re-derived against the working tree in this session, not taken from the implementer's report:

| Gate | Expected | Actual |
|---|---|---|
| `rg -U -in 'milestones?' src/skills/detangle/SKILL.md` | zero | exit 1 ✅ |
| `rg -U -in 'spec\s+notes?\|milestones?'` over the six | zero | exit 1 ✅ |
| `rg -in 'spec-note'` over the six + `detangle` | zero | exit 1 ✅ |
| `git status --short -- src/ active/ upstream/` | one line | `M src/skills/detangle/SKILL.md` ✅ |
| `git diff --stat` (src) | 1 file, 1 ins, 1 del | exact match ✅ |
| diff filtered to `loads:`/`name:`/`description:`/`argument-hint`/`allowed-tools` | empty | exit 1 ✅ |

The spec's own three verification items are satisfied by the same runs, including `git status` showing nothing under `upstream/`.

### Correctness of the substitution itself

- **Right word.** `task` is the registry name for the `N.M` unit whose in-progress/planned state moves an impact analysis; `phase` would have been wrong (strategic tier, not the unit). Matches the contract line's mandate verbatim.
- **Right scope for the qualifier.** Dropping `roadmap` rather than rendering "roadmap task" follows the reserved-words qualifier rule — the paragraph names `.ai-factory/ROADMAP.md` at line 30, three lines above, so the qualifier disambiguates nothing.
- **Grammatical.** The article `an` binds to `in-progress`, not to the substituted noun, so the sentence survives the shortening intact. Read in place, the section still reads coherently: one name for the unit, no leftover synonym, the instruction to re-read the entry map unchanged.
- **No live reference broken.** The trailing `Step 4` pointer survives, and `### Step 4 — Synthesize` exists at line 80 — the reference resolves.
- **Line wrapping preserved.** The edit shortens line 33 without rewrapping line 32, exactly as the plan required.

### Runtime-breakage surfaces — all checked, none touched

This is a skill body, so "runtime" means what the agent loads and what greps it. Each candidate failure mode was checked rather than assumed:

- **Frontmatter untouched** — `name`, `description`, `argument-hint` byte-identical; the always-loaded `description:` field is not on the edited line, so the skill-description-field is unchanged.
- **No `loads:` edge exists** in `detangle` (frontmatter verified in full), so the byte-stability guard is vacuous here, as the plan stated.
- **No scanned literal, needle, or protocol token** on the edited line — it is descriptive prose, not a grep target or an emitted artifact shape.
- **Reverse graph clean.** `detangle` is named by `src/skills/temporal-tree/SKILL.md` (lines 7, 16, 21, 170) and `CLAUDE.md` (57, 78, 193) — all references are to the **skill name**, never quotations of the edited sentence. `rg -in 'in-progress or planned'` across `src/`, `docs/`, and `CLAUDE.md` returns the edited line and nothing else, so no cross-file citation went stale.
- **Symlink layer intact.** `active/skills/detangle → ../../src/skills/detangle` resolves; the edit lands in the active set automatically with no symlink change needed.
- **`aif-skill-generator` untouched.** Its symlink still points at `../../upstream/ai-factory/aif-skill-generator`, and `git status -- upstream/` is empty — the pristine mirror and the conflict-free sync split are preserved.

### The anti-manufacture discipline held

The task's defining risk was manufacturing work in the six files the spec certifies clean. It did not happen: the six are byte-unchanged, and a scan of `detangle` for the wider synonym family (`spec note`, `roadmap line`, `task line`, `governing spec`, `contract line`, `named roadmap`) returns zero — so no discretionary edit was slipped in under cover of the sanctioned one. One changed line across seven files is precisely the outcome the plan predicted and the spec's guard demands.

### Critical Issues

None.

### Findings

None.

### Positive Notes

- **The diff is exactly the planned diff** — no scope creep, no opportunistic cleanup, no reflowed paragraph. For a naming-only conformance task this is the whole ballgame, and it is rarer than it sounds.
- **The certified-clean six were genuinely left alone**, not "cleaned up a little while I was in there." Verified by grep and by `git status`, not by trusting the report.
- **The path-scoped `git status` gate proved its worth at run time.** Four pipeline artifacts were sitting untracked when the gate ran; the unscoped form the round-1 plan-review caught would have produced exactly the ambiguity it predicted. The scoped form returned one unambiguous line.
- **The substitution respects the vocabulary contract on both axes** — it retires a synonym (naming) without touching spelling, wrapping, or any machine-resolved identifier.

REVIEW_PASS
