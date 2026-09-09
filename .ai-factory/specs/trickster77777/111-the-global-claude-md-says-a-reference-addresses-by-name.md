# The global CLAUDE.md says a reference addresses by name

## Current state (grounded, read fresh)

`src/global/CLAUDE.md` § "Grounding claims" holds seven paragraphs. One says how to *follow* a reference — read down the chain of explicit references to the leaf, and attribute what you do not open rather than inventing it. None says how a reference is *written*: the file never mentions a line number, and the only paths it carries are `.ai-factory/` ones.

The discipline itself is ratified and has a home — `docs/reference-by-name.md` in this repository: a name survives every insertion above it, a line number survives none and nothing reports it when it rots, so a `file:line` is a defect report against its target. That home is reachable only from this repository. Every other project loads the global CLAUDE.md and nothing else of ours, so a project that meets the defect states the rule locally or not at all. One does: `tradeoxy_core`'s `.ai-factory/RULES.md` says a planning artifact cites `ARCHITECTURE.md` by the rule's own bolded name and never by a `:NNN` line number, because an insertion above silently retargets every numeric anchor and nothing checks that a moved anchor still names the rule it once did. None of that rule is about that project. A sweep of the `RULES.md`, `ARCHITECTURE.md` and `CLAUDE.md` of every repository here that carries an `.ai-factory/` — the other tradeoxy repositories, the orchestrator, and those under `mind` — finds no second statement of it anywhere, so what this task retires is one duplicate and not a pattern.

`active/CLAUDE.md` is already a symlink to `src/global/CLAUDE.md`, and `~/.claude/CLAUDE.md` points at that symlink, so editing the source is editing what every session loads. No symlink work.

## The change

One paragraph joins § "Grounding claims", immediately after the paragraph beginning "Before acting on an artifact" (the one ending "— never invent.") and immediately before the paragraph beginning "The opening task statement is the first artifact". It is pinned verbatim:

A reference addresses by **name**, never by position. A heading, a bolded rule, a symbol, a numbered item survives every insertion above it; a line number survives none, and nothing reports it when it rots. A `file:line` is a defect report against its target: the thing you needed had no name. The repair belongs there — add the name, or use the one present — never in the reference. Position addresses live in a work-order, thrown away when applied; they never enter a doc, a spec, or a roadmap line, which outlive the numbering they were written against.

Nothing else in the file changes.

Then one handoff goes to `tradeoxy_core`, into that repository's own `.ai-factory/handoffs/`, written after the paragraph is in place so it reports what is true. It is a new file in that folder's existing form — the next free number in its numbering, the `# Handoff — <slug>` title, and directly under it the mark line `**Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.` It says: the naming rule is now stated in the global CLAUDE.md, which that project already loads in every session; its local rule in `.ai-factory/RULES.md` is therefore a duplicate for that project to drop, on its own judgement and in its own time; and the `file:line` citations that same `RULES.md` carries in its other rules are instances of the very defect the rule names. Nothing in that repository is edited — not `RULES.md`, not any other file. Where the run cannot write into that folder because the directory was never made writable to it, it says so plainly and completes the rest of the task rather than failing it.

## Files & types

- edit: `src/global/CLAUDE.md` — § "Grounding claims", one inserted paragraph

## Guards

- The deep home is not linked. `docs/reference-by-name.md` exists only in this repository while this file is loaded in every project, so the paragraph carries no path to it and no path into any sibling repository.
- `tradeoxy_core`'s `RULES.md` is another repository's file. Dropping the local rule it now duplicates is that repository's own work, not this task's.

## Verification

Counts against a whitespace-normalized read of `src/global/CLAUDE.md`, never a line-oriented `grep`; the closing `git diff` check names its own scope.

- the paragraph appears verbatim → 1, and its neighbours are the two named paragraphs: the one above ends "— never invent." and the one below begins "The opening task statement is the first artifact"
- `reference-by-name` in the file → 0
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/global/CLAUDE.md` and nothing else
- the handoff exists in `tradeoxy_core`'s `.ai-factory/handoffs/` under the next free number in that folder, carries the mark line unprocessed, and names both the global paragraph and the local rule it makes redundant
- that repository is otherwise untouched → `git -C <tradeoxy_core> status --short` shows the new handoff and nothing else; `RULES.md` there is byte-identical to HEAD
