# Plan: test-philosophy — rename `test-engine` + separate the test philosophy from the algorithm

## Context
Rename the mislabeled `test-engine` skill to `test-philosophy` (name-only, byte-identical content) and make it user-invocable, then refactor `roadmap-test-coverage` to **load** that philosophy for its silent-failure discriminator instead of inlining it — its 8-layer algorithm stays verbatim.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Scope guardrails (read before starting)
- **This is a rename + extraction, NOT a rewrite.** `test-philosophy`'s body is byte-identical to `test-engine`'s except the name (frontmatter `name`, H1, and the word "engine" in the opening body sentence). `roadmap-test-coverage`'s pipeline/agents/hand-off stay byte-identical except the two discriminator sites.
- **Enumerate references exhaustively before editing.** Run `grep -rn 'test-engine' src/ CLAUDE.md .ai-factory/ROADMAP.md` and handle every live hit. Live reference sites are only: the skill itself, `CLAUDE.md` (tree + never-overwrite list), `roadmap-decompose-skeleton/SKILL.md`, and `roadmap-test-coverage/SKILL.md`.
- **Do NOT edit historical artifacts.** Files under `.ai-factory/reviews/`, `.ai-factory/plan-reviews/`, `.ai-factory/plans/` (old), and `.ai-factory/notes/` (incl. note 29) are historical records — leave them. They will show up in the grep; ignore them.
- **ROADMAP.md needs no rename edits.** Line 43 is the completed `test-engine` creation milestone (history — keep). Line 47 already reads `test-philosophy`. Line 49 is this milestone describing the rename action (keep). Confirm via grep; do not rewrite history lines.

## Tasks

### Phase 1: Rename test-engine → test-philosophy

- [x] **Task 1: Rename the skill directory and update its own content**
  Files: `src/skills/test-engine/SKILL.md` → `src/skills/test-philosophy/SKILL.md`
  Rename the directory with `git mv src/skills/test-engine src/skills/test-philosophy` (preserves history; the `~/.claude/skills` symlink follows automatically). Then edit the moved `SKILL.md`:
  - Frontmatter `name: test-engine` → `name: test-philosophy` (must match the new directory name — validator constraint).
  - Flip `user-invocable: false` → `user-invocable: true` (a philosophy is usable standalone). Keep `disable-model-invocation: false` and `allowed-tools: Read` unchanged (consumers still load it via the Skill tool).
  - H1 heading `# Test Engine — Shared Silent-Failure Testing Philosophy` → `# Test Philosophy — Shared Silent-Failure Testing Philosophy`.
  - Body wording: the opening sentence says "shared pure-content philosophy unit" — replace any remaining "engine" wording with "philosophy" (e.g. the description already says "philosophy"; verify no stray "engine" remains in the body). The discriminator table, rule text, and After-the-Fact Corollary content stay **byte-identical**.

- [x] **Task 2: Update `CLAUDE.md` references** (depends on Task 1)
  Files: `CLAUDE.md`
  Two edits:
  - Repository Structure tree (line 34): `│   │   ├── test-engine/    #   shared silent-failure testing philosophy` → `test-philosophy/` (keep the comment; re-align the tree box if needed to keep it valid ASCII).
  - "Custom skills — never overwrite from upstream" list (line 117): replace `test-engine` with `test-philosophy` so the next upstream sync does not wipe it.

- [x] **Task 3: Update `roadmap-decompose-skeleton/SKILL.md` references** (depends on Task 1)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Replace every `test-engine` with `test-philosophy` (grep found lines 7, 9, 36, 44, 84, 141, 142). While doing so, collapse the now-stale alias note at lines 36–38 — currently `the silent-failure test engine, installed in this repo as \`test-engine\` (referred to as "test-philosophy" in some specs — same skill)`. After the rename the skill *is* `test-philosophy`, so simplify this to name `test-philosophy` directly and drop the "installed as test-engine / referred to as test-philosophy" alias caveat. Update the call-graph diagram (line 44) and the Critical Rules mentions (lines 141–142) to `test-philosophy`. Do not change any lens logic — only the skill name.

### Phase 2: Separate philosophy from algorithm in roadmap-test-coverage

- [x] **Task 4: Load `test-philosophy` for the discriminator in `roadmap-test-coverage`** (depends on Task 1)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Three edits, nothing else in the 8-layer algorithm changes (pipeline, parallel agents, area grouping, hand-off stay byte-identical):
  - **`allowed-tools` (line 13):** append `Skill` (currently absent) so the orchestrator can load the philosophy.
  - **Layer 3 — Silent-Failure Filter (lines 60–96):** replace the inlined core question (lines 64–68) and the loud/silent table (lines 70–76) with an instruction to **load `test-philosophy` once via the Skill tool and apply its silent-failure discriminator to each candidate area, dropping loud-failure areas.** Keep everything else in Layer 3 verbatim: the "most important gate" framing (lines 61–62), the "Apply the filter … Drop loud-failure areas" line, the user-facing `After silent-failure filter…` present block (lines 80–94), and the `$RESEARCH_AREAS` store (line 96).
  - **Layer 7 — Class A/B (lines 244–265):** add a reference that the API-drift (Class A) vs silent-bug (Class B) split **applies `test-philosophy`'s After-the-Fact Corollary** rather than presenting the definitions as freestanding. Keep the agent-prompt classification table and the Class A/B definitions **inside the agent prompt intact** — that subagent runs in isolation and must stay self-contained (it does not load the skill). Keep the post-table patch (Class A) / escalate (Class B) actions (lines 261–265) and the re-run step verbatim. The load itself happens once at Layer 3; Layer 7 only points its own decision prose at the loaded corollary.

## Verification (not a task — do while implementing)
- `grep -rn 'test-engine' src/ CLAUDE.md` returns **no live hits** (only historical `.ai-factory/` artifacts, which are intentionally untouched).
- `git diff src/skills/roadmap-test-coverage/SKILL.md` shows only the `allowed-tools` `Skill` addition and the two discriminator sites swapped to a load — the rest of the algorithm is byte-identical.
- `src/skills/test-philosophy/SKILL.md` differs from the old `test-engine` version only in `name`, `user-invocable`, H1, and the one body "engine"→"philosophy" wording.
