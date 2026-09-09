# Architect buffer — 07

Two zones. **Live** is the architect's own and is not read by the editor: a hand that already holds the head's conclusion returns an echo where an independent reading was wanted. **Settled** is the editor's to hold as its own working context, re-read when it changes. The governing account of this file is [paired-loop](../../docs/paired-loop.md).

---

# Live — the architect's own

## Editor

- Handle: `ad6a88c15b45ee4f5`, agent type `editor`, spawned on the first authored apply work-order.
- It has read `docs/paired-loop.md` as instructions addressed to itself, and holds this file's Settled zone as its own working context. It does not read this Live zone.
- Accumulated: every apply round of specs 106–115, the roadmap through phases 36–37, `docs/paired-loop.md`, the two phase notes; one `REPORT-ONLY` relay of the user's `/task-rescue ::`; two delegated sweeps — the open tasks against the documentation, and the four paired-loop artifacts against the spec.
- It has consumed well over 400k tokens this session, past any window, so it has silently lost early history. Treat its accumulated context as partial, never as a record: a round it handled hours ago may be gone from it while the file it produced is not.

## Pairing role

None assigned; `architect-pairing-engine` not loaded. A second architect works this repository concurrently, reached only through the user — its buffers are `05-` and `06-`, never edited from here.

## Where the work stands

Every task through 35.1 has landed; the roadmap holds 35 closed tasks and no open ones. Phases 36 and 37 are drafted with no tasks under them, and `docs/paired-loop.md` is the governing spec they are executed against.

Next in the cycle: `roadmap-prune` to fold the closed tasks into Features, then `roadmap-outline-deep` and `roadmap-decompose` over 36 and 37.

## Open deferrals

- **`note`'s numbering glob cannot see a three-digit file.** Its scan is `[0-9][0-9]-*.md`; in `.ai-factory/specs/trickster77777/` that matches 19 files with a maximum of `99`, while the directory's real maximum is `115`. Followed literally the next number is 100, colliding with a file already there. The failure is silent — no error, two files sharing a prefix, and every later scan compounding it — and `note` is loaded by eight callers, so every destination folder is exposed. *Trigger:* the user says to write the task.

- **`$HANDOFF_LIST` in `roadmap-test-coverage`.** The word carries a second concept there — items handed to `roadmap-decompose`, nothing to do with `.ai-factory/handoffs/`. Not a registry violation: `handoff` is absent from `docs/reserved-words.md`, and that document declares itself final. Task 34.4 set the precedent for removing exactly this kind of collision without breaking that finality. *Trigger:* the user rules on whether the registry admits the genre.

---

# Settled — the editor's to hold

## Working discipline

**Standing rule about this section: whenever the user gives feedback on how the architect works, record it here immediately, as settled behaviour — not as an episode.** A ruling that stays in the chat dies with the chat, and the next session repeats the correction.

Keep the chat on substance. Investigation legwork goes to the editor as one `REPORT-ONLY` batch rather than a run of greps in the chat; file writes, scripts included, go as `APPLY-EDIT`. Verification of what landed stays with the architect — that is the layer that caught every discrepancy, including a silent bug in the architect's own analysis script. **The architect** never pastes its raw output into the chat: it states the conclusion in a line. The editor's own reports are the opposite — they carry the raw output to the architect, which is how a wrong expectation is caught, and `editor.md` requires it. A single decisive check is cheaper run directly than relayed.

Until the shared engine holds this file, the editor has no way to notice a change here on its own. The architect names it when the settled zone moves; an unannounced edit reaches nobody.

**The marker and delegation are different axes.** `::` governs whose message crosses the channel: it forwards the *user's* payload for an independent read, and an unmarked user message is never forwarded. Delegating the architect's *own* legwork needs no marker and no permission. When the user's payload is relayed, the editor's agreement is signal and gets reconciled; when the architect's legwork is relayed, there is no second opinion in it — it is a hand, and treating its agreement as corroboration mistakes an echo for evidence.

**Handoffs, the buffer and rescue reports are written by the architect's own hands.** A handoff is the architect's own context; having the editor retell it produces something unpredictable, because the context is not the editor's to hold. The same holds for anything the architect authors from its own reading, and for a mark an artifact addresses to its own reader. Everything else goes to the editor by default.

**The pairing is a brush and its fingers, not a specification and its auditor.** The architect supplies meaning, constraint and place; the editor writes the artifact. Pin what a sentence must say and where it goes — not its characters — because a writer with the file open never restates what already stands beside it, and an architect composing replacement text blind does exactly that. What stays is mechanism, not ceremony: anchor by a unique string rather than a position, so two sessions editing one file do not collide; and read the landed result — not to audit the editor, which over a full session never once silently deviated, but to see what the decision looks like once it is real. Every defect that reading caught was the architect's own.

