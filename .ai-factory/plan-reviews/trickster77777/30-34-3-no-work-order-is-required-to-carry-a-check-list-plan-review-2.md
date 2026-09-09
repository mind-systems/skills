# Plan Review — 34.3 no work-order is required to carry a check list (round 2)

## Code Review Summary

**Files Reviewed:** plan (1) + targets (4): `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md`, `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md` (read-only); plus the task spec `112-no-work-order-is-required-to-carry-a-check-list.md`, the contract line at roadmap line 186 under the `### Phase 34` header and its preamble, `.ai-factory/ARCHITECTURE.md`, `CLAUDE.md`, `docs/reserved-words.md`, `docs/using-the-language.md`, and round 1 of this plan review
**Risk Level:** 🟡 Medium — the round-1 findings are all closed and every pinned block was applied to a scratch copy of the tree and verified byte-for-byte; but the acceptance sweep the plan pins still cannot return the number the plan pins for it, and the one file that takes two edits gives both spans in pre-edit coordinates after a length-changing first edit.

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is undisturbed: the two *policy* skills (`agent-architect`, `architect-pairing-engine`) drop a required component while the *format engine* (`architect-editor-engine`) keeps its generic `self-verifies` — policy thinned, mechanism untouched, which is where the tiering says each change belongs. No skill is added or re-tiered, no `loads:` edge moves, no engine gains policy. Body caps intact: all three edited files shrink (net −1 line each in `agent-architect` and `architect-pairing-engine`, ±0 in `editor.md`).
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` does not exist in this repo; nothing to check against. The governing conventions live in `CLAUDE.md`, `.ai-factory/ARCHITECTURE.md`, `docs/reserved-words.md` and `docs/using-the-language.md` — all checked below.
- **Roadmap** — PASS. Line 186 of `.ai-factory/roadmaps/trickster77777.md` is the first `- [ ]` line in the file — the seam — and it is 34.3. The plan's `# Plan:` heading matches the contract-line title verbatim. The `Spec:` tag resolves to `.ai-factory/specs/trickster77777/112-no-work-order-is-required-to-carry-a-check-list.md`, which exists and was read in full; the plan covers all four of its obligations. `### Phase 34` names no `Governing spec:` and no phase note, so the chain runs contract line → task spec → the four files and terminates at code.
- **Vocabulary** — PASS. No protocol token is touched: `APPLY-EDIT` and `REPORT-ONLY` stay byte-exact and out of scope, and `architect-editor-engine`'s "held byte-exact, like `PLAN_REVIEW_PASS`" sentence sits outside every edited span. `work-order`, `editor`, `architect` are used at their registry meanings; the plan does not deepen the `work-order` collision that 34.4 removes.

### Critical Issues

**1. The pinned acceptance sweep is case-sensitive and cannot return the three hits the plan pins for it — one of the three named hits is a capitalized heading.**
Task 4 prescribes `grep -rn "self-verif" src/ docs/` and states the implementer should "expect exactly three hits … `src/agents/editor.md` `description:`, `src/agents/editor.md`'s section heading, and `src/skills/architect-editor-engine/SKILL.md`'s `self-verifies`". The second of those three is `src/agents/editor.md:71` — `## Self-verify, flag every judgment call, escalate ambiguity` — with a capital **S**. `grep` without `-i` never matches it.

Verified by applying all three of the plan's pinned blocks to a scratch copy of `src/` and `docs/` and running the plan's own command:

```
src/agents/editor.md:6:  a decided work-order exactly as written — self-verifying and reporting back
src/skills/architect-editor-engine/SKILL.md:24:- **`APPLY-EDIT`** — … self-verifies, and does not commit.
```

Two hits, not three, and the heading the plan names is absent. The same command with `-i` returns exactly the three the plan describes, heading included.

This is the plan's own indictment reproduced: the contract line names "a count that cannot return its number by construction" as one of the three recurring shapes this task exists to remove, and the plan's single acceptance check is one. The failure mode is not cosmetic — an implementer who trusts the count over the command has only two moves, and both are wrong: read the two-hit result as a landing defect and go hunting for a fourth home that was never there, or "fix" it by touching `editor.md:71`'s heading, which the plan's own guard forbids ("the section heading keeps the word 'Self-verify'").

Repair: make the command `grep -rni "self-verif" src/ docs/` and leave the expected three hits as written. (Expecting two and dropping the heading from the list also resolves the arithmetic, but loses the heading as a checked survivor, which is the more useful of the two readings.)

**2. `architect-pairing-engine` takes two span replacements, both addressed in pre-edit line numbers, and the first one shortens the file.**
Task 2 says "(1) Replace lines 35–42 …" (8 lines → a 7-line block, net −1) and then "(2) Replace lines 44–48 …" (5 lines → a 5-line block). Both spans are correct against the file *as it stands now*; neither is correct after the other lands. Applied in the stated order, literally — and the plan's Context explicitly prescribes span replacement: "Replace the named line span with the block's contents verbatim" — edit (2) targets post-edit lines 44–48, which after edit (1) hold the *tail* of the second paragraph plus the blank line separating it from § "Departure from the generic spawn trigger". The result is a mangled paragraph and a lost paragraph break, silently, with no string mismatch to trip on.

