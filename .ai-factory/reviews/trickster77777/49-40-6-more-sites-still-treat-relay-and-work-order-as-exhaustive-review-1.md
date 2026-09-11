## Review — 40.6 — more sites still treat relay-and-work-order as exhaustive

**Plan:** `.ai-factory/plans/trickster77777/49-40-6-more-sites-still-treat-relay-and-work-order-as-exhaustive.md`
**Changed files:** `src/skills/agent-architect/SKILL.md` (3 hunks, +8/−5); plan, plan-review, and sidecar under `.ai-factory/` (artifacts, not reviewed as code)
**Risk Level:** 🟢 Low

### What was checked

`git diff HEAD` and `git status` read; `src/skills/agent-architect/SKILL.md` read in full (370 lines), not just the hunks. Each edited sentence was checked against the plan's per-task instruction, spec 133 § "The change", and the governing spec `docs/paired-loop.md` § "The user's marker".

**Site 1 — spawn sentence (§ "Spawn once, message thereafter").** Now names three possibilities for the first channel-message — the first `::` relay, the first authored apply work-order, or "a `REPORT-ONLY` round on your own initiative delegating your own legwork" — whichever arrives first. The construction is the file's own (the case-naming paragraph in § "Relay on the marker; author the apply work-order and your own legwork" reads "a `REPORT-ONLY` round on your own initiative, delegating your own legwork"); no noun for the round is coined. The tail from "and its content *is* the spawn prompt" through "never a fresh spawn per task" is byte-identical, and the memory-snapshot paragraph below it (40.7's site, "Each new snapshot supersedes the last by name") is untouched. Correct.

**Site 2 — respawn sentence (dead-editor paragraph, same section).** The two branches become three: "the user re-phrases a relay as a self-contained spawn prompt, an apply work-order is resent as-is, or a `REPORT-ONLY` round delegating your own legwork is resent the same way." "Resent the same way" binds the third branch to the apply work-order's as-is resend, which is what the spec asks. "Never eager with authored prose" and the non-replay rule for an undelivered *payload* still hold: the relay is the user's words and is still never auto-replayed, while the architect's own composed round — like the apply work-order already beside it — is its own to resend. The following sentences ("A respawned editor resumes through the same two channels …", "Losing the editor is never fatal …") are unchanged, and "two channels" still means the two formats, which a delegated round already belongs to. The fallback-recovery paragraphs above (40.2's) are untouched. Correct.

**Site 3 — marker-decides sentence (§ "Review in parallel, reconcile before the apply order").** "You never decide *when* something goes to the editor; the marker does." → "You never decide *when* a relay goes to the editor; the marker does." Narrowed to exactly what is true of the marker; nothing added beside it, no exception clause, no pointer to the case-naming paragraph — matching the spec's "dropping the overreach, not restating or pointing at". The apply-work-order timing sentence before it is unchanged. Correct.

**Guards.** Exactly three hunks, each on its own sentence. Added lines grepped for "delegated round", "delegation", "delegated legwork round" — none. The case-naming paragraph including 40.5's echo sentences is byte-identical. `src/agents/editor.md` and `src/skills/architect-editor-engine/` are untouched (`git status`). Frontmatter (`description:`, `loads:`) unchanged; body is 370 lines, within the 500-line limit. No other file in `src/`, `docs/`, or `.ai-factory/specs` quotes the old sentences, so no cross-reference went stale. The sidecar reads `"step": "implemented:1"`, consistent with the indexed marker grammar.

**Vocabulary.** "Relay", "apply work-order", "channel-message", "round" all keep their established meanings; the added phrase reuses the one construction the file already has for the delegated case, so the one-word-one-meaning contract on skill bodies is honored without a new term entering.

### Critical Issues

None.

### Non-blocking notes

- Site 1's "whichever arrives first, where none of the others has arrived before it" says the same thing twice; "whichever arrives first" alone carries it. Meaning is correct either way — a wording redundancy, not a defect, and not worth a round.
- Line 163 wraps at 80 columns against the file's usual ~78; lines 148 and 245 already do the same, so it is within the file's existing tolerance.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/133-sites-still-treat-relay-and-work-order-as-exhaustive.md` § "Blast radius" — carried from plan-review-1: the paragraph says the spawn-sentence site "sits directly after the paragraph 40.7 edits — the memory-snapshot paragraph"; in the file the spawn sentence's paragraph comes *before* the memory-snapshot paragraph. The edit landed correctly because the plan anchored by sentence, and the non-collision conclusion holds in either order; the wording belongs corrected at the spec (and in 40.7's spec if it repeats it), not here.

REVIEW_PASS
