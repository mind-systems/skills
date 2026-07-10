# Plan: agents: Editor — persistent subagent, the apply-and-report half of the paired loop

## Context
Add the editor half of the architect↔editor paired loop as a spawnable **agent definition** (`src/agents/editor.md`), plus a new `active/agents/` activation layer so task 16's architect can spawn it by name.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Design source (read before Task 1)
- `.ai-factory/specs/17-agents-editor-skill.md` — the spec (contracts, guards, verification).
- `.ai-factory/handoffs/10-editor-paired-loop.md` — the **full role text**; `editor.md`'s system-prompt body is authored from this handoff, not invented.
- `src/agents/agent-architect/SKILL.md` — task 16's counterpart; the editor names it as counterpart but does not redefine it.

## Tasks

### Phase 1: Author the editor agent definition

- [x] **Task 1: Create `src/agents/editor.md` (agent definition — frontmatter + system-prompt body)**
  Files: `src/agents/editor.md`
  Author the editor as an **agent definition, not a SKILL.md**. Frontmatter is the agents format only — `name: editor`, `description:` (written for the architect's spawn call), `tools: Read, Grep, Glob, Bash, Write, Edit, Skill`, `model: sonnet`, plus the reasoning-effort pin (see the grounding step below). **No** `user-invocable`, `argument-hint`, or `disable-model-invocation` (those are SKILL.md-only). The body is a **system prompt** — the editor is born into the role at every spawn.

  **Ground the reasoning-effort key before authoring (load-bearing, silent-failure surface).** Spec 17's Guard makes the pin non-negotiable — *"the pin lives in the frontmatter, so no spawn call can silently override it"* — but neither the spec nor this plan names the actual YAML key, and there is **no existing agent-definition file anywhere on this machine to pattern-match** (verified: no `~/.claude/agents`, no `*/agents/*.md`; `agent-architect` is a SKILL.md, not an agent definition). Claude Code is `2.1.198`. A wrong key (`effort:` vs `reasoning-effort:` vs `reasoningEffort:` vs something else) is **silently ignored** and the editor runs at default effort — the exact failure the Guard exists to prevent. Therefore:
  1. Determine the exact frontmatter key that Claude Code 2.1.198 recognizes for per-agent reasoning effort, grounded against the harness's live agent-definition schema (the `/agents` config surface / subagent frontmatter reference), not from memory.
  2. Pin **that exact key** with value `high` in the frontmatter.
  3. If the schema has **no** per-agent reasoning-effort field, do **not** invent one — the "Sonnet at high effort" contract cannot be met by an ignored key; flag it back for a spec decision rather than shipping a silently-inert field.

  Compose the body from `.ai-factory/handoffs/10-editor-paired-loop.md`, preserving these pinned contracts:
  - apply the work-order **faithfully** — every change exactly as specified, values pinned as given, guardrails honored; add no scope, "improve" nothing past the brief;
  - **collision-safe execution** when the work-order fixes an order — map every reference from its **original** value in one pass, never a cascading blind substitution;
  - **self-verify before reporting** — run the work-order's own verify commands; do not report until they hold;
  - **report by fact, flag every judgment call** — state what changed, paste verify output, surface anything decided beyond the brief; never a bare "done";
  - **escalate, don't invent** — an ambiguous/underspecified work-order, or one that would break something, is flagged back, never confidently filled in;
  - **catch the architect's own errors** — a bad value, collision, or stale reference in the work-order is fixed and flagged explicitly, never silently deviated from;
  - **skill-by-reference execution** — a work-order pinning "Read `<path>/SKILL.md` and apply it with arguments: …" is executed as if the skill were invoked with those arguments; internal relative references (`references/`, `scripts/`) resolve against the skill's own directory; engine skills the body loads are invoked normally via the Skill tool;
  - **one session, growing history** — history sharpens the editor and its reports may surface what the architect missed, but is never depended upon: every work-order must succeed for a fresh editor too;
  - **commit only on explicit permission** — do not commit unless the work-order or user says so; when told to, follow the project's own commit discipline; **works and reports in English, always**.
  Register discipline: two-reader register (imperatives for the executor, declarations for whoever edits the definition); **process only** — no project domain terms, the work-order's unit is whatever the architect handed over (do not bake in a shape). Name the architect as counterpart without redefining it.

### Phase 2: Activation & registration

- [x] **Task 2: Create the `active/agents/` activation layer and the machine load point** (depends on Task 1)
  Files: `active/agents/editor.md` (in-repo symlink), `~/.claude/agents` (machine symlink)
  A new load point mirroring skills/commands, distinct from `active/skills/` (where task 16's `agent-architect` skill lives). Create the in-repo per-item symlink `active/agents/editor.md` → `../../src/agents/editor.md` (create the `active/agents/` directory first). Then create the machine-level load point `~/.claude/agents` → `/Users/max/projects/skills/active/agents` (parallel to the existing `~/.claude/skills` and `~/.claude/commands` symlinks). Verify: `ls -lL ~/.claude/agents/editor.md` resolves to `src/agents/editor.md`.

- [x] **Task 3: Register the agents activation layer in `CLAUDE.md`** (depends on Task 2)
  Files: `CLAUDE.md`
  CLAUDE.md describes the symlinked working sets in **three** places — update all of them so none is left enumerating two of three sets ("one home per fact / describe current state only"):
  1. **Repository Structure tree** (≈ lines 50–53): add the `active/agents/` zone under `active/` (per-item symlinks → `src/agents/*`) alongside `active/skills/` and `active/commands/`.
  2. **Purpose, line 12** (*"`active/skills/` and `active/commands/` hold per-item symlinks…"*): extend the enumeration to include `active/agents/`.
  3. **Purpose, line 14** (*"available globally via `~/.claude/skills` → … and `~/.claude/commands` → …"*): add the `~/.claude/agents` → `active/agents` machine symlink.
  Add **only** the agents *activation* layer — the `src/agents/` category registration from task 16 (tree line 46) stands as-is; do not re-describe or duplicate it.

- [x] **Task 4: Add the agents symlink to the README Setup guide** (depends on Task 2)
  Files: `README.md`
  In `## Setup (one-time, per machine)`, add the agents symlink line next to the existing two — `ln -s ~/projects/skills/active/agents ~/.claude/agents` — following the exact style of the `~/.claude/skills` and `~/.claude/commands` lines. Update the surrounding prose only if it enumerates the symlinked working sets.

## Verification
- **Symlink chain (Task 2):** `ls -lL ~/.claude/agents/editor.md` resolves to `src/agents/editor.md`.
- **Reasoning-effort pin is live, not silently inert (Task 1 — silent-failure surface).** Do not merely assert "Sonnet at high effort" from the frontmatter text; confirm the runtime honors it. Spawn the editor via the `Agent` tool by name (the architect's spawn path) and confirm operationally that it runs on **Sonnet** at **high** reasoning effort — e.g. the agent self-reports its model/effort, or the harness surfaces them for the spawned subagent. A pinned key that the runtime ignores must fail this check, not pass on the strength of the YAML alone.
- **Behavioral (per spec 17):** the spawned editor applies a work-order faithfully, executes collision-safe when order matters, self-verifies before reporting, reports by fact in English with judgment calls flagged, escalates rather than invents, and never commits without permission; a work-order pinning a skill path + arguments is executed via **Read** (no Skill-tool call against a `disable-model-invocation: true` skill), while its `loads:` engines resolve via the Skill tool normally.
- **Process-only body:** `grep` the body for domain terms → none.
