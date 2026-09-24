## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/01-56-1-the-blast-radius-repair-clause-stops-ordering-the-census-it-forbids.md`
**Task:** 56.1 — the blast-radius repair clause stops ordering the census it forbids
**Spec:** `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md`
**Governing spec:** `docs/counts-go-stale.md` (phase 56 header)
**Files Reviewed:** 4 targets/sources read in full (`src/commands/command-pin-gaps.md`, spec 154, phase note 150, note 138) plus roadmap, governing spec, ARCHITECTURE
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" governs skill/engine boundaries; this task edits a command's own prose only, adds no `loads:` edge, and moves no content between a lens and an engine. No boundary touched.
- **Rules** — n/a (WARN). No `.ai-factory/RULES.md` in this repo; nothing to check against.
- **Roadmap** — OK. The plan's title matches roadmap line 56.1 in `.ai-factory/roadmaps/trickster77777.md` (owner `trickster77777@gmail.com`) verbatim, the `Spec:` tag resolves to spec 154, and the phase header names `docs/counts-go-stale.md` as the governing spec and note 150 as the phase note. Both were read. The contract line's "stay untouched" list (definition sentence, blocker sentence, tail, Value holes) is reproduced in the plan.
- **Contract-text fidelity** — OK, verified mechanically. The plan's new `Repair:` sentence and its new `default:` line are byte-identical to spec 154's "The change" section (diffed character-for-character, bold markers and em dashes included). The "currently" quotation in step 1 matches the **Blast-radius holes** clause in `src/commands/command-pin-gaps.md` exactly. Symlink claim verified: `active/commands/command-pin-gaps.md -> ../../src/commands/command-pin-gaps.md`, so no `active/` work is needed.

### Critical Issues

**1. The Blast radius step's Rule excludes the very file its Invariant targets** — `.ai-factory/plans/trickster77777/01-56-1-….md`, step "Re-run the sweep and check the invariant"

The Rule reads: "…except a task spec's own current-state section, and a phase note or handoff, which record what was true when written and are not kept in sync here." The Invariant then demands the sweep "no longer returns either target — `src/commands/command-pin-gaps.md` or `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`".

Note 138 **is a phase note** — its first line is `# Phase 44 — four witnesses, each trusted where it is blind`. So the Rule's own exception excludes 138 from the affected set, while the Invariant requires it to have been changed. The block contradicts itself, and it does so in the one step whose job is to demonstrate the rule/sweep/invariant form this very task installs in `command-pin-gaps.md`. It also reads as arbitrary next to the plan's own acceptance of "phase note 150" as a legitimate remaining hit: two phase notes, opposite treatment, no stated discriminator.

Spec 154 carries the discriminator and the plan dropped it: the spec's Invariant names 138 as "phase 44's own note, **phase 44 not yet decomposed**, whose Q4 paragraph quotes this exact sentence as current ground truth". That is the property that separates 138 from 150 — an undecomposed phase's note is still live input to planning, a decomposed phase's note is already history.

*Failure scenario:* an implementer (or the reviewer after it) reads the Rule literally, classifies 138 under the phase-note exception, and skips the step-3 edit as out of the affected set — then the Invariant fails and the task loops. Or the edit is made and the verification step is judged incoherent on review.

*Repair:* restate the Rule so its exception carries the discriminator, e.g. "…except a task spec's own current-state section, and the note of a phase already decomposed or a handoff, which record what was true when written; the note of a phase not yet decomposed still reads as current ground truth for planning and is in scope."

**2. The Blast radius step writes a census — and it is already wrong** — same step

"Remaining hits fall under the rule's own exceptions (this task's spec 154, phase note 150, handoffs 24 and 27) and are left alone."

Two problems. First, the sweep as written greps `.ai-factory/`, which contains `plans/` and `plan-reviews/`: **the plan file itself already matches** (it quotes the old wording three times, in steps 1, 3 and 4), and this plan-review does too. Verified — running the plan's own sweep today returns 7 files including the plan; after the change it returns 6, not the 4 the plan enumerates. Second, a plan file is neither a task spec's current-state section, nor a phase note, nor a handoff, so no clause of the stated Rule covers it.

