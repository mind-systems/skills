# Review — 58.2 the snapshot itself, not only its digest, is never delegated to the editor

## Summary

**Task:** `.ai-factory/roadmaps/trickster77777.md` → 58.2 · **Spec:** `.ai-factory/specs/trickster77777/160-the-snapshot-itself-is-never-delegated.md` · **Plan:** `.ai-factory/plans/trickster77777/06-…md`
**Changed:** `src/skills/agent-architect/SKILL.md` — two hunks, two sentences, nothing else in the working tree.
**Verdict:** 🟢 No findings. Both appended clauses reproduce the spec's pinned wording word for word, both edits stay inside their declared span, and every check the plan's Verification section specifies was run and passed.

This is prose that is executed, not compiled — "runtime" here is an agent reading the file, so the failure modes worth hunting are a paraphrase of pinned text, a dropped markup token, a disturbed neighbour, and a sentence elsewhere in the file that now contradicts the new one. All four were checked directly.

## Verification performed

**Arrival — both sentences against the spec, word for word.** Extracted each edited sentence from the file with newlines collapsed to spaces and compared it to the corresponding blockquote in spec `160-…md` § "What must be true after":

- **Digest sentence** (§ "Spawn once, message thereafter") — byte-identical to the spec's blockquote, including the em dash and the appended clause's tail "…and only the head that held it can write what happened there."
- **Channel-contents sentence** (§ "Relay on the marker; author the apply work-order and your own legwork") — identical to the spec's blockquote in words and order, differing only in that `REPORT-ONLY` and `APPLY-EDIT` are backticked in the file where the spec's blockquote renders them bare. This is the divergence the plan anticipated and ruled on (the spec is the authority on the words, the file on the markup); the file's pre-edit markup is preserved, which is the correct outcome. `**never**` retains its emphasis.

**Survival — the anchor other artifacts key on.** `grep -rln "digest is your own recovery note" src/ docs/ .ai-factory/` still returns `src/skills/agent-architect/SKILL.md`. The phrase was appended to, not replaced — the sweep's whole point. The other five hits classify under the plan's rule (*does this file quote the passage as ground truth for a standing claim about the present?*): the roadmap's own contract line for this task, spec `160`, phase note `152`, and plans `05-`/`06-` — the first three describe a moment or state a problem permanently, the last two are this task's own working communication. Nothing unclassified; nothing to edit.

**No new contradiction.** `grep -n "written by the editor\|editor.*compose\|compose.*editor\|has the file open" src/skills/agent-architect/SKILL.md` returns two lines, inside the plan's stated ceiling of two and consistent with its `DEVIATION` from the spec's "exactly one line":

- line 253 — "the text is written by the editor, who has the file open", expected and not a contradiction: it describes composing an `APPLY-EDIT` in general, and the exclusion added by this task closes the door 24 lines later in the same section.
- line 74 — the first appended clause itself, matching `editor.*compose` because the re-wrap happened to put "editor to compose" on one line. Wrap-dependent by construction, exactly as the plan predicted.

Read rather than grepped: no sentence in the file affirmatively licenses delegating the snapshot.

**Scope and neighbours.** `git diff HEAD` touches one file and shows two hunks, each replacing one line with three or four. No neighbour line is rewritten — the re-wrap stayed local to the appended text, so 58.1's three landed sentences ("What a snapshot carries is the volatile residue…", the thickness sentence, the supersession sentence), 58.4's two opening sentences, the closing "Of the recorded state, only the buffer's path travels:" sentence, and every other sentence of the channel-contents paragraph are byte-identical to `HEAD`. The contract line's "Touch only these two sentences" holds literally.

**Formatting.** New lines measure 63–75 columns, inside the file's own body-prose convention (which tops out at 80, with one 81-column line at 19). The cross-reference `(see "Spawn once, message thereafter")` is the file's existing form — it already appears three times, including five lines above the new use — and addresses by heading name, never by position. No position address was introduced anywhere.

**Blast radius.** `src/skills/architect-editor-engine/SKILL.md` and `src/agents/editor.md` mention the snapshot nowhere, so no counterpart edit is owed on the editor's side; the prohibition is policy and correctly stays with the caller under ARCHITECTURE § "Composition: mechanism vs policy". No file outside the target and its own spec carries either edited sentence — checked for both "carries the apply work-order alone" and "nor, ever, the memory snapshot". `active/skills/agent-architect` is a symlink into `src/skills/agent-architect`, so the one edit deploys as one edit.

## Deferred observations

- Affects: Phase 58 / `src/skills/agent-architect/SKILL.md` § "Your buffer is shared; you alone write it" — Raised in both plan-reviews and now observable in the landed file: that section closes "It is the one file you edit directly: you are its only writer." (line 365). After this task the snapshot is explicitly a second file the architect composes with its own hands and may not delegate, so "the one file you edit directly" is a claim the same file contradicts two sections earlier. The repair is one clause in a sentence this task's contract line forbids touching, and no sibling owns it — 58.4 takes the two-occasions sentence and `command-handoff.md`, and Phase 59 enters that section only for the zone split (59.1) and the buffer-creation paragraph (59.2). A phase-level call; the implementation was right to follow its spec and leave it.
- Affects: Phase 58 / `.ai-factory/specs/trickster77777/160-the-snapshot-itself-is-never-delegated.md` § "What must be true after" — The clause the spec pins ends `(see "Spawn once, message thereafter")`, and the paragraph it lands in already carries that identical cross-reference five lines earlier (line 272, "handing it the buffer's path at spawn"). A reader now meets the same pointer twice in one paragraph. The two uses point at different facts, so the repetition is not wrong, only close — and copying the spec verbatim was the correct call here. Whether the second reference earns its place is the spec's call, not this task's.

REVIEW_PASS
