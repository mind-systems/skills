# Code Review: `loads:` convention — declared, colocated skill dependencies

**Plan:** `24-loads-convention-declared-colocated-skill-dependencies-graph-derived-by-grep.md`
**Scope of changes:** 5 skill frontmatter edits, 1 sentence in `milestone-rescue`, 1 CLAUDE.md subsection, ROADMAP bookkeeping. No executable code — all Markdown/YAML frontmatter and prose.

## What was verified

**Edge accuracy (Task 1) — every declared edge matches a real body load instruction:**

- `roadmap-outline` → `roadmap-engine`: body load instructions at SKILL.md:76 and :147 ("Ensure `roadmap-engine` is loaded once this chat via the `Skill` tool"). ✓
- `roadmap-decompose` → `roadmap-engine`: caller confirmed, `Skill` in allowed-tools. ✓
- `roadmap-decompose-skeleton` → `roadmap-engine test-philosophy`: both mentioned/loaded; matches its existing "Call graph" body section. ✓
- `roadmap-test-coverage` → `test-philosophy`: body load at SKILL.md:65 ("Load `test-philosophy` once via the `Skill` tool"). ✓
- `roadmap-engine` → `note`: body load at SKILL.md:30 ("load `note` once per chat via the Skill tool"). The engine has `allowed-tools: Read` (no `Skill`) because the *caller* executes the load — declaring its own forward dependency is correct and does not breach caller-agnosticism. ✓

**Edge completeness (Task 2) — cross-checked callers against declarations:**

- Callers of `roadmap-engine` (excluding self): `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton` — all three declare it. ✓
- Callers of `test-philosophy` (excluding self): `roadmap-decompose-skeleton`, `roadmap-test-coverage` — both declare it. ✓
- Skills with `Skill` in `allowed-tools` are exactly the four philosophy skills, all of which now carry `loads:`. No skill that loads another is missing a declaration.
- No reverse-edge / `loaded-by:` field was introduced anywhere. `test-philosophy` and `note` (leaf engines) correctly have no `loads:` field.
- `command-handoff.md`'s `/note` reference is an explicit **do-not-route** instruction (":110"), not a load — correctly excluded. `ui-ux-pro-max`'s only `Skill` hit is a body heading — correctly excluded.

**Both-ends invariant (Task 3):** The added sentence in `milestone-rescue/SKILL.md:121-122` ("This narrative register is shared with `milestone-rescue-audit`'s output — change it in both files or neither") correctly closes the previously one-sided coupling; the audit end (`:145-146`) already declared it. `milestone-rescue-audit` was left untouched as specified. No other rescue body/frontmatter/sidecar changes — behavior-identical constraint honored.

**CLAUDE.md subsection (Task 4):** Added as a sibling `###` under `## Skill Authoring`, after "Composition — mechanism vs policy". Lean (~20 lines), covers convention, forward/reverse derivation, both-ends invariants, and all five editing rules. Contains no static map, no generated-graph script, no `loaded-by:` list — the rejected cache-without-invalidation design is avoided.

## Correctness / runtime considerations

- **YAML validity:** each `loads:` value is a plain space-separated scalar, identical in shape to the existing `allowed-tools:` line — parses cleanly, no quoting needed. Insertion points sit among existing top-level keys; no indentation or block-structure issues.
- **No runtime hazard:** unknown frontmatter keys are ignored by the harness (already demonstrated by coexisting `disable-model-invocation`/`user-invocable` keys), so `loads:` is inert metadata — nothing to break at load time, no migration, no type surface.
- **ROADMAP `---STOP---` shift:** the marker now sits directly below the in-flight `loads:` milestone — standard orchestrator bookkeeping (the current task sits above STOP), not a defect. The task line itself is unchanged and there is no duplicate/orphaned marker.

## Notes (non-blocking)

- `roadmap-engine`'s *description* still reads "Currently loaded by roadmap-decompose" — stale caller-naming, but explicitly out of scope here and already owned by a later roadmap task (engine caller-boundary cleanup, note 38). Not introduced by this change.

The implementation matches the plan exactly, the declared graph is provably accurate and complete against the actual body load instructions, and there is no executable surface to break.

REVIEW_PASS
