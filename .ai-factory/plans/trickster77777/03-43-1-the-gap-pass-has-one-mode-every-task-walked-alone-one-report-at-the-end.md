# Plan: 43.1 — the gap pass has one mode: every task walked alone, one report at the end

## Context
`src/commands/command-pin-gaps.md` gets one mode: each task the target names is walked alone, in roadmap order, finished before the next, without stopping, and one report comes at the end with every task's blockers gathered and owners named. The scan mode, its trigger words, its list format, its argument hint, and "a plan" in the description are removed. Every replacement text is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0199-the-gap-pass-walks-every-task-alone-and-reports-once.md` § "What must be true after". Copy those texts exactly as written. Do not paraphrase them.

Blast radius, from the spec's sweep (re-run while planning, same result): `spec-location`, `scan mode` / `только скан` and `closed from source` appear only in `src/commands/command-pin-gaps.md`. Nothing else under `src/`, `docs/` or `CLAUDE.md` changes. `docs/sakshi-harness/skill-cycle.md` § "Пины — `command-pin-gaps`" stays as it is (per the spec).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit the command

- [x] **Frontmatter: description and argument hint**
  Files: `src/commands/command-pin-gaps.md`
  In the `description: >-` folded block, change the opening "Scan a plan, task, phase, or task spec for where…" to "Scan a task, a phase, or a task spec for where…", and delete the final sentence `Pass "scan" to only list findings without editing.`. The block must then end on "Closes what it can in place.". Keep the folded `>-` form and its line-wrapped indentation, and re-wrap only the lines the edit changes. Change `argument-hint: "[path | scan]"` to `argument-hint: "[path]"`, keeping the quotes. Leave `allowed-tools` and `loads:` as they are.

- [x] **Targeting paragraph: per-task walk**
  Files: `src/commands/command-pin-gaps.md`
  The paragraph starting "Target, in priority order:" now ends "…above `---STOP---`, scanning each contract line and its `Spec:`-tagged task spec.". Replace everything after "above `---STOP---`" with the spec's text: ". Each task the target names is walked alone, in roadmap order: the command reads that task's contract line and its `Spec:`-tagged task spec, holds that task and nothing else, finishes that task's findings before the next is opened, and does not stop between tasks." Leave the start of the paragraph (the priority order and the named-roadmap resolution) as it is.

- [x] **Two-ends sentence and the "both modes" clause**
  Files: `src/commands/command-pin-gaps.md`
  In the paragraph starting "The two ends are not classes:", change "— in place, or `owner: <skill>` in the scan line's `fix` token." to "— in place, or `owner: <skill>` in the report.". Leave the rest of that paragraph as it is. In the paragraph starting "A task that cannot be planned coherently belongs to…", change "a hole whose repair belongs elsewhere is reported, in both modes." to "a hole whose repair belongs elsewhere is reported.". Leave the sentences around it as they are.

- [x] **Replace the two closing mode paragraphs with one** (depends on the edits above, which touch the same file)
  Files: `src/commands/command-pin-gaps.md`
  Delete both final lines, the `**scan mode** (…)` line and the `**default:** edit the file in place …` line. In their place write this single paragraph, verbatim and with no bold label: "For each task in turn the command edits its file in place — replacing each vague spot with the concrete value, spec clause, or rule-sweep-invariant — and moves on to the next task. One report comes at the end, `N closed from source · M blocking · K owned elsewhere`, with the blockers of every task gathered under it, each naming its task, and each hole owned elsewhere naming its owner as `owner: <skill>`."
  Afterwards, `rg -n "scan|spec-location|только скан|both modes|\"report\"" src/commands/command-pin-gaps.md` must return no line that names a mode, a trigger word or the list format.
