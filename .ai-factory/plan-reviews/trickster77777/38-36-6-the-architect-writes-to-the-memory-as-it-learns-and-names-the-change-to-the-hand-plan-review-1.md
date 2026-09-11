## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/38-36-6-the-architect-writes-to-the-memory-as-it-learns-and-names-the-change-to-the-hand.md`
**Files targeted:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. The plan edits the policy skill only and restates nothing the engine (`architect-editor-engine` § "The architect's buffer") holds; consistent with ARCHITECTURE.md "Composition: mechanism vs policy". No new `loads:` edge, frontmatter pinned byte-identical.
- **Rules** — WARN (non-blocking): `.ai-factory/RULES.md` is absent; nothing to check.
- **Roadmap** — OK. Contract line 36.6 in `.ai-factory/roadmaps/trickster77777.md` → `Spec:` `specs/trickster77777/124-…` → phase note `114-…` → governing spec `docs/paired-loop.md` § "What the memory holds, and who holds it" and § "How the memory begins, and how it survives" — all walked. The plan's three facts (occasion, form, announce-obligation) are the spec's sentences verbatim; the "no zone / no list / no drain / no re-read restatement" guardrails match the contract line. Task 36.1 (the dependency) is `[x]` and the engine already carries the definition the plan points at.
- **Ground truth** — verified against HEAD `df94aa1`: file is 282 lines; § "Your buffer is yours alone" is exactly the two paragraphs quoted; `awk 'length > 77' | wc -l` = 17; `grep -c "memory snapshot"` = 3; `grep -c "REPORT-ONLY\|APPLY-EDIT"` = 8; `settled zone` = 1, `live zone` = 0, `drain` = 1, `re-read` = 1, `episode` = 0, `stretch of work` = 0; "The handoff continuing you across a compact" = 1 hit. Every baseline the plan's verification step relies on is correct.
- **Carried-in scope** — the name alignment of paragraph 1's "handoff … across a compact" sentence is the deferred observation addressed to 36.6 in both 36.5 reviews; pulling it in is correct, bounded to one sentence in the section this task already edits, and the plan pins that the opening clause "must survive a compact" is left alone.

### Critical Issues
None.

### Issues

1. **Fact 3's suggested wording collides with the plan's own verification check** — `Tasks › State the occasion…` item 3 vs. `Tasks › Verify against the file`.
   Item 3 hands the implementer the clause "whatever the hand's own discipline says about re-reading", and the Context section permits passing the governing spec's sentences through, whose announce sentence reads "however plainly the discipline says the hand re-reads on change". Both contain the substring `re-read`. The verification step then requires `grep -c "re-read" src/skills/agent-architect/SKILL.md` → **exactly `1`** (the existing pointer line). An implementer who follows either the suggested wording or the spec pass-through fails that check and must guess whether the check means "don't restate the re-read rule" (an allusion is fine) or "don't use the substring" (reword). The intent is clearly the former — the same bullet says "neither restated" — but the grep is a stricter proxy than the intent. Pin one of the two: either state in item 3 that the closing clause must not carry the `re-read` substring (e.g. "whatever the hand's own discipline says about reading on change"), or change the check to "`grep -n "re-read"` → the existing pointer line, plus at most one hit inside the inserted paragraph that alludes to the hand's discipline without stating the rule". Either way the plan and its check agree.

### Positive Notes
- The plan grounds every claim on the file as it stands after 36.5 and cites the exact HEAD; all baseline counts check out.
- Guardrails are drawn precisely where prior tasks in this phase and 37.1 draw theirs: no zone, no token, no restatement, no touch on the two sentences 37.1 rescopes.
- The announce-obligation is handled as the governing spec says — an obligation, no form, no carrier — and the "before an editor exists there is no hand to tell" clause pre-empts the one edge the spec leaves implicit.
- Insertion position keeps "the deferral entries below" pointing downward and leaves "you are its only writer." last; the verification step reads the section as a whole rather than trusting the diff.

## Deferred observations
- Affects: task 37.1 / `.ai-factory/specs/trickster77777/119-architect-authors-more-than-one-prompt.md` — once this task lands, `agent-architect` will carry an announce-obligation toward the editor while the same file still says "Two channel-message formats, nothing else" and "You author your own prompt in exactly one case". The plan correctly leaves both sentences to 37.1, which rescopes them to what opens a round (per `docs/paired-loop.md` § "What crosses the channel"); until 37.1 lands the file states a closed list it no longer honors. Nothing for 36.6 to do.
- Affects: `.ai-factory/specs/trickster77777/124-the-architect-writes-to-the-memory-as-it-learns.md` — the section's opening clause "whatever of your own state must survive a compact" is the second phrase the 36.5 review named; the plan deliberately leaves it (the buffer's purpose is survival across a compact regardless of which snapshot occasion recovers the architect). Defensible; recorded here so the choice is visible to the spec's owner rather than silently dropped.
