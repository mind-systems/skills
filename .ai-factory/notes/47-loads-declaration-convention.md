# `loads:` frontmatter convention: declared, colocated skill dependencies; graph derived by grep

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- Skill-to-skill dependencies ("ensure `roadmap-engine` is loaded once this chat") exist only as prose inside SKILL.md bodies — invisible to the orchestrator, which in a normal codebase recovers the whole picture from imports by grep. A hand-maintained central map in CLAUDE.md was considered and rejected: it is a cache without invalidation — every future task would have to remember to update it, and it would go stale silently.
- The fix mirrors how programming languages solved this: make the dependency **syntactic and colocated** (declared in the depending skill's own frontmatter), and **derive** the whole-picture graph on demand by grep. Changing a load and updating its declaration are edits to the same file — forgetting is structurally hard.
- Direction is one-way, preserving the caller-agnostic engine principle (note 38): callers declare what they load; engines never list who loads them. The reverse graph is derived: `grep -l "<name>" src/skills/*/SKILL.md src/commands/*.md`.
- Cross-file invariants that no grep can derive (shared output register of `milestone-rescue`/`milestone-rescue-audit`; rescue's sidecar `step` table mirroring the orchestrator's `_validate_sidecar_step()`) are declared **at the coupling point in both files**, so anyone editing either end sees the leash.

## Details

### Edit 1 — frontmatter declarations

Add a top-level `loads:` frontmatter field (space-separated skill names; unknown frontmatter fields are ignored by the harness, so this is safe) to every skill/command that loads another via the Skill tool:

- `src/skills/roadmap-outline/SKILL.md` → `loads: roadmap-engine`
- `src/skills/roadmap-decompose/SKILL.md` → `loads: roadmap-engine`
- `src/skills/roadmap-decompose-skeleton/SKILL.md` → `loads: roadmap-engine test-philosophy`
- `src/skills/roadmap-test-coverage/SKILL.md` → `loads: test-philosophy`
- `src/skills/roadmap-engine/SKILL.md` → `loads: note` (the engine is a *caller* of `note` — declaring its own dependency does not violate caller-agnosticism, which only forbids knowing one's callers)

Verify completeness by grepping `src/skills/*/SKILL.md` and `src/commands/*.md` for Skill-tool load instructions and `Skill` in allowed-tools; declare every found edge, none invented. Skills that load nothing get no `loads:` field.

`roadmap-decompose-skeleton`'s existing "Call graph" body section stays (it is colocated and correct) — just verify it matches its new `loads:` line.

### Edit 2 — both-ends declaration of cross-file invariants

- `milestone-rescue-audit` already references "the same register as `milestone-rescue`'s Diagnosis Report" — the audit end is done.
- Add the missing rescue end: one sentence in `milestone-rescue`'s Diagnosis Report spec noting the register is shared with `milestone-rescue-audit` (change it in both or neither). The sidecar `step` table's mirror note already exists in rescue — no change there.

### Edit 3 — CLAUDE.md convention section (no static map)

Add a compact subsection under "Skill Authoring" — "Dependencies and the skill graph":

- Dependencies are declared in the depending skill's frontmatter `loads:` field; engines never list their callers.
- Forward graph: read `loads:` fields. Reverse graph: `grep -l "<name>" src/skills/*/SKILL.md src/commands/*.md`. There is no central map to maintain — the declarations are the map.
- Cross-file invariants (shared output registers, mirrored tables) are declared at the coupling point in **both** files.
- Editing rules: before editing an engine, grep for its callers — their expectations are part of its contract; never inline engine content into a philosophy; "behavior-identical" / "word-for-word" in spec notes are contract text — the only type system this code has; a skill's output register is behavior, never "simplify" a prose-narrative requirement into tables; a refactored skill is unverified until a live run compares its output. Pointers: `docs/skill-composition-model.md` (semantics), `docs/workflow.md` (pipeline order).

Keep the whole subsection lean (~25 lines) — CLAUDE.md is loaded every session; every line is a recurring cost.

### Constraints

- Engines gain no caller knowledge anywhere (note 38 holds).
- No body behavior changes in any skill — frontmatter lines, one both-ends invariant sentence in rescue, and the CLAUDE.md subsection only.
- Do not create a generated-map script or a static graph document.

## What NOT to do

- Do not add a `loaded-by:` or any reverse-edge field — reverse edges are derived by grep, never declared.
- Do not write a static dependency map into CLAUDE.md, AGENTS.md, or any doc — that is the rejected cache-without-invalidation design.
- Do not add "update the graph" obligations to other tasks' notes — colocation is the whole point.
