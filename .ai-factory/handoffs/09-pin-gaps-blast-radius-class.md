# Handoff — pin-gaps has two finding classes and needs a third: the blast radius

## 1. Frame

`command-pin-gaps` interrogates an artifact's own text and never asks what the repository already contains that the artifact's change will break, and that blind spot has now cost two tasks in a downstream project — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `src/commands/command-pin-gaps.md` — the file to change, 26 lines, the whole subject ← lead here. Its shape: frontmatter `:1-12`; target resolution `:17`; the premise sentence `:19` ("Any question that would need an answer *during implementation* is space for the agent to fantasize. Close all of it now."); **value holes** `:21`; **meaning holes** `:23`; **scan mode** `:25`; **default mode** `:26`.
- `src/commands/command-pin-gaps.md:2-8` — the `description:` folded block. It enumerates the two classes by name ("pin value holes to a concrete value from the actual code/proto, and close meaning holes …"), so it is a **third edit site**, not a bystander. A change that adds the class to the body and not here ships a command whose own description contradicts it.
- `src/commands/command-pin-gaps.md:10` — `allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill`. `Bash(grep *)` is **not** in that list. The new class's repair is a repository sweep, so it must be phrased on the `Grep` tool or `rg`, never on `grep`. Getting this wrong produces a class that cannot execute its own repair.
- `.ai-factory/handoffs/06-allowed-tools-syntax-contradicts-the-shipped-corpus.md` — the precedent for why the `allowed-tools` line is read before, not after, writing a clause that runs a command.

### Read on demand

- `src/skills/roadmap-decompose/SKILL.md` — the tier that writes a spec *from* the change; the distinction against it is in §7 and matters for where the new class does **not** belong.
- `.ai-factory/roadmaps/trickster77777.md` — the roadmap in play in this repo; a task for this change lands there. It carries an `> Owner:` line and belongs to a different architect (see §3).
- `.ai-factory/handoffs/08-applying-half-must-apply-through-its-own-editor.md` — the most recent handoff; useful only for the house style of a task and its work-order.

## 3. Current state

**Done:**

- The gap is diagnosed and evidenced twice over, with measurements (§6). Nothing has been written into this repository for it.
- Reverse graph checked: `grep -rl 'command-pin-gaps' src/` returns nothing. The command has no callers, loads only `roadmap-engine`, and is not itself a load-once engine — so the change is local to one file and breaks no contract anyone else depends on.

**In-flight:**

- No task written, no spec written, no roadmap line added. The change is fully specified in §4 and is waiting to be turned into a task in this repo's own two-tier form.

**Uncommitted working-tree state:**

- `HEAD` is `13b677a` ("27.1 — the global CLAUDE.md never says the project's docs are the ТЗ").
- ` M .ai-factory/notes/05-architect-buffer.md`
- ` M .ai-factory/roadmaps/trickster77777.md`
- `?? .ai-factory/specs/trickster77777/102-roadmap-outline-deep.md`

All three belong to a **different** architect's in-flight work. None of them is this change's, none is touched by it, and a tree-wide `git add -A` while they sit there strands whatever they belong to.

## 4. Next step

Write the task and its work-order for one file: `src/commands/command-pin-gaps.md` gains a **third finding class — the blast-radius hole** — beside value holes and meaning holes.

**What the class is.** Both existing classes ask the same question in two registers: *what would the implementing agent have to invent?* Value holes ask it of symbols and numbers, meaning holes ask it of behavior and boundaries. Both interrogate the artifact's own text. Neither asks the other question: *what does the repository already contain that this change breaks?* That question has no owner anywhere in the chain, and the blast-radius hole is it.

**The two triggers.** The class fires when either holds:

1. **The change narrows what is accepted** — a new validation, a stricter type, a newly required field, a removed default, a tightened format. Everything that relied on the old width is now invalid: existing fixtures, existing call sites, rows already stored. This set is not a risk to be flagged; it is a finite list that a search returns.
2. **The change touches a shared surface** — a constructor signature, an exported helper, a test harness, a fixture builder, a module-level double. Every existing consumer moves with it whether the task names them or not.

