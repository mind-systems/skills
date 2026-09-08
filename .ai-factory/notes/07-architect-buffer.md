# Architect buffer — 07

Private to this architect session. Not a shared artifact; no work-order references it.

## Editor

- Handle: `ad6a88c15b45ee4f5`, agent type `editor`, spawned this session on the first authored apply work-order (the `command-pin-gaps` apply over spec 106).
- Accumulated context so far: that work-order alone. No `REPORT-ONLY` relay has been sent — the user has used no `::` marker this session.

## Pairing role

None assigned. Unpaired session; `architect-pairing-engine` not loaded.

## Session state

- Unit of work: task `31.1` in `.ai-factory/roadmaps/trickster77777.md`, spec `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md`.
- `command-pin-gaps` scan produced six findings. №5 was withdrawn, and it stays withdrawn — but on the pass-test argument alone (neither pin-gaps question fires: the run invents nothing, the task is implementable), not on the seven-descriptions count, which is false. See the deferral below. №1 resolved by user ruling. №2/3/4/6 are the apply round now in flight.

## Rulings recorded this session, in the user's own terms

- **A handoff is `note` under a lens, nothing more.** "Хэндоф, это просто ноут, немного специфичный... Это просто надстройка над ноутом, как дистиллятором смысла! Мы же не пронизываем все скилы ноутами! Хэндоф важен только один раз тому, кому я его отдаю или тому, кому агент его передал." Already the governing position in `docs/sakshi-harness/skill-graph.md` — the skills drifted from the doc, so this is a defect against an existing spec, not a new decision.
- **Provenance is not reference.** A document written after reading a handoff is fine; citing the handoff is not. This is why the mark literal enters spec 106 unattributed.
- The boundary that cuts cleanly: `docs/sakshi-harness/skill-cycle.md` blesses the *act* of handing off (prune's blocked gate). No doc blesses a *reference to a handoff artifact*.

## Open deferrals

- **`$HANDOFF_LIST` in `roadmap-test-coverage`.** The word carries a second concept there — items handed to `roadmap-decompose`, nothing to do with `.ai-factory/handoffs/`. Not a registry violation: `handoff` is absent from `docs/reserved-words.md`, and that document declares itself final and not subject to update. Parked, not dropped. *Trigger:* the user rules on whether the registry admits the genre.

## Closed this session

- **Phase 33 written** (round in flight): one task, not three. The user's correction was right by the project's own rule — four sites, four files, one reason to revert. Splitting by file is not splitting by reason.
- **The citation rule left 31.1 entirely** — the user's ruling: the task states no rule about what may cite a handoff, not in the `description:` and not in the body. Reason, in the user's terms: `note` carries no such rule and a handoff is `note` under a lens. The mark's own mechanics stay untouched. The removal covers the contract line and four places in spec 106.
- **The doc-gap deferral is dropped with it.** Nothing will prescribe from a `description:`, so `docs/always-loaded-discipline.md` has no gap left to close. Kept only as method: the claim that seven shipped `description:` blocks already prescribe does not survive inspection — every candidate is a scope statement (`test-philosophy`, `architect-editor-engine`, `roadmap-engine`), a routing statement (`architect-pairing-engine`'s "Load only when…", which `docs/skill-description-field.md` names as the field's own purpose), a quoted error literal (`task-rescue`), or an agent definition outside the skills manifest (`src/agents/editor.md`). Counterexamples: zero. The original entry here copied another architect's count without checking it — a count is a claim about files, and it is verified against the files.
- **Contract line `31.1`** measured 993 code points before the citation rule came out of it, against a 400–1000 budget. Related: task `32.1` pins how a code point is counted.

## Standing method rule, learned the hard way this session

**An expectation in a work-order is scoped to what the order changes — never to the whole file or the whole tree.** Four violations, all the same shape:

- `git status --porcelain` pinned as "exactly two entries", twice, ignoring pre-existing modified and untracked files including another architect's.
- `cited as confirmation` → 0 across the whole file, while the same order's guardrail explicitly preserved a sentence containing that phrase.
- `handoffs/` → 0 across the whole file, while three pre-existing occurrences were guardrail-protected — `roadmap-prune`'s gate legitimately names the directory, which is the task's own ruling.

The last two are self-contradicting orders: a verify command that can only pass by breaking a guardrail in the same order. The editor caught all four and never trimmed text to force a match. Write the count over the added text, or name the pre-existing occurrences in the expectation itself.

## Buffer ownership

`.ai-factory/notes/` in this repository holds only architect buffers, one per session; `06-` belongs to another architect and is never edited from here.
