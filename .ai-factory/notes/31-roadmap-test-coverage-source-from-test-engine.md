# roadmap-test-coverage: source silent-failure rule from test-engine

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- Once `test-engine` exists (note 29), refactor `roadmap-test-coverage` to **load test-engine for the silent-failure discriminator** instead of inlining it.
- Surgical change — only the two places that state the rule: Layer 3 (the Silent-Failure Filter) and Layer 7 (the Class A / Class B classification). The 8-layer pipeline, the parallel agents, the area grouping, and the test-roadmap hand-off are unchanged.

## Details

### Concrete edits to `src/skills/roadmap-test-coverage/SKILL.md`

- **Layer 3 — Silent-Failure Filter** — replace the inlined core question and the loud/silent table with: "Ensure `test-engine` is loaded once in this chat, then apply its silent-failure discriminator to each candidate area; drop loud-failure areas." Keep the existing "After silent-failure filter: N areas remain (dropped M)" output block and the `$RESEARCH_AREAS` store.
- **Layer 7 — Existing Tests Run** — the Class A (API drift) / Class B (silent bug) definitions in the agent prompt reference test-engine's corollary rather than restating it. Keep the classification table, the Class A patch / Class B escalate actions, and the re-run gate.
- **Load-once:** ensure `test-engine` is loaded once per chat (mirrors the family's load-once convention).
- **Frontmatter `allowed-tools`** — add `Skill` if absent (needed to load test-engine).

### Files

- Edit `src/skills/roadmap-test-coverage/SKILL.md`.
- If `roadmap-test-coverage` is not already protected in `CLAUDE.md` Upstream Sync, add it to "Custom skills — never overwrite from upstream" (it is a local skill).

### Regression guard (static diff)

After the edit, `git diff src/skills/roadmap-test-coverage/SKILL.md` must contain **only** the two swapped sites: Layer 3's inline question + table replaced by the load-`test-engine` call, and Layer 7's Class A/B referencing test-engine. The text moved into `test-engine` must be **byte-identical** to Layer 3's removed lines. Any change elsewhere — pipeline, agent prompts, test-roadmap hand-off — is a regression; revert it.

### What NOT to do

- **Preserve verbatim, do not paraphrase.** Everything outside the two swapped sites stays **byte-identical**. The silent-failure question + table moved to `test-engine` is **copied verbatim** from Layer 3, not rewritten. A refactor here is a move, not a rewrite.
- Do not change the pipeline, the agent prompts' research structure, or the test-roadmap hand-off.
- Do not move any coverage/area logic into test-engine — only the silent-failure discriminator is shared.
