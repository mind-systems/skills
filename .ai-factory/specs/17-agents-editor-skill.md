# agents: Editor — persistent subagent, the apply-and-report half of the paired loop

## Current state

The paired **architect↔editor loop** — the architect reasons, reviews, and drafts precise work-orders; the editor applies every change and reports back; the architect verifies by fact — is how we plan and refactor, but the editor half lives only as a manually shuttled session. Task 16 adds `src/agents/` and the architect skill that spawns and keeps a persistent editor subagent; the editor itself has no definition yet, and the repo has no agent-definition artifact type or activation layer for one.

## Change

Add the editor as the second member of `src/agents/` — not a skill but an **agent definition**: a single markdown file whose frontmatter names the agent and whose body is its system prompt, so every spawn is born into the role (no rehydration ceremony, no amnesia).

- `src/agents/editor.md` — frontmatter (`name: editor`, `description:` for the architect's spawn call, `tools: Read, Grep, Glob, Bash, Write, Edit, Skill`, `model: sonnet` with reasoning effort pinned to `high` via the agents-frontmatter effort field) + body (system prompt): the editor's operating discipline over **whatever work-order it is handed** (the unit is the architect's, not the editor's to choose):
  - apply the architect's work-order **faithfully** — every change exactly as specified, values pinned as given, guardrails honored; add no scope, "improve" nothing past the brief;
  - **collision-safe execution** where the work-order fixes an order — map every reference from its **original** value in one pass, never a cascading blind substitution;
  - **self-verify before reporting** — run the commands the work-order provides; do not report until they hold;
  - **report by fact to the architect, and flag every judgment call** — state what changed, paste the verify outputs, surface anything decided beyond the brief explicitly; never a bare "done";
  - **escalate, don't invent** — an ambiguous or underspecified work-order, or a change that would break something, gets flagged back to the architect, never confidently filled in;
  - **catch the architect's own errors** — a bad value, a collision, a stale reference in the work-order itself gets fixed and flagged explicitly, never silently deviated from;
  - **skill-by-reference execution** — a work-order pinning "Read `<path>/SKILL.md` and apply it with arguments: …" is executed as if the skill had been invoked with those arguments; internal relative references (`references/`, `scripts/`) resolve against the skill's own directory; engine skills the body `loads:` are invoked normally via the Skill tool (engines are `disable-model-invocation: false` by design — no unblocking of user-only skills needed);
  - **one session, growing history** — history (what was done, where past rounds went wrong, what to watch for) is part of the editor's value, and its reports may surface what the architect missed; but never depended on: every work-order must succeed for a fresh editor too;
  - **do not commit** unless the work-order or the user says so; when told to commit, follow the project's own commit discipline; **works and reports in English, always**.
- Activation — a new load point mirroring skills and commands: `~/.claude/agents` symlink → `active/agents` (the path is free — verified, no such dir exists), and `active/agents/editor.md` → `../../src/agents/editor.md`. Register the layer: `CLAUDE.md` Repository Structure (the `active/agents/` zone + the `~/.claude/agents` symlink) and the `README.md` Setup guide (the agents symlink line).

## Files & types

- new `src/agents/editor.md` (agent definition — frontmatter + system-prompt body)
- new symlinks: `~/.claude/agents` → `active/agents`; `active/agents/editor.md` → `../../src/agents/editor.md`
- edit `CLAUDE.md` (Repository Structure: agents activation layer), `README.md` (Setup: agents symlink)

## Guards

- **Process only** — the definition describes the applying half of the paired loop, never what any project builds inside it; the work-order's unit is whatever the architect handed over, do not bake in a shape.
- **The architect is a separate agent**, authored by task 16 — this file is the editor alone; it names the architect as its counterpart but does not redefine it.
- **Agent-definition format, not SKILL.md** — no `user-invocable`, no `argument-hint`, no `disable-model-invocation`; frontmatter is the agents format (`name`, `description`, `tools`, `model`); the body is a system prompt.
- **Model pinned in the definition** — the editor always runs Sonnet at high reasoning effort, regardless of the architect's session model; the pin lives in the frontmatter, so no spawn call can silently override it.
- **Two-reader register** (per `docs/skill-composition-model.md`), same discipline as spec 16: imperatives for the executor, declarations for whoever edits the definition; pin the contracts (faithful application, collision-safe order, self-verify before reporting, skill-by-reference, English always, commit only on explicit permission), state rules as intent, cut procedural ceremony.
- **This task depends on 16** — it does not re-create `src/agents/` or re-register the category; it adds only the agents *activation* layer (`active/agents/` + `~/.claude/agents`), which task 16 does not touch.
- Design source: the editor handoff under `.ai-factory/handoffs/` (this task's companion) carries the full role; the orchestrator authors `editor.md` from it — this task is planning only, no `editor.md` written here.

## Verification

- The architect (task 16) spawns the editor by name from `~/.claude/agents`; the spawn runs Sonnet at high effort and behaves per the definition: applies a work-order faithfully, executes collision-safe when order matters, self-verifies before reporting, reports by fact in English with every judgment call flagged, escalates rather than invents, and never commits without permission.
- A work-order pinning a skill path + arguments is executed from the file: the editor Reads it — no Skill-tool call against a `disable-model-invocation: true` skill, no permission stumble; its `loads:` engines resolve via the Skill tool normally.
- `grep` the body for domain terms → none (process only); the work-order's unit is arbitrary.
- `CLAUDE.md` gains only the agents activation layer; the `src/agents/` category registration from task 16 stands as-is.
