# roadmap-decompose: slim to philosophy-only; delegate maintenance flow to roadmap-engine

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- Depends on note 43 (engine gains the shared maintenance flow) being implemented first. Also presumes notes 36 (stale references removed) and 38 (inline format duplication removed) have landed — do not reintroduce what they removed.
- After the engine absorbs the flow, `src/skills/roadmap-decompose/SKILL.md` keeps only its **philosophy**: everything that makes decompose *decompose* rather than any roadmap maintainer. The duplicated flow text (Step 0, modes 1/2/3 machinery, dialogs, check scan, shared critical rules) is deleted and replaced with "ensure `roadmap-engine` is loaded once this chat and run its maintenance flow with the hooks below".

## Details

What stays (the philosophy):

- **Granularity:** each entry is one atomic task — one file boundary, one concern, one reason to revert; the two-tier discipline statement (contract line + spec note, never a full spec inline).
- **The Atomicity Gate** — stated once (not twice as today): after drafting each entry's full spec, before its contract line — "can the first half be deployed without the second half and still make sense?"; split recursively; "make sense" = compiles, breaks nothing, delivers independently observable value. Registered as the engine flow's per-entry gate hook.
- **Target-file routing** (policy): default `ROADMAP.md`; explicit filename argument wins; test-context keywords (test/tests/spec/testing/тест/тесты) → `ROADMAP_TESTS.md`.
- **Decompose-specific update action** — "Decompose existing": expand a vague milestone into a full spec, with the existing note-handling rule (existing `Spec:` tag → update note in place, tag unchanged; legacy inline → new note + add tag; offer split when 2+ concerns; no bulk migration of untouched legacy tasks).
- Philosophy-tier critical rules: atomic and specific; two-tier always; plans only — the orchestrator implements (post-36 wording).

What goes: all text now covered by the engine's flow section (modes, dialogs, exploration, draft-in-memory/confirmation, check mode, progress review, reprioritize, summary blocks, mechanism-tier critical rules).

Expected size: roughly 60–100 lines. Frontmatter unchanged except nothing needed. Verify against the engine's hook list — every hook decompose needs must be explicitly supplied.

## What NOT to do

- Do not change any behavior — a user invoking `/roadmap-decompose` in any mode must get the same interaction as today, with the flow text coming from the engine.
- Do not restate engine flow or format content inline "for convenience".
- Do not drop the load-once discipline sentence — the engine is loaded once per session and reused if already in context.
