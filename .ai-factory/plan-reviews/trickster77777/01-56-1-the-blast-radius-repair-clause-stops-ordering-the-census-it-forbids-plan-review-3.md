## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/01-56-1-the-blast-radius-repair-clause-stops-ordering-the-census-it-forbids.md` (round 3)
**Task:** 56.1 — the blast-radius repair clause stops ordering the census it forbids
**Spec:** `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md`
**Governing spec:** `docs/counts-go-stale.md` (phase 56 header)
**Files Reviewed:** `src/commands/command-pin-gaps.md`, note 138, spec 154, phase note 150, `docs/counts-go-stale.md`, `.ai-factory/roadmaps/trickster77777.md`, ARCHITECTURE, plus plan-review-1 and plan-review-2
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is the governing boundary here; the task rewrites prose inside one command body and one note, adds no `loads:` edge, extracts nothing into an engine, and inlines nothing from one. No boundary moves.
- **Rules** — n/a (WARN). No `.ai-factory/RULES.md` in this repo; nothing to check against.
- **Roadmap** — OK. The plan's title matches roadmap line 56.1 in `.ai-factory/roadmaps/trickster77777.md` (owner `trickster77777@gmail.com`) verbatim; the contract line's `Spec:` tag resolves to spec 154; the phase 56 header names `docs/counts-go-stale.md` as governing spec and note 150 as the phase note. Both walked. The contract line's untouched list — definition sentence, blocker sentence, correct-as-written tail, Value holes — is reproduced in the plan.
- **Contract-text fidelity** — OK, re-verified mechanically this round. All three pinned strings diff byte-identical against spec 154's "The change" section: the new `Repair:` sentence, the new `**default:**` line (compared against the *second* `> **default:**` blockquote in the spec — the first is the current-state copy), and step 3's note-138 replacement (the `Repair:` sentence minus its `Repair: ` prefix and its terminal period, exactly as spec 154 renders the resulting paragraph). Both "currently" quotations also diff identical against ground truth — `src/commands/command-pin-gaps.md` line 44 and note 138 line 11 — and note 138's quote characters are straight `"`, as the plan states.
- **Governing spec** — OK. `docs/counts-go-stale.md` § "The worse failure is reconciling one" ("Membership is answerable and actionable; a discrepancy in a total is neither") is what the plan's Blast radius step now enacts: membership check, total explicitly disclaimed, no remaining hit edited.

### Round-2 findings: both resolved

1. **The Invariant passed vacuously on a broken sweep pattern** — fixed, and fixed in the form the clause being installed demands. The Invariant now opens with a positive term: the sweep "must still return `.ai-factory/specs/trickster77777/154-…md`, whose current-state section records the old wording deliberately and keeps it after the change — an empty or 154-free result means the pattern was mistyped, not that the repository is clean," and the disappearance of the two targets is made conditional on that result ("Given that result…"). The optional pre-edit baseline run was also taken up ("run the same sweep once **before** editing and confirm both targets appear, so their later absence is a measured change rather than an absence of evidence"). Verified against ground truth: 154's current-state section does hold the old wording and is pinned to keep it, so the anchor is guaranteed present on both sides of the change.
2. **The fourth membership class living only in the Invariant** — fixed. The Rule's exception list now reads as one statement of four classes: "a task spec's own current-state section, the note of a phase already decomposed, a handoff, and a run artifact of this task itself (this plan and its plan-reviews)."

### Critical Issues

None.

Verification performed this round, beyond the byte-diffs above:

