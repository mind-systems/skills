# Review — 34.4 `work-order` names one thing in the registry (round 1)

## Code Review Summary

**Files Reviewed:** the one changed file `docs/reserved-words.md` (read in full, post-edit), the plan, the task spec `.ai-factory/specs/trickster77777/113-work-order-names-one-thing-in-the-registry.md`, the contract line at roadmap line 187 under `### Phase 34`, `.ai-factory/ARCHITECTURE.md`, `CLAUDE.md`, the grove root `../CLAUDE.md`, `docs/using-the-language.md`, `docs/reference-by-name.md`, `docs/sakshi-harness/skill-cycle.md`, `src/global/CLAUDE.md`, the four paired-loop surfaces (`src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md`, `src/agents/editor.md`), and both rounds of this task's plan review
**Risk Level:** 🟢 Low — `git diff HEAD` touches exactly one line of one file, and that line is byte-for-byte the text the plan pins. No executable surface, no protocol token, no machine-resolved name is in the changed span.

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is undisturbed: no skill added or re-tiered, no `loads:` edge touched, no engine gains policy, no lens inlines mechanism. The change lands on the language-contract surface `ARCHITECTURE.md:56` names, and only on its naming. Delivery is clean: `active/` symlinks `skills/`, `commands/`, `agents/` and `CLAUDE.md` only — never `docs/` — and `upstream/ai-factory/` holds no counterpart to `docs/reserved-words.md`, so `scripts/sync-upstream.sh` cannot overwrite the edit. The file reaches every session through `../CLAUDE.md:14`'s `@skills/docs/reserved-words.md` import, so the edited text is live as it stands, with nothing to regenerate.
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` does not exist in this repo; the governing conventions are in `CLAUDE.md`, `.ai-factory/ARCHITECTURE.md`, `docs/reserved-words.md` and `docs/using-the-language.md`, all read and checked below.
- **Roadmap** — PASS. Line 187 is the seam and is 34.4; the plan implements its `Spec:` tag exactly and adds nothing beyond it.
- **Vocabulary** — PASS. Prose only was removed. The `Spec:` tag, the PASS signal literals and `## Deferred observations` sit nowhere near the edited span. `task spec`, `contract line`, `two-tier`, `work-order` and `architect` are at their registry meanings. The edit is the registry conforming to its own bidirectional rule.

### Findings

None.

### Verified against ground truth

- **The diff is exactly the pinned edit.** `git diff HEAD -- docs/reserved-words.md` is one hunk, `-1/+1`, at line 25, with `docs/reserved-words.md | 2 +-` the only source change in `git diff HEAD --stat`. The removed clause is `; the implementation-tier work-order`, taken together with its joining semicolon, and the line now ends `… referenced by the contract line's tag.` — the literal ending the plan pins. The bold term, the em-dash and both inline-code spans (`` `.ai-factory/specs/` ``, `` `note` ``) are unchanged, as the plan's negative space requires. No trailing whitespace was introduced, no `\ No newline at end of file` marker appears, and the line stayed one unwrapped line (176 → 146 characters) — the reflow the plan forecloses did not happen.
- **The task's goal is reached.** `grep -n work-order docs/reserved-words.md` now returns one hit: line 95, § "Paired loop", `drafts work-orders`. The word names one concept in the registry, and that line was not touched to get there.
- **The negative space held.** The `contract line`, `two-tier` and `governing spec` entries around the edit are unmodified — the diff's context lines show them verbatim, and no other entry, section or heading in the file moved. No term was added, retired, or re-homed; the set the registry binds is unchanged, which is what makes this a removal of a collision rather than the update the file's opening banner forecloses.
- **Nothing is orphaned.** `grep -rn "implementation-tier\|implementation tier"` over the repo outside `.ai-factory/` returns nothing at all after the edit — the phrase had exactly one home and no copy anywhere. The fact it carried still has its own home: `src/skills/roadmap-engine/SKILL.md` § "The two-tier artifact" states the task spec "holds the full implementation detail", with 34.1's paragraph naming the three parts directly below it. The registry's own rule at line 15 — "it indexes names, it never re-homes facts" — is why the entry should not have carried it.
- **Nothing downstream had to move, and nothing did.** `work-order` survives in the seven files the plan names, and every hit is the paired-loop artifact; `docs/reference-by-name.md:27` and `src/global/CLAUDE.md:59` name a work-order and a spec as separate things in one sentence, so both read correctly after the removal rather than in spite of it. `CLAUDE.md:24` and `../CLAUDE.md:10` summarise the registry without mentioning a work-order or a tier; `.ai-factory/ARCHITECTURE.md:56` names the file, not its entries. `git status` confirms no other source file is modified — the remaining staged paths are this task's own planning artifacts.
- **The file reads coherently after the edit.** `tier` now has its two consistent senses in § "Roadmap artifacts" — `phase` ("the strategic tier") and `two-tier` — and the third sense that cut across the `two-tier` entry immediately below it is gone. The `task spec` entry still names the artifact fully: its file, its directory, how it is written, how it is reached.
- **No test is owed.** Under `test-philosophy` this is one prose clause deleted from a markdown glossary: no executable surface, nothing that can fail silently. `Testing: no` in the plan is correct, and the checkbox is marked `[x]` against work that is actually on disk.

### Positive Notes

- The landing is the whole plan and nothing else — a one-line diff on a one-checkbox plan, with no tidying of the paragraph around it, no new registry entry for the now-single `work-order`, and no reach into the four skills that use the word. The contract line's "no term is added or retired" is honoured literally.
- The removal leaves the registry obeying its own bidirectional rule without any statement of that rule having to change, which is exactly the claim the plan made for why a file declaring itself final could be edited at all.

REVIEW_PASS