**The repair.** Sweep the repository with the `Grep` tool or `rg` for what depends on the old behavior, and write the resulting **enumeration** into the spec. The enumeration is the deliverable. A sentence warning that fixtures "may need updating" is not a repair of this class — it reproduces the hole in prose. What closes it is the list, so the implementer starts from it instead of discovering it one entry at a time.

**The four sites in the file.** Three take an edit, one already generalizes:

- `:2-8` — the `description:` block names both classes; it gains the third.
- after `:23` — the new class paragraph, in the same shape as its two siblings: **bold name**, definition, then `Repair:`.
- `:25` — scan mode's line format reads `[file:line|spec-location] → value|meaning → what's missing → fix`; the middle token gains a third alternative.
- `:26` — the default-mode report already reads "then report `N closed from source · M blocking` (optionally split the count by class)". Class-agnostic as written; **no edit needed**. Verify this rather than assuming it — if it is edited, say why.

**One judgment left open, and it is the task's own to settle:** whether the repair may write into `## Blocking decisions` the way meaning holes do. Meaning holes escalate there when the code cannot settle the question. A blast radius is always answerable by a search — the code always settles it — so on the face of it the escalation path does not apply. The counter-case is a sweep whose result is too large to enumerate, which is itself a finding worth raising rather than pinning. Decide it in the task; do not leave it for the implementing agent.

## 5. Working discipline

- The user marks with `::`. Everything before the mark relays to the editor verbatim as a `REPORT-ONLY` channel-message; everything after it is the architect's alone and is never forwarded. No mark anywhere means the message is conversation, not a relay. The marker is unconditional — never judge whether it was "meant".
- **Nothing that closes a round — a summary, a verdict, or a work-order — leaves before the report on that round exists.** The architect's own parallel pass runs through the wait; what defers is the announcement, never the work.
- Verification is by fact: open the file, run the search, quote the line. A report is a claim, including a report that says a thing is *absent*.
- Small and surgical. Ship the sentences the request contains and nothing past them. This change is one class and its wiring — it is not an occasion to restructure the command.
- Never commit without explicit permission. Work-orders end with "do not commit."
- Work-orders and files are English; conversation may be Russian.

## 6. Error log

These are not this repository's mistakes — they are the evidence that produced the change, and each carries the measurement that makes it checkable.

1. **A task added a format check and never listed what the check invalidates.** In a downstream NestJS project, a task added a UUID-format check to two start handlers. Its spec's test section was written **forward** from the change — here are the three new scenarios the fix needs — and never **backward** from the repository. Every subscription-id fixture already in the largest suite was a value the old code accepted and the new code rejects, and the spec named none of them. The planner rediscovered them across three planning rounds, one cluster per round, and the pipeline allows exactly three: 35 completed tasks in that repo passed plan review on round 1, 27 on round 2, 9 on round 3, and **zero on round 4**. The task stopped at low risk with four cosmetic findings outstanding. It ran out of rounds; it did not fail.
2. **The sweep that was never run costs one second.** Executed after the fact, it returns `subscriptionId: 'sub-1'` ×5, `subscriptionId: 'sub-no-owner'` ×1, `subscriptionId: 'sub-invalid-layout'` ×1, plus 12 call sites passing a variable whose source must be traced. That is the whole list. Placed in the spec at decomposition time, it would have cost one line of the planner's attention instead of three rounds of discovery.
3. **The same blind spot, one task earlier, wearing a different shape.** A pin-gaps round on another task pinned every positive gate — a warn level, a null guard's position, a retargeted test — and never asked what the repository's own verification commands do to a task that guarantees untouched lines. Both `npm run lint` and `npm run format` rewrite files in place, so the ordinary reflex after finishing the change would have breached the task's own fence while the type-check and the tests stayed green: a silent breach by construction. Two instances of one blind spot make it a property of the lens, not an incident.
4. **The class was nearly proposed as a clause bolted onto meaning holes.** It is not one, and §7 and §10 say why. Bolting it on would have left the repair — a repository sweep — inside a class whose every other repair is answered by reading the artifact and the code the artifact names.

