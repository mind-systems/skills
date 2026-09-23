# 56.1 — the blast-radius repair clause stops ordering the census it forbids

## Current state

`src/commands/command-pin-gaps.md`'s **Blast-radius holes** clause reads in full:

> **Blast-radius holes:** what the repository already contains that this change breaks — a caller, a format, an assumption elsewhere in the code that the change invalidates on contact. Repair: a `Grep`/`rg` sweep whose enumeration goes into the task spec, never a sentence saying something may need updating. A contradiction that resolves against the code is closed in place; a fundamental conflict, or code that does not come apart, is raised as an explicit blocker instead of being quietly repaired. A sweep too large to enumerate is itself a finding: report the search and its count with owner `roadmap-decompose`, never filed under `## Blocking decisions`.

The `**default:**` line, a few lines below, reads in full:

> **default:** edit the file in place — replace each vague spot with the concrete value, spec clause, or sweep enumeration — then report `N closed from source · M blocking · K owned elsewhere`.

`docs/counts-go-stale.md` (this phase's governing spec) rules a census — "how many call sites there are, how they spread across files, how many files a sweep will touch" — a defect in any durable artifact, true at the moment of writing and false the instant a sibling task lands; a task spec is such an artifact. The `Repair:` sentence's second clause ("a `Grep`/`rg` sweep whose enumeration goes into the task spec") orders exactly that census. The `default:` line's third list member, "sweep enumeration," names the same thing in two words and would leave the file arguing with itself if only the `Repair:` sentence were fixed. The **Value holes** clause, a few lines above, already states the equivalent discipline correctly for a value ("never a line number, because the spec outlives the numbering it was written against") and is the model this repair follows, not a target of this task.

## The change

The `Repair:` sentence of the Blast-radius holes clause becomes:

> Repair: the **rule** that defines the affected set, the literal `Grep`/`rg` **sweep** that finds it on demand, and the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found.

The `default:` line's third list member becomes:

> **default:** edit the file in place — replace each vague spot with the concrete value, spec clause, or rule-sweep-invariant — then report `N closed from source · M blocking · K owned elsewhere`.

Both sentences move together, in one task: deploying either alone leaves the file self-contradictory (the `Repair:` sentence forbidding a tally while `default:` still names one, or the reverse), which fails the atomicity gate's "make sense" test on its own.

Two things weighed and left alone. The `default:` line's short name, `rule-sweep-invariant`, still names the form correctly: the new requirement — that the invariant name a result the sweep must return — is a property of what makes an invariant well-formed under this repair, not a fourth element beside the three, so the three-word name still points at the whole thing and gains nothing by growing a fourth word. And the clause's tail sentence about a sweep too large to enumerate, listed untouched below, is not disturbed by this addition: it governs the opposite failure, a result too large rather than too empty, and a floor requiring at minimum the task's own target to appear is satisfied inside an oversized result exactly as it is inside an ordinary one — the two failure modes never interact, so the tail's own instruction (report the search and its count to the owner, never a spec) stands as written.

`.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`'s Q4 paragraph is this task's second target. It currently reads: *"Q4 needs no new class. The blast-radius repair already reads 'a `Grep`/`rg` sweep whose enumeration goes into the task spec, never a sentence saying something may need updating' — one clause is owed to it, naming what a rename's sweep searches for: declarations, not readers."* The quoted string is updated to the new `Repair:` wording above, so the paragraph reads in full: *"Q4 needs no new class. The blast-radius repair already reads 'the **rule** that defines the affected set, the literal `Grep`/`rg` **sweep** that finds it on demand, and the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found' — one clause is owed to it, naming what a rename's sweep searches for: declarations, not readers."* The sentence's own argument — Q4 needs no new class, and the class needs one further clause naming declarations over readers — does not rest on the old phrasing and stands unchanged.

Untouched, verbatim: the clause's opening definition sentence ("what the repository already contains that this change breaks — a caller, a format, an assumption elsewhere in the code that the change invalidates on contact") — phase 45, which would have claimed this sentence, is deleted, and nothing else in this task claims it. The contradiction-and-blocker sentence. The tail sentence about a sweep too large to enumerate — correct as written, its count going to a chat report rather than a spec, per this phase's own note. The entire **Value holes** clause. Every other line of `command-pin-gaps.md`. Every other line of note 138.

## Blast radius

**Rule:** any file in this repository that quotes the `Repair:` sentence's current wording verbatim, as ground truth for its own argument, reads stale the moment this sentence's wording changes — except a task spec's own current-state section, whose job is to record the old wording as history, and a phase note or a handoff, whose job is to record what was true at the moment it was written rather than to track the code going forward; keeping either in sync is not this command's territory.

**Sweep (re-runnable):**
```
grep -rln "sweep whose enumeration goes into the task spec, never a sentence saying something may need updating" .ai-factory/ docs/ src/
```

**Invariant:** after the change, the sweep no longer returns this task's own two targets — `src/commands/command-pin-gaps.md` and `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`, phase 44's own note, phase 44 not yet decomposed, whose Q4 paragraph quotes this exact sentence as current ground truth — because the change above updates both quotations in place. The sweep may keep returning other files under the rule's own exceptions; their count is not this invariant's concern.