- **The sweep and its membership claim, run.** `grep -rln "sweep whose enumeration goes into the task spec, never a sentence saying something may need updating" .ai-factory/ docs/ src/` returns 8 files today; after the two target edits it returns 6, and each of the 6 falls in a named class — spec 154 (task spec current-state), note 150 (phase 56's note, phase decomposed into 56.1/56.2), handoffs 24 and 27, this plan and plan-review-2. The membership claim holds exactly, with no number asserted anywhere in the plan.
- **The sweep roots are sufficient.** A repo-wide `grep -rln` over the same pattern excluding `.git` returns the identical 8 files, so `.ai-factory/ docs/ src/` misses nothing in `active/`, `upstream/`, or the repo root — the affected set is not under-swept.
- **The discriminator's two claims.** Roadmap line 84 holds `### Phase 44` with no `44.M` task lines (note 138 → undecomposed, in scope); the roadmap holds 56.1 and 56.2 under phase 56 (note 150 → decomposed, excepted). Both as the plan states.
- **Step 2's replacement is unambiguous.** `sweep enumeration` occurs exactly once in `src/commands/command-pin-gaps.md` (line 49); the other occurrences in the repo are the roadmap contract line, spec 154's current-state quotation, and the plan itself — none a target, all correctly left alone.
- **Symlink.** `active/commands/command-pin-gaps.md -> ../../src/commands/command-pin-gaps.md`, so the plan's "no symlink work is needed" is fact, not assumption.
- **Settings.** Testing `no` is right — a prose edit to a command body; by `test-philosophy`'s discriminator there is no silent-failure surface here, and the blast-radius sweep, not a test, is what catches a non-landing edit. Docs `no` is right — the change conforms to `docs/counts-go-stale.md` rather than amending it.

### Positive Notes

- The plan's own Blast radius block now clears the floor the clause it installs sets: it names a result the sweep must return, so a zero-hit run reads as a broken pattern rather than a clean repository. The first exercise of the new form satisfies the new form — which is the right thing for the task that authors it.
- The pre-edit baseline run turns the targets' later absence into a measured change. That closes the residual path where the edit silently misses and the post-edit sweep is read as evidence.
- Every string the roadmap treats as a type system was re-diffed byte-for-byte and none drifted: bold markers, the `Grep`/`rg` backticks, the em-dash pairs, the `·` separators, and — the easiest thing to get wrong — the dropped `Repair: ` prefix and terminal period in the note-138 variant.
- The discriminator hoisted into the Rule in round 1 still carries its reason rather than a special case ("still live input to planning, read as current ground truth"), which is what makes it reusable for the next reader of the same sweep.
- Atomicity is carried correctly: step 2 declares its dependency on step 1 and repeats the reason, so the pair cannot split across runs.
- Spec 154's two "weighed and left alone" rulings — the three-word short name and the untouched tail — are restated rather than silently re-opened.

## Deferred observations

- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md` — The clause this task installs sets its floor as "naming, at minimum, **the task's own target** as a result the sweep must return." That floor is satisfiable only when the sweep searches for the *new* string a change introduces; for a deprecation sweep like this task's own — searching for the *old* wording, which the change is removing — the task's own targets must, by construction, stop being returned, and no wording of the invariant can name them as must-return results. This task's Blast radius block shows the gap and works around it correctly, anchoring on a third file (spec 154, pinned to keep the old wording) instead. The workaround is sound and the purpose is served, but the clause states the floor in terms of the task's own target and does not name the anchor-on-a-guaranteed-third-party case, so the next implementer meeting a deprecation sweep has to re-derive it. Changing the clause means amending contract text pinned by spec 154 and by the roadmap line, which is outside this task's authority; it wants an amendment to 154 or a follow-on task.
- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-…md` — Spec 154's own **Rule** still excepts "a phase note or a handoff" with no decomposition discriminator, while its **Invariant** requires note 138 — a phase note — to change, carrying the discriminator only as a parenthetical ("phase 44 not yet decomposed"). The plan repaired its own copy of the Rule in round 1 and the repair holds, but the spec keeps the inconsistent form, so the next reader of 154 meets the same contradiction. The task's file boundary is `command-pin-gaps.md` and note 138; repairing the spec is out of scope here.
- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-…md` — Carried forward from rounds 1 and 2, re-verified against the file. After this task lands, `src/commands/command-pin-gaps.md` still describes its own output as an enumeration in two other places: line 36, **The shape it repairs toward** ("a blast-radius hole by enumerating *what breaks on contact*"), and line 38, **What the pass never writes** ("it pins values and enumerates breakage"). Spec 154 pins "Every other line of `command-pin-gaps.md`" as untouched, so the plan is right not to reach them — but the spec's own atomicity argument for pairing the `default:` line applies to these two sentences word for word: the file will forbid the sweep's enumeration in its `Repair:` clause while advertising enumeration as its output two paragraphs above. Phase 56's other task, 56.2, reaches only `roadmap-engine`'s "What a task spec holds" paragraph (`enumerated` → `pinned rather than hedged`), which is the root line 36 derives from by name — leaving line 36 the last place in the chain still saying "enumerating". No task in the phase owns these two sentences; they want an amendment to spec 154's untouched list or a 56.3.

PLAN_REVIEW_PASS