## 7. Orientation

- **This does not belong to `roadmap-decompose`.** Decompose writes the spec *from* the change and looks forward by design; that is correct and is not the defect. `pin-gaps` runs after, over an artifact that already exists, and is the only lens in the chain positioned to look backward at the repository. Adding the question to decompose instead would ask an author to audit a change they have not finished describing.
- **A blast radius is not a scope boundary.** A scope boundary is a meaning hole: it says which files the task must **not** touch. A blast radius says which files the task **will break**, whether it touches them or not. The two are frequently disjoint — the fixtures a narrowing change invalidates usually sit in files the task's own boundary declares out of scope, which is exactly why the boundary clause never catches them.
- **A blast radius is not a "risk".** Both other classes end in something concrete — a pinned value, a written constraint. This one ends in an enumeration. Prose that flags a possibility is the hole, not its repair.

## 8. Domain model spine

- **`pin-gaps` is a lens, not a linter.** It reads one artifact and repairs it in place, and its whole premise (`:19`) is that any question left open until implementation is space for an agent to invent an answer. The third class is that premise applied to questions the artifact does not know it is asking.
- **`pin-gaps` has two modes and one report.** `scan` lists and stops (`:25`); default edits in place and reports counts (`:26`). Any new class must be visible in both or it ships half-wired — the counter already generalizes, the scan-line format does not.
- **The command loads `roadmap-engine` and nothing else** (`:11`), and nothing loads it (`grep -rl` returns nothing). It is not a load-once engine and carries no reverse-graph obligation.

## 9. Hard rules

- **A count is a claim and carries its unit.** `grep -c` returns matching *lines*; occurrences need `-o | wc -l`. An unlabelled number is re-read downstream as whichever unit the reader assumes.
- **An expected value is produced by running the exact command it sits beside**, at the moment the order is written — never from memory of a similar command run earlier, and this bites hardest on `git status`, the one value that feels already known.
- **A citation lifted out of a review, a report or another artifact is opened before it is transcribed** — including, especially, when the file it lands in already carries the same anchor.
- **A literal gate is right only when the literal *is* the contract** — a marker, a filename, a task number. For prose carrying an idea it verifies that a string is present, not that the idea is, and it pushes the author to write toward the grep. There, the check is "quote the resulting sentence back".
- **A grep with a `.` in a filename pattern needs `-F` or an escape**; an unescaped dot is a wildcard and over-counts.
- Never commit without explicit permission; never push.
- All files in English regardless of the conversation's language.

## 10. Cross-cutting contracts / invariants checklist

- **The three classes answer three different questions, and the distinction must not blur in the wording.** Value holes pin what is **missing** from the artifact. Meaning holes write the constraint that is **undecided** in the artifact. The blast-radius hole enumerates what **exists** in the repository and will break. The first two are answered by reading the artifact and the code it names; the third is answered only by sweeping code the artifact does **not** name. That asymmetry is the whole reason it is a third class.
- **Every class's paragraph has the same shape**: a bold name, the definition of what it looks for, then `Repair:` and how it is closed. The new paragraph matches it or the file grows a second register.
- **Every class must reach both mode branches.** The class exists in the body, appears in the scan-mode line format, and is countable by the default-mode report.
- **The repair verb is `Grep`/`rg`, never `grep`** — set by the frontmatter's `allowed-tools`, not by taste.
- **The frontmatter `description:` is part of the contract, not a summary of it.** It names the classes; a class absent from it is a class the invoking agent may never learn about.

## 11. Per-unit map with watch-points

- **`src/commands/command-pin-gaps.md` — gains a third finding class.** *Watch:* four sites, and three of them are easy to miss because only one is the obvious one. The new paragraph after `:23` is the visible edit; the `description:` block at `:2-8` and the scan-mode format at `:25` are the two that make it real; `:26` is the one that looks like it needs an edit and does not — confirm rather than assume. And check `:10` before writing the repair sentence: the tool the class is allowed to sweep with is `Grep`/`rg`, and a clause naming `grep` would be unrunnable inside the command that contains it.
