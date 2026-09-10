# `note`'s numbering scan is blind past ninety-nine

## Current state (grounded, read fresh)

`src/skills/note/SKILL.md` states the same two-digit pattern in four places. The destination-directory hook: "the `mkdir -p`, the `[0-9][0-9]-*.md` numbering scan, and the final path." The width itself, in the note-file-path description: "`<NN>` is a zero-padded two-digit sequence number (`01`, `02`, `03` …)." The determination rule right beside it: "To determine `<NN>`, find the highest existing `NN` prefix among files matching `[0-9][0-9]-*.md` in `<destination>` and add 1. If no numbered files exist yet, start at `01`." And folder style, which reuses the identical scan: "before composing the body, reuse that same `[0-9][0-9]-*.md` scan to read the 1–2 most recent (highest-numbered) sibling files in `<destination>`." A fifth site, "Note File Handling," restates the determination rule in full rather than pointing at it: "`<NN>` determined by scanning existing `[0-9][0-9]-*.md` files per-directory in `<destination>` and incrementing the highest."

The pattern matches exactly two leading digits — a third digit before the hyphen fails the match entirely, so a three-digit file is invisible to the scan, not merely under-counted.

Re-derived against `.ai-factory/specs/trickster77777/`, not assumed: the glob matches **19** files (the run `78`–`99`, non-consecutive). The highest the scan can see is **99**. `note` would therefore propose **100**. That file already exists — `100-single-editor-assumption.md` — and the directory's true maximum is 124. The proposal is not merely stale; it collides with a real file.

This is not specific to this directory. `tradeoxy_core`'s own flat `.ai-factory/specs/` — a different repository, the same shared `note` skill — shows the identical shape independently: glob-visible maximum 99, true maximum 125, and `100-read-the-alert-log.md` already on disk.

A second consequence sits in the same pattern and is not about numbering: folder style (the fourth quotation above) reuses the scan to sample the 1–2 highest-numbered siblings and match the destination's prevailing register. Past 99 it samples whichever two-digit files still rank highest to a scan that cannot see the real top of the shelf — files from long-closed work — and matches a voice the folder has already moved past.

## The change

The scan matches a leading run of digits of any length, not a fixed two — `[0-9]+-*.md` in shape, wherever the pattern is written — and both the numbering determination and the folder-style sample read the true highest number in the directory, three digits or four, not the highest two-digit match. The width wording — "zero-padded two-digit sequence number" — stops capping at two: a number under 100 still pads to two digits, but nothing above that is truncated or wrapped.

Pinned so the implementer does not invent it: existing file names do not change — no rename, no back-fill of the files already past the old ceiling — and the two-digit padding becomes a **minimum** width, never a maximum. All four sites quoted above move together, since they are one pattern restated four times, not four independent claims.

## Blast radius

Four skills declare `note` in their own `loads:` field: `roadmap-engine`, `roadmap-outline-deep`, `task-rescue`, and `command-handoff`. `roadmap-engine` is itself loaded by `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-outline`, `roadmap-test-coverage`, `temporal-tree`, and `command-pin-gaps` — every task spec the family writes funnels through `roadmap-engine` into `note`, so this is not one folder's exposure; it is every destination `note` ever numbers.

Checked the other destinations `note` writes to against the same ninety-nine test: `.ai-factory/handoffs/` (highest `22`), `.ai-factory/rescue-reports/skills/` (highest `08`), and `.ai-factory/rescue-reports/tradeoxy_core/` (highest `04`) are all well under the ceiling — not yet exposed. `.ai-factory/specs/trickster77777/` is already past it, and `tradeoxy_core`'s own flat `.ai-factory/specs/` independently confirms the same wall in a second repository.

No file is renamed by this task — the repair changes how the scan reads the shelf, not what is already on it.
