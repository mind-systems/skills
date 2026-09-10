# `roadmap-test-coverage`'s own numbering scan carries three defects, not one

## Current state (grounded, read fresh)

`src/skills/roadmap-test-coverage/SKILL.md` mints its own note numbers in Layer 4 rather than calling `note`: "Determine next note number:" followed by

```bash
mkdir -p .ai-factory/specs
find .ai-factory/specs -name "[0-9][0-9]-*.md" | sort | tail -1
```

"Extract highest two-digit prefix + 1. If none, start at `01`. Store as `$NEXT_NOTE_NUM`." It never loads `note` — the file's own `loads:` field names only `test-philosophy roadmap-engine` — so the family's usual sweep for `note`'s callers cannot see this carrier at all.

Three defects, each verified independently rather than inferred from the others:

**The pattern sees two digits only.** `-name "[0-9][0-9]-*.md"` matches exactly two leading digits — the identical shape `note`'s own scan carries, identically blind to a third digit.

**Widening the pattern alone makes the result worse, not better — established by running it, not by reasoning about it.** Simulated the widened form against this repository's own `.ai-factory/specs/` tree: `find .ai-factory/specs -name "[0-9]*-*.md" | sort | tail -1` returns `.ai-factory/specs/trickster77777/99-pairing-wiring-left-half-finished.md` — a two-digit name, even though names past the glob's old two-digit reach exist in the same directory beyond it. Lexicographic sort of the matched paths places `"100-…"` and `"125-…"` before `"99-…"` (the character `'1'` sorts before `'9'`), so `tail -1` still returns a two-digit name once three-digit files are visible to the pattern. Today the bug is masked only because the unwidened pattern already excludes three-digit files from the candidate set, so every candidate shares length and sorts correctly by accident; widening the pattern without also fixing the comparison trades one wrong answer for a different wrong answer.

**The scan recurses the whole specs tree; the engine's own numbering is per-directory.** `find .ai-factory/specs ...` carries no depth limit and walks every subdirectory as one namespace. `note`'s own text — the mechanism this carrier bypasses — states "Numbering stays **per-directory** (scan the chosen directory only)." A second named roadmap under `.ai-factory/specs/` would share one numbering space with this one under the recursive scan, while `note`'s own rule would give it a numbering space of its own — the two schemes would silently disagree about a file's number.

## The change

All three land together: fixing one and leaving the others changes only how the collision shows up, not whether it does. The `find` pattern matches a leading run of digits of any length. The comparison switches from `sort`'s lexicographic order over matched path strings to a numeric comparison over the parsed integer, so a three-or-more-digit name compares correctly against a two-digit one. The scan is scoped to the flat `.ai-factory/specs/` directory, non-recursive — the same destination every note this skill writes names, in every place one is named — rather than recursing the whole tree beneath it, so it stops sharing a numbering space with subdirectories it never writes into. The width and the bound both become the same format 38.1 gives `note`, not a rule of this task's own: a new file is written with exactly four zero-padded digits, bounded `0001` through `9999`. At a destination already holding `9999`, Layer 4 writes nothing and reports that the bound is reached, naming the destination — and because `$NEXT_NOTE_NUM` is computed once, before the parallel agents launch, that is also where the stop happens: before any agent is spawned, not part-way through one.

On this skill's own side the two-digit width lives in the same sentence Current State already quotes for the pattern defect — "Extract highest two-digit prefix + 1. If none, start at `01`" — and its two clauses split by which side of the rule they sit on: "Extract highest two-digit prefix" reads existing names, so it widens to any length, matching the `find` pattern fix above rather than narrowing to four — narrowing it would re-blind the very reading this task just fixed. "If none, start at `01`" writes a number of its own, for the empty-directory case, so it becomes `0001` — the same fixed width as every other new name. The scan that reads existing names is otherwise unaffected: it keeps matching a leading run of digits of any length, since the directory holds mixed widths today and every existing name must keep being counted toward the true maximum; reading and writing are not the same rule.

The seven sites that name a note's destination elsewhere in the file — the agent prompt's "Note to write:", its write instruction, its saved-file confirmation line, and the four later report templates — all carry the bare placeholder `<NN>-<slug>.md`, with no width embedded in any of them; checked directly. None needs touching: each already inherits whatever `<NN>` becomes from the one definition site above.

The parallel structure is untouched, and stays that way: `$NEXT_NOTE_NUM` is still computed once, before the parallel agents launch, and each `Explore` agent still writes its own note from that one pre-computed number handed to it in its prompt template. Nothing here serialises the agents or has them coordinate a shared counter live — only the computation of that one number, before any agent starts, changes.

## Blast radius

`note` itself is untouched by this task — its own repair is 38.1's, and lands first. This task brings a second, independent carrier into line with the same shape rather than replacing it with a call to `note`: the user has ruled that `roadmap-test-coverage`'s parallel note-writing is well-described and works, and it is not transplanted onto `note` — `note` gains no ability to reserve a block of numbers and stays generic.

`aif-plan` carries the identical two-digit defect and is untouched by this task too: it is out of the active set, and no task exists for it in this phase — it stays a dormant carrier of the same defect, recorded rather than deleted.

This task leaves one thing open rather than hiding it: the skill loads `roadmap-engine` and resolves the roadmap in play by that engine's own named-roadmap resolution — its own opening line says as much: "it defines the named-roadmap resolution referenced below." Yet every destination it names for a note — in every one of the seven places one is named — is the flat `.ai-factory/specs/<NN>-<slug>.md`; it never writes into the `<slug>/` subdirectory the engine mandates for a named roadmap. This task brings the scan and the writes into agreement with each other, not with the engine: after it lands, both read and write the same flat directory, and both are in the wrong place whenever the roadmap in play is a named one. That contradiction is unowned by any task in this phase and is not repaired here.

No file is renamed by this task, and no existing note number under `.ai-factory/specs/` changes.
