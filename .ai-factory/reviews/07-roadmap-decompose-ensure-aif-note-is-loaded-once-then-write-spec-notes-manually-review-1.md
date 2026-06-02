# Code Review — roadmap-decompose: ensure aif-note is loaded once, then write spec notes manually

## Scope
- **Code change reviewed:** `src/skills/roadmap-decompose/SKILL.md` (only changed source file; the other staged files are the plan, plan-reviews, sidecar, ROADMAP/note edits — not runtime code).
- **Plan:** `.ai-factory/plans/07-roadmap-decompose-ensure-aif-note-is-loaded-once-then-write-spec-notes-manually.md`
- **Spec:** `.ai-factory/notes/16-task-decompose-inline-notes-aif-note-format.md`

This is a documentation/skill-instruction edit — no executable code, migrations, types, or runtime state. "What breaks at runtime" reduces to: does the skill still instruct the agent correctly and self-consistently, and does it leave any stale per-task-invocation wording that re-introduces the confusion the task removes.

## Verification performed

**1. New mechanism is correctly stated (Two-Tier Output, lines 290–291, 296).**
- Step 3: "if `aif-note` has not yet been invoked in this chat, invoke it once now … if it has already been invoked, do not invoke it again" — matches the spec's load-once rule exactly.
- Step 4: "Write the spec note manually with the `Write` tool, following aif-note's in-context instructions" with `<NN>` derived by scanning `.ai-factory/notes/` and `<slug>` lowercase-hyphenated — matches the spec.
- Line 296: "`aif-note` is invoked at most once per chat … never per task" replaces the old "Sequential invocations only" paragraph. Correct.

**2. No stale per-task-invocation wording remains.** Grepped the file (case-insensitive) for `invoke aif-note`, `note invocation`, `invocations`, `sequentially`, `reports back`, `as the subject`, `blend`, `$1 slug`, `capture the note path` → **zero matches**. Both plan-review-1 findings (step 2 parenthetical "two notes + two contract lines"; lines 16/105/115/193/197) are resolved. Confirmed individually:
- Line 16 intro, line 6 frontmatter, line 105 (1.3), line 115 (1.3.1), line 136 (1.4), line 187 (2.4), lines 193/197 (2.4.1), lines 209–210 (2.5), line 289 (Two-Tier step 2), line 321 (contract-line rule), line 332 (Critical Rule 6) — all reworded to the manual-`Write` / load-once model.

**3. The "subject so aif-note does not blend siblings" cruft is fully removed** (was the wrong-parameter instruction the task targets). Confirmed absent.

**4. decompose carries no note-format of its own.** Step 4 defers structure to "aif-note's in-context instructions." Step 1's spec-content list (current state / change / files / guards / verify) describes *what to write*, not aif-note's note structure, and predates `0bfa177` — so nothing was added beyond the pre-commit baseline, satisfying the guard.

**5. aif-note is unchanged and still invocable.** `git status` shows no edits under `src/skills/aif-note/`. Its frontmatter has `disable-model-invocation: false`, so the load-once Skill-tool invocation in step 3 will actually succeed — the mechanism is not broken.

**6. `allowed-tools` is correct.** `Skill` (one-time aif-note load), `Write` (note authoring), and `Glob` (scan `.ai-factory/notes/` for next `<NN>`) are all present. YAML frontmatter is well-formed; the folded `>-` description block tolerates the longer line and the `aif-note's` apostrophe without quoting.

**7. Internal consistency.** Mode 1 Step 1.4 and Mode 2 Steps 2.4/2.5 all route through the Two-Tier Output procedure, so the load-once check fires once regardless of entry point. Mode 2.5's "update the named note file in place with `Write`" override is consistent with the procedure (it explicitly overrides step 4's new-`<NN>` path for the update case) and matches the pre-existing 2.5 structure — not a regression.

## Findings
None. The diff faithfully implements the plan and spec, resolves both prior plan-review findings, introduces no stale wording, leaves `aif-note` untouched, and is internally consistent.

REVIEW_PASS
