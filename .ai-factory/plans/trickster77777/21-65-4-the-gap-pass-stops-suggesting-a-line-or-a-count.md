# Plan: 65.4 — the gap pass stops suggesting a line or a count

## Context
Three sentences in `src/commands/command-pin-gaps.md` ask for a position or a tally, which goes against the command's own **Value holes** repair ("never a line number") and against `docs/counts-go-stale.md`:
- The walk paragraph ends each behavior "at a `file:line` landing in the code".
- The **Meaning holes** repair asks for "citing the code that grounds it" and gives no form for the citation.
- The **Blast-radius holes** repair has a too-large sweep "report the search and its count".

This task rewrites all three. The landing and the grounding code each become a file plus the named thing inside it, and a too-large sweep is reported as its search, with no number. The spec pins all three sentences verbatim. Task spec: `.ai-factory/specs/trickster77777/183-the-walk-lands-on-a-file-and-a-named-thing.md`. Governing specs: `docs/counts-go-stale.md`, `docs/reference-by-name.md` and `docs/what-a-task-carries.md`. None of them is edited, because the phase note says nothing under `docs/` is written.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the three sentences

The three edits are in the same file. Each target paragraph is one physical line of the file, so each replacement stays on that one line: do not add line breaks. Change only the quoted span and leave the rest of each paragraph byte-identical.

- [x] **Walk paragraph: the landing is a file and a named thing**
  Files: `src/commands/command-pin-gaps.md`
  Find the paragraph that opens "The unit of the walk is one behavior the task claims." Replace its second sentence, currently:
  > Each such behavior either ends at a `file:line` landing in the code or becomes a finding; the walk descends into code the named files themselves reference only as far as that behavior's landing requires, never past the question.

  with exactly this (pinned by the spec):
  > Each such behavior either ends at a landing in the code — a file and the named thing inside it that holds the behavior — or becomes a finding; the walk descends into code the named files themselves reference only as far as that behavior's landing requires, never past the question.

  The first sentence and the "Two questions decide a finding: …" sentence that follow stay unchanged.

- [x] **Meaning holes repair: the grounding code is named, not cited**
  Files: `src/commands/command-pin-gaps.md`
  In the paragraph led by `**Meaning holes:**`, replace the clause
  > citing the code that grounds it where a concrete source exists

  with exactly this (pinned by the spec):
  > naming the code that grounds it — the file and the named thing inside it that holds the constraint — where a concrete source exists

  The result reads "…derived from the observed behavior of the actual code, naming the code that grounds it — the file and the named thing inside it that holds the constraint — where a concrete source exists; when the code can't settle it (genuine product decision), don't fabricate it — …". Nothing else changes: the list of edge cases, the `## Blocking decisions` routing, and the `aif-docs` owner sentence all stay as they are.

- [x] **Blast-radius holes repair: a too-large sweep is reported as its search**
  Files: `src/commands/command-pin-gaps.md`
  In the paragraph led by `**Blast-radius holes:**`, the last sentence currently reads:
  > A sweep too large to enumerate is itself a finding: report the search and its count with owner `roadmap-decompose`, never filed under `## Blocking decisions`.

  Replace it with exactly this (pinned by the spec):
  > A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`.

  The rest of the paragraph stays unchanged. That includes the rule, sweep and invariant/finding form, and the contradiction/blocker sentence.

- [x] **Leave the rest of the command untouched**
  Files: `src/commands/command-pin-gaps.md`
  Do not edit any of these:
  - The **Value holes** paragraph. It already reads "never a line number".
  - The scan-mode line `[file:line|spec-location] → value|meaning|blast-radius → …`. It is chat output that no artifact keeps.
  - The default-mode report line `N closed from source · M blocking · K owned elsewhere`. It counts the run's own outcomes as chat output.
  - The frontmatter or description.
  - Any other file in `src/` or `docs/`.

### Confirm the blast radius

- [x] **Re-run the spec's sweep** (depends on the three rewrites above)
  Files: none (read-only check)
  Run:
  ```
  grep -rn "file:line" src/ docs/ CLAUDE.md
  grep -rn "command-pin-gaps" src/ docs/ CLAUDE.md
  grep -rn "and its count" src/ docs/ CLAUDE.md
  grep -rn "citing the code" src/ docs/ CLAUDE.md
  ```
  The spec's **Rule** is the stop condition. A hit breaks only if it depends on the wording of any of the three sentences, or describes a landing or a grounding citation as a line, or a too-large sweep as a count. If a hit does that and sits outside this command, report it and do not edit it.

  Expected:
  - The third and fourth searches return nothing.
  - In `command-pin-gaps.md`, the first search now hits only the scan-mode line `[file:line|spec-location]`. That line stays.
  - The first search's other hits are docs and the global CLAUDE.md, which name `file:line` as the defect. None of them needs an edit:
    - `src/global/CLAUDE.md` § "Grounding claims"
    - `docs/reference-by-name.md`
    - `docs/counts-go-stale.md`
    - the `CLAUDE.md` index row
  - The `roadmap-outline-deep` and `roadmap-prune` hits the spec mentions were already removed by 65.1 and 65.3, so they no longer appear.
  - The second search hits only docs and the `CLAUDE.md` index. None of them describes the walk's landing, the grounding citation, or the report of a large sweep:
    - `docs/skill-description-field.md`
    - `docs/sakshi-harness/skill-cycle.md` (the pins chapter and the pipeline diagram)
    - `docs/sakshi-harness/skill-graph.md`
    - `docs/reference-by-name.md`

  If this list and the actual output differ, that alone is not a reason to stop. Only a hit that meets the Rule is.
