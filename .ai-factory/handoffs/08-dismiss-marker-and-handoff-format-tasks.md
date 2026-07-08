# Handoff — two skills-repo tasks stand ready: the dismiss marker and the handoff skill's own shape

A narrative, continuing `07-rescue-dismiss-disposed-observations.md` — read that first for the
rescue-dismiss backstory; this picks up after it and won't repeat it. The originating session's
context isn't available here; trust these files, not memory. (No compact happened — this is a
cross-project working session; the point is simply that the reasoning below lives in files now.)

## Where we are

Two planning tasks are written into `.ai-factory/ROADMAP.md` (the two newest `- [ ]` lines before
`---STOP---`) with full specs, **uncommitted**. Both are ready to hand to an implementation run.
Nothing is half-built; the only in-flight thing is the decision to commit and schedule them.

## Task one — spec 13 (rescue may *dismiss*, not just promote)

Handoff 07 left this as a fresh task. Since then a skills agent revised the spec, and we **verified
that revision against the real skill files** (not from memory — that discipline mattered twice this
session). Two "cracks" the agent closed, both confirmed sound:

- The `## What NOT to do` clause in `milestone-rescue/SKILL.md` isn't just a banned-marker list — it
  also asserts *"Rescue's only marker is `[promoted → <path>]`"* and *"evaluating, dismissing…
  stay `milestone-rescue-audit`'s"*, plus *"do not dismiss an observation by marker"*. All three
  become false. The spec now correctly instructs a **whole rewrite** of that clause with exact
  target text, not a "remove one item from the list" — verified the live clause really contains all
  three assertions (lines 464–468).
- The verify step's note-37 baseline is now honestly labelled *(output shape)*, with the caveat
  that note-37 probed a *passed* outlier (audit-flavoured territory the audit already covers), while
  the capability's real target is the ordinary rescue of a **failed** task. The verify holds on
  marker output shape regardless of which skill pins.

One nit I found and **did not apply** (offered, awaiting the user): the spec pins the clause as
`milestone-rescue:464-467`, but it actually runs **464–468** (the closing `` `milestone-rescue-audit`'s ``
sits on 468). Low risk — the spec quotes the clause text verbatim so an implementer greps for it —
but `464-467 → 464-468` is the precise fix. Also a mild heading label: §1 still says "(one sentence)"
though the §6 writer-set is now two sentences post-spec-09. Both intra-spec; the ~600-char contract
line stays valid either way.

## Task two — spec 14 (the handoff skill's own shape)

This one came out of critiquing `command-handoff` itself, prompted by two live failures *this
session*: (a) handoff 07 opened "the chat is compacted" and the receiving agent announced *"we had a
compact, rehydrating"* — but there was no compact; (b) getting a narrative instead of the 11-section
skeleton required saying "не делай этот дурацкий нумерованный ноут" by hand. So spec 14 fixes the
skill's over-fit to *post-compact skeleton state-transfer*, in one file (`src/commands/command-handoff.md`),
two facets under one thesis:

- **Boundary-neutral framing** — strip the hard-coded `/compact` from the description (`:3-6`), the
  Frame skeleton (`:54-55`), and the example pointer (`:136`); the trigger becomes *any* boundary
  (new session / cross-project / self-handoff / compact), keeping only the "mine while context is
  still live" truth.
- **A first-class narrative register** — a second axis *orthogonal* to the note/chat **destination**
  axis: skeleton (state-transfer) vs narrative (understanding-transfer). Narrative × note-destination
  has the agent compose prose and `Write` it directly to `.ai-factory/handoffs/`, **not** through
  `note`'s distiller (distillation flattens the causal thread). This very handoff, and 07, are the
  live baseline.

The non-obvious thing to watch when implementing 14: **keep the two axes distinct.** Destination
(chat vs file) and register (skeleton vs narrative) are orthogonal — do not collapse them into one
four-way enum. And the skeleton register must come out byte-identical; facet B *adds* a register, it
doesn't touch the existing skeleton, proportionality guard, read-map rule, or self-check gate.

The one open decision the user deferred: spec 14 deliberately **bundles** the two facets (one file,
one thesis, discovered together). It is honestly two independently-revertible concerns; I offered to
split into 14a (compact wording) + 14b (narrative register) and the user hasn't chosen. If they say
split, that's a roadmap edit, not a code change.

## State, next step, discipline

- **Uncommitted in this repo:** `specs/13-rescue-dismiss-disposed-observations.md`,
  `specs/14-handoff-narrative-register-boundary-neutral.md`, and the two matching `- [ ]` lines in
  `ROADMAP.md`. Handoffs 07 and 08 themselves are also uncommitted.
- **Already committed elsewhere:** the note-37 dismissal that motivates spec 13 — broker repo commit
  `9fb4891` (separate git), the live baseline spec 13's verify step points at.
- **Next:** the user decides commit + scheduling. On the two micro-decisions above (13's `464-468`
  line-ref fix; 14's split-or-keep), apply only on their word. Then hand 13 and 14 to implementation
  runs — chat plans, the orchestrator implements.
- **Discipline that held all session:** confirm before committing (nothing here is committed);
  ground every claim by reading the actual file, never memory; keep tasks atomic and resist bundling
  adjacent-but-separate concerns (the one place we bundled, spec 14, is flagged and reversible); all
  artifacts in English.
