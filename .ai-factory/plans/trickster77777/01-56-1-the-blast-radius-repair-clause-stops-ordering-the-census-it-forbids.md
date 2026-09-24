# Plan: 56.1 — the blast-radius repair clause stops ordering the census it forbids

## Context
`command-pin-gaps.md`'s Blast-radius holes `Repair:` sentence orders a `Grep`/`rg` enumeration into the task spec, and the `default:` line repeats the same order as "sweep enumeration" — both write the census `docs/counts-go-stale.md` rules a defect. Both are rewritten together to the rule/sweep/invariant form, and the one note quoting the old sentence as current ground truth is updated with them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The clause and its short name

- [x] **Rewrite the Blast-radius holes `Repair:` sentence**
  Files: `src/commands/command-pin-gaps.md`
  In the `**Blast-radius holes:**` paragraph, replace only the second sentence — currently `Repair: a `Grep`/`rg` sweep whose enumeration goes into the task spec, never a sentence saying something may need updating.` — with the wording fixed by the task spec:
  `Repair: the **rule** that defines the affected set, the literal `Grep`/`rg` **sweep** that finds it on demand, and the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found.`
  This is contract text: reproduce it character-for-character, bold markers included. Nothing else on the line moves — the opening definition sentence (`what the repository already contains that this change breaks — …`), the contradiction-and-blocker sentence, and the tail sentence about a sweep too large to enumerate stay byte-identical, as does the whole **Value holes** clause a few lines above (it is the model this repair follows, not a target).

- [x] **Rewrite the `default:` line's third list member** (depends on Rewrite the Blast-radius holes `Repair:` sentence)
  Files: `src/commands/command-pin-gaps.md`
  In the `**default:**` line at the end of the file, replace `sweep enumeration` with `rule-sweep-invariant`, so the line reads:
  `**default:** edit the file in place — replace each vague spot with the concrete value, spec clause, or rule-sweep-invariant — then report `N closed from source · M blocking · K owned elsewhere`.`
  The rest of the line — the scan-mode line above it and the report format `N closed from source · M blocking · K owned elsewhere` — is untouched. The three-word short name is deliberate and stays three words: the invariant's new well-formedness requirement is a property of the invariant, not a fourth element. Ship this edit in the same change as the one above; either alone leaves the file ordering a tally in one place and forbidding it in the other.

### The quotation that reads the old wording as current

- [x] **Update note 138's Q4 quotation** (depends on Rewrite the Blast-radius holes `Repair:` sentence)
  Files: `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`
  In the paragraph beginning `Q4 needs no new class.`, the sentence reads `The blast-radius repair already reads "…" — one clause is owed to it, …`. Replace only what sits inside those double quotes — currently `a `Grep`/`rg` sweep whose enumeration goes into the task spec, never a sentence saying something may need updating` — with, character-for-character:
  `the **rule** that defines the affected set, the literal `Grep`/`rg` **sweep** that finds it on demand, and the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found`
  The `Repair: ` prefix that opens the sentence in `command-pin-gaps.md` does **not** enter the quotation — note 138's own lead-in `The blast-radius repair already reads` already says it, and spec 154 pins the resulting paragraph starting at `the **rule** that defines the affected set`. Keep note 138's existing straight double quotes around it. The paragraph's own argument — Q4 needs no new class, and one clause is owed to the class naming what a rename's sweep searches for, declarations not readers — plus its following sentence about the compiler pulling reads along, stay unchanged. Every other line of note 138 is untouched.

### Blast radius

- [x] **Re-run the sweep and check the invariant** (depends on Update note 138's Q4 quotation)
  Files: — (verification, no edit)
  Rule: any file quoting the old `Repair:` wording verbatim as ground truth for its own argument reads stale once the wording changes — except a task spec's own current-state section, the note of a phase already decomposed, a handoff, and a run artifact of this task itself (this plan and its plan-reviews), all of which record what was true when they were written, or record the run rather than instruct the family, and none of which is kept in sync here. The note of a phase **not yet decomposed** carries no exception: it is still live input to planning, read as current ground truth, and is in scope. That is what separates note 138 (phase 44, no task lines in the roadmap) from note 150 (phase 56, decomposed into 56.1 and 56.2).
  Sweep: `grep -rln "sweep whose enumeration goes into the task spec, never a sentence saying something may need updating" .ai-factory/ docs/ src/`
  Invariant: the sweep must still return `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md`, whose current-state section records the old wording deliberately and keeps it after the change — an empty or 154-free result means the pattern was mistyped, not that the repository is clean. Given that result, the sweep must no longer return either target — `src/commands/command-pin-gaps.md` or `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`; run the same sweep once **before** editing and confirm both targets appear, so their later absence is a measured change rather than an absence of evidence. Every remaining hit falls in one of the Rule's excepted classes. Check that membership, never a total: the number of remaining hits is not this invariant's concern, and no remaining hit is edited. No symlink work is needed — `active/commands/command-pin-gaps.md` already points at the edited source.
