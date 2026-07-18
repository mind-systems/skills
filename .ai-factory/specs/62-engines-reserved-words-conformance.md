# Engines: one dictionary in note, roadmap-engine, test-philosophy, orchestrator-artifacts

Task 17.1 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). The contract is naming-only — reserved is the meaning, not the spelling — so what conforms is word choice: synonyms for registry concepts are retired, and spellings that are neither registry nor ordinary English are normalized. Attributive compounds ("two-tier entry", "named-roadmap resolution order") are legal English hyphens and stay; noun uses are unhyphenated ("a task spec", "a silent failure"). Zero behavior change.

## Current state — per-file inventory (line numbers from the 2026-07-13 grep; re-verify by grep before editing)

**`note` (118 lines)** — no synonym tokens. Genre-neutral distiller; its own vocabulary ("research notes / task specs / handoffs") is already fine. **Audit-clean → no change**; certified as the deepest trunk.

**`roadmap-engine` (315 lines)**:
- `spec note` → **`task spec`**: lines 5, 28, 69, 103, 105, 209 (a synonym — the registry concept is task spec).
- `milestone` → **`task`**: line 104 ("make two milestones" = make two tasks; roadmap-engine's unit is the task-tier entry).
- **email**: line 57 `kg.wmservice@gmail.com` → `john.doe@example.com`; line 58 `kg-wmservice` → `john-doe` ([handoff 18](../../.ai-factory/handoffs/18-canonical-example-email-is-a-real-address.md)).
- **Already conformant, leave**: `contract line`, `named roadmap`, `owner line`, "Two-Tier" in the H1 heading (title case is ordinary English), "two tiers" prose (line 42), generic "fields" (line 99).

**`test-philosophy` (53 lines)**:
- Prose casing: `Silent-Failure` (lines 14, 25), `Loud-failure` (line 41) → ordinary English per grammatical position — noun "silent failure" / "loud failure", attributive "silent-failure surface"; capitalized only at a sentence start or in a heading.
- **Leave**: "field" (line 35 — generic, "Mapper with wrong field type").

**`orchestrator-artifacts` (84 lines)**:
- `spec note` → **`task spec`**: line 68.
- `milestone` (the processed unit) → **`task`**: lines 49 ("a milestone's artifacts together with the milestone" → a task's… the task), 73 ("that milestone's" → that task's).
- **email**: lines 28, 29 `kg-wmservice` → `john-doe`.
- **Already conformant, leave**: `PASS signal` prose (line 5), the literal `## Deferred observations` heading (lines 5, 53 — protocol token, see Guards), `named roadmap` (line 27), generic "fields"/"field" (lines 5, 41, 58).

## Change

Retire the synonyms and normalize the odd casing listed above; swap the example email. Behavior byte-identical — this is the outward vocabulary, not the mechanism.

## Files & types

`src/skills/{note,roadmap-engine,test-philosophy,orchestrator-artifacts}/SKILL.md`. Frontmatter `name` / `loads:` / `allowed-tools` untouched; each engine's reverse-graph marker sentence byte-identical; no `references/` or `scripts/` touched.

## Guards

- **Skill names are not renamed in this task.** In `orchestrator-artifacts` lines 7 and 44 the string "milestone" is inside the skill names `milestone-rescue` / `milestone-rescue-audit` — **leave them here**: Phase 16 renames those two skills and updates this reference in its own pass.
- **`loads:` edges + reverse-graph markers byte-identical.** The dependency graph and the "load-once engine, callers found by grep" marker in each body are not touched.
- **Tags stay legacy.** The on-disk `` Spec: `` tag, a `Governing spec:` header tag, and the `.ai-factory/specs/` directory are structural — never renamed (tag ≠ reserved word).
- **Protocol literals stay (cross-repo shared surface).** The literal heading `## Deferred observations` and the entry line `- Affects: …` are a joint protocol the orchestrator's `reviewer.md` **emits** and this skill **scans** — same class as the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals. Byte-identical; a one-sided rewrite silently breaks the scan (see [handoff 21](../handoffs/21-review-file-protocol-is-shared-conform-in-lockstep.md)).
- **Spelling is ordinary English, not a token grammar.** Hyphens in attributive compounds stay; capitals at sentence starts and in headings stay. Only spellings that are neither registry-plain nor grammatical English (mid-prose `Silent-Failure`) are normalized.
- **Generic `field`/`fields` left.** Every occurrence above is a data-field, not the skill description field.
- **Behavior baseline:** a live run of a caller that renders through `roadmap-engine` (e.g. a `roadmap-decompose` pass) must produce the same two-tier artifact shape pre/post — a rename that changes output is a bug, not a conformance.
- **`note` lands no change** — verify zero tokens first; its inclusion is a certification, not an edit.

## Verification

- `grep -in 'spec note' src/skills/{note,roadmap-engine,test-philosophy,orchestrator-artifacts}/SKILL.md` → zero.
- `grep -in 'kg.wmservice\|kg-wmservice' src/skills/{roadmap-engine,orchestrator-artifacts}/SKILL.md` → zero.
- `grep -inE '[^-]milestone' src/skills/orchestrator-artifacts/SKILL.md` → only the skill names `milestone-rescue` / `milestone-rescue-audit` (until Phase 16 lands).
- `grep -inE 'Silent-Failure|Loud-failure' src/skills/test-philosophy/SKILL.md` → zero mid-prose (sentence-start/heading capitals legal).
- `grep -c '## Deferred observations' src/skills/orchestrator-artifacts/SKILL.md` → unchanged pre/post.
- Diff each engine's `loads:` line and reverse-graph marker sentence pre/post → byte-identical.
- Live caller run (a `roadmap-decompose` render through `roadmap-engine`) → same two-tier artifact.
