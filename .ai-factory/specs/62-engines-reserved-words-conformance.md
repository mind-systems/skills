# Engines: conform note, roadmap-engine, test-philosophy, orchestrator-artifacts to the reserved-words contract

Phase 9 of the Language-integration direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Vocabulary-only: rename the reserved-word tokens in the four engine bodies to their canonical form, zero behavior change.

## Current state — per-file token inventory (grep, 2026-07-13)

**`note` (118 lines)** — no reserved-word tokens. Genre-neutral distiller; its own vocabulary ("research notes / task specs / handoffs") is already fine. **Audit-clean → no change**; certified as the deepest trunk.

**`roadmap-engine` (315 lines)** — the heavy one:
- `spec note` → **`task-spec`**: lines 5, 28, 69, 103, 105, 209.
- `contract line` → **`contract-line`**: lines 5, 16, 27, 32, 33, 42, 46, 72, 98, 134, 192, 193, 243.
- `two-tier` casing/spacing: line 14 heading "Two-Tier" → lowercase `two-tier`. Line 42 "two tiers" is **prose** (the two levels) — leave. The rest are already `two-tier`.
- `named roadmap` → **`named-roadmap`**: lines 49 ("Named roadmap" heading), 60, 65, 72, 138.
- `owner line` → **`owner-line`**: lines 60 ("Owner line"), 67.
- `milestone` → **`task`**: line 104 ("make two milestones" = make two tasks; roadmap-engine's unit is the task-tier entry).
- **email**: line 57 `kg.wmservice@gmail.com` → `john.doe@example.com`; line 58 `kg-wmservice` → `john-doe`.
- Leave: "fields" (line 99 — generic, "files, methods, types, or fields").

**`test-philosophy` (53 lines)**:
- casing → lowercase `silent-failure` / `loud-failure`: line 14 "Silent-Failure", line 25 "Silent-Failure", line 41 "Loud-failure" (line 41's "silent-failure" already ok).
- Leave: "field" (line 35 — generic, "Mapper with wrong field type").

**`orchestrator-artifacts` (84 lines)**:
- `spec note` → **`task-spec`**: line 68.
- `PASS signal` → **`PASS-signal`**: line 5.
- `Deferred observations` → **`deferred-observations`**: lines 5, 53.
- `named roadmap` → **`named-roadmap`**: line 27.
- `milestone` (the processed unit) → **`task`**: lines 49 ("a milestone's artifacts together with the milestone" → a task's… the task), 73 ("that milestone's" → that task's).
- **email**: lines 28, 29 `kg-wmservice` → `john-doe`.
- Leave: "fields"/"field" (lines 5, 41, 58 — generic, marker columns).

## Change

Rename each token above to its canonical reserved-word form per `reserved-words.md`. Behavior byte-identical — this is the outward vocabulary, not the mechanism.

## Files & types

`src/skills/{note,roadmap-engine,test-philosophy,orchestrator-artifacts}/SKILL.md`. Frontmatter `name` / `loads:` / `allowed-tools` untouched; each engine's reverse-graph marker sentence byte-identical; no `references/` or `scripts/` touched.

## Guards

- **Skill names are not renamed in this phase.** `roadmap-prune`, `roadmap-engine`, etc. stay exactly; only the bare word `milestone` denoting the roadmap unit → `task`. In `orchestrator-artifacts` lines 7 and 44 the string "milestone" is inside the skill names `milestone-rescue` / `milestone-rescue-audit` — **leave them here**: Phase 11 renames those two skills to `task-rescue` / `task-rescue-audit` and updates this reference in the same pass.
- **`loads:` edges + reverse-graph markers byte-identical.** This task is vocabulary-only; the dependency graph (`loads: note`, `loads: orchestrator-artifacts roadmap-engine`, etc.) and the "load-once engine, callers found by grep" marker in each body are not touched.
- **Tags stay legacy.** The on-disk `` Spec: `` tag, a `Governing spec:` header tag, and the `.ai-factory/specs/` directory are structural — never renamed (tag ≠ reserved word).
- **Generic `field`/`fields` left.** Every `field`/`fields` occurrence above is a data-field, not the `skill-description-field` reserved word.
- **Casing:** reserved words are lowercase kebab even in a heading or at sentence start (`two-tier`, `silent-failure`, `named-roadmap`, `owner-line`) — consistent with the docs sweep already committed.
- **Behavior-baseline:** each engine's behavior byte-identical. A live run of a caller that renders through `roadmap-engine` (e.g. a `roadmap-decompose` pass) must produce the same two-tier artifact shape pre/post — a rename that changes output is a bug, not a conformance.
- **`note` lands no change** — verify zero tokens first; its inclusion is a certification, not an edit.

## Verification

- `grep -inE 'spec note|contract line|PASS signal|deferred observ|owner line|named roadmap' src/skills/{note,roadmap-engine,test-philosophy,orchestrator-artifacts}/SKILL.md` → zero.
- `grep -in 'kg.wmservice\|kg-wmservice' src/skills/{roadmap-engine,orchestrator-artifacts}/SKILL.md` → zero.
- `grep -inE '[^-]milestone' src/skills/orchestrator-artifacts/SKILL.md` → only the skill names `milestone-rescue` / `milestone-rescue-audit`.
- `grep -inE 'Silent-Failure|Loud-failure|Two-Tier' src/skills/{test-philosophy,roadmap-engine}/SKILL.md` → zero (all lowercased).
- Diff each engine's `loads:` line and reverse-graph marker sentence pre/post → byte-identical.
- Live caller run (a `roadmap-decompose` render through `roadmap-engine`) → same two-tier artifact.
