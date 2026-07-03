## Code Review Summary

**Files Reviewed:** 1 plan (`plans/45-…-no-slug-matching.md`) against target `src/skills/roadmap-prune/SKILL.md`, spec note `notes/56-prune-deletes-pruned-specs.md`, and `ROADMAP.md` line 101
**Risk Level:** 🟡 Medium

### Context Gates
- **Roadmap** — WARN→PASS: the plan heading matches `ROADMAP.md:101` (`roadmap-prune: sweep the artifact dirs; delete completed tasks' specs by tag — no slug matching`, `[ ]` open). The contract line's `Spec:` tag (`.ai-factory/notes/56-prune-deletes-pruned-specs.md`) exists and the plan's four tasks faithfully cover Edits 1–3 + constraints of that note. Milestone linkage present.
- **Architecture** — PASS: no boundary violation. The change is confined to one skill file; ARCHITECTURE.md `## Features` write behavior (roadmap-prune's anchor store) is untouched. The "Composition: mechanism vs policy" rule is not implicated — this is a single mechanism edit, not a new skill/router.
- **Rules** — N/A: no `.ai-factory/RULES.md` present.
- **Skill-context** — N/A: no `.ai-factory/skill-context/aif-review/SKILL.md` present.

### Critical Issues
None (no blocking bug, missing migration, or runtime error).

### Issues / Ambiguities

**1. `Path base` instruction, read literally, will silently fail to delete every spec (`rm -f` no-ops).** — Task 1, plan line 21 (mirrored in spec note line 22).

The plan states: *"all paths — the four dirs **and the tag paths** — resolve against the target ROADMAP.md's own `.ai-factory/` (the same directory the skill reads ROADMAP.md from)."* But the two path classes have **different bases**:

- The four bare dir names (`plans/`, `plan-reviews/`, `reviews/`, `patches/`) are relative to `<root>/.ai-factory/` → correct base is `.ai-factory/`.
- The captured `Spec:` tag paths are **literal and already contain the `.ai-factory/` prefix** — e.g. `ROADMAP.md:101` ends with `` Spec: `.ai-factory/notes/56-prune-deletes-pruned-specs.md` ``. These are repo-**root**-relative, not `.ai-factory/`-relative.

Resolving a literal tag path against `<root>/.ai-factory/` yields `<root>/.ai-factory/.ai-factory/notes/56-…md`, which does not exist. Because the step uses `rm -f`, the miss is **silent** — the specs are never deleted, and the summary report would still list them as "deleted." This is exactly the silent-failure surface the skill is meant to close.

This directly contradicts two other statements the plan itself makes:
- Task 1 step 1: *"Paths are literal from the tag … works across the lazy `notes/`→`specs/` migration"* — literal tag paths must be used verbatim, not re-based.
- The migration-robustness claim only holds if the tag path is applied as-is from the repo root.

**Fix:** clarify the path model in the plan (and, since "behavior is defined by the spec note," in note 56 too). Recommended wording: *derive the target project **root** from the skill argument (the directory that contains `.ai-factory/`); prepend `.ai-factory/` to the four bare dir names; use each captured `Spec:` tag path **verbatim** relative to that root. The point of "never a fixed top-level path" is to anchor on the argument-derived root — not the session's CWD repo — not to prepend `.ai-factory/` to tag paths that already include it.*

### Minor Notes

- **Renumbering (Task 1).** Inserting the sweep as a new step between Step 4 and Step 5 shifts Step 5 (Update ROADMAP.md) → 6, Step 6 (Verify) → 7, and Task 4's summary report → 8. Task 4 says "renumber consistently" for the report, but Task 1 does not call out that its insertion also cascades the numbering. Not a defect — an implementer will handle it — but worth an explicit "renumber the following steps" note so the two renumbering instructions don't collide.
- **`Reading the history later` section stays valid.** SKILL.md lines 209–211 tell future agents to read pruned plans via `git diff <hash>~1 <hash> -- .ai-factory/plans/` — i.e. through git history, not the working tree. The sweep deletes `plans/` only at HEAD, so this section remains correct and needs no edit. Good that the plan does not touch it.
- **Commit message.** `Roadmap prune` conforms to the global commit-message convention (sentence case, no prefix, no period) and is distinct from the existing `command-commit-roadmap-update` message (`Roadmap update`). No conflict.
- **`allowed-tools`.** Adding `Bash(rm *)` to the current `Read Write Edit Bash(git *)` is correct and minimal for the sweep.

### Positive Notes
- Faithful, near-lossless encoding of spec note 56 — plain `rm` / `git add -A`-once mechanism, no `git rm`, instructions-only (no rationale prose), tag-only spec deletion, `handoffs/` untouched, `test-runs/` parity for `ROADMAP_TESTS.md`.
- Correct ordering discipline: tag capture is sequenced **before** ROADMAP line deletion (Task 2), and the sweep is placed after the Step 4.1 snapshot so full history stays reachable.
- Safety-by-construction is preserved: specs are deleted only through `[x]` lines' tags, so open `[ ]` tasks' specs can never be swept — no directory scan exists to catch them.
- Verify (Step 6) is explicitly left intact; the summary report is additive and informational, matching the note's "no extended verify" scope boundary.
- Settings (Testing: no) are appropriate — the target is skill-instruction markdown with no silently-failing runtime surface of its own.

Resolve Issue #1 (path-base wording) before implementation; everything else is sound.
