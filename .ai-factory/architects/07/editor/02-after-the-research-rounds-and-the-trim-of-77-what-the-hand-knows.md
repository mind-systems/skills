# Editor snapshot — after the research rounds and the trim of phase 77

Written by the hand itself, at the seam the head chose, for the hand that starts from this file and the buffer. The buffer holds the practice and the rulings and is read first; `01-…` before this one still holds the shape of an order, the budgets and the mechanics of the machine, and nothing here repeats it. This file holds what I learned after that: how the research rounds went, where I slipped, and what the material did to me. Everything here is a description; the files win.

## What the rounds looked like since

Apply orders were of different kinds. Most pinned a place and a meaning and asked for the text to be written with the file open. Some were edits the user wanted done in chat, such as a doc paragraph; the order says so and says not to mark the roadmap for it. Research orders were larger than before: reconstruct a command's history, test a theory against the record, find out whether a pass ran before a run. They want a narrative or a table, evidence inline, and the plain statement of where the record is silent. A premise in the brief can be wrong on the files. It was: who still calls a command, and where rescues happen. I said so first and then answered what the record shows. The head valued that more than a tidy answer.

A message marked as arriving while I worked is handled before the earlier thread resumes. A background-task notification is not a message from anyone and is not consent; I carried on and used its result.

## The material, and where it bit

The roadmap and the specs are one material with the thing they describe, so the rule in 01 about target files stays live. More facts about it.

Numbers in the specs folder are assigned once. A spec that was deleted still owns its number, even if the scan of the folder would hand it out again; the head had me rename a fresh spec past the deleted pair. A committed file is removed with `git rm -f` when it has local changes; an untracked one is moved with plain `mv`.

A pinned text is only as good as its wrap. The docs wrap near the high eighties, skills and the seed much narrower. I rewrap with `textwrap` at the target's own width and then check equality against the spec's pinned paragraph with all whitespace collapsed. That check is cheap and it caught nothing only because I ran it before reporting.

Specs written in the three-part shape quote the file as it stands unless an earlier open task changes the same passage, and then they quote that task's pinned after-text under its name. The user ruled that the skills need not state this rule; only the seed entry carries it, and one doc keeps its clause by his word. So a spec may quote that doc clause while no skill says it. Read the buffer entry before touching any spec in phase 77.

For research, the useful sources and their traps:
- Session transcripts live under the home directory's `.claude/projects`, one folder per working directory with every non-alphanumeric turned into a hyphen. Each line is JSON. A command invocation shows as a `<command-name>` marker in a user line, with its arguments next to it. The same message is often present several times, so dedupe by timestamp. Times are UTC.
- A rescue deletes the failed run's plan, plan-reviews, reviews and sidecar. Counts of rounds per task therefore describe only the run that landed. The rescue reports, in this repo's rescue-reports folder, are the only account of the failed run.
- "Roadmap update" commits are amended repeatedly, so the author date is the start of a chain and the commit date is the end. I used the author date as when something happened and was wrong by days. Use the commit date for landing and the transcript for authoring.
- A pruned contract line is found with `git log --all -S"**N.M —" -- <roadmap>`; its spec path is in the Spec tag of the first version. The spec itself is read at the landing commit's parent.
- The core and broker repos carry their own plans, reviews and handoffs; before the architect folders existed, snapshots were handoffs.
- Scripts written to a temporary folder disappear between sessions. Build the extraction again; do not trust a remembered result.

## Where I was wrong, and the pattern behind it

A write that was not written. I edited the roadmap in one block, kept the result in a variable, then re-read the file in a later block and edited that, so the first edit was lost. The only sign was that a printed length did not change. The pattern: several blocks each re-reading the same file. Do every change to one file on one buffer, write once, and print the thing you measured from the file, not from the variable.

A quote left behind. I removed a clause from a doc and a spec still quoted the old wording; it surfaced only in the chain check. After changing any text, search every place that quotes it.

Titles that outlive their cuts. A task's title more than once still named a clause the task no longer carried. After every cut, ask whether the title still describes the task. Filenames stay as identifiers, but contract lines and headings follow.

Counting and position words again, the same reflex 01 describes. "Both read…", "the two sentences", "the first paragraph", "opening paragraph" each got into a spec or a note and each was found by a search I ran after writing. Run the search of number words and of position words before the report, over what I wrote, and cite a passage by a quoted fragment or a heading.

Treating the brief's account as fact. Beyond the premises above: a heuristic I built to detect pinned wording first counted quotes of the current text, not of the after-text. I found it by sampling specs by hand. When a measurement is a heuristic, sample before you report its totals, and say what the threshold is.

Dates and records that disagree. An escalation's date, a commit's date and a transcript's time rarely agree. State which clock each number uses.

A reversal not noticed. A task I wrote removed a parenthesis that an earlier task had kept "by the user's word". I flagged it only because I had read the contract line of the earlier one. Before removing or rewording something, look for the history of why it stands.

## What is in flight

Nothing is half-applied. The tree holds the buffer and a head snapshot; everything else is committed. The phases above the stop are all held by the user: his decision, not a gap. Phase 77 has open tasks on the engine paragraph, the pin-gaps invariant, the seed's counts entry, the seed's "a task's now" entry and the decompose hook; their order is the order of the lines, with no sequencing words. Phase 79 is outlined and deepened. Phase 78's note carries what a compact keeps and loses.

Known, not decided by me: phase 77's title and preamble speak of measurement while one task carries the "now" rule; the first-landed doc task's spec no longer matches the doc it pinned; the engine paragraph and the doc differ on "now" by the user's choice. Open questions are the user's: retiring the gap pass, and the grove's CEO candidate. A live run of the rewritten architecture skill is pending and is not mine to start.

## What will slip first for a hand without my history

The search for number words and position words before any report, over my own text.

The single buffer and a single write per file, and printing the measured value from disk.

The chain check after a spec edit: does anything else quote the passage I changed, and does any spec quote a file that an earlier open task rewrites.

Reading the history before touching a clause, since a reversal is the user's to rule.

Which clock a date is on, and which fraction of an artifact survives a rescue.

Stating a wrong premise before answering, plainly, and answering from the files.

When unsure whether something belongs to the round, put it in the report as a flag and leave the file alone.
