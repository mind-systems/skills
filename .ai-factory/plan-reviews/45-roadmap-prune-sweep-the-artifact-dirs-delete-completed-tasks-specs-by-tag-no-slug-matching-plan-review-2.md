## Code Review Summary

**Files Reviewed:** 1 plan (`plans/45-…-no-slug-matching.md`) against target `src/skills/roadmap-prune/SKILL.md`, governing spec note `notes/56-prune-deletes-pruned-specs.md`, and `ROADMAP.md` line 101
**Risk Level:** 🟡 Medium

### Context Gates
- **Roadmap** — PASS: the plan heading matches `ROADMAP.md:101` (`roadmap-prune: sweep the artifact dirs; delete completed tasks' specs by tag — no slug matching`, `[ ]` open). The contract line's `Spec:` tag (`.ai-factory/notes/56-prune-deletes-pruned-specs.md`) exists; the plan's four tasks cover Edits 1–3 + constraints of that note. Milestone linkage present.
- **Architecture** — PASS: no boundary violation. The change is confined to one skill file; ARCHITECTURE.md `## Features` write behavior (roadmap-prune's anchor store, consumed by `temporal-tree`) is untouched. The "Composition: mechanism vs policy" rule is not implicated — a single-mechanism edit, not a new skill/router.
- **Rules** — N/A: no `.ai-factory/RULES.md` present.
- **Skill-context** — N/A: no `.ai-factory/skill-context/aif-review/SKILL.md` present.

### Round-1 follow-up
Review-1 raised one issue and two minor notes. Status:
- **Issue #1 (path base silent-failure)** — **partially resolved.** The plan body (Task 1, line 21) now states the correct two-base model. **But the governing spec note was not updated** — see Critical Issue below.
- **Minor: renumbering cascade** — resolved. Task 4 now spells out the tail order explicitly ("sweep, Update ROADMAP.md, Verify, Summary report").
- **Minor: `Reading the history later` / commit message / `allowed-tools`** — all confirmed still correct; no action was needed.

### Critical Issues

**1. The path-base fix landed in the plan but NOT in note 56 — and the plan declares the note authoritative.** — Plan line 4 vs. note `56-prune-deletes-pruned-specs.md` line 22.

The plan's own framing (line 4): *"All changes are to one skill file; **behavior is defined by the spec note** (`.ai-factory/notes/56-prune-deletes-pruned-specs.md`)."* So the note is the contract; the SKILL.md edit must conform to it.

Task 1 (plan line 21) now carries the **corrected** path model:
> "The captured tag paths are **repo-root-relative** — they already begin with `.ai-factory/` — so join them onto the **target repo root**, not onto `.ai-factory/` (joining onto `.ai-factory/` would double the segment)."

That is right. But note 56 line 22 still carries the **pre-fix** model that review-1 identified as the silent-failure bug, verbatim:
> "All paths — the four dirs **and the tag paths** — resolve against the **target** ROADMAP.md's own `.ai-factory/` (the same directory the skill reads ROADMAP.md from), never a fixed top-level path."

These now **directly contradict** each other on the load-bearing path base. A captured tag path is literal (`.ai-factory/notes/56-…md`); resolving it against `<root>/.ai-factory/` — as the note still instructs — yields `<root>/.ai-factory/.ai-factory/notes/56-…md`, which does not exist. Under `rm -f` the miss is **silent**: specs are never deleted, yet the Task 4 summary report still lists them as deleted. This is exactly the silently-failing surface the milestone exists to close, and it is the single most safety-critical instruction in the change (`rm` on an argument-derived base).

Because the plan itself points the implementer at the note as the definition of behavior, an implementer who follows the note over the plan body will re-introduce the bug. Review-1's fix was explicit that both surfaces needed updating: *"clarify the path model in the plan (and, since 'behavior is defined by the spec note,' in note 56 too)."* Only the plan half was done.

This also collides with the global **"One home per fact"** rule: the path base now lives in two places with two different, mutually exclusive values — the definition of drift.

**Fix (either):**
- Update note 56 line 22 to the two-base model (four bare dir names → prepend `.ai-factory/`; captured `Spec:` tag paths → used **verbatim** relative to the argument-derived target root), so the contract and the plan agree; **or**
- Add one sentence to the plan stating that where the plan body and note 56 differ on the path base, the plan's corrected two-base model governs, and schedule the note correction.

Updating the note is the cleaner option — it keeps the note as the single home of the behavior the plan says it defines.

### Minor Notes
- **Contract line carries the same stale wording.** `ROADMAP.md:101` also says *"All paths resolve against the **target** ROADMAP.md's own `.ai-factory/`."* The contract line is a ~600-char summary and the plan body is authoritative for implementation, so this is lower-stakes than the note — but it is the same drift and is worth correcting in the same pass so all three surfaces (plan, note, contract line) state one path model.
- **`allowed-tools`.** Adding `Bash(rm *)` to the current `Read Write Edit Bash(git *)` is correct and minimal for the sweep (Task 1, plan line 22).
- **Renumbering.** With the sweep inserted after Step 4, the tail becomes: sweep → Update ROADMAP.md (was 5) → Verify (was 6) → Summary report (new). Task 4 states this; Task 2 correctly constrains the ROADMAP.md line deletion to run only after Task 1's tag capture.

### Positive Notes
- The path-base correction in the plan body is precise and closes review-1's Issue #1 on the plan side.
- Faithful encoding of note 56's mechanism otherwise: plain `rm` / `git add -A`-once, no `git rm`, instructions-only (no rationale prose), tag-only spec deletion, `handoffs/` untouched, `test-runs/` parity for `ROADMAP_TESTS.md`.
- Safety-by-construction preserved: specs are deleted only through `[x]` lines' tags, so open `[ ]` tasks' specs can never be swept — no directory scan exists to catch them.
- Verify (Step 6) is explicitly left intact; the summary report is additive and informational, matching the note's "no extended verify" scope boundary.
- `Reading the history later` (SKILL.md 209–211) reads pruned plans through git history, so the HEAD-only sweep leaves it valid — correctly left untouched.
- Settings (Testing: no) are appropriate — the target is skill-instruction markdown with no silently-failing runtime surface of its own.

Resolve Critical Issue #1 (align note 56 — and ideally the contract line — with the plan's corrected two-base path model) before implementation. Everything else is sound.
