# Code Review: test-philosophy — rename `test-engine` + separate philosophy from algorithm

**Scope:** rename `src/skills/test-engine` → `test-philosophy`, make it user-invocable, rewire consumers, and load the philosophy for `roadmap-test-coverage`'s discriminator instead of inlining it.

**Files changed (code):**
- `src/skills/test-engine/SKILL.md` → `src/skills/test-philosophy/SKILL.md` (rename + 4 content edits)
- `CLAUDE.md` (tree + never-overwrite list)
- `src/skills/roadmap-decompose-skeleton/SKILL.md` (reference rename + alias-note collapse)
- `src/skills/roadmap-test-coverage/SKILL.md` (allowed-tools + Layer 3 + Layer 7)

These are agent-instruction skills, not executable code, so "runtime" review means: frontmatter validity, name/directory consistency, dangling skill references, load-invocation contracts, and content fidelity (byte-identical carve-out).

## Verification performed

- **`git status` / `git diff HEAD`** reviewed in full; each changed file read in context.
- **Directory/`name` consistency:** `git mv` renamed the directory; `name: test-philosophy` (SKILL.md:2) matches the new directory name — validator constraint satisfied. Git reports the move as a rename at 95% similarity, consistent with only the 4 intended line edits.
- **Frontmatter:** `user-invocable: true` (was `false`), `disable-model-invocation: false` preserved, `allowed-tools: Read` unchanged. Both consumers load it via the Skill tool (model invocation), which requires `disable-model-invocation: false` — correctly kept. Flipping only `user-invocable` is the exact, minimal change the spec calls for. YAML block scalar well-formed.
- **Content fidelity:** the discriminator table, rule text, and After-the-Fact Corollary in `test-philosophy/SKILL.md` are byte-identical to the former `test-engine` version; only `name`, `user-invocable`, and the H1 changed. `grep -in engine` over the file returns no stray "engine" wording. ✔ matches the "rename, not rewrite" guardrail.
- **No dangling references:** `grep -rn 'test-engine' src/ CLAUDE.md AGENTS.md README.md` returns **none**. All live sites now say `test-philosophy`. Remaining `test-engine` strings exist only in historical `.ai-factory/` artifacts (notes, reviews, plans, ROADMAP history lines), which the plan intentionally leaves untouched.
- **`roadmap-test-coverage` carve-out:** the diff touches exactly three sites — `allowed-tools` gains `Skill` (needed for the Layer 3 load), Layer 3's inline question+table swapped to a `Skill`-tool load of `test-philosophy`, and a Layer 7 note pointing the Class A/B split at the loaded corollary. Layers 1–2, 4–6, 8, and the Critical Rules are byte-identical. The 8-layer algorithm, parallel agents, area grouping, and hand-off are unchanged. ✔
- **Layer 7 isolation handled correctly:** the Class A/B definitions remain inline inside the subagent prompt (SKILL.md:236–242). This is correct — that agent runs in an isolated context and cannot load the skill, so it must stay self-contained. The added orchestrator note (SKILL.md:215–217) explains this and references `test-philosophy`'s corollary without removing the inline definitions. No behavioral break.
- **`roadmap-decompose-skeleton`:** all 7 references renamed; the stale alias note ("installed as `test-engine`… referred to as test-philosophy") correctly collapsed to name `test-philosophy` directly; call-graph diagram and Critical Rules updated. `Skill` was already in its `allowed-tools` — no spurious edit. Lens logic unchanged.
- **`CLAUDE.md`:** tree entry and never-overwrite list both updated; the skill stays protected from upstream sync. Tree remains valid ASCII (alignment cosmetic only).

## Findings

None. The change is an accurate, tightly-scoped rename + extraction. Frontmatter is valid and name/directory-consistent, no dangling skill references remain, the load/invocation contracts are internally consistent (`Skill` added where a load was introduced), the Layer 7 subagent-isolation edge case is handled, and the byte-identical carve-out for both the philosophy body and the `roadmap-test-coverage` algorithm holds. Nothing will break at runtime.

REVIEW_PASS
