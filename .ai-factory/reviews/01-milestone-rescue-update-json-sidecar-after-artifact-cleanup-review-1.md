# Code Review: milestone-rescue — update JSON sidecar after artifact cleanup

**Plan file:** `.ai-factory/plans/01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.md`
**Changed file:** `.claude/skills/milestone-rescue/SKILL.md`
**Companion doc (not changed):** `.claude/skills/milestone-rescue/docs/overview.md`

## Risk Level
🔴 **High** — one critical ordering bug that defeats the stated preservation invariant in the most common code path.

---

## Critical Issues

### 1. Cleanup deletes the sidecar before the new sub-step can read it — `planner`/`implementer`/`elapsed` get silently lost

The new sub-step is inserted **after** the existing "Clean up artifacts" block (SKILL.md lines 185–194). That block reads, unchanged by this plan:

> delete all uncommitted files from `plans/`, `plan-reviews/`, `reviews/`, and `patches/` that belong to this milestone's slug.
>
> - Files marked `??` (untracked) → `git clean -f -- <path>`
> - Files marked `A ` (staged/added) → `git rm -f -- <path>`

The sidecar lives at `.ai-factory/plans/{seq}-{slug}.json` — same slug, same directory. According to `docs/overview.md` line 45 (`All of these are uncommitted. The orchestrator only commits on success.`), when `milestone-rescue` runs after a failed pipeline, the sidecar is almost always uncommitted (status `??` or `A`). Therefore the cleanup block matches the sidecar and deletes it via `git clean -f` or `git rm -f`.

Then the new sub-step at SKILL.md lines 196–224 executes:

1. Line 196–199: locate the sidecar. → file is gone.
2. Line 201–202: "If the file exists, read it … If it does not exist, start from an empty JSON object." → falls into the empty-object branch.
3. Line 221–223: "Preserve every other key already present — `planner`, `implementer`, `elapsed`, and any others — untouched." → there are no other keys to preserve; the freshly emitted sidecar contains only `{"step": "<value>"}`.

Net result: **the planner/implementer session IDs and elapsed counter are erased on every normal rescue invocation**, exactly the failure mode the plan's design decisions and the source note (`notes/08`, lines 32–38) explicitly forbid:

> - `planner` session ID — keep (planner can resume its session)
> - `implementer` session ID — keep
> - `elapsed` — keep
>
> Only `step` is updated.

The plan's instruction 7 enforces preservation in the prose, and Task 2 reinforces it in "What NOT to do," but the surrounding *ordering* in SKILL.md makes both instructions vacuous in the common case.

**Verification against the current repo state.** The on-disk sidecar `.ai-factory/plans/01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.json` is currently `A` in `git status`. Running the new sub-step against it after the cleanup block would produce exactly the data-loss path described above (planner=`a2d157a0…`, implementer=`64c03021…`, elapsed=`589` would all be lost).

**Required fix — pick one:**

- **(A) Reorder: read the sidecar before the cleanup runs.** Capture the sidecar contents in memory (or note the current `planner`/`implementer`/`elapsed`) at the *start* of Step 5 — before any deletion. After cleanup, write back the preserved keys with the new `step`.
- **(B) Narrow the cleanup scope.** Change the existing cleanup block so it deletes only `.md` files in `plans/` for this slug, leaving `.json` sidecars in place. Then the new sub-step's "preserve existing keys" instruction works as intended.
- **(C) Re-stage / restore the sidecar before reading.** After cleanup, run `git checkout HEAD -- <sidecar>` to bring back the last-committed version, then update. This only helps if the sidecar was previously committed — fragile.

(A) and (B) both solve the bug. (B) is the smaller diff and preserves Git history; (A) is more defensive against future cleanup-scope changes. Either way, **the plan must update the cleanup block too** — not just append a sub-step that assumes the sidecar survives.

---

## Medium Issues

### 2. `docs/overview.md` Step 5 is now stale

`docs/overview.md` lines 128–145 describe Step 5 ("Apply and clean up"). The body, the "Clean up" subsection, and the "What NOT to do" list (lines 149–156) make no mention of the sidecar update — yet the actual `SKILL.md` Step 5 now contains a substantial new sub-step and a new "What NOT to do" bullet. Future readers will see two contradictory descriptions of the same step.

