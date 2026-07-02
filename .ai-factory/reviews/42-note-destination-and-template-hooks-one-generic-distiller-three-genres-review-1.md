# Code Review — note: destination and template hooks

**Scope reviewed:** `git diff HEAD` — the only product change is `src/skills/note/SKILL.md`. The other staged files are planning/handoff artifacts (`.ai-factory/handoffs/04-*`, `.ai-factory/plan-reviews/42-*`, `.ai-factory/plans/42-*.json`, `.ai-factory/plans/42-*.md`) with no runtime effect; not part of the code change.

The `note` skill is an instruction file the agent executes, so "correctness" here means: does the reworked prose produce the same behavior as before when the new hooks are unset, and correct behavior when they are set.

## Verification against the hard invariant (byte-identical unset behavior)

Spec note 53 and the plan require standalone `/note` with no caller inputs to remain byte-identical to today. Confirmed on every axis:

- **Destination** — `<destination>` defaults to `.ai-factory/notes/`, stated in Step 3, Step 4, and Note File Handling. The default is unchanged, so lazy migration is preserved.
- **Template** — the default template block (Key Findings / Details / Open Questions, with `# <Topic Title>`, `**Date:**`, `**Source:**`) is carried over verbatim inside the code fence. Unset case explicitly routes to it.
- **Numbering** — the rule ("highest existing `NN` prefix among files matching `[0-9][0-9]-*.md` … add 1; if none, start at `01`") is preserved word-for-word, with only the scanned directory abstracted to `<destination>` (which resolves to `.ai-factory/notes/`). Per-directory scoping is stated in both Step 3 and Note File Handling.
- **Report** — resolves to `Note saved: .ai-factory/notes/<NN>-<slug>.md` when unset.

## Other checks

- **Frontmatter** — `name: note` unchanged (matches directory), `argument-hint: "[topic-slug]"` still quoted, `user-invocable: true` and `disable-model-invocation: false` retained per spec. New `description` is ~430 chars, well under the 1024 limit.
- **allowed-tools** — unchanged (`Read Write Bash(ls *) Bash(mkdir *) Glob`); still covers the placeholderized `mkdir -p <destination>` and the ls/glob numbering scan.
- **Placeholder convention** — `<destination>` is introduced and defined the same way the file already uses `<NN>` and `<slug>`; low risk of literal interpretation because Step 3 defines it explicitly as "the destination-directory hook … defaulting to `.ai-factory/notes/` when unset".
- **Scope discipline** — no caller (`roadmap-engine`, `command-handoff`) touched; no genre-specific content leaked into the engine; no rename; load-once discipline unaffected. Matches the plan's "Notes for the implementer" constraints exactly.

## Findings

None. The change faithfully implements the three planned edits, preserves the byte-identical unset invariant, and introduces no correctness, security, or runtime issues.

REVIEW_PASS
