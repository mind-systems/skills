# Plan: 1.4 — command-handoff: rewrite to a lens over `note`

## Context
Rewrite `src/commands/command-handoff.md` from a 140-line engine-restating command into a ~80-line lens over the `note` engine — carrying only route plus policy, absorbing the destination invariant (a handoff always lives in `<root>/.ai-factory/handoffs/`), and cutting everything `note` already does. Behavior byte-equivalent except the destination fix.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rewrite command-handoff as a lens

- [x] **Task 1: Pin the pre-rewrite policy inventory (byte-equivalence checklist)**
  Files: (read-only) `src/commands/command-handoff.md`, `.ai-factory/specs/20-command-handoff-destination-always-handoffs.md`, `src/skills/note/SKILL.md`
  Do not edit yet. Read the current command and the spec, and record — as a working checklist for Task 3 — every load-bearing policy element that must survive the rewrite unchanged in meaning: (1) the meaning-tree mandate (verbose, leaf→branch→trunk, strip dross); (2) the next-step-scoped read-first map rule (must-read-now = only what the next action needs, per-work-unit trees when a session spans several units); (3) both shapes — the 11-section grid skeleton verbatim (section names + order + placeholder descriptions, which are the mining lens) and the prose/causal-thread directive; (4) the tree-completeness self-check gate and its explicit exemption of the paste-back pointer; (5) the verbosity directive text that overrides `note`'s Rule 1+2; (6) the semantic-slug rule (derived from subject, never the literal word `handoff`); (7) the minimal paste-back pointer contract (path, one-sentence frame, next step, optional work-unit count; exactly one chat block, not the full body); (8) the "write the handoff in English regardless of conversation language" directive. This checklist is the contract Task 2 must not break; it is not a file to write into the repo — keep it in-session for Task 3.

- [x] **Task 2: Rewrite the file as a lens** (depends on Task 1)
  Files: `src/commands/command-handoff.md`
  Rewrite the whole file to route + policy only, ~80 lines aspiration (never a clamp — the grid skeleton is legal payload mass, not ceremony). Requirements:
  - **Frontmatter stays functional and unchanged:** keep `loads: note`; keep `allowed-tools` at `note`'s full grant set plus `Skill` — `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` — do **not** strip `Write` or `Bash(mkdir *)`. `note` is loaded via the Skill tool and executes inline in the same agent; its Step 3 `mkdir -p <destination>` and `Write` are performed by the agent running this command, so the grants are required (a foreign-root handoff creates a new dir and writes into it). Spec 20's "no file mechanics re-enter the command" governs the **body** (no restated mkdir/Write prose), not the frontmatter grant set. Keep `argument-hint: ""` — spec 20 frames the destination as an invariant of the artifact, not a new parameter (this is a conscious keep, not a carry-over).
  - **Drop the literal `Read `$ARGUMENTS`` line:** under the new invariant `$ARGUMENTS`, when present, is a project-root **directory** naming where the handoff lives, not a file to read. The whole-file rewrite replaces that opener; the executor must not re-read the argument as a file.
  - **Destination invariant (the fix):** state as an invariant of the artifact — a handoff always lives in `<root>/.ai-factory/handoffs/`. A user-named path in `$ARGUMENTS` names the **project root only**; the destination is always `<that root>/.ai-factory/handoffs/`, never the named path itself and never `notes/`. With no target named, `<root>` is the current project. No new parameters, no modes. This resolved directory is what gets passed to `note`'s **destination-directory hook**.
  - **Keep as compressed policy** (from the Task 1 checklist): meaning-tree mandate, next-step-scoped read-first map, both shapes with the grid skeleton inline verbatim and the prose directive, the tree-completeness gate (with the paste-back-pointer exemption), the verbosity directive, the semantic-slug rule, the minimal paste-back pointer contract.
  - **Three `note` hooks** stay the delegation surface: destination directory (the resolved `<root>/.ai-factory/handoffs/`), template (the chosen shape — grid skeleton passed **blank** as the mining lens, or the free-form prose directive through the same hook), verbosity directive (the meaning-tree override text). Slug is `note`'s `$1`/topic derivation, supplied semantically.
  - **Cut everything `note` already does:** mining choreography, numbering, `mkdir`/`Write` mechanics, transitional/explanatory prose, and ceremony around the delegation — none may be restated. Follow the composition rule: a top loads the engine, never inlines it.
  - **Two-reader register throughout:** imperatives addressed to the executing agent, declarations addressed to the editor.
  - Write in English.

- [x] **Task 3: Verify against guards** (depends on Task 2)
  Files: (read-only) `src/commands/command-handoff.md`
  Confirm each spec guard before declaring done:
  - `grep -n "mkdir\|Write\|numbering" src/commands/command-handoff.md` → no re-stated engine mechanics in the **body**. `Write` matches as a bare substring, so eyeball each hit: benign, expected matches are the frontmatter `allowed-tools` line, "delegate to `note`, do not mkdir/Write/number yourself" negations, and the "Write **in English**" directive (a language rule, not a file mechanic — it survives the rewrite). Fail only on a hit that *restates* file mechanics as command procedure.
  - Frontmatter grant set preserved unchanged: `allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob Skill` — `Write` and `Bash(mkdir *)` NOT stripped (the agent executes `note`'s mkdir/Write inline). `loads: note` present and the three-hook delegation intact; no file mechanics re-stated in the body; `argument-hint: ""` retained; no `Read `$ARGUMENTS`` line remains.
  - Destination reasoning: an explicit foreign project path resolves to `<that root>/.ai-factory/handoffs/<NN>-<slug>.md`, never `notes/`; no-target case resolves to the current project's `.ai-factory/handoffs/`.
  - Byte-equivalence: walk the Task 1 checklist — every preserved policy element present and unchanged in meaning (grid skeleton section names/order/placeholders verbatim; gate semantics, pointer contract, verbosity/slug rules intact).
  - Line count near the ~80 aspiration (report actual; do not pad or clamp — skeleton mass is legal).
  - Note for the reviewer: the spec's live pre/post session-baseline check (same tree at same depth, identical pointer structure) requires a real mineable session and is performed by the user, not the orchestrator — flag it as user-run, do not fabricate a baseline.
