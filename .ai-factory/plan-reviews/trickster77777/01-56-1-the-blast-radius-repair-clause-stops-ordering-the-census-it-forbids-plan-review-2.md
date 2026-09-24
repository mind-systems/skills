## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/01-56-1-the-blast-radius-repair-clause-stops-ordering-the-census-it-forbids.md` (round 2)
**Task:** 56.1 — the blast-radius repair clause stops ordering the census it forbids
**Spec:** `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md`
**Governing spec:** `docs/counts-go-stale.md` (phase 56 header)
**Files Reviewed:** `src/commands/command-pin-gaps.md`, note 138, spec 154, note 150, `docs/counts-go-stale.md`, `.ai-factory/roadmaps/trickster77777.md`, ARCHITECTURE, plus plan-review-1
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is the governing boundary; this task rewrites prose inside one command file and one note, adds no `loads:` edge, and moves nothing between a lens and an engine.
- **Rules** — n/a (WARN). No `.ai-factory/RULES.md` in this repo.
- **Roadmap** — OK. Plan title matches roadmap line 56.1 (`.ai-factory/roadmaps/trickster77777.md`) verbatim; the `Spec:` tag resolves to spec 154; the phase 56 header names `docs/counts-go-stale.md` and note 150. Both read.
- **Contract-text fidelity** — OK, re-verified mechanically this round. All three pinned strings diff byte-identical against spec 154: the new `Repair:` sentence, the new `default:` line, and step 3's note-138 replacement (which correctly omits the `Repair: ` prefix). Both "currently" quotations also diff identical against ground truth — `src/commands/command-pin-gaps.md` line 44 and note 138 line 11. The clause occurs exactly once in the file, so "replace only the second sentence" is unambiguous.
- **Governing spec** — OK. `docs/counts-go-stale.md` § "The worse failure is reconciling one" states "Membership is answerable and actionable; a discrepancy in a total is neither." The plan's Blast radius step now checks membership and explicitly disclaims a total, matching the governing spec rather than merely the task spec.

### Round-1 findings: all three resolved

1. **Rule/Invariant contradiction over note 138** — fixed. The Rule now carries the discriminator: "The note of a phase **not yet decomposed** carries no exception … That is what separates note 138 (phase 44, no task lines in the roadmap) from note 150 (phase 56, decomposed into 56.1 and 56.2)." Both claims verified against ground truth: note 138 is headed `# Phase 44 …` and the roadmap holds only a phase 44 header with no `44.M` task lines; note 150 is headed `# Phase 56 …` and the roadmap holds 56.1 and 56.2.
2. **The census in the Blast radius step** — fixed. The parenthesised four-file enumeration is gone, replaced by a membership clause plus "Check that membership, never a total". Re-ran the plan's own sweep: 7 hits today, 5 after the change, and every one of the 5 falls in a named class (spec 154 current-state, note 150 decomposed-phase note, handoffs 24 and 27, this plan) — the membership claim holds exactly, with no number asserted.
3. **Unpinned replacement boundary in step 3** — fixed. The target string is now reproduced character-for-character with an explicit ruling that the `Repair: ` prefix stays out, plus the reason. Note 138's quote characters confirmed straight `"` (hex-checked), matching the plan's "keep note 138's existing straight double quotes".

### Critical Issues

**1. The plan's own Invariant passes vacuously on a broken sweep pattern — the exact failure the clause it installs forbids** — plan step "Re-run the sweep and check the invariant"

The Invariant has two terms, and both are satisfied by an empty sweep result:

- "the sweep no longer returns either target" — trivially true of zero hits;
- "Every remaining hit is a task spec's own current-state section, a decomposed phase's note, a handoff, or a run artifact of this task itself" — vacuously true over an empty set.

The sweep is a long single-line literal (`"sweep whose enumeration goes into the task spec, never a sentence saying something may need updating"`) containing a comma and spaces, re-typed by hand at verification time. Truncate or mistype one word of it and it matches nothing.

This is precisely the defect the new contract text exists to prevent. The wording being installed reads: "naming, at minimum, the task's own target as a result **the sweep must return**, so an empty result reads as a broken pattern rather than a clean repository." The plan's block states no result the sweep must return, so a zero-hit run reads as success. It matters more here than in an ordinary verification step, because this block is the plan's own first exercise of the form the task is installing — the exemplar fails its own floor.

