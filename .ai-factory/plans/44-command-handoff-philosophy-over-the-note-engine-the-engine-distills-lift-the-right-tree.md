# Plan: command-handoff: philosophy over the note engine — the engine distills; lift the right tree

## Context
Rework `command-handoff` into a philosophy over the `note` engine: `note` gains a generic verbosity hook, note mode delegates distillation + file mechanics to `note`, and the read-first map is scoped to the next step instead of inflating into a full session inventory.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Extend the note engine

- [x] **Task 1: Add the verbosity hook to `note`**
  Files: `src/skills/note/SKILL.md`
  Add a third optional caller input alongside the existing **Destination directory** and **Template** hooks in the "Hooks (caller inputs)" section (currently "Two optional inputs…" — update the count/wording to three):
  - **Verbosity directive** — free-text depth/length policy for the distillation. Unset → the current default (Important Rule 1, "Be concise"). When set, the caller's directive **replaces** the default concision rule for this run; all other Important Rules still apply.
  Adjust the sentence in Step 3 that currently binds the Important Rules unconditionally ("The Important Rules (concise, findings-focused, include file paths, English) apply to both cases") so concision is stated as the *default* verbosity directive that a caller-supplied directive takes the place of, while findings-focus / file-paths / English still always apply. Keep the phrasing **generic** — no mention of `command-handoff` or handoffs; standalone `/note` with no hooks stays behavior-identical.
  Before editing, confirm the reverse graph: `grep -l "note" src/skills/*/SKILL.md src/commands/*.md` then check which actually load the engine — the only current engine caller is `roadmap-engine`, which supplies only the destination hook and no verbosity, so it is unaffected. Verify this still holds.

### Phase 2: Rework the command as a philosophy over the engine

- [x] **Task 2: Scope the read-first map to the next step** (depends on Task 1)
  Files: `src/commands/command-handoff.md`
  Rework the **## 2. Read-first map** part of the skeleton (and any surrounding guidance) so the map serves the **next step**, not the session inventory: "Must-read now" = only what a fresh agent must read to execute the next action and avoid the error log; exclude subsystems that were touched but require nothing from the successor. State the multi-tree case explicitly: a session spanning several independent work-units hands off several small cross-linked trees, not one merged inventory tree — the skill already cross-links well, keep that. Align this rule with the existing proportionality guard, in the same register. Do NOT shrink the error log or the working-discipline sections — the fix targets over-lifting only.

- [x] **Task 3: Delegate note mode to the engine + fix frontmatter** (depends on Task 2)
  Files: `src/commands/command-handoff.md`
  Two coupled changes:
  1. **Frontmatter:** add `loads: note`. Widen `allowed-tools` to the union of the command's own needs and `note`'s grants plus `Skill` — i.e. `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` (never a partial copy).
  2. **Note mode (Step 3):** replace the command's own note-mode mining/composition/file-mechanics choreography — delete the `ls`/`<NN>`-scan/slug/`mkdir`/Write instructions and the "do not route through /note" note. Instead, ensure `note` is loaded once this chat and produce the handoff **through `note`'s own flow**, supplying only hooks:
     - destination = `.ai-factory/handoffs/`
     - template = the handoff skeleton passed **blank** — its placeholder descriptions are the mining lens (do NOT pre-fill it; a filled skeleton that makes distillation a no-op is the explicitly rejected approach)
     - verbosity directive = the handoff's proportionality policy (output tracks how much was done; enumerate work-units individually; never collapse a subsystem; small session → short handoff) plus the self-check gate, applied to the note-file content before the Write
     - slug = derived semantically from the session subject (never the literal word `handoff`)
     `note`'s own Step 4 report is not surfaced; the command emits only its minimal paste-back pointer (path, one-sentence frame, next step) — exactly one chat block.
     **Chat mode stays a direct compose-and-emit path** (no file, no engine): the agent composes per the same skeleton + verbosity policy and emits to chat. The skeleton and proportionality/verbosity policy text live once in the command, shared by both modes; note mode references them as the hooks' values rather than restating them. Keep the skeleton, proportionality guard, error-log-first rule, self-check gate, semantic-slug rule, and paste-back pointer format — only their *application* in note mode moves into the engine's flow.
