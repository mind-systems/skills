# 61.1 — the repair is a mood, not a mechanism

## What is true now

`src/commands/command-pin-gaps.md` carries two paragraphs that contradict each other. **What the pass never writes** reads in full:

> **What the pass never writes:** it pins values and enumerates breakage, and
> it never authors a verification check — no step, command, or bullet whose
> only job is to confirm the instruction was carried out. Such a check can
> only fail where the instruction was ignored, and by `test-philosophy`'s
> discriminator that is a loud failure, which is not written. A surface
> that fails silently still owes a test, routed to its owner as below.

**Blast-radius holes**, a few lines below, reads in full (this exact wording is what task 56.1 installed):

> **Blast-radius holes:** what the repository already contains that this
> change breaks — a caller, a format, an assumption elsewhere in the code
> that the change invalidates on contact. Repair: the **rule** that
> defines the affected set, the literal `Grep`/`rg` **sweep** that finds
> it on demand, and the **invariant** every match must satisfy after the
> change — naming, at minimum, the task's own target as a result the
> sweep must return, so an empty result reads as a broken pattern rather
> than a clean repository — never the sweep's own enumeration of what it
> found. A contradiction that resolves against the code is closed in
> place; a fundamental conflict, or code that does not come apart, is
> raised as an explicit blocker instead of being quietly repaired. A
> sweep too large to enumerate is itself a finding: report the search and
> its count with owner `roadmap-decompose`, never filed under `##
> Blocking decisions`.

The **invariant** clause is addressed forward — "every match must satisfy after the change" instructs whoever acts on the spec to run the sweep once the edit lands and confirm the result. That is, word for word, the object the first paragraph forbids: "a step, command, or bullet whose only job is to confirm the instruction was carried out." The specs this clause produces render the rule, the sweep, and the invariant under a heading with a fenced command — the shape of a step — and `roadmap-decompose` turns each such block into a plan task. Task 58.2's rescue is the evidence: its plan carried two edit tasks and four verification tasks, every one of the three rounds it failed was inside the verification half, and none ever faulted the change itself.

`.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md` — phase 44's own note, not yet decomposed — quotes the Blast-radius holes Repair sentence live, as grounding for its own Q4 paragraph:

> Q4 needs no new class. The blast-radius repair already reads "the
> **rule** that defines the affected set, the literal `Grep`/`rg`
> **sweep** that finds it on demand, and the **invariant** every match
> must satisfy after the change — naming, at minimum, the task's own
> target as a result the sweep must return, so an empty result reads as
> a broken pattern rather than a clean repository — never the sweep's
> own enumeration of what it found" — one clause is owed to it, naming
> what a rename's sweep searches for: declarations, not readers. The
> distinction decides the outcome because reads are pulled along by the
> compiler and independent declarations are not, so a green build is
> compatible with a half-converted vocabulary.

Because phase 44 has not been decomposed, this quote is still live grounding rather than history, exactly the position `138-`'s Q4 paragraph was in when 56.1 updated it the first time (`154-…md` § "The change").

**Where the repair lands, and why only one paragraph moves.** The contradiction is repaired by changing what the Blast-radius holes Repair sentence instructs the pass to write, not by touching *What the pass never writes*. Once the invariant is defined as a recorded finding — what the sweep, run at spec-authoring time, reaches, and how each match reads against the rule — its job is evidentiary, the same job Value Holes' pinned value and Meaning Holes' decided constraint already do; it is no longer "a step... whose only job is to confirm the instruction was carried out," so it no longer meets the forbidden paragraph's own definition. The fenced sweep command stays, unaddressed to anyone in particular: a tool a future reader may re-run to re-derive the set, never an instruction that a plan turns into a task. Touching *What the pass never writes* as well would restate the same distinction twice for no further gain.

## What must be true after

The Blast-radius holes clause's Repair sentence becomes:

> Repair: the **rule** that defines the affected set, the literal
> `Grep`/`rg` **sweep** that finds it on demand, and the **invariant** —
> a recorded finding of what the sweep, run now, reaches and how each
> match reads against the rule, naming at minimum the task's own target
> among what it finds, so a reader can tell a genuinely narrow set from
> a broken pattern — never an instruction for a later run to confirm,
> never the sweep's own enumeration of what it found.

No other sentence in the Blast-radius holes clause changes: its opening definition sentence, the contradiction-and-blocker sentence, and the tail sentence about a sweep too large to enumerate stay word-identical. *What the pass never writes*, the `default:` line, and every other paragraph of the file stay untouched.

`138-four-witnesses-each-trusted-where-it-is-blind.md`'s Q4 paragraph is this task's second target, updated the same way `154-…md` updated it the first time — only the quoted string changes, the paragraph's own argument does not:

> Q4 needs no new class. The blast-radius repair already reads "the
> **rule** that defines the affected set, the literal `Grep`/`rg`
> **sweep** that finds it on demand, and the **invariant** — a recorded
> finding of what the sweep, run now, reaches and how each match reads
> against the rule, naming at minimum the task's own target among what
> it finds, so a reader can tell a genuinely narrow set from a broken
> pattern — never an instruction for a later run to confirm, never the
> sweep's own enumeration of what it found" — one clause is owed to it,
> naming what a rename's sweep searches for: declarations, not readers.
> The distinction decides the outcome because reads are pulled along by
> the compiler and independent declarations are not, so a green build is
> compatible with a half-converted vocabulary.

## What breaks on contact

**Rule:** any file that quotes the Repair sentence's current exact wording ("must satisfy after the change") as live ground truth for its own argument reads stale once this task's wording lands — except a spec's or phase note's own record of a past moment, and a closed task's plan, plan-review, or handoff, each of which documents what was true when it was written rather than tracking the code going forward.

**Sweep (re-runnable):**
```
grep -rln "must satisfy after the change" src/ docs/ .ai-factory/
```

**Finding.** The sweep separates into two kinds. The live kind is what this task carries: its own target, `command-pin-gaps.md`'s Repair sentence, whose phrase the change above drops; and phase 44's own note (`138-…md`), the one note quoting that sentence live as grounding for its own argument, whose Q4 paragraph this task updates in the same stroke. Everything else is the other kind, one category: artifacts recording a past moment rather than tracking the code going forward — this phase's own note, a landed sibling task's own spec together with its plan and plan-review, and a handoff. This task's own spec and the roadmap's own contract line for it join that same historical kind once written, quoting the pre-task wording permanently as the problem they describe.

**On sequencing against 56.1.** This task edits the same Repair sentence task 56.1 already edited — but 56.1 is landed (commit `02ff899`), not a sibling awaiting decomposition in this same pass, so there is no plan-level ordering conflict the way `57.3` needed sequencing after `57.2`: this task's own `## What is true now` cites the post-56.1 text as already-standing ground truth, and this task decomposes and executes on its own, no earlier task pending. Folding it into 56.1 is not available either, on the same ground — 56.1 is closed, and reopening a landed task is not what folding two concerns into one unlanded task (58.1's precedent) means.