The plan does not mention `docs/overview.md` at all (Files lists only `SKILL.md` for all three tasks). Either:
- Add a Task 3 to mirror the sidecar-update sub-step into `docs/overview.md` Step 5 and the "What NOT to do" list, OR
- Explicitly state in the plan that `docs/overview.md` is intentionally not updated (and why — e.g. it's a higher-level orientation doc).

Leaving the doc silently out of sync is the worst option.

### 3. Cleanup behavior of `.json` sidecar interacts with mapping-table rules in subtle ways

Even if Critical #1 is fixed by narrowing cleanup to `.md` files only, the mapping table's row 1 ("Plan-reviews deleted (or none pass) → `planned`") and row 2 ("Plan-reviews exist and pass, reviews deleted → `plan_reviewed`") implicitly assume the cleanup *only* removed plan-reviews/reviews — never the plan file itself. But the current cleanup block deletes uncommitted files from **all four directories including `plans/`**. If the plan `.md` is uncommitted and gets deleted, writing `step: "planned"` is misleading — there is no plan on disk for the orchestrator to resume against.

This is a pre-existing concern (the cleanup language predates this plan), but the new sub-step makes it more user-visible: the sidecar will now confidently claim `step: "planned"` even when the plan file is gone. Worth flagging in the plan even if not fixed here.

---

## Minor Issues

### 4. Fall-through case (instruction 9) is unreachable through the normal entry path

Step 1 (SKILL.md lines 41–42) stops the skill with "there is nothing to rescue" if no uncommitted files exist in the four artifact directories. The fall-through "both plan-reviews and reviews pass on disk" case (SKILL.md lines 218–219) would only fire if there are uncommitted artifacts in *some* directory (so Step 1 lets us through) but the plan-reviews and reviews on disk all pass. That happens essentially only when uncommitted patches exist alongside passing reviews — an unusual state. Not a defect; just worth knowing the branch is defensive rather than load-bearing.

### 5. "Check the working tree" via `Glob` — Glob behavior on a non-matching pattern

Line 198–199 suggests checking existence via `Glob`. `Glob` returns no matches when the file does not exist (it does not error), which is fine. A failed `Read` is also fine. Both paths are well-defined; no change needed. (Noted only because plan-review-2 flagged this as "non-blocking" — confirmed harmless.)

### 6. Template-vs-literal `{value}` in the confirmation line

Line 226 prescribes the exact form `Sidecar updated: step set to "{value}"`. The braces are placeholder syntax — the agent should substitute (e.g. `Sidecar updated: step set to "planned"`). The plan does not explicitly say so, but in context any reasonable agent will interpret it correctly. Plan-review-2 already noted this. No change needed.

### 7. `git status` ordering nuance

The new sub-step says (line 204) "Inspect which plan-review and review files for this slug remain on disk **after** the cleanup deletions above." The deletions use `git rm -f` which both removes from index and from disk, so a follow-up `Glob` or `ls` will reflect the post-cleanup state correctly. Just worth noting the agent must *re-check* disk after the cleanup, not rely on cached state from Step 1.

---

## Positive Notes

- Frontmatter update (line 11) cleanly inserts `Write` between `Read` and `Edit` with no YAML breakage.
- Mapping table is copied verbatim from `notes/08-milestone-rescue-sidecar-update.md` lines 14–20 as required (cross-checked character-by-character).
- Clarifying sentence after the table (lines 214–216) correctly resolves the recursive "Sidecar doesn't exist" row.
- Insertion point sits inside Step 5, before Step 5.5, exactly as the design decisions specify.
- New "What NOT to do" bullet (lines 279–280) matches the imperative style of the surrounding bullets.
- The duplication between in-flow instruction 8 and the "What NOT to do" bullet is explicitly defense-in-depth and works as intended (modulo Critical #1).
- Tool-agnostic prose ("parse it as JSON", "serialize the result back as JSON with 2-space indentation") matches the surrounding skill's voice; no Python leakage.

---

## Summary

The mechanical changes match the plan's intent exactly. The plan, however, did not account for the fact that the existing cleanup block — which the new sub-step explicitly sits *after* — already deletes the sidecar in the common case. As a result, the preservation invariant for `planner`/`implementer`/`elapsed` is silently violated on every normal rescue invocation, which is the opposite of what `notes/08` mandates.

Fixing Critical #1 (and ideally Medium #2) is required before this change is safe to ship. Once the cleanup vs sidecar ordering is reconciled, the rest of the diff is clean.