*Failure scenario:* the implementer runs the sweep, gets 6 hits against an enumeration of 4, and either reports a false failure or "repairs" the extra hits — editing the plan file or the plan-review to strip the old wording, destroying the record they exist to hold.

*Repair:* delete the parenthesised list. The spec deliberately does not enumerate the remainder ("their count is not this invariant's concern"), the plan says the same thing one clause later ("their number is not the invariant's concern"), and the list is precisely the tally this task exists to remove from durable artifacts — a bad exemplar even in an ephemeral plan. If a check on the remainder is wanted, state it as membership: every remaining hit is a spec current-state section, a decomposed phase's note, a handoff, or a run artifact of this task.

**3. Step 3 leaves the replacement string for note 138 unpinned at its boundary** — same plan, step "Update note 138's Q4 quotation"

The step says: replace the quoted string "with the new `Repair:` wording, quoted identically to what now stands in `command-pin-gaps.md`." In `command-pin-gaps.md` that wording now *begins with* the literal token `Repair: `. Note 138's sentence, however, reads `The blast-radius repair already reads "…"` — the prefix must **not** enter the quotation, and spec 154 pins that unambiguously by writing the resulting paragraph out in full, starting at `the **rule** that defines the affected set`.

*Failure scenario:* the implementer takes "quoted identically" literally and writes `The blast-radius repair already reads "Repair: the **rule** …"`, which reads as a stutter and diverges from the paragraph spec 154 pinned — a deviation from contract text that is only caught if the reviewer re-reads spec 154 word by word.

*Repair:* reproduce the target string in the step the way step 1 does, with the same character-for-character instruction: replace with `the **rule** that defines the affected set, the literal `Grep`/`rg` **sweep** that finds it on demand, and the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found`, keeping note 138's existing straight double quotes and dropping the `Repair: ` prefix.

### Positive Notes

- Both contract strings were reproduced from spec 154 without drift — diffed byte-for-byte, including the bold markers, the `Grep`/`rg` backticks, the em-dash pair and the `·` separators in the report format. Step 1's explicit "reproduce it character-for-character, bold markers included" is the right instruction for text the roadmap treats as a type system.
- The atomicity argument is carried correctly: step 2 declares its dependency on step 1 and repeats the spec's reason ("either alone leaves the file ordering a tally in one place and forbidding it in the other"), so the two edits cannot be split across runs.
- The plan preserved spec 154's "weighed and left alone" ruling on the three-word short name rather than silently re-opening it, and restated the reason (the new well-formedness requirement is a property of the invariant, not a fourth element).
- The untouched list is concrete and matches the file: the opening definition sentence, the contradiction-and-blocker sentence, the oversized-sweep tail, and the whole **Value holes** clause — with Value holes correctly flagged as the model, not a target.
- The symlink question was asked and answered correctly instead of being assumed.

## Deferred observations

- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md` — After this task lands, `src/commands/command-pin-gaps.md` still asserts in two other places that a blast-radius hole is repaired by an enumeration: the **The shape it repairs toward** paragraph ("a blast-radius hole by enumerating *what breaks on contact*") and the **What the pass never writes** paragraph ("it pins values and enumerates breakage"). Spec 154 pins "Every other line of `command-pin-gaps.md`" as untouched verbatim, so the plan is right not to touch them and I am not blocking on it — but the spec's own atomicity argument for pairing the `default:` line ("deploying either alone leaves the file self-contradictory") applies to these two sentences word for word: the file will forbid the sweep's enumeration in its `Repair:` clause while describing its own output as an enumeration two paragraphs above. Phase 56's other task, 56.2, reaches only `roadmap-engine`'s "What a task spec holds" paragraph (`enumerated` → `pinned rather than hedged`), which makes the **The shape it repairs toward** sentence doubly stale — it derives its wording from that root by name and would be the last place in the chain still saying "enumerating". With only 56.1 and 56.2 in the phase, no task currently owns the two residual sentences; they want either an amendment to spec 154's untouched list or a 56.3.
