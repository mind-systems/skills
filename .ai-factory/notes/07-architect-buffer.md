# Architect buffer — 07

Private to this architect session. Not a shared artifact; no work-order references it.

## Editor

- Handle: `ad6a88c15b45ee4f5`, agent type `editor`, spawned on the first authored apply work-order.
- Accumulated: every apply round of specs 106–110 and the roadmap, plus one `REPORT-ONLY` relay — the user's `/task-rescue ::` on task 31.1, which the editor worked independently and reported on.

## Pairing role

None assigned; `architect-pairing-engine` not loaded. A second architect works this repository concurrently, reached only through the user — its buffers are `05-` and `06-`, never edited from here.

## Where the work stands

| task | state |
|---|---|
| 31.1 | landed and committed |
| 32.1 | rescued at spec+plan depth by the second architect; sidecar `planned:1`, plan kept, no plan-reviews on disk, awaiting a run |
| 33.1 | spec 108 cut back to behaviour — **this is the experiment**, it runs first |
| 34.1, 34.2 | written, phase 34 |

Uncommitted: specs 107–110, the roadmap, 32.1's plan and sidecar, rescue report 05, the buffers. Nothing under `src/`, `docs/`, `active/`, `CLAUDE.md`.

## The open deferral

- **`$HANDOFF_LIST` in `roadmap-test-coverage`.** The word carries a second concept there — items handed to `roadmap-decompose`, nothing to do with `.ai-factory/handoffs/`. Not a registry violation: `handoff` is absent from `docs/reserved-words.md`, and that document declares itself final. *Trigger:* the user rules on whether the registry admits the genre.

## The pending experiment

33.1 goes to the orchestrator with a spec that holds behaviour and no check list. Its result decides two things that are otherwise guesses: whether `command-pin-gaps` needs more than task 34.2 gives it, and whether the thirteen infected `tradeoxy_core` specs are worth a batch cut. Read the next rescue report, or its absence. Change one thing and measure — the reports have existed only since 30.1, and until now nobody read them as a series.

## Rulings recorded, in the user's own terms

- **A handoff is `note` under a lens, nothing more.** "Это просто надстройка над ноутом, как дистиллятором смысла! Мы же не пронизываем все скилы ноутами!" Already the governing position in `docs/sakshi-harness/skill-graph.md`; the skills drifted from the doc.
- **Provenance is not reference.** A document written after reading a handoff is fine; citing it is not.
- **A skill is its own documentation.** `docs/` describes the system; a single skill's behaviour belongs in the skill. This is why the handoff's lifetime stays in `command-handoff` and never entered `skill-graph.md`.
- **A task spec holds three things and nothing else** — what is true now, read from code with exact values; what must be true after, in the code's own terms; what breaks on contact, enumerated. Phase 34 gives that shape a home in `roadmap-engine` and a base in `command-pin-gaps`.
- **A task is not an instruction for reviewing itself.** The orchestrator has a department for that. Guards against what nobody would do, and counts that restate the instruction, belong to neither tier.

## The discriminator that decides a check

`test-philosophy`, applied one tier up. **Silent failure → check it. Loud failure → do not.** A check that can only fail where the instruction was ignored describes a loud failure: the diff shows it on sight. Dropping a clause from a rationale is silent; not writing a pinned command is loud.

Where the register came from: self-verify is prescribed in `agent-architect`, `architect-editor-engine`, `architect-pairing-engine` and `editor.md` — all four for the **channel-message**, none for a task spec. The habit leaked from the channel into the artifact, and `roadmap-engine`'s contract-line bullet naming "guards / verify" was the open door. Task 34.1 closes it.

## Measurements worth keeping

- Rescue reports 02 and 03 diagnose **over**-specification; 04 and 05 diagnose **under**-verification and prescribe more of what 02/03 identified as the disease. Two architects reached the same wrong prescription independently — convergence here is a shared blind spot, not confirmation.
- Every task from 29.1 on has a rescue report: 29.1, 30.1 twice, 31.1, 32.1. The data cannot separate "rescues began at 29.1" from "recording began at 29.1" — reporting landed with 30.1 and 01 was written retroactively.
- `tradeoxy_core`: 31 open tasks, **13** whose spec carries the counting register, 18 clean. In its eight most recent specs — Guards 17%, Tests 13%, Acceptance 5%. The cut is Guards + Acceptance, about 22%. **`## Tests` stays** — tests are a `test-philosophy` deliverable, not review instructions, and an unwary cleanup takes them first.

## Standing method rule, learned the hard way

**An expectation in a work-order is scoped to what the order changes — never to the whole file or the whole tree.** Seven violations this session, three shapes:

- stale state ignored — `git status` pinned as "exactly N entries" while other files were already modified or untracked, twice;
- a count contradicting the order's own guardrail — `cited as confirmation` → 0 and `handoffs/` → 0 while both were guardrail-protected;
- a count that cannot return the number by construction — a phrase the check must restate to check it; an unanchored grep catching the word in prose; plain arithmetic.

The editor caught all seven and never trimmed text to force a match. Count over the added text, anchor the pattern, or name the pre-existing occurrences in the expectation itself.

## Buffer ownership

`.ai-factory/notes/` in this repository holds only architect buffers, one per session; `05-` and `06-` belong to the other architect and are never edited from here.
