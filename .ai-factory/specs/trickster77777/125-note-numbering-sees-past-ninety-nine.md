# `note`'s numbering scan is blind past ninety-nine

## Current state (grounded, read fresh)

`src/skills/note/SKILL.md` states the same two-digit pattern in four places. The destination-directory hook: "the `mkdir -p`, the `[0-9][0-9]-*.md` numbering scan, and the final path." The width itself, in the note-file-path description: "`<NN>` is a zero-padded two-digit sequence number (`01`, `02`, `03` …)." The determination rule right beside it: "To determine `<NN>`, find the highest existing `NN` prefix among files matching `[0-9][0-9]-*.md` in `<destination>` and add 1. If no numbered files exist yet, start at `01`." And folder style, which reuses the identical scan: "before composing the body, reuse that same `[0-9][0-9]-*.md` scan to read the 1–2 most recent (highest-numbered) sibling files in `<destination>`." A fifth site, "Note File Handling," restates the determination rule in full rather than pointing at it: "`<NN>` determined by scanning existing `[0-9][0-9]-*.md` files per-directory in `<destination>` and incrementing the highest."

The pattern matches exactly two leading digits — a third digit before the hyphen fails the match entirely, so a three-digit file is invisible to the scan, not merely under-counted.

Re-derived against `.ai-factory/specs/trickster77777/`, not assumed: the glob matches **19** files (the run `78`–`99`, non-consecutive). The highest the scan can see is **99**. `note` would therefore propose **100**. That file already exists — `100-single-editor-assumption.md` — and names past the glob's two-digit reach exist in the same directory beyond it, uncounted by the scan. The proposal is not merely stale; it collides with a real file.

This is not specific to this directory. `tradeoxy_core`'s own flat `.ai-factory/specs/` — a different repository, the same shared `note` skill — shows the identical shape independently: glob-visible maximum 99, and `100-read-the-alert-log.md` already on disk.

A second consequence sits in the same pattern and is not about numbering: folder style (the fourth quotation above) reuses the scan to sample the 1–2 highest-numbered siblings and match the destination's prevailing register. Past 99 it samples whichever two-digit files still rank highest to a scan that cannot see the real top of the shelf — files from long-closed work — and matches a voice the folder has already moved past.

## The change

The scan matches a leading run of digits of any length, not a fixed two, wherever the pattern is written. Every comparison it makes — the numbering determination, and folder style's pick of the 1–2 highest-numbered siblings — is numeric, over the parsed integer, never lexicographic order over the matched strings, so a three-digit or four-digit name compares correctly against a two-digit one. The width wording — "zero-padded two-digit sequence number" — becomes four: a new file is written with exactly four zero-padded digits, `0001` through `9999`, regardless of how small the number is. That fixed width governs only what `note` writes — the scan that reads existing names keeps matching a leading run of digits of any length, because the directory already holds names of mixed width and every one of them must keep being seen and counted toward the maximum; reading and writing are not the same rule.

The determination rule's own empty-case default moves with it, named separately because it is a write, not a read: "If no numbered files exist yet, start at `01`" becomes `0001` — the same fixed width, sitting in the one clause of the determination sentence that produces a number rather than finding one.

The scan declares its own bound instead of walking past one silently: numbers run `0001` through `9999`, and at a destination already holding `9999`, `note` writes nothing and reports that the bound is reached, naming the destination, rather than proposing `10000` or colliding with a number already taken.

Pinned so the implementer does not invent it: existing file names do not change — no rename, no back-fill of the files already past the old ceiling. Every site quoted above moves together, since they are one pattern restated several times, not independent claims.

## Blast radius

Four skills declare `note` in their own `loads:` field: `roadmap-engine`, `roadmap-outline-deep`, `task-rescue`, and `command-handoff`. `roadmap-engine` is itself loaded by `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-outline`, `roadmap-test-coverage`, `temporal-tree`, and `command-pin-gaps` — every task spec the family writes funnels through `roadmap-engine` into `note`, so this task's own reach is real and wide, not one folder's.

Two other carriers exist, and this task repairs neither. `roadmap-test-coverage`'s Layer 4 mints its own numbers with a hand-rolled scan and never loads `note` at all — its own `loads:` field names only `test-philosophy` and `roadmap-engine` — so a sweep for `note`'s callers is structurally blind to it; it carries the identical width defect independently, plus two more of its own, closed by 38.2 instead. `aif-plan` carries the identical prose verbatim — the same width claim, the same determination rule, the same restatement — but is not in the active set; no task is written for it here, and it stays a dormant carrier that would reintroduce this exact defect the moment it is symlinked into `active/skills/`.

Checked the other destinations `note` writes to against the same ninety-nine test: `.ai-factory/handoffs/` (highest `22`), `.ai-factory/rescue-reports/skills/` (highest `08`), and `.ai-factory/rescue-reports/tradeoxy_core/` (highest `04`) are all well under the ceiling — not yet exposed. `.ai-factory/specs/trickster77777/` is already past it, and `tradeoxy_core`'s own flat `.ai-factory/specs/` independently confirms the same wall in a second repository.

No file is renamed by this task — the repair changes how the scan reads the shelf, not what is already on it.