Verified: after edit (1) the second paragraph occupies lines 43–47, not 44–48; old line 49 (blank) becomes new 48.

This is precisely the "collision-safe method where order matters" that `agent-architect`'s own guardrail component — the one component this task deliberately keeps — exists to force into a work-order. A plan that thins the work-order's required list should not be the plan that drops the guardrail it kept.

Repair: one sentence, either form. State that the two spans are pre-edit coordinates and edit (2) applies first (bottom-up, so no span moves under the other); or anchor each replacement by its opening and closing line text instead of by number. The pinned blocks themselves need no change.

### Verified against ground truth

- **Every pinned block reproduces exactly.** All three replacements were applied to a scratch copy and diffed. `agent-architect` 155–161: the block is the current paragraph with the clause `the commands the editor runs to self-verify before reporting; ` removed and the remainder re-flowed to 51–78 chars (file body runs to 81, so the widest new line is in range). `architect-pairing-engine` (1) is lines 35–42 minus `self-verify commands, `, re-flowed to 71–77 (file body max 77); (2) is lines 44–48 minus `, self-verify command`, re-flowed to 67–70.
- **The round-1 comma inconsistency is closed.** Both deletion spans are now stated with the comma on the same side (`self-verify commands, ` and `, self-verify command`), and each stated operation now yields its own pinned result character-for-character.
- **`editor.md`'s sentence is now pinned, and the byte-identity claim holds.** Joining the plan's 11-line block and the current lines 73–83 and comparing from `re-check your findings` to `difference later.`: identical, character for character. Only the leading apply-mode clause differs, exactly as the plan states. The block is 11 lines against 11 replaced, widths 69–75 inside the file's 67–77 body range, apostrophes ASCII, `—` the only non-ASCII character — consistent with the file.
- **Round-1 finding 1 is genuinely resolved, not papered over.** Task 4 now sweeps `self-verif` alone and states in the imperative why `verify command` is *not* swept, naming `editor.md`'s new body clause as the reason. That is the right direction: the sweep no longer contradicts task 3.
- **Round-1 finding 3 is mooted.** The wrap-width instruction measured off a heading is gone; the sentence is pinned, so the wrap is decided rather than described.
- **The task spec's four obligations are all covered**: drop the component from `agent-architect`'s list, drop it from both `architect-pairing-engine` enumerations, restate `editor.md`'s apply-mode verification as an unconditional diff read-back with a verify command only where pinned, and leave `architect-editor-engine` alone. Nothing in the spec is left unplanned and nothing is planned beyond it.
- **No stale count is left behind.** `grep -w` for `four`/`three` (either case) returns nothing in any of the three edited files, so removing a component orphans no numeral. `agent-architect`'s other `work-order` mentions were read; none enumerates the components, so line 159 is the single home in that file.
- **Leaving `architect-editor-engine` alone is correct.** Its line 24 — "makes exactly the edits specified, self-verifies, and does not commit" — names a step that still happens once the diff read-back becomes unconditional. Editing it would push policy into a format engine, against the tiering.
- **§ "Verify the report by fact" genuinely stands alone afterwards.** Lines 212–219 make the architect run its own greps and reads against the real files and check the reporter's judgment calls "on the file, not on the note". Nothing in it depends on a work-order having carried commands, so the removal leaves no dangling reference. The plan names it untouchable *with the reason*.
- **The residual asymmetry is ratified, not drift.** After the change `agent-architect` no longer requires a verify command while `editor.md` still says what to do "where the work-order pins one" — silence is not prohibition, and the task spec prescribes that exact shape. `architect-pairing-engine`'s applying half is unaffected: it composes an arriving decision into its own `APPLY-EDIT`, and its "The deciding half verifies what landed against the files" already rests on the architect's file-check.
- **Delivery is clean.** `active/skills/agent-architect`, `active/skills/architect-pairing-engine` and `active/agents/editor.md` are live symlinks into `src/`, so all three edits go live with no `active/` work; `upstream/ai-factory/` holds no counterpart for any of the four files, so a re-sync cannot clobber them. The working tree carries only this task's own plan artifacts and the round-1 review.

### Positive Notes

- The three pinned blocks are the right response to round 1: the deliverable that *is* wording is now a string a reviewer can diff, not an example. The `editor.md` block in particular re-flows ten lines of untouched prose so that the new sentence lands without a visibly narrow paragraph — the harder, correct way to pin a mid-paragraph rewrite.
- Task 4's negative instruction — "Do **not** sweep for `verify command`", with the reason that a zero-expectation "would only pass by reversing the task above" — is exactly the kind of guard that stops a downstream agent from optimizing an acceptance check into a regression. It closes round-1 finding 1 by reasoning about *why* the sweep exists, not by deleting the awkward half.
- The negative space is pinned where an implementer would actually drift: no replacement component, the diff read-back deliberately not named in `agent-architect`, § "Verify the report by fact" named untouchable with its reason, `architect-editor-engine` named read-only rather than merely unmentioned, and `.ai-factory/` history explicitly excluded so no already-sent work-order is retracted.
- The task order is right: the two mirrored enumerations are cut "in lockstep with the above", so no intermediate state has the pairing engine promising a component the generic skill no longer defines.
