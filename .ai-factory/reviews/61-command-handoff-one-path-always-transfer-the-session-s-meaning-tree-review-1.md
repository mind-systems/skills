## Code Review — milestone 61 (command-handoff single path + note verbosity hook)

**Files reviewed (code changes only):**
- `src/skills/note/SKILL.md` — engine, verbosity-hook broadening (Rule-2 override) + template free-form
- `src/commands/command-handoff.md` — caller, collapse to single path

Read both in full plus governing spec `specs/15-…meaning-tree.md` and the other `note` caller (`roadmap-engine`). Reference tree resolved: `ROADMAP.md:133` → spec 15 → the two files.

### Verification gates (spec §"How to verify") — all pass
Ran each grep against the edited working tree:
- #2 `<NN>|highest existing prefix|zero-padded` in command-handoff → **empty** (numbering delegated to `note`). ✓
- #4 `compact` → **empty** (boundary-neutral preserved). ✓
- #5 `always apply|other Important Rules` in note → only file-paths/English named as always-on; **no** clause names findings-focus as always-on. Both hits read "File paths and English…". ✓
- #7 `proportional` in command-handoff → **empty**. ✓
- #8 `register|note mode|chat mode|destination axis|note destination|Write.*(direct|itself)` → **empty** (completeness gate clean; both direct-write sites collapsed). ✓
- token target `200k|token` → **empty** in both files (metaphor not encoded). ✓

### Additivity / load-once contract — holds
`grep -rn "^loads:.*\bnote\b"` returns exactly `roadmap-engine` and `command-handoff`. `roadmap-engine` invokes `note` with a **destination** hook only (`SKILL.md:35-36`) and no verbosity directive, so the Rule-2 broadening is inert for it — unset ⇒ default Rule 1 + Rule 2, byte-identical. The `note` diff leaves Rule text 1–5, the default template block, and Steps 1–4 mechanics untouched; only the two hook descriptions and the one template-note sentence changed. Strict-additive guarantee confirmed by `git diff`.

### Caller correctness — sound
- Both shapes now delegate mining/population to `note`; the old Step-1 agent-mining instruction is reframed as `note`'s **lens** (`command-handoff.md:17-31`), pre-empting the milestone-55 double-mining regression.
- The fixed invariant is at the Step-2 opener (`:37`), governing both shapes before the shape-specific headings.
- The verbosity directive passed to `note` (`:119`) explicitly names the Rule-2 override — correctly coupled to the engine change; the prose shape works *only because* Rule 2 is now overridable.
- Self-check (`:109`) tests tree-completeness; the paste-back-pointer exemption (`:131`) quotes it consistently — no orphaned proportionality reference.
- `allowed-tools` retains `Write Bash(mkdir *)` now-unused — per spec ("unused, not newly granted"); not a defect.

### Findings

**1. [Low, non-blocking] `note` SKILL.md:62 still says "caller's skeleton verbatim" — stale sibling of the broadened template hook at `:32`.**
The Template hook description was broadened at `:32` to permit *"a section skeleton **or** a free-form (non-skeleton) body directive … (grid or prose)."* But the second site describing the same behavior — the "Note file template" sentence at `:62` — still reads *"the note body follows the caller's **skeleton** verbatim instead."* This is the exact stale-sibling pattern the milestone's engine half is built to avoid (the Rule-2 fix names all three sites precisely; the template broadening updated only one of its two). Runtime impact is minimal — an agent follows the caller's directive verbatim regardless of the label, and `:32` is the authoritative hook definition — but for the **prose-shape** handoff, which passes `note` a free-form (non-skeleton) directive, `:62`'s "skeleton" wording is narrower than the hook it describes and could read as "coerce into a skeleton." Recommend aligning `:62` to "the note body follows the caller's directive (section skeleton or free-form) verbatim instead," matching `:32`.

### Summary
The change faithfully implements spec 15: single path, `note`-owned numbering, Rule-2 override wired end-to-end, boundary-neutral framing intact, no literal token target, and every roadmap-family caller byte-identical for the unset case. One low-severity documentation-consistency nit (`note:62`), non-blocking.
