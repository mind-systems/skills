# Plan: agents: Architect — plan-and-review skill of the paired loop (new `src/agents/` category)

## Context
Package the plan-and-review half of the architect↔editor loop as an invocable skill and open a new `src/agents/` category to host it. The architect persona rehydrates on invocation, never edits shared artifacts, drives a persistent editor subagent by work-order, and speaks Russian to the user.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Author the architect skill

- [x] **Task 1: Author `src/agents/agent-architect/SKILL.md` from the design source**
  Files: `src/agents/agent-architect/SKILL.md`
  Create the new directory `src/agents/agent-architect/` and author its `SKILL.md`. **The design source is the companion handoff `.ai-factory/handoffs/09-architect-paired-loop.md`** — the orchestrator authors the skill body from it; do not invent process, transcribe and shape the handoff's disciplines. Also read the spec `.ai-factory/specs/16-agents-architect-skill.md` for the exact contracts.
  Frontmatter (exact): `name: agent-architect`, `description:` (what it does + when to use — the architect persona of the paired plan-and-review loop, invoked by the user), `argument-hint: "[unit of work — e.g. a phase, a task, a file]"` (brackets **must** be quoted), `user-invocable: true`, `disable-model-invocation: true`, `allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage`. `name` must match the directory name exactly.
  Body — the architect's operating discipline over **any unit of work** (a roadmap phase, one task, a class, a module, a review dimension — the loop is invariant, only the unit changes); each discipline from handoff 09:
  - reason and review; **never edit the shared artifacts** (roadmap, specs, code, docs) — the editor applies every change; the architect's only direct write is its own buffer;
  - **spawn the editor once, message it thereafter** — one `Agent` spawn at the start of the work, every subsequent work-order via `SendMessage` into the same conversation; never a per-task spawn (accumulated history is part of the editor's value); losing the editor is recoverable (work-orders are self-contained) but losing it silently is a defect;
  - **pre-compact handoff records the editor** — the reachable handle, a digest of what it accumulated, and the recovery path (continue in place if alive; respawn + re-brief from the digest if not);
  - **draft from ground truth** — read the files down to the leaf; never from memory or a description;
  - **one self-contained work-order per change — always exactly one fenced block, always English** — objective, every contract/value pinned, guardrails (what not to touch, collision-safe order where it matters), the editor's self-verify commands, the report shape, an explicit "do not commit";
  - **pass skills by reference, never by retelling** — pin the skill file's path + argument string (`Read \`~/.claude/skills/<name>/SKILL.md\` and apply it with arguments: …`); the editor reads it itself; never restate/summarize skill content;
  - **parallel review with reconcile** — the review command lands on the architect alone: send the editor its review work-order, run your own review concurrently, reach an independent verdict, then reconcile (concede where the editor's catch is sharper, hold where the principle says so; adversarial — name the plantable failure; hunt propagation gaps); show the user your own review + your summary of the editor's; the apply work-order leaves **only on the user's explicit go**;
  - **verify the editor's report by fact** — run your own greps/reads against the files, never trust the word;
  - **private, architect-only buffer** for deferred items (what / why deferred / trigger) at `.ai-factory/notes/<NN>-architect-buffer.md` (notes numbering, so several architects coexist; ownership not secrecy — no firewall, the editor is simply never told; the one file the architect edits directly);
  - **the user rules the forks and owns the commits** — decisive on clear calls, surface the marginal fork, never commit without explicit permission; **speaks Russian to the user, always**; the work-order block itself is always English; re-invoked after every compact — the body carries zero session state.
  Constraints: **process only** — describe the paired loop, never any project's domain; the unit of work is arbitrary, do not bake in "phase". **Two-reader register** (per `docs/skill-composition-model.md`): imperatives for the executor, declarations for whoever edits the skill; pin the contracts (buffer is architect-only; work-orders are single fenced blocks; skills by reference; commit only on explicit permission); state rules as intent, cut procedural ceremony. Body ≤ 500 lines. Do **not** define the editor here — it is a separate sibling agent (task 17); name it as counterpart only.

### Phase 2: Register and activate the new category

- [x] **Task 2: Register the `src/agents/` category in `CLAUDE.md`** (depends on Task 1)
  Files: `CLAUDE.md`
  Three edits, all registering the new category as ours:
  - **Repository Structure tree** (`:31-60`): add an `agents/` zone under `src/` parallel to `skills/`, `commands/`, `global/` — e.g. `│   ├── agents/                   #   paired-loop agent skills (agent-architect + editor)`.
  - **Active-set paragraph** (`:62`): add `agent-architect` to the list of our skills the active set loads (it activates through `active/skills/` like the rest).
  - **Upstream Sync** (`:177`): `agent-architect` (and the `src/agents/` zone) is ours with no upstream counterpart — a re-sync must never overwrite it. Extend the "Everything else … is ours" statement to cover `src/agents/` so the never-overwrite guarantee is explicit.

- [x] **Task 3: Register the `agents` category in `ARCHITECTURE.md`** (depends on Task 1)
  Files: `.ai-factory/ARCHITECTURE.md`
  In **Skill categories** (`:15-24`): record the new `src/agents/` category — the paired-loop agent skills (architect + editor), parallel to `src/skills/` and `src/commands/`. Extend the three-zone provenance sentence (`:24`) if needed so `src/agents/` is covered under "skills we authored". Keep it a category note, not a file listing.

- [x] **Task 4: Activate the architect through `active/skills/`** (depends on Task 1)
  Files: `active/skills/agent-architect` (symlink)
  Create the working-set symlink: `ln -sfn ../../src/agents/agent-architect active/skills/agent-architect`. Verify it resolves to `src/agents/agent-architect/SKILL.md` (the target path is relative to `active/skills/`; `../../` reaches the repo root, then `src/agents/agent-architect`).

### Phase 3: Verify

- [x] **Task 5: Verify the skill and the paired loop** (depends on Tasks 1-4)
  Files: (none — verification only)
  - **Live continuity test first**: spawn the editor subagent (`Agent`), send two work-orders in sequence via `SendMessage` — the second must land with the first still in the editor's context (history retained). This is the gating check.
  - Invoking the skill from the active set rehydrates the architect: reasons/reviews in Russian, drafts single-block English work-orders, passes skills by reference, verifies by fact, keeps a private buffer under `.ai-factory/notes/`, never edits the shared artifacts itself.
  - `grep` the skill body for domain terms → none (process only; the unit of work is arbitrary).
  - Confirm the new category appears in `CLAUDE.md` Repository Structure + active set and in `ARCHITECTURE.md` Skill categories, and that Upstream Sync lists it under "never overwrite".

## Commit Plan
- **Commit 1** (after task 1): "Add agent-architect skill and src/agents category"
- **Commit 2** (after tasks 2-4): "Register and activate the agents category"
