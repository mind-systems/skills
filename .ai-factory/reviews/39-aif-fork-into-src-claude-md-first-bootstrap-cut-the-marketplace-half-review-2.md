# Code Review (round 2) — Milestone 39: aif fork into `src/`, CLAUDE.md-first bootstrap

**Reviewed:** `git diff HEAD` + full read of `src/skills/aif/SKILL.md` (496 lines), references, symlink, repo `CLAUDE.md`.
**Risk:** 🟢 Low — all round-1 findings resolved; one residual documentation contradiction.

## Round-1 findings — all fixed (verified)

1. **(was Medium) Language resolution ordered after CLAUDE.md generation** — FIXED. Language resolution is now the first step in every mode: Mode 1 Step 2 (before CLAUDE.md at Step 3), Mode 2 Step 1 (before Step 2), Mode 3 Step 1 (before the description prompt at Step 2 and CLAUDE.md at Step 3). Mode 3's "Ask this prompt in resolved `language.ui`" (line 298) now follows resolution. The fresh-English-CLAUDE.md pollution of the `language.ui` chain is gone. ✓
2. **(was Low) Stale `/aif-plan` / `/aif-rules` references** — FIXED. The git question is reframed as "how should full plans behave in git" with "(sets `git.create_branches`)" (lines 74, 80–81); line 118 now reads "managed by area-specific rules tooling outside this skill." `grep` for `/aif-plan|/aif-rules|/aif-implement|…` returns nothing. ✓
3. **(was Low) Dangling `#architecture-generation` anchor** — FIXED. Line 247 now links `[CRITICAL: Do NOT Implement](#critical-do-not-implement)`. All eight in-file anchor references now resolve to real headings (verified against normalized heading slugs). ✓
4. **(was Low) Duplicate "Step 7" label** — FIXED. The global architecture step is relabeled "**Final step: Generate Architecture Document**" (line 475). ✓
5. **(was Low) Config-source prose path inconsistent** — FIXED. Line 87 now uses `~/.claude/skills/aif/references/…`, matching the executed command. ✓
6. **(was Low) Stale `"what skills do I need"` trigger** — FIXED. Removed from the `description` frontmatter (line 3). ✓

Also re-verified: references byte-identical to upstream (`diff -q` clean), symlink `active/skills/aif → ../../src/skills/aif`, zero `{{…}}` placeholders, 496 lines, repo `CLAUDE.md` bookkeeping intact.

## Residual finding

### 1. (Low) `config.yaml`-persist prose still asserts config precedes the first artifact — contradicts CLAUDE.md-first
The config-machinery block (kept verbatim from upstream) states at line 88 *"Write or update `.ai-factory/config.yaml` immediately after resolving the run-scoped language state"* and line 89 *"This write MUST happen before writing the first setup artifact …"*. But the milestone's core design (line 33) puts CLAUDE.md **first, before `.ai-factory/config.yaml`**, and every mode now writes CLAUDE.md (Mode 1 Step 3 / Mode 2 Step 2 / Mode 3 Step 3) before persisting config (Step 4). So the retained lines 88–89 directly contradict lines 33/205/257/300: one says config precedes all setup artifacts, the other says CLAUDE.md precedes config.

**Impact:** documentation-only. The operative order is unambiguous from each mode's numbered steps and from Mode 1's Execute block (item 1 saves CLAUDE.md, item 4 runs the config helper), so CLAUDE.md-first wins in practice — no runtime break. This is a stale ordering claim inherited when the config prose was kept verbatim; the reconciliation (plan Task 5) didn't reach it.

**Suggested fix:** reword lines 88–89 to exempt CLAUDE.md — e.g. "This write MUST happen after CLAUDE.md is generated but before `rules/base.md`, MCP config, `AGENTS.md`, and before invoking `/aif-architecture`." Optionally soften line 88's "immediately after resolving the run-scoped language state" to "after CLAUDE.md generation."

## Verdict
No blocking issues. The single residual item is a low-severity internal contradiction with no runtime effect; worth a one-line reword for consistency but does not gate the milestone.
