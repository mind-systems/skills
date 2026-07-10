# Plan Review — agents: Editor (apply-and-report half of the paired loop)

**Plan:** `.ai-factory/plans/63-agents-editor-persistent-subagent-the-apply-and-report-half-of-the-paired-loop.md`
**Governing spec:** `.ai-factory/specs/17-agents-editor-skill.md`
**Design sources read:** spec 17, `handoffs/10-editor-paired-loop.md`, `src/agents/agent-architect/SKILL.md`
**Roadmap line:** ROADMAP.md:137 (task 17, depends on 16)

## Code Review Summary

**Files Reviewed:** 1 plan + 3 design sources + codebase targets (CLAUDE.md, README.md, ARCHITECTURE.md, `active/`, `src/agents/`, `~/.claude` symlinks)
**Risk Level:** 🟢 Low

The plan faithfully implements spec 17. Its four tasks map cleanly to the spec's Change/Files sections; the pinned contracts in Task 1 are transcribed from the handoff (the ratified design source) essentially verbatim; the dependency on task 16 is respected (architect already present at `src/agents/agent-architect`, activated via `active/skills/`). I verified the codebase claims the plan rests on:

- `active/agents/` does **not** exist and `~/.claude/agents` does **not** exist — the load-point paths are free, exactly as the spec asserts. ✔
- `~/.claude/skills` and `~/.claude/commands` are machine symlinks into `active/*` — the parallel pattern Task 2 mirrors. ✔
- The symlink target arithmetic is correct: from `active/agents/editor.md`, `../../src/agents/editor.md` resolves to repo-root `src/agents/editor.md`. ✔
- `src/agents/` category is already registered in CLAUDE.md (tree line 46) and ARCHITECTURE.md (line 22), both already naming the editor sibling — so Task 3's "add only the activation layer, do not re-describe the category" is correct and non-duplicative. ✔
- The editor's `tools` set (`Read, Grep, Glob, Bash, Write, Edit, Skill`) covers every discipline: Read for skill-by-reference, Bash for self-verify, Write/Edit for apply, Skill for engine invocation. No missing tool; no over-grant. ✔
- Subagent resolution is sound: the architect spawns via the `Agent` tool with a named subagent type, which resolves from `~/.claude/agents/*.md` — so Task 2's machine symlink is what makes the architect's spawn call work. ✔

### Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** WARN — see Deferred observations. The category is registered (line 22); the activation layer is not, and line 24 enumerates the `~/.claude/*` symlinks. Out of the plan's declared file boundary (spec scopes edits to CLAUDE.md + README), so deferred, not blocking.
- **Rules:** No `.ai-factory/RULES.md` present — gate skipped.
- **Roadmap (`.ai-factory/ROADMAP.md`):** PASS — line 137 matches the plan title and spec tag; `Depends on 16` honored; task 16 (line 135) is `[x]`.
- **Skill-context (`aif-review`):** absent — gate skipped.

### Critical Issues

None. Nothing here is a runtime error, missing migration, or security hole.

### Issues to address

**1. (Medium) The reasoning-effort frontmatter key is named only as "the agents-frontmatter effort field" — pin the exact key and ground it, because a wrong key fails silently.**
Task 1 and spec 17 both require the editor to run "Sonnet at high reasoning effort" pinned in the definition, and the spec's Guard makes this load-bearing: *"the pin lives in the frontmatter, so no spawn call can silently override it."* But neither the plan nor the spec names the actual YAML key, and there is **no existing agents-format file in the repo to pattern-match** — `agent-architect` is a SKILL.md, not an agent definition, so the orchestrator has no precedent to copy. If it authors a key the runtime does not recognize (e.g. `effort:` vs `reasoning-effort:` vs something else), the field is silently ignored and the editor runs at default effort — the exact silent-override the Guard exists to prevent. The plan should (a) pin the exact frontmatter key, grounded against the harness's actual agent-definition schema, and (b) make the spec's Verification bullet ("the spawn runs Sonnet at high effort") an operational check rather than an assertion, since the failure mode is silent. This lives entirely within the plan's file boundary (`src/agents/editor.md` frontmatter).

**2. (Low) Task 3 under-specifies the CLAUDE.md edit sites — the symlinked-set enumerations in Purpose would go partially stale.**
CLAUDE.md describes the symlinked working sets in more than one place: the Purpose section states *"`active/skills/` and `active/commands/` hold per-item symlinks…"* (line 12) and *"available globally via `~/.claude/skills` → … and `~/.claude/commands` → …"* (line 14), in addition to the Repository Structure tree (lines 50–53). Task 3 pins the tree zone and "note the symlink where the skills/commands symlinks are described" (line 14) but does not call out line 12's enumeration. If only the tree and line 14 are touched, line 12 is left enumerating two of three sets — a partial-staleness drift the repo's own "describe current state only / one home per fact" discipline warns against. Recommend Task 3 enumerate all three CLAUDE.md sites (tree 50–53, Purpose line 12, Purpose line 14) so nothing is left half-updated.

### Positive Notes

- Task 1's contract list is a near-verbatim transcription of `handoffs/10-editor-paired-loop.md` — the plan correctly treats the handoff as the design source and does not reinvent the role text.
- The agent-definition-vs-SKILL.md distinction is handled precisely: the plan explicitly forbids `user-invocable`, `argument-hint`, `disable-model-invocation` (SKILL.md-only) and specifies comma-separated `tools` (agents format) — matching how the architect (SKILL) and editor (agent definition) are meant to differ.
- The skill-by-reference contract is transcribed correctly, including the subtle point that a pinned skill is executed by **Read** (avoiding a Skill-tool call against a `disable-model-invocation: true` skill) while `loads:` engines invoke normally via the Skill tool — the exact nuance spec 17 Verification calls out.
- Task 2's verification (`ls -lL ~/.claude/agents/editor.md` resolves to `src/agents/editor.md`) is a concrete, correct end-to-end symlink check.
- Dependency discipline is clean: the plan does not recreate `src/agents/` or re-register the category, adding only the activation layer task 16 left untouched.

## Deferred observations
- Affects: `.ai-factory/ARCHITECTURE.md` (line 24) / spec 17 Files & types — ARCHITECTURE.md line 24 reads *"`active/` … is the only layer `~/.claude/skills` and `~/.claude/commands` point at,"* enumerating exactly the machine symlinks. This milestone adds a third (`~/.claude/agents`), which will leave that enumeration incomplete (still true about `active/`, but no longer naming all the symlinks). Spec 17's Files & types deliberately scopes edits to CLAUDE.md and README.md only, so ARCHITECTURE.md is outside this milestone's file boundary — hence deferred rather than a finding. Whoever owns doc-consistency for the agents category (or a follow-up prune/docs pass) may want to extend line 24 to name `~/.claude/agents` alongside skills and commands.

REVIEW_PASS is withheld: findings 1 and 2 above are within the plan's file boundary and should be resolved before implementation.
