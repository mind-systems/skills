# Task Spec — command-handoff (self-handoff prompt command that survives /compact)

**Date:** 2026-06-01
**Roadmap:** ROADMAP.md Milestones
**Provenance:** user request; concept from note `10-continuation-handoff-skill.md`.

## Current state

There is no first-class way to produce a high-quality continuation/handoff prompt before a `/compact` or a fresh session. The user currently does it with an ad-hoc freeform prompt ("I'm about to compact, write me instructions on what we're doing and the next step, plus a map of what to read to rehydrate context"). It works well but **fires inconsistently** — being freeform, the agent sometimes interprets it loosely instead of treating it as a fixed instruction. The built-in `/compact` summary is the fallback and is impoverished: it keeps recent transcript but drops the domain model, the working discipline, and the error log, so the next turn behaves like amnesia.

The repo hosts skills under `.claude/skills/`, symlinked globally via `~/.claude/skills` → `~/projects/skills/.claude/skills` (a whole-dir symlink). The `.claude/commands/` directory and its `~/.claude/commands` symlink are now provisioned (empty, awaiting the command file). `CLAUDE.md` ("Repository Structure" and "Upstream Sync") and `ARCHITECTURE.md` still describe skills only — no mention of commands.

## Target

Create a **slash command** (NOT a skill) named `command-handoff`, invoked as `/command-handoff`, that mines the live conversation and emits a dense, self-contained handoff/continuation prompt the user pastes after `/compact` to rehydrate the whole effort.

Why a command, not a skill: it's just a fixed prompt the user always triggers manually. Naming avoids the `aif-` prefix on purpose — `aif-*` is the upstream-synced domain (`github.com/lee-to/ai-factory`) and must not be touched; `command-handoff` is clearly ours. Functionally a command runs in the main session and inherits its tools — it grants no new capability; `allowed-tools` in command frontmatter only **pre-approves** specific calls to skip permission prompts. No namespace conflict with skills.

**Steps:**

1. **Prerequisites — already provisioned, do NOT create.** The `.claude/commands/` directory and the `~/.claude/commands` → repo symlink already exist (provisioned out-of-band, as the orchestrator lacks rights to create system-level symlinks). The command is globally resolvable as soon as its file exists. Do no `mkdir`/`ln` work.

2. **Write `.claude/commands/command-handoff.md`** with frontmatter:
   - `description` — what it does + when (run before compact while context is still full).
   - `argument-hint: "[note]"` (quote the brackets per repo convention).
   - `allowed-tools: Read Write Glob Bash(ls *)` — needed only by the note path, which writes the file inline (Glob/`ls` to scan existing `<NN>` notes, Write to author it). Pre-approves to avoid a permission stall. The default chat path uses no tools.

3. **Default behavior (no args):** emit the handoff prompt to **chat only** — the ~95% copy-paste case. No file written.

4. **Note trigger:** if `$ARGUMENTS` contains any of `note`, `ноут`, `давай ноут`, `с ноутом` → ALSO persist the handoff to disk. **The command writes the file itself (Write); it must not route this through `aif-note`** — aif-note reshapes content into its own note template and would lose the skeleton. Persist the exact handoff emitted to chat, in the step-6 skeleton format. Filing convention (same numbering rule as aif-note, applied inline): `mkdir -p .ai-factory/notes`; `<NN>` = next zero-padded two-digit prefix found by scanning `[0-9][0-9]-*.md` and incrementing the highest; **`<slug>` derived semantically from the session's subject matter** (lowercase, hyphens), not a hardcoded `handoff`; English. Path: `.ai-factory/notes/<NN>-<slug>.md`. The default (no-arg) path stays chat-only and writes nothing.

5. **Output language:** English regardless of conversation language (matches repo doc conventions).

