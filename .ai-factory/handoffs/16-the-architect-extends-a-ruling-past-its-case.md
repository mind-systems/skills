# Handoff — the architect extends a ruling past the case it was written for

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

One defect recurred four times in a single day of architect work, cost six planning rounds and three full reversals, and was caught every time by the user rather than by any gate in the family. The proposal on the table is to teach `agent-architect` not to do it. The originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now

- `.ai-factory/notes/06-architect-buffer.md` — the architect's own recovery file: the pairing role, the editor's handle, and, at the end, four rulings recorded verbatim in the user's words with the corrections that followed. The specimens below are all recorded there. ← lead here.
- `src/skills/agent-architect/SKILL.md` — the skill the proposal would change. It carries no rule about how a ruling becomes an artifact; that absence is the subject.
- `.ai-factory/rescue-reports/skills/03-30-1-six-rounds-on-a-two-part-write-nobody-asked-for.md` — the fullest specimen, written up in its own genre: a mechanism nobody asked for, six planning rounds, and the moment it entered.

### Read on demand

- `.ai-factory/handoffs/13-phase-note-plain-behavior-no-ceremony.md` § 8 — the user's own words on what they wanted from the phase-note work, and § 6, the first chain of unrequested additions.
- `.ai-factory/rescue-reports/skills/01-…` and `02-…` — the other two rescues of the same week.
- `docs/always-loaded-discipline.md` and `docs/reference-by-name.md` — written this session and the previous one; both bear on how a rule reaches an agent without being restated.

## 3. Current state

**Done:**

- **Task 30.1 landed** (`248ebbe`) after two failures and two rescues. `task-rescue` now writes one report per run, once, at the end.
- **Task 29.1 landed** (`0762ab8`) after one failure and one rescue. `command-pin-gaps` walks the task into the code.
- **The always-loaded discipline has a doc** — `docs/always-loaded-discipline.md`, with edges from `skill-description-field`, `context-tree`, `ARCHITECTURE.md` § Composition and the CLAUDE.md guides table. Uncommitted.
- **Three rescue reports for `skills` and three for `tradeoxy_core`** sit under `.ai-factory/rescue-reports/`. They are the record the deletions used to destroy.

**Open:**

- **31.1** — the handoff says on itself that it is a spent, temporary buffer. Written, not run. Spec 106.
- **The proposal in this handoff.** Nothing is written for it. It is a question for the user, not a task.

**Uncommitted:** the roadmap, `ARCHITECTURE.md`, `CLAUDE.md`, `docs/skill-description-field.md`, `docs/philosophy/context-tree.md`, the architect buffer, and the untracked new docs, specs, handoffs and rescue reports listed by `git status`.

## 4. Next step

Ask the user whether to teach `agent-architect` this, and in what form. Do not draft the task first — a gate written against this defect is itself an instance of it, and that trap is the whole reason the session stopped here.

## 5. Working discipline

- **Do what was asked, nothing more.** A ruling is a sentence to write down, not a taxonomy to build.
- **Subtract before adding.** When something is wrong, the first candidate is deleting the clause that misbehaves, not adding a concept that classifies it.
- **The pair.** The architect decides; a work-order to the applying half is one code block with every value pinned and a self-verify list. But the pair is for work that can be wrong and needs a second reader — a roadmap line, a spec, a skill body, a doc. What the architect authors from its own reading, and what an artifact instructs its own reader to do, the architect does with its own hands: handoffs, its buffer, rescue reports, a mark addressed to the reader.
- **Measure, never estimate.** Contract lines in characters, with `python3` or `wc -m`; `awk` counts bytes here whatever the locale says.
- Never commit without explicit permission; never push; two repositories, two permissions.

## 6. Error log — the four specimens

Each begins with something the user said that is true, and ends in a structure they did not ask for. The step between is silent and feels like diligence.

- **The governing-spec hole.** The ruling was one sentence: where behavior is not described in the docs, that is a hole in the ТЗ and the docs step's job. It became, in a task spec, a routed finding class with an owner; then a new concept, "phase-header gap", invented to classify a missing header line; then two `Governing spec:` lines added to phases of the roadmap. **Reverted in full.** The user's word: «ёбаный фанатизм».
- **The two-part report.** The user asked for one report, written when a rescue has finished and the task is ready to run again. They then remarked that a whole history can pass between the start of a rescue and its end — a difficulty named, not a mechanism requested. The architect answered with a design that opened the report early and completed it later, which forced a path to be carried across an arbitrary gap and then recovered when lost. **Six planning rounds across two orchestrator runs, both failed, both rescued.** Deleted; the task landed on the next run.
- **Self-sufficiency read as blindness.** The ruling was that a task is self-sufficient and the orchestrator's job is code, not validating tasks. The architect turned it into "the run must not open a document" and recommended deleting the `Governing spec:` clause from three orchestrator prompts. **Withdrawn** on the user's correction: nobody forbids reading the documentation, that is what the links are for; the real hole is a run that amends a document because the task disagrees with it.
- **The handoff mark.** "The architect never touches a shared artifact" was applied to a one-character mark that the handoff addresses to its own reader, producing a work-order for it — in a session that had already written a handoff by hand with no work-order. **Corrected.**

Two mechanical errors from the same day, listed so they do not return: `LC_ALL=en_US.UTF-8 awk '{print length($0)}'` returns bytes on this machine, and every contract line measured this way was measured wrong (all were inside the band regardless); and a verification bullet that names the very token it requires to be absent will always fail against itself.

## 7. Orientation

- **The defect is not "adding things".** It is extending a true rule past the case it was written for. The input is always correct. That is why it survives review: each artifact is consistent with the one above it, and the reviewer checks consistency, not aim.
- **It is invisible to every gate the family owns.** The atomicity gate asks about size, `command-pin-gaps` asks how a task lands on the code, the plan review asks whether the plan matches the spec. All of them make an unasked-for task *better*.
- **Writing a gate against it is the trap.** "Detect fanaticism" is exactly the kind of classifying structure the defect produces. Whatever is done here has to be smaller than the thing it prevents.
- **The cheapest existing counter already worked, twice.** The user caught three of the four within minutes, by asking what the task was for. And an agent elsewhere refused to decompose a phase whose documentation did not describe it, on the strength of one line in the global CLAUDE.md — a discipline in the always-loaded layer produced the refusal with no gate at all.

## 8. Domain model spine

- **A ruling is a sentence, and stays one.** Where the architect believes a ruling implies more than it says, the implication is a question for the user, not an artifact.
- **The reader of a work-order cannot see what was not asked for.** The applying half checks the order against the files; it has no access to the conversation the order came from. So the proportion check — what did the user ask for, in their words, and what does this order do beyond it — has no owner but the architect.
- **The candidate landing points**, none chosen: one line in `agent-architect` making a ruling's own scope the architect's responsibility; a proportion check before a work-order ships; or nothing at all, on the argument that a human catching it in minutes is cheaper than any machinery. The third is a real option and should not be dismissed to look thorough.

## 9. Hard rules

- Never commit without explicit permission; never push.
- All artifacts in English; the user's words may be quoted verbatim in the language they were said.
- No new term, token, class, owner or task unless the user asked for it in words.
- A contract line is 400–1000 characters, measured in characters.
- Position addresses (`file:line`) belong in a work-order, never in a spec, a roadmap line or a doc — `docs/reference-by-name.md`. Spec 105, which is committed and closed, carries ten of them; it predates the rule.
