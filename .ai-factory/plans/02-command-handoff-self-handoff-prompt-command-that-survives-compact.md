# Plan: command-handoff — self-handoff prompt command that survives /compact

## Context
Add a new slash command `/command-handoff` that mines the live session and emits a dense, self-contained handoff prompt (with an optional inline-written durable note), and register `.claude/commands/` as a hosted artifact type across the repo's docs.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Author the command

- [x] **Task 1: Write the `command-handoff` slash command**
  Files: `.claude/commands/command-handoff.md` (new)
  Author the command file (its parent dir `.claude/commands/` and the `~/.claude/commands` symlink already exist — do NOT `mkdir`/`ln`).
  Frontmatter:
  - `description` — what it does + when to run it. Make the timing explicit: **run before `/compact`, while context is still full** (after compact there is nothing to mine).
  - `argument-hint: "[note]"` — brackets quoted per repo convention.
  - `allowed-tools: Read Write Glob Bash(ls *)` — used only by the note path (Glob/`ls` to scan existing `<NN>` notes, Write to author the file). Pre-approves to skip permission stalls; the default chat path uses no tools.
  Body — two behaviors:
  - **Default (no args):** emit the handoff prompt to **chat only** (~95% case). Write no file, touch no tools.
  - **Note trigger:** if `$ARGUMENTS` contains any of `note`, `ноут`, `давай ноут`, `с ноутом` → ALSO persist the exact same handoff. The command writes the file itself via Write — it must **not** invoke/route through `aif-note` (that would reshape into aif-note's template and lose the skeleton). Filing (same numbering rule as aif-note, inline): `mkdir -p .ai-factory/notes`; `<NN>` = next zero-padded two-digit prefix found by scanning `[0-9][0-9]-*.md` and incrementing the highest; `<slug>` derived **semantically** from the session's subject matter (lowercase, hyphens) — NOT a hardcoded `handoff`. Path: `.ai-factory/notes/<NN>-<slug>.md`.
  Output language: **English** regardless of conversation language.
  **Content skeleton** (mined from the live session, not a blank template) — this single skeleton is the format for BOTH the chat message and the inline file, verbatim, no second reshaped format. Core sections (always; omit only if genuinely empty):
  1. **Frame** — one line: where we are + the load-bearing instruction *"the chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory."*
  2. **Read-first map** — highest-value section, **two tiers:** (a) *must-read now* — minimal set that rehydrates everything, each with a one-line "what it answers", lead with the single best entry doc; (b) *read-on-demand* — go there on the first related question.
  3. **Current state** — done vs in-flight; explicitly call out **uncommitted** working-tree state.
  4. **Next step** — the one thing to do next, and who does what.
  5. **Working discipline** — the user's decision rhythm (confirm-before-execute, "show the diff before applying", when to stop and ask).
  6. **Error log** — concrete mistakes made this session and their corrections, named specifically.
  Optional sections (only if the session has them): 7. **Orientation** ("two of a kind" traps), 8. **Domain model spine** (settled model + "don't re-litigate" + pointer per point), 9. **Hard rules** (commits/permission, file language, memory-write triggers, conventions).
  Tone: dense, organized, addressed to the next agent ("you are picking up…").

### Phase 2: Register `.claude/commands/` as a hosted artifact type

- [x] **Task 2: Update `CLAUDE.md`** (depends on Task 1)
  Files: `CLAUDE.md`
  - *Repository Structure* — add `.claude/commands/` as a new artifact type: our slash commands (e.g. `command-handoff`).
  - *Upstream Sync* — add a line that `.claude/commands/` are **ours** and are **never** synced/overwritten from upstream (alongside the custom-skills list).

- [x] **Task 3: Update `README.md` Setup guide** (depends on Task 1)
  Files: `README.md`
  In "Setup (one-time, per machine)", add the commands symlink alongside the existing skills one: `ln -s ~/projects/skills/.claude/commands ~/.claude/commands`, so a fresh machine links both. Keep the "that's it / no per-project config" framing and match surrounding doc language/tone.

- [x] **Task 4: Update `ARCHITECTURE.md`** (depends on Task 1)
  Files: `.ai-factory/ARCHITECTURE.md`
  Add a one-line note that the repo also hosts slash commands under `.claude/commands/`, so ARCHITECTURE.md and CLAUDE.md agree on what the repo produces. Keep it to a line — do not restructure the doc.
