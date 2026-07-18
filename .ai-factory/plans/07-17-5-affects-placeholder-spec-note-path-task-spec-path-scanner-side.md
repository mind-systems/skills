# Plan: 17.5 — `- Affects:` placeholder: `spec-note path` → `task-spec path` (scanner side)

## Context
Retires the last surviving `spec-note` synonym in `orchestrator-artifacts` by renaming one field in the deferred-observations entry placeholder, closing the lockstep pair whose emitter half already landed in the orchestrator repo (commit `8f34644`, `reviewer.md:108` reads `task-spec path`).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rename the field

- [x] **Task 0: Grep the engine's callers before touching it**
  Files: read-only — `src/skills/*/SKILL.md`, `src/commands/*.md`
  `orchestrator-artifacts` is an engine; `skills/CLAUDE.md` § "Dependencies and the skill graph" requires grepping its callers before an edit, because their expectations are part of its contract. Run `grep -rn 'Affects:' src/skills/ src/commands/ docs/` and confirm no caller depends on the placeholder's inner field text. Expected result (already verified during review): `task-rescue-audit` and `roadmap-prune` reference `Affects:` only as a target field name, and `docs/using-the-language.md` names the token as `- Affects: …` with the placeholder elided — none of them reads `spec-note path`. If any caller does depend on the inner field, stop and report rather than proceeding.

- [x] **Task 1: Replace `spec-note path` with `task-spec path` in the entry placeholder** (depends on Task 0)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Section 5 (`## Deferred observations` section) documents the entry on lines 55–56, wrapped mid-placeholder:
  ``Present in both review genres. Entry: `- Affects: <phase / spec-note path /`` / ``"unknown"> — <observation>``. Change the single field `spec-note path` → `task-spec path` on line 55. Nothing else on that line or anywhere else in the file changes — the wrap point stays where it is — both strings are exactly 14 bytes, so the column count of line 55 is unchanged; do not reflow the paragraph.
  Hard guards, per the task spec:
  - The scanned literals stay byte-identical: the `## Deferred observations` heading (both occurrences — the section header at line 53 and the description prose) and the `- Affects: ` prefix.
  - The tail stays `— <observation>` — here it is a format description; the emitter's `— <one-paragraph observation>` is a length instruction to the reviewer. The per-side difference is recorded in both specs, not drift. Do not "harmonize" it.
  - Do not touch the frontmatter (`description:`, `allowed-tools:`), the reverse-graph marker in the body header, the `[fixed]` / `[routed → <path>]` / `[dismissed]` marker literals, the legacy-marker list, PASS-signal literals, or any other protocol token.
  This is the sanctioned unfreeze of exactly one field frozen by task 17.1; it is not a licence to re-edit the rest of the file.

- [x] **Task 2: Verify the edit** (depends on Task 1)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Run and confirm:
  - `grep -n 'task-spec path' src/skills/orchestrator-artifacts/SKILL.md` → line 55 only.
  - `rg -in 'spec-note' src/skills/orchestrator-artifacts/SKILL.md` → zero matches.
  - `grep -c '## Deferred observations' src/skills/orchestrator-artifacts/SKILL.md` → 2, unchanged.
  - `git diff` on the file → exactly one changed line, the only delta being `spec-note` → `task-spec`.
  If any check disagrees, correct the edit rather than adjusting the check.
