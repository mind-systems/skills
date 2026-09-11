# Review: 38.1 — the numbering scan sees past ninety-nine

**Plan:** `.ai-factory/plans/trickster77777/41-38-1-the-numbering-scan-sees-past-ninety-nine.md`
**Changed files:** `src/skills/note/SKILL.md`, `src/skills/task-rescue/SKILL.md` (both read in full, not just the diff)

## What was checked

**Every site named in the plan moved, and moved together.**
- § "Hooks (caller inputs)", Destination directory bullet — the glob is gone; the scan is defined once as "a run of one or more digits followed by a hyphen … ends in `.md`" with the `^[0-9]+-.*\.md$` form, read as an integer, compared numerically (`100-…` above `99-…`). "Numbering stays **per-directory**" retained verbatim.
- § "Step 3", `<NN>` bullet — four-digit width with `0001`, `0002`, `0003` examples, and the read/write split stated in the same bullet ("this width governs only what `note` writes — existing names of any width are still read"). The reading rule is not narrowed to a four-digit glob anywhere — the one careless outcome the plan foreclosed.
- § "Step 3", determination sentence — keeps the find/default two-clause shape, points at the hook's scan, parses as integer, `0001` default, "exactly four zero-padded digits regardless of how small".
- § "Step 3", bound paragraph — placed directly after the determination sentence, before Folder style and before `mkdir -p`; the predicate is the plan's one sentence ("`9999` or greater"), the stop covers `mkdir -p`, the file, and sibling reads, and the destination is named in the report.
- § "Step 3", Folder style — "most recent (highest-numbered)" now decided over the parsed integer; precedence, guards, and "at most 2 sibling reads" are word-for-word unchanged; the phrase "two-digit" is absent.
- § "Step 4" — a second, separate report form for the bound; the "Note saved:" block and its trailing default sentence are unchanged.
- § "Important Rules" Rule 5 — the bound named as the one exception to "always create a new file", with the same "`9999` or above" predicate.
- § "Note File Handling" — the copy of the rule collapsed into a pointer at Step 3, bounded at `9999`; the `<slug>` bullet and lead-in unchanged.
- `task-rescue` — only the quoted glob removed from the destination-hook bullet; the paragraph now reads "its per-directory numbering scan", consistent with the file's own "not restated here" sentence two lines below. No other change.

**Verification commands from the plan, re-run against the working tree:**
- `grep -n '\[0-9\]\[0-9\]\|two-digit\|start at `01`' src/skills/note/SKILL.md` → nothing.
- `grep -c '0001' src/skills/note/SKILL.md` → 3 (≥ 2).
- `grep -n '9999' src/skills/note/SKILL.md` → exactly four hits: Step 3 bound paragraph, Step 4 bound report, Rule 5, Note File Handling. None stray.
- `grep -rn '\[0-9\]\[0-9\]' src/skills src/commands` → only `aif-plan` (×2) and `roadmap-test-coverage` (×1), the two carriers this task leaves alone by contract.
- `<NN>` still appears unchanged as the placeholder in the path templates (Step 3, Step 4, Note File Handling); callers that resolve it by name (`roadmap-engine`, `architect-editor-engine`, `docs/philosophy/multiuser-roadmaps.md`) are unaffected.
- Frontmatter untouched (`name`, `description`, `allowed-tools` identical to HEAD); reverse-graph marker sentence intact; body is 126 lines.
- No file on disk renamed or back-filled; `active/skills/note` still symlinks to `src/skills/note`, so the edited file is the one loaded.

**Runtime reasoning.** Applied by hand to `.ai-factory/specs/trickster77777/` (the collision case from the spec): the widened scan sees `126-test-coverage-numbering-joins-the-family-rule.md`, the numeric maximum is 126, the next name is `0127-<slug>.md` — no collision with `100-…`, and the folder-style siblings become `125`/`126` rather than the two-digit stragglers. Applied to an empty destination: `0001-<slug>.md`. Applied to a destination holding `9999-x.md`: no `mkdir -p`, no write, the bound report with the destination named. Mixed-width directories (`06-…` beside `0007-…`) parse to consecutive integers and count together, as the spec requires. The comparison is done by the agent over `ls`/Glob output, which the existing `allowed-tools` grant already covers.

**Style / discipline.** Present tense throughout; no plan-layer citation (no phase number, roadmap, spec, or `.ai-factory/` path in either skill); the reserved vocabulary is unchanged; the one-home-per-fact direction is respected (the scan defined once in the hook, every later site points at it).

Cosmetic only, not a finding: the regex is written as `` `^[0-9]+-.*\.md$` `` (a single-backtick span inside a double-backtick span) at both sites, which renders with the inner backticks visible. The plan spelled it that way and the implementation copied it faithfully; it is harmless to the agent reading the skill and the file already carries the same double-backtick convention on its reverse-graph line.

The caller-side gap already recorded in plan-review-1 and plan-review-2's `## Deferred observations` (`command-handoff` suppresses `note`'s Step 4 report and always emits a paste-back pointer, so at the bound it would point at a file never written) is outside this task's file boundary and is not repeated here as a new entry.

No findings.

REVIEW_PASS
