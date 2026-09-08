# Handoff — why the budget fix is one sentence, and what it cost to find out

**Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

Task 32.1 is written and has not run. It adds one sentence to `roadmap-engine` and one pointer to `roadmap-outline-deep`, so that a budget stated in characters says what a character is counted with. The task is that small on purpose: it is the residue of a long investigation whose main output was deciding not to build anything.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `.ai-factory/specs/trickster77777/107-character-budget-names-its-method.md` — the task spec, two items and five guards.
- The `32.1` contract line under `### Phase 32` in `.ai-factory/roadmaps/trickster77777.md`.
- `docs/reference-by-name.md` — the rule ratified by the same investigation; this task is its first mechanical consequence.

### Read on demand

- `.ai-factory/rescue-reports/tradeoxy_core/02-the-census-nobody-takes.md` — the sibling project's account of the same defect class, written independently.

## 3. Current state

The roadmap line and the spec are written and uncommitted. Nothing under `src/` is touched.

The defect: two budgets in this family are stated in characters — the contract line's in `roadmap-engine`, the phase preamble's in `roadmap-outline-deep` — and neither says how to count one. The machine sets no locale, so `wc -m` and `awk`'s `length` both return bytes. A line of 991 characters reads as 995. Eight measurements over one session reported bytes as characters before being caught.

The fix keeps every number where it is and adds a unit and a method, in the engine, once — the sibling loads the engine and points at it rather than restating.

## 4. Next step

The task goes to the orchestrator. Nothing needs deciding first.

## 5. Working discipline

**Why it is one sentence and not a project.** The investigation started from a real complaint: roughly a third of reasoning and chat was going into counting characters, bullets and line numbers, and none of it was changing decisions. The obvious diagnosis was that the documents were too glued together, forcing references into their guts. That was measured and refuted: docs in this repository and in both sibling projects are small and split by subject, and citation density does not track file size — a 75-line file carried eleven line-addresses while a 693-line one carried thirteen.

**What the real defect turned out to be.** Naming granularity coarser than reference granularity. A file with a heading every nine lines is still addressed by line when what a caller needs is one bullet out of three and the three are unnamed. A file with no headings at all is cited by name when its parts open with bold lead-ins. From that: a `file:line` reference is a defect report against its target, and position addresses belong in a work-order that is thrown away, never in a spec, a roadmap line or a document.

**Why nothing is being repaired.** Live surfaces in this repository carry zero position addresses; the five in the ratified document are quotations of the defect as evidence. The five hundred-odd in task specs and plans are per-task and perishable, pruned with their tasks. The sibling project carries two dead documentation paths in its roadmap's direction preambles, which is its own two-line fix. There was no repair project to run, and inventing one would have been the failure this session kept catching elsewhere: a mechanism added on top of a remark that asked for none.

**The one thing this task does not close.** The counting habit itself. The rule that produced eight byte-for-character errors lives nowhere — no skill prescribes what a self-verify may ask for, so every work-order invents its checks, and inventions default to the environment's wrong answer. This task fixes the unit. It does not stop a self-verify from demanding a count nobody will act on.

**And the standing observation about the architect.** The same discipline that catches a missing tool grant, a substring containment that would have tripled three paths, and a bare `git clean` next to an untracked sidecar also produces the fanaticism: measurements no decision rests on, inconsistencies without consequence reported as findings, inputs verified while outputs go unsimulated. Turning it down blindly would lose the first set with the second. The distinguishing question that emerged, and the one worth teaching rather than a new mechanism: **will anyone act on this number, and is this a consequence or merely an inconsistency?**

## 6. Error log

Weighed and deliberately not done. Re-opening any of these re-opens a decision:

- **Restructuring the documentation.** Proposed by the symptom, refuted by measurement. Docs are already split by subject in all three projects.
- **Backfilling the position addresses in existing specs and plans.** They are perishable and pruned with their tasks.
- **A skill or a check that enforces reference-by-name.** The rule is a document. Nothing scans for it, and nothing should until it has earned one.
- **Changing the budget numbers.** `~600`, `400–1000` and `~200–500` are untouched; this task adds a unit, not a policy.
- **Writing the self-verify rule.** Named as the open half above, deliberately left unwritten rather than bundled in here.

## 7. Orientation

Phase 32's direction states it in one line: a budget stated in characters is measured in bytes. Everything in the task follows from putting the unit next to the number, at the number's own home.

## 8. Domain model spine

A budget is a rule about an artifact's size, stated where the artifact's format is defined. Its home is the skill that owns the format — `roadmap-engine` for the contract line, `roadmap-outline-deep` for the phase preamble — and a skill that loads another inherits its rules rather than copying them. A budget has two parts: a number and a unit. Until this task, this family stated only the number, and the unit was supplied by whatever command the reader happened to reach for.