**Fingers explore a surface before anything is written about it, and whoever touched it writes.** A grounded section — what is true now, read from the code with exact values — belongs to the hand that had the file open, not to an architect who compressed a sweep into a claim and passed the claim on. The claim is where the detail dies: a grep showing six hits became "the shape occurs twice" in a spec when the file holds it once, because the output was read and the lines were not. The architect keeps the decision — what must change and why.

The split that governs it: a **factual** question (what does this line say, how many times does this word occur) is best answered by one careful reader who touches and writes, since two summarisers are worse than one; a question of **judgment** (is this task right, does it contradict a doc) needs two independent readings reconciled, and there the independence is the whole point.

**A ruling recorded here is a debt against the skill, not a record of one.** It is erased when it reaches the artifact that should hold it. A buffer that works well as shared context makes it more comfortable to leave rulings in it, so the drain tightens rather than relaxes.

## Rulings, in the user's own terms

- **A handoff is `note` under a lens, nothing more.** "Это просто надстройка над ноутом, как дистиллятором смысла! Мы же не пронизываем все скилы ноутами!" Already the governing position in `docs/sakshi-harness/skill-graph.md`; the skills drifted from the doc.
- **Provenance is not reference.** A document written after reading a handoff is fine; citing it is not.
- **A skill is its own documentation.** `docs/` describes the system; a single skill's behaviour belongs in the skill. Behaviour spanning several artifacts — the paired loop — belongs in `docs/`.
- **A task spec holds three things and nothing else** — what is true now, read from code with exact values; what must be true after, in the code's own terms; what breaks on contact, enumerated.
- **A task is not an instruction for reviewing itself.** The orchestrator has a department for that. Guards against what nobody would do, and counts that restate the instruction, belong to neither tier.

## The discriminator that decides a check

`test-philosophy`, applied one tier up. **Silent failure → check it. Loud failure → do not.** A check that can only fail where the instruction was ignored describes a loud failure: the diff shows it on sight. Dropping a clause from a rationale is silent; not writing a pinned command is loud. A check that cannot fail on this repository at all — that an interpreter counts characters, that a file contains what was just written into it — is not a weak check but not a check.

## Standing method rule

**An expectation in a work-order is scoped to what the order changes — never to the whole file or the whole tree.** Seven violations in one session, three shapes:

- stale state ignored — `git status` pinned as "exactly N entries" while other files were already modified or untracked;
- a count contradicting the order's own guardrail — a phrase counted at zero while the same order preserved a sentence containing it;
- a count that cannot return its number by construction — a phrase the check must restate to check it; an unanchored grep catching the word in prose; plain arithmetic.

Count over the added text, anchor the pattern, or name the pre-existing occurrences in the expectation itself.

## Measurements worth keeping

- **Where the pipeline fails:** across three months of run notifications, 91 of 94 failures happen before any code is written — 73 at plan review, 18 at review, 3 at implement. The run-event log seeded from that history is `orchestrator/metrics/runs.jsonl`.
- Rescue reports 02 and 03 diagnose **over**-specification; 04 and 05 diagnose **under**-verification and prescribe more of what 02/03 identified as the disease. Two architects reached the same wrong prescription independently — convergence here is a shared blind spot, not confirmation.
- **Seven tasks landed in a row with no rescue** after the specs were cut back to behaviour, against five rescues over the four tasks before. The sharpest point: a task that had burned six planning rounds and two rescues passed first time once its spec pinned a paragraph's text instead of describing its scope. The run does not separate the cut check lists from the three-part shape — one intervention through several channels.
- `tradeoxy_core`: 31 open tasks, **13** whose spec carries the counting register, 18 clean. In its eight most recent specs — Guards 17%, Tests 13%, Acceptance 5%. The cut is Guards + Acceptance, about 22%. **`## Tests` stays** — tests are a `test-philosophy` deliverable, not review instructions, and an unwary cleanup takes them first.

## Where the skills lag this practice — the drift register

Verified against the files, not assumed:

- **`agent-architect`: "You author your own prompt in exactly one case: the apply work-order"** — false, in the section heading and in the body. The architect also authors `REPORT-ONLY` prompts for its own legwork.
- **Handoffs and rescue reports are named nowhere in `agent-architect`.** It names only the buffer as the file the architect edits directly; `rescue report` appears zero times.
- **`agent-architect` says the editor is never told about the buffer**, and `architect-editor-engine` holds only the two message formats. Phases 36 and 37 close both, against `docs/paired-loop.md`.

## Buffer ownership

`.ai-factory/notes/` in this repository holds only architect buffers, one per session; `05-` and `06-` belong to the other architect and are never edited from here.
