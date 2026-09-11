# Plan: 36.3 — the rule that no architect reads another's buffer gets a home

## Context
`docs/paired-loop.md` § "What the memory holds, and who holds it" states the isolation rule unconditionally — "Two architects are two heads. No architect reads another's buffer, and an editor reads only its own architect's" — but no skill artifact states it, and the only candidate previously named (`architect-pairing-engine`) loads only in a paired session. This task gives the rule its home in `src/skills/architect-editor-engine/SKILL.md`, the engine both halves load at birth and the home 36.1 gave the buffer's definition, so the rule is resident wherever more than one architect exists.

Ground truth verified fresh: 36.1 (`4eb7b0c`) and 36.2 (`053797a`) are committed; the engine's § "The architect's buffer" exists with path/numbering, the two zones, re-read on change, and the drain rule — the isolation rule is absent there and everywhere else under `src/` (`grep -rn "another's buffer\|two heads\|reads only its own" src/` returns nothing). `architect-pairing-engine` mentions no buffer and is not touched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### State the isolation rule beside the buffer's definition

- [x] **Add the two-clause isolation rule to the engine's buffer section**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In § "The architect's buffer", add one short closing paragraph after the drain-rule paragraph ("A ruling recorded in the buffer is a debt against the skill… no artifact states."), mirroring the governing spec's own placement of the rule at the end of its buffer section. The paragraph carries both clauses, in the engine's own present-tense voice, without narrating the move:
  1. **Architect clause** — several architects may coexist (the numbering above exists for exactly that), and each architect's buffer is its own: no architect reads another architect's buffer.
  2. **Editor clause** — an editor reads only its own architect's buffer, the memory of the head it is the hand of; another architect's buffer is not its working context, settled zone included.
  State the reason in one clause, the way the rest of the section does (e.g. two architects are two heads, and a head that reads another's memory is no longer holding its own). Keep it to one paragraph of two or three sentences — this engine is loaded on every paired-loop birth, so every line is recurring context cost. Do not restate the two-zone split, the re-read rule, or the drain rule; do not mention pairing roles, `architect-pairing-engine`, `docs/paired-loop.md`, or any task/phase number (comments and skill text never cite the plan layer).

- [x] **Extend the `description:` enumeration by the new clause** (same file, same pass)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  The frontmatter `description:` enumerates the buffer definition's contents exhaustively after a colon ("its path and numbering, its settled zone …, the editor's re-read …, and the drain rule that a ruling leaves the buffer once it reaches the artifact that should hold it"). The body now holds a fifth element, so the always-loaded skill description must name it or it misdescribes its own load. Append one short clause to that enumeration, before "When-to-use policy stays with the caller." — e.g. "…and the drain rule that a ruling leaves the buffer once it reaches the artifact that should hold it, and the rule that no architect reads another's buffer and an editor reads only its own architect's." Keep the YAML `>-` folded-block form and re-wrap lines to match the existing width; the description is ~712 characters today and must stay ≤ 1024 after the addition. Change nothing else in the frontmatter.

  Leave untouched: the load instruction, § "The two channel-message formats", § "The mode rule", `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`, `src/skills/architect-pairing-engine/SKILL.md`, and `docs/paired-loop.md` (it is the governing spec — the engine implements it; nothing there changes).

- [x] **Verify the rule now has exactly one home under `src/`** (depends on the two tasks above)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Re-read the edited section in full to confirm it reads as one continuous account (path/numbering → zones → re-read → drain → isolation) and that both clauses are present in the body and named in the description. Run `grep -rn "another" src/skills/architect-editor-engine/SKILL.md src/skills/architect-pairing-engine/SKILL.md src/skills/agent-architect/SKILL.md src/agents/editor.md` and confirm the isolation rule appears only in the engine (description and body). Check the description length stays ≤ 1024 characters (e.g. `awk '/^description:/,/^user-invocable:/' src/skills/architect-editor-engine/SKILL.md | wc -c`). Confirm `git status` shows `src/skills/architect-editor-engine/SKILL.md` as the only *modified tracked* file — the untracked plan and plan-review artifacts under `.ai-factory/` are expected and not part of this change.