*Failure scenario:* the implementer edits `command-pin-gaps.md` (step 1 and 2) but the step-3 edit to note 138 silently does not land — a path typo, or the replacement applied to the wrong one of the two identical-looking old-wording strings in the specs directory. At verification the sweep pattern is mistyped and returns nothing. Both Invariant terms pass, the task is reported converged, and note 138 still quotes the superseded wording as current ground truth for phase 44's planning — the one stale-reader this task exists to fix.

*Repair (one sentence, inside the plan's boundary):* give the Invariant a positive term naming a result the sweep must return. `.ai-factory/specs/trickster77777/154-…` is the natural choice — its current-state section is pinned to keep the old wording, so it is guaranteed present before and after the change. E.g.: "The sweep must still return `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md`, whose current-state section records the old wording deliberately; an empty or target-free result means the pattern is broken, not that the repository is clean." Optionally also read the sweep once before editing and confirm both targets appear, so their later absence is a measured change rather than an absence of evidence.

*Minor, same block:* the fourth membership class, "a run artifact of this task itself", appears only in the Invariant, while the Rule's exception list names three (spec current-state section, decomposed phase's note, handoff). The Rule's own predicate — quoting the old wording "as ground truth for its own argument" — arguably keeps a run artifact out of the affected set to begin with, and the Invariant explains the class well ("records of the run, not instructions the family reads"), so this is not the round-1 contradiction returning. Folding the class into the Rule alongside the other three would make the block read as one statement rather than two.

### Positive Notes

- Every string the roadmap treats as a type system was re-diffed byte-for-byte this round and none drifted: bold markers, the `Grep`/`rg` backticks, the em-dash pair, the `·` separators. Step 1's "reproduce it character-for-character, bold markers included" is the right register for contract text.
- Step 3 resolved a genuine ambiguity in the spec rather than inheriting it. Spec 154 renders the note-138 passage with single quotes (a nesting artifact of quoting inside a quoted italic passage) while note 138 actually uses straight doubles; the plan names the real characters and says why, so the implementer has nothing to guess.
- The discriminator hoisted into the Rule in round 1's repair is not just a patch — it states the underlying reason (an undecomposed phase's note is live planning input; a decomposed one is history), which is what makes the rule reusable rather than a special case for note 138.
- The membership-not-total framing follows the governing spec's own language, not merely spec 154's, and the plan says "no remaining hit is edited" — closing the round-1 failure mode where an implementer "repairs" the records.
- Atomicity is carried correctly: step 2 declares its dependency and repeats the reason, so the pair cannot split across runs.
- The symlink question is answered from fact — `active/commands/command-pin-gaps.md -> ../../src/commands/command-pin-gaps.md` verified — rather than assumed.
- Settings are right for the change: no tests (prose edit to a command body, a loud-failure surface by `test-philosophy`'s discriminator), no docs (the change conforms to `docs/counts-go-stale.md`; nothing there needs amending).

## Deferred observations

- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md` — Spec 154's own **Rule** still excepts "a phase note or a handoff" with no decomposition discriminator, while its **Invariant** requires note 138 — a phase note — to change, carrying the discriminator only as a parenthetical ("phase 44 not yet decomposed"). That is the round-1 contradiction at its source: the plan repaired its own copy, but the spec keeps the inconsistent Rule, and the next reader of 154 meets it again. The task's file boundary is `command-pin-gaps.md` and note 138, so repairing the spec is out of scope here; it wants either an amendment to 154 or a note for whoever next touches phase 56.
- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-…md` — Carried forward from plan-review-1 and re-verified against the file. After this task lands, `src/commands/command-pin-gaps.md` still describes its own output as an enumeration in two other places: line 36, **The shape it repairs toward** ("a blast-radius hole by enumerating *what breaks on contact*"), and line 38, **What the pass never writes** ("it pins values and enumerates breakage"). Spec 154 pins "Every other line of `command-pin-gaps.md`" as untouched, so the plan is right not to reach them — but the spec's own atomicity argument for pairing the `default:` line applies to these two sentences word for word: the file will forbid the sweep's enumeration in its `Repair:` clause while advertising enumeration as its output two paragraphs above. Phase 56's other task, 56.2, reaches only `roadmap-engine`'s "What a task spec holds" paragraph (`enumerated` → `pinned rather than hedged`), which is the root line 36 derives from by name — leaving line 36 the last place in the chain still saying "enumerating". No task in the phase owns these two sentences; they want an amendment to spec 154's untouched list or a 56.3.
