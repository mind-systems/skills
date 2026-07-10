# agents: Architect — plan-and-review skill of the paired loop (new `src/agents/` category)

> The architect is a **skill** (invoked by the user, rehydrates the role in the main session). Only its counterpart, the editor (task 17), is an **agent definition**. The `agents:` prefix names the `src/agents/` category — the pair's home — not the artifact type.

## Current state

The paired **architect↔editor loop** — the architect reasons, reviews, and drafts precise work-orders; the editor applies every change and reports back; the architect verifies by fact — is how we plan and refactor, but it lives only as session habit across two manually shuttled sessions. There is no packaged "architect" persona to invoke, and no `src/agents/` category to host one. `src/` today holds `skills/`, `commands/`, and `global/` only.

## Change

Add an agent-skill category and its first member — the architect — capturing the loop's **process**, not any project's domain. The editor becomes a **persistent subagent the architect itself spawns and keeps** (defined by sibling task 17); the manual user-courier shuttle is retired.

- New category `src/agents/` (parallel to `src/skills/`, `src/commands/`).
- `src/agents/agent-architect/SKILL.md` — frontmatter (`name: agent-architect`, `user-invocable: true`, `disable-model-invocation: true`, `argument-hint: "[unit of work — e.g. a phase, a task, a file]"`, `allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage`) + body: the architect's operating discipline over **any unit of work** (a roadmap phase, one task, a class, a module, a review dimension — the loop is invariant, only the unit changes):
  - reason and review; **never edit the shared artifacts** (roadmap, specs, code, docs) — the editor applies every change;
  - **spawn the editor once, message it thereafter** — one spawn at the start of the work, every subsequent work-order into the same conversation via SendMessage; never a per-task spawn (the editor's accumulated history is part of its value); losing the editor is never fatal — work-orders are self-contained, a fresh editor picks up from the next one alone — but losing it silently is a defect;
  - **the pre-compact handoff records the editor** — the handle a message can reach it by, a digest of what it has accumulated, and the recovery path (continue in place if alive; respawn and re-brief from the digest if not) — so the post-compact architect keeps its handle instead of spawning a blank editor;
  - draft from ground truth (read the files down to the leaf), never from memory or a description;
  - hand the editor **one self-contained work-order per change — always exactly one fenced block, always English** — objective, every contract/value pinned, guardrails (what not to touch, collision-safe order where it matters), the editor's self-verify commands, the report shape, an explicit "do not commit";
  - **pass skills by reference, never by retelling** — when the user's task arrives through a skill, the work-order pins the skill file's path and the argument string ("Read `~/.claude/skills/<name>/SKILL.md` and apply it with arguments: …") and the editor reads it itself; never restate or summarize skill content into a work-order (a retelling is a description; descriptions drift);
  - **parallel review** — the user's review command lands on the architect alone: send the editor its review work-order, run your own review concurrently, reach your own verdict independently, then reconcile (concede where the editor's catch is sharper, hold where the principle says so; adversarial — name the plantable failure; hunt propagation gaps); show the user your own review plus your summary of the editor's; the apply work-order leaves only on the user's go;
  - **verify the editor's report by fact**, never by its word — run your own greps/reads against the files;
  - keep a **private, architect-only buffer** for deferred items (what / why deferred / trigger) at `.ai-factory/notes/<NN>-architect-buffer.md` — notes numbering, so several architects coexist; ownership, not secrecy — no firewall: the editor is simply never told and no work-order references it; it is the one file the architect edits directly;
  - the **user rules the forks and owns the commits** — decisive on clear calls, surface the marginal fork, never commit without explicit permission; the architect **speaks Russian to the user, always**; re-invoked after every compact to restore the role — the body carries zero session state.
- Register the category: `CLAUDE.md` Repository Structure (the `src/agents/` zone + activation of the architect through `active/skills/` symlinks) and Upstream Sync ("never overwrite" — it is ours); `ARCHITECTURE.md` Skill categories.

## Files & types

- new `src/agents/agent-architect/SKILL.md`
- edit `CLAUDE.md` (Repository Structure + Upstream Sync), `ARCHITECTURE.md` (Skill categories)
- (activation, the working-set step) `active/skills/agent-architect` symlink → `../../src/agents/agent-architect`

## Guards

- **Process only** — the skill describes the paired loop, never what any project builds inside it; the unit of work is arbitrary, do not bake in "phase".
- **The editor is a separate agent** — a persistent subagent defined by its own sibling task (an agent definition, not a skill); this file is the architect alone; it names the editor as its counterpart but does not define it.
- **Spawn once, message thereafter** — never a per-task spawn; the apply work-order waits for the user's explicit go (the greenlight is a hard rule of the skill body).
- **Two-reader register** (per `docs/skill-composition-model.md`): imperatives for the executor, declarations for whoever edits the skill; pin the contracts (buffer is architect-only; work-orders are single fenced blocks; skills by reference; commit only on explicit permission), state rules as intent, cut procedural ceremony.
- Body ≤ 500 lines; frontmatter per the repo's authoring rules (quoted `argument-hint`).
- Design source: the architect handoff under `.ai-factory/handoffs/` (this task's companion) carries the full rehydration; the orchestrator authors `SKILL.md` from it — this task is planning only, no `SKILL.md` written here.

## Verification

- **Live continuity test first**: spawn the editor, send two work-orders in sequence via SendMessage — the second must land with the first still in the editor's context (history retained); only then verify the rest.
- Invoking the skill (from the active set) rehydrates the architect: it reasons/reviews in Russian, drafts single-block English work-orders, passes skills by reference, verifies by fact, keeps a private buffer in `.ai-factory/notes/`, and never edits the shared artifacts itself.
- `grep` the body for domain terms → none (process only); the unit of work is arbitrary.
- The new category appears in `CLAUDE.md` Repository Structure and `ARCHITECTURE.md` Skill categories; a re-sync does not overwrite it (listed under "never overwrite").
