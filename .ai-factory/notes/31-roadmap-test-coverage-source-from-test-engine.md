# test-philosophy: rename from test-engine + separate philosophy from algorithm

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- `test-engine` is a **misnomer**. What was extracted from `roadmap-test-coverage` is a **philosophy** — "test only what fails silently, skip what fails loudly" — not an engine. Unlike the roadmap family (where `roadmap-decompose`'s artifact format is a genuine shared mechanism), the test family has **no shared algorithm-engine**: `roadmap-test-coverage`'s 8-layer pipeline is its own algorithm and is not shared. The "engine" analogy was forced.
- Rename the skill `test-engine` → `test-philosophy`. Its consumers (`roadmap-test-coverage`, `roadmap-decompose-skeleton`) then load a **philosophy**, not an abstract engine.
- This is a **separation of philosophy from algorithm, not a rewrite** — the same discipline the roadmap-engine mistake violated (that extraction turned into a rigid rewrite). Here: pull the philosophy out, keep the algorithm verbatim.

## Details

### The rename

- `src/skills/test-engine/` → `src/skills/test-philosophy/` (directory + frontmatter `name: test-philosophy`). Rename also the H1 heading (`# Test Engine — …` → `# Test Philosophy — …`) and any "engine" wording in the body → "philosophy". The **rule content** is unchanged.
- **Flip `user-invocable: false` → `true`.** `user-invocable: false` was justified for `roadmap-engine` — it is meaningless standalone (it only renders when a philosophy hands it a task). A **philosophy is usable standalone**: a user can invoke `/test-philosophy` to consult or apply the rule, so it must be user-invocable. Keep `disable-model-invocation: false` (consumers still load it via the Skill tool).
- Update every reference: `CLAUDE.md` ("never overwrite" list + repo structure), `roadmap-decompose-skeleton` (its TDD lens loads it), and any ROADMAP mentions.

### Separate philosophy from algorithm in `roadmap-test-coverage`

Refactor `src/skills/roadmap-test-coverage/SKILL.md` to **load `test-philosophy`** for the silent-failure discriminator instead of inlining it — two sites only:
- **Layer 3 (Silent-Failure Filter):** replace the inline core question + loud/silent table with "load `test-philosophy` once, apply its discriminator, drop loud-failure areas." Keep the `$RESEARCH_AREAS` output block.
- **Layer 7:** the Class A (API drift) / Class B (silent bug) definitions reference `test-philosophy`'s corollary. Keep the table + patch/escalate actions.

Add `Skill` to `allowed-tools` if absent.

### This is extraction, not a rewrite (the lesson)

- `test-philosophy`'s content is **byte-identical** to test-engine's — only the name changes.
- `roadmap-test-coverage`'s 8-layer pipeline, its parallel agents, area grouping, and test-roadmap hand-off stay **byte-identical**. Only the discriminator moves from inline → loaded.

### Verify

- `git diff` on `roadmap-test-coverage/SKILL.md` shows **only** the two discriminator sites swapped to a load — nothing else in the algorithm changes.
- `test-philosophy` = the former test-engine content, renamed, not rewritten.

### What NOT to do

- Do not invent a "test engine" or any shared algorithm — the test family has none; there is only a shared philosophy.
- Do not rewrite `roadmap-test-coverage`'s pipeline — extract the philosophy, keep the algorithm.
- Do not change the philosophy content — the rename is name-only.
