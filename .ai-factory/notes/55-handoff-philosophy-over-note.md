# command-handoff: philosophy over the note engine; lift the right tree, not the maximal one

**Date:** 2026-07-03
**Source:** conversation context (notes-are-specs review)

## Key Findings

- `command-handoff` carries its own file-writing machinery (numbering scan, slug rules, `mkdir`, Write protocol for `.ai-factory/handoffs/`) — a hand-rolled copy of what the `note` engine does. With note 53's hooks, the command becomes a **philosophy over the note engine**: it keeps the session-mining lens and the handoff skeleton (its policy) and delegates the file mechanics (mechanism) to `note`, passing destination `.ai-factory/handoffs/` and its own skeleton as the template. The handoff skill gets stronger, not thinner — its whole body is now about *what to hand off*.
- Format complaint to fix while here: the handoff's read-first map **over-lifts** — it tends to raise a maximal tree instead of the tree the receiving agent actually needs. The map is a *lazy tree scoped to the next step* (the follow-mentions principle applied to handoffs): root = the next action, branches = only what that action needs read first. When a session genuinely spanned several independent work-units, **several small trees with cross-links between them are correct** — the skill already does cross-linking well; keep that. The failure mode is one inflated inventory-tree of everything touched.

## Details

### Edit 1 — delegate note mode to the engine

Replace the note-mode file mechanics (steps that `ls .ai-factory/handoffs/`, compute `<NN>`, derive slug, Write the file) with: ensure `note` is loaded once this chat, then produce the handoff file through it — destination `.ai-factory/handoffs/`, template = the handoff skeleton, content = the mined handoff verbatim (the engine must not reshape it — note 53 guarantees caller templates pass through). Keep: the semantic-slug rule (never the literal word `handoff`), the minimal chat pointer, the pointer's paste-back format. Add `loads: note` to frontmatter.

### Edit 2 — the map lifts the scoped tree

Rework the read-first-map section of the skeleton instructions: the map serves the **next step**, not the session inventory — include what a fresh agent must read to execute the next action and avoid the error log; exclude subsystems that were touched but require nothing from the successor. State the multi-tree case explicitly: a session spanning several independent work-units hands off several small trees with cross-links, not one merged tree. The existing proportionality guard already points this way — align the map rule with it in the same register.

### Constraints

- Chat mode (no file) unchanged except the map rework, which applies to both modes.
- The mining discipline, proportionality guard, error-log-first rule, and self-check gate stay — they are the philosophy.
- Depends on note 53 (hooks) being implemented; independent of note 54.

## What NOT to do

- Do not let `note`'s default template leak into handoffs — the skeleton is supplied by this command, verbatim.
- Do not shrink the error log or the working-discipline sections — the fix targets the map's over-lifting only.
- Do not move existing handoff files or renumber anything.
