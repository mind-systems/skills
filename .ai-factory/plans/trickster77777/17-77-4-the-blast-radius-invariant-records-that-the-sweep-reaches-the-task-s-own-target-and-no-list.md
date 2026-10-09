# Plan: 77.4 — the blast-radius invariant records that the sweep reaches the task's own target and no list

## Context
Rewrite the **invariant** clause inside the bold lead-in `**Blast-radius holes:**` in `src/commands/command-pin-gaps.md`. As things stand it asks for a record of what the sweep reaches now and how each match reads, and it judges a "genuinely narrow set". That is a snapshot and a size, and the governing specs `docs/what-a-task-carries.md` § "Blast radius: the rule, not the snapshot" and `docs/counts-go-stale.md` keep both out of a spec. The task spec (`.ai-factory/specs/trickster77777/0218-the-blast-radius-invariant-asks-for-no-size.md`, § "What must be true after") pins the new clause verbatim and is the authority.

Ground truth at planning time: the whole "Blast-radius holes" paragraph is one unwrapped line in `src/commands/command-pin-gaps.md`. `active/commands/command-pin-gaps.md` is a symlink to it, so only the `src/` file is edited. The clause's current text matches the spec's § "What is true now" quote word for word. No open task above 77.4 in the roadmap edits this file.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the invariant

- [x] **Replace the invariant clause with the pinned text**
  Files: `src/commands/command-pin-gaps.md`
  In the `**Blast-radius holes:**` paragraph, replace this exact span:
  `the **invariant** — a recorded finding of what the sweep, run now, reaches and how each match reads against the rule, naming at minimum the task's own target among what it finds, so a reader can tell a genuinely narrow set from a broken pattern — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found.`
  with the text quoted in the spec's § "What must be true after", word for word and punctuation for punctuation:
  `the **invariant** — a recorded finding that the sweep reaches the task's own target, so a reader can tell a working pattern from a broken one — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found.`
  Copy from the spec, not from this plan, if they differ. Keep the literal em dashes `—` and the bold `**invariant**`. Leave the rest of the paragraph as it is: the opening definition, the rule/sweep part of "Repair:", the contradiction/blocker sentence, and the sentence "A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`.". The paragraph stays a single line. Change nothing else in the file. Line 48 says "rule-sweep-invariant", and that also stays.

### Blast radius

- [x] **Run the spec's sweep and confirm nothing else asks for a size or a list** (depends on Replace the invariant clause with the pinned text)
  Files: none edited
  Run the two searches from the spec's § "What breaks on contact":
  ```
  grep -rn "run now\|narrow set\|how each match\|too large to enumerate" src docs --include="*.md"
  grep -rn -i "blast-radius\|blast radius" src docs --include="*.md" -l
  ```
  Expected reach, per the spec's finding. After the edit, the first search reaches only the kept "too large to enumerate" sentence in `src/commands/command-pin-gaps.md`. The second reaches `src/commands/command-pin-gaps.md`, `src/skills/roadmap-engine/SKILL.md`, `docs/sakshi-harness/skill-cycle.md` and `docs/what-a-task-carries.md`. The three besides the edited command already agree: none asks a spec to record what a sweep reaches beyond the task's own target or how large the reached set is. If any match outside this set asks for that, stop and report it rather than editing it.
