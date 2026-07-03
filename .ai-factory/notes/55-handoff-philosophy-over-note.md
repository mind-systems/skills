# command-handoff: philosophy over the note engine — the engine distills; lift the right tree

**Date:** 2026-07-03
**Source:** conversation context (notes-are-specs review; respec after first implementation attempt)

## Key Findings

- `command-handoff` duplicates the `note` engine's core behavior: it carries its own mine-the-context instruction (Step 1), its own compose-the-body choreography (Step 2), and its own file-writing machinery (numbering scan, slug rules, `mkdir`, Write). But distillation is performed by the agent in-context either way — the agent only needs *one* instruction for it, and that instruction is `note`. The command becomes a **philosophy over the note engine**: it keeps the lens (the handoff skeleton, whose placeholder descriptions state what to mine), the verbosity policy, the semantic-slug rule, and the minimal chat pointer — and in note mode hands the **blank** skeleton to `note`, which does the distillation and the file mechanics itself.
- A first implementation attempt took the opposite reading — `command-handoff` composed the full body itself and passed it to `note` as a *fully-populated* template so the engine's distillation became a no-op. That inverts the composition model (the philosophy pre-does the engine's work and keeps a duplicate mining instruction); it is explicitly rejected. The correct fix for the "note trims what handoff wants verbose" tension is a new **verbosity hook on `note`**, not a filled-template workaround.
- Format complaint to fix while here: the handoff's read-first map **over-lifts** — it tends to raise a maximal tree instead of the tree the receiving agent actually needs. The map is a *lazy tree scoped to the next step* (the follow-mentions principle applied to handoffs): root = the next action, branches = only what that action needs read first. When a session genuinely spanned several independent work-units, **several small trees with cross-links between them are correct** — the skill already does cross-linking well; keep that. The failure mode is one inflated inventory-tree of everything touched.

## Details

### Edit 1 — `note` gains a third hook: verbosity/depth directive

In `src/skills/note/SKILL.md`, alongside the destination and template hooks, add a third optional caller input:

- **Verbosity directive** — free-text depth/length policy for the distillation. Unset → the current default (Important Rule 1, "Be concise"). When set, the caller's directive **replaces** the default concision rule for this run; all other Important Rules still apply.

Adjust the wording that currently binds Rule 1 unconditionally ("The Important Rules … apply to both cases") so it reads: concision is the *default* verbosity directive; a caller-supplied directive takes its place. Generic phrasing — no mention of `command-handoff` or handoffs; the hook serves any caller. Standalone `/note` with no hooks set stays behavior-identical. Before editing the engine, grep its callers (reverse graph: `loads:` fields) — today the only one is `roadmap-engine`, which supplies just the destination hook and no verbosity, so it is unaffected by construction; verify this still holds at implementation time.

### Edit 2 — delegate note mode to the engine (engine distills)

Rework `src/commands/command-handoff.md` note mode: ensure `note` is loaded once this chat (`loads: note` in frontmatter), then produce the handoff **through `note`'s own flow** — the engine mines the conversation and fills the skeleton; the command supplies only hooks:

- destination = `.ai-factory/handoffs/`
- template = the handoff skeleton, passed **blank** — its placeholder descriptions are the mining lens
- verbosity directive = the handoff's proportionality policy (output tracks how much was done; enumerate work-units individually; never collapse a subsystem; small session → short handoff) plus the self-check gate, which is applied to the note-file content before the Write
- slug = derived semantically from the session subject (never the literal word `handoff`)

Delete the command's own note-mode mining/composition/file-mechanics choreography — no pre-composed body, no `ls`/`<NN>`/`mkdir`/Write instructions. `note`'s own Step 4 report is not surfaced; the command emits only its minimal paste-back pointer (path, frame, next step) — exactly one chat block.

Chat mode keeps a direct compose-and-emit path (no file, no engine): the agent composes per the same skeleton and verbosity policy and emits to chat. The skeleton and policy text live once in the command, shared by both modes; note mode must not restate them — it references them as the hooks' values.

Frontmatter: `allowed-tools` must cover the engine's whole mechanism when applied in-context — the union of the command's own needs and `note`'s grants (`Read Write Bash(ls *) Bash(mkdir *) Glob`) plus `Skill`; never a partial copy.

### Edit 3 — the map lifts the scoped tree

Rework the read-first-map section of the skeleton: the map serves the **next step**, not the session inventory — include what a fresh agent must read to execute the next action and avoid the error log; exclude subsystems that were touched but require nothing from the successor. State the multi-tree case explicitly: a session spanning several independent work-units hands off several small trees with cross-links, not one merged tree. The existing proportionality guard already points this way — align the map rule with it in the same register.

### Constraints

- The skeleton, proportionality guard, error-log-first rule, self-check gate, semantic-slug rule, and paste-back pointer format stay — they are the philosophy; only their *application* in note mode moves into the engine's flow via hooks.
- Depends on note 53 (hooks) being implemented; independent of note 54.

## What NOT to do

- Do not pass a pre-filled template to `note` — the engine distills; a filled skeleton that makes distillation a no-op is the rejected first attempt.
- Do not let `note`'s default template or default concision leak into handoffs — both are replaced via hooks.
- Do not make the verbosity hook handoff-specific in `note` — it is a generic caller input.
- Do not shrink the error log or the working-discipline sections — the map fix targets over-lifting only.
- Do not move existing handoff files or renumber anything.
