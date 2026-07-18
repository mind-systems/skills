# Engines: one dictionary in note, roadmap-engine, test-philosophy, orchestrator-artifacts

Task 17.1 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). The contract is naming-only — reserved is the meaning, not the spelling — so what conforms is word choice: synonyms for registry concepts are retired, and spellings that are neither registry nor ordinary English are normalized. Attributive compounds ("two-tier entry", "named-roadmap resolution order") are legal English hyphens and stay; noun uses are unhyphenated ("a task spec", "a silent failure"). Zero behavior change.

## Current state — per-file inventory (line numbers from the 2026-07-13 grep; re-verify by grep before editing)

**`note` (118 lines)** — no synonym tokens. Genre-neutral distiller; its own vocabulary ("research notes / task specs / handoffs") is already fine. **Audit-clean → no change**; certified as the deepest trunk.

**`roadmap-engine` (315 lines)**:
- `spec note` → **`task spec`**: **seven** sites — lines 5, **16–17** (wrapped across the line break: `spec` ends 16, `note` opens 17 — invisible to a single-line grep, and the one site where the substitution itself spans the break), 28, 69, 103, 105, 209. Line 5 is the `description:` field — the always-loaded surface, in scope. Line 69 is plural.
- Bare artifact-`note`/`notes` → **`task spec`**: eight sites — 33 (phrase wraps 32–33), 36, 43, 47, 75 (phrase wraps 74–75; the substitution falls wholly on 75 — line 74 carries the named-roadmap path template and stays byte-identical), 212, 213, 214 — the same artifact under a second name is the drift the contract forbids. **Stay byte-identical:** every backticked `` `note` `` (the skill name), `loads: note` (11), "written via note" in the description (5), both `` `<note pending>` `` placeholders (190, 210 — protocol axis).
- `roadmap line` → **`contract line`**: line 105 (the same bullet as its `spec note`, inside the section headed "Rules for writing a contract line" — the file teaches the term and mis-names it in one list).
- `milestone` → **`task`**: line 104 ("make two milestones" = make two tasks; roadmap-engine's unit is the task-tier entry).
- **email**: line 57 `kg.wmservice@gmail.com` → `john.doe@example.com`; line 58 `kg-wmservice` → `john-doe` ([handoff 18](../../.ai-factory/handoffs/18-canonical-example-email-is-a-real-address.md)).
- **Already conformant, leave**: `contract line`, `named roadmap`, `owner line`, "Two-Tier" in the H1 heading (title case is ordinary English), "two tiers" prose (line 42), generic "fields" (line 99).

**`test-philosophy` (53 lines)**:
- Prose casing: `Silent-Failure` (lines 14, 25), `Loud-failure` (line 41) → ordinary English per grammatical position — noun "silent failure" / "loud failure", attributive "silent-failure surface"; capitalized only at a sentence start or in a heading. **All three sit in exonerating positions** (14 is the H1, 25 an H2, 41 sentence-initial attributive) — expected outcome: **no change**; judge by the rule, do not manufacture an edit to satisfy this inventory.
- **Leave**: "field" (line 35 — generic, "Mapper with wrong field type").

**`orchestrator-artifacts` (84 lines)**:
- `spec note` → **`task spec`**: line 68 — a literal substitution yields the clumsy "an open task's task spec"; reword to "the task spec of an open task" (naming binds, phrasing is ordinary English).
- `roadmap line` → **`contract line`**: line 31 ("recoverable from a roadmap line" — the string sits entirely on 31; no wrap).
- `milestone` (the processed unit) → **`task`**: lines 49 ("a milestone's artifacts together with the milestone" → a task's… the task), 73 ("that milestone's" → that task's; the phrase wraps 73–74 but the substitution falls wholly on 73).
- **email**: lines 28, 29 `kg-wmservice` → `john-doe`.
- **Already conformant, leave**: `PASS signal` prose (line 5), the literal `## Deferred observations` heading (lines 5, 53 — protocol token, see Guards), `named roadmap` (line 27), generic "fields"/"field" (lines 5, 41, 58).

## Change

Retire the synonyms and normalize the odd casing listed above; swap the example email. Behavior byte-identical — this is the outward vocabulary, not the mechanism.

## Files & types

`src/skills/{note,roadmap-engine,test-philosophy,orchestrator-artifacts}/SKILL.md`. Frontmatter `name` / `loads:` / `allowed-tools` untouched; each engine's reverse-graph marker sentence byte-identical; no `references/` or `scripts/` touched.

## Guards

- **Skill names were Phase 16's, and it has landed.** `orchestrator-artifacts` lines 7 and 44 already read `task-rescue` / `task-rescue-audit` (16.1 `[x]`); the file carries `milestone` only at lines 49 and 73, both in scope here — no skill-name exemption remains.
- **`loads:` edges + reverse-graph markers byte-identical.** The dependency graph and the "load-once engine, callers found by grep" marker in each body are not touched.
- **Tags stay legacy.** The on-disk `` Spec: `` tag, a `Governing spec:` header tag, and the `.ai-factory/specs/` directory are structural — never renamed (tag ≠ reserved word).
- **Protocol literals stay (cross-repo shared surface).** The literal heading `## Deferred observations` and the entry line `- Affects: …` are a joint protocol the orchestrator's `reviewer.md` **emits** and this skill **scans** — same class as the `PLAN_REVIEW_PASS` / `REVIEW_PASS` literals. Byte-identical; a one-sided rewrite silently breaks the scan (see [handoff 21](../handoffs/21-review-file-protocol-is-shared-conform-in-lockstep.md)).
- **Spelling is ordinary English, not a token grammar.** Hyphens in attributive compounds stay; capitals at sentence starts and in headings stay. Only spellings that are neither registry-plain nor grammatical English (mid-prose `Silent-Failure`) are normalized.
- **Generic `field`/`fields` left.** Every occurrence above is a data-field, not the skill description field.
- **Behavior baseline:** a live run of a caller that renders through `roadmap-engine` (e.g. a `roadmap-decompose` pass) must produce the same two-tier artifact shape pre/post — a rename that changes output is a bug, not a conformance.
- **`note` lands no change** — verify zero tokens first; its inclusion is a certification, not an edit.

## Verification

- `rg -U -in 'spec\s+notes?' src/skills/{note,roadmap-engine,test-philosophy,orchestrator-artifacts}/SKILL.md` → zero (multiline-tolerant and case-insensitive — a single-line form returns zero over the live wrap at `roadmap-engine:16–17`; the hyphenated `spec-note path` at `orchestrator-artifacts:55` is correctly not matched — that field is 17.5's).
- `rg -U -in 'the\s+note\b' src/skills/roadmap-engine/SKILL.md` → zero; `rg -U -in '\bnotes?\b' src/skills/roadmap-engine/SKILL.md` → every hit is one of the four legal residue classes (backticked skill name, `loads: note`, "written via note", `` `<note pending>` ``) and none is the artifact noun — verify by class, line numbers shift with the edits.
- `rg -U -in 'roadmap\s+lines?' src/skills/{roadmap-engine,orchestrator-artifacts}/SKILL.md` → zero (scoped to these two files — `roadmap-prune` is 17.3's).
- `grep -in 'kg.wmservice\|kg-wmservice' src/skills/{roadmap-engine,orchestrator-artifacts}/SKILL.md` → zero, and the new slug reads `john-doe` — arithmetically true to the derivation rule stated in the same sentence.
- `grep -inE '[^-]milestone' src/skills/orchestrator-artifacts/SKILL.md` → **zero** (16.1 landed; the former skill-name exemption no longer applies).
- `grep -inE 'Silent-Failure|Loud-failure' src/skills/test-philosophy/SKILL.md` → zero mid-prose (sentence-start/heading capitals legal).
- `grep -c '## Deferred observations' src/skills/orchestrator-artifacts/SKILL.md` → unchanged pre/post.
- Diff each engine's `loads:` line and reverse-graph marker sentence pre/post → byte-identical.
- Behavior baseline: a live `roadmap-decompose` render is not headlessly runnable (`roadmap-engine` drives `AskUserQuestion` at 164–182 and 196–206, and a real render writes stray files into `.ai-factory/`). The gate is **static byte-identity** pre/post of: the `## Roadmap File Format` block, the `Spec:` tag literal (34), both `` `<note pending>` `` placeholders (190, 210), and the spec-path templates as literals wherever they appear — flat `` `.ai-factory/specs/<NN>-<slug>.md` `` and the named-roadmap form at line 74. A live render against a scratch target outside `.ai-factory/` confirms, never gates.