6. **Content skeleton — mined from the live session, not a blank template.** Core sections (always, omit only if genuinely empty):
   1. **Frame** — one line: where we are + the load-bearing instruction *"the chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory."*
   2. **Read-first map** — the highest-value section. **Two tiers:** (a) *must-read now* — the minimal set of files that rehydrate everything, each with a one-line "what it answers", lead with the single best entry doc; (b) *read-on-demand* — not required up front, but go there on the first related question.
   3. **Current state** — done vs in-flight; explicitly call out **uncommitted** working-tree state.
   4. **Next step** — the one thing to do next, and who does what.
   5. **Working discipline** — the user's decision rhythm (confirm-before-execute, "show the diff before applying", when to stop and ask). Always dropped by summaries.
   6. **Error log** — concrete mistakes made this session and their corrections, named specifically, so they aren't repeated.

   Optional sections (include only if the session actually has them):
   7. **Orientation** — moving parts; "two of a kind" traps (e.g. two roadmaps, two agents) that are easy to confuse.
   8. **Domain model spine** — the settled model in one screen, with "don't re-litigate" + a pointer per point.
   9. **Hard rules** — commits/permission, file language, memory-write triggers, project conventions.

   Tone: dense, organized, addressed to the next agent ("you are picking up…").

   **This skeleton is the format for both outputs** — the chat message AND the inline-written file (step 4) use it verbatim. There is no second, reshaped format; the durable file is the same handoff.

7. **Update `CLAUDE.md`** (part of this task):
   - *Repository Structure* — add `.claude/commands/` as a new artifact type: our slash commands (e.g. `command-handoff`).
   - *Upstream Sync* — add a line: `.claude/commands/` are ours and are **never** synced/overwritten from upstream.

8. **Update the linking guide** (part of this task). A guide already exists: `README.md` → "Setup (one-time, per machine)" (currently a single `ln -s ~/projects/skills/.claude/skills ~/.claude/skills`). It covers **only** the skills symlink and never mentions commands. Update it to also document the commands symlink (`ln -s ~/projects/skills/.claude/commands ~/.claude/commands`) so a fresh machine links both. Keep the "that's it / no per-project config" framing. (If at implementation time no such guide exists anymore, write one in README.) Match the surrounding doc language/tone.

9. **Register the new artifact type in `ARCHITECTURE.md`** (part of this task). `ARCHITECTURE.md` opens with "this repo produces skills" and frames everything through skill anatomy/categories; it has no notion of `.claude/commands/`. Add a one-line note that the repo also hosts slash commands under `.claude/commands/`, so ARCHITECTURE.md and CLAUDE.md don't diverge on what the repo produces. Keep it to a line — do not restructure the doc.

## Guards

- **Run before compact, not after.** The command mines the live conversation; after `/compact` there is nothing to mine. Make this timing explicit in the command's `description`/body.
- **The note path writes the file inline — do NOT route through `aif-note`** (it would reshape the handoff into its own template and lose the skeleton). The command persists the skeleton verbatim via Write.
- **Filename slug is semantic** — derived from the session's subject matter (lowercase, hyphens), the way aif-note derives its slug. **Not** a hardcoded `handoff`. `<NN>` is the next free two-digit prefix in `.ai-factory/notes/`.
- **The file format = the chat format** — the step-6 skeleton, identical for both. No reshaping.
- **`argument-hint` brackets must be quoted** (`"[note]"`) — unquoted breaks YAML in some agents (repo convention).
- The default path writes **no file** and uses **no tools** — keep it pure chat output; only the `note` trigger touches disk.

## Files

- `~/projects/skills/.claude/commands/command-handoff.md` (new) — the command. (Its parent dir and the `~/.claude/commands` symlink already exist — see Prerequisites.)
- `~/projects/skills/CLAUDE.md` (modify) — Repository Structure + Upstream Sync.
- `~/projects/skills/README.md` (modify) — "Setup" section: add the commands symlink alongside the skills one.
- `~/projects/skills/.ai-factory/ARCHITECTURE.md` (modify) — one line registering `.claude/commands/` as a hosted artifact type.

## Verify

- `/command-handoff` in a real session emits a chat-only handoff prompt with the core 6 sections, English, with a two-tier read-first map.
- `/command-handoff note` (or `ноут`) additionally writes `.ai-factory/notes/<NN>-<slug>.md` **inline** — the same skeleton it emitted to chat, correct next `<NN>`, semantic slug (not hardcoded `handoff`). aif-note is never invoked.
- Once the command file exists, `/command-handoff` resolves globally (the symlink is already in place) and does not collide with any skill name.
- `ARCHITECTURE.md` and `CLAUDE.md` agree that the repo hosts both skills and commands.
