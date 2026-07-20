# Code Review — 20.2 `$TEST_CMD` derivation rule + Layer 7 no-command behavior

## Code Review Summary

**Files Reviewed:** `src/skills/roadmap-test-coverage/SKILL.md` (read in full), `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md`, plan, plan-review-1, `src/skills/aif/SKILL.md` (§ CLAUDE.md Generation)
**Risk Level:** 🟢 Low — one correctness gap worth closing, one spec-text drift. No security surface; the change is instruction text in a skill body, and the one behavioral effect on the runtime is to *stop* an empty command from executing.

**Guard verification — all pass.** `git diff HEAD -- src/skills/roadmap-test-coverage/SKILL.md` touches exactly the four authorized regions:
- Layer 1 read list (+2 lines, L29–30)
- `$TEST_CMD` paragraph (L51–67, replacing the old L49–54)
- Layer 7 empty-command guard (L288–292) and the re-run gate (L352–354)
- Layer 8 counts-block line (L372) plus its conditionality note (L377–378)

`$STACK`'s block (L38–48) is byte-identical to post-20.1. Layers 2–6 have no diff hunks at all, and I confirmed by reading them in full (L71–282) that none of them reference `$TEST_CMD` — so the skip path has no downstream consumer that assumes a runnable suite. Layer 8's `$HANDOFF_LIST` print instruction, both category headings, the per-item pointer paragraph, and `Next step:` are byte-identical. The four-manifest list is not extended, and the `package.json` → `test`-script fallback survives verbatim at L57–61. `allowed-tools` correctly unchanged — the primary rule adds only a `Read`, granted at L10.

### Findings

**1. The `CLAUDE.md` read-list entry is unpinned prose, which partly undercuts the reason it was added. (Medium)**
`src/skills/roadmap-test-coverage/SKILL.md` L29–30: `- The project's `CLAUDE.md` — the declared test command in its `## Commands` section`.

Both sibling entries in that same list resolve to something concrete: `.ai-factory/ARCHITECTURE.md` is an explicit relative path (L28), and the roadmap entry delegates to a named resolution order in `roadmap-engine` (L31–35). The new entry does neither — "the project's `CLAUDE.md`" names no path and no resolution rule.

That matters specifically because of the rationale recorded in the spec guard and the plan: the entry exists precisely so the skill does not lean on the ambient auto-loaded `CLAUDE.md`, since in a grove the loaded one may not be the sub-repo's. As written, an agent has no rule telling it *which* `CLAUDE.md` to open, so it may well resolve to the ambient one — the exact outcome the guard was added to prevent.

This is live in this very repo, not hypothetical: `/Users/max/projects/sakshi/CLAUDE.md` and `/Users/max/projects/sakshi/skills/CLAUDE.md` are different files, and a session rooted at the grove root has the former loaded while `.ai-factory/` resolves against the latter.

Failure scenario: a Python sub-repo declares `| Tests | uv run pytest |` in its own `CLAUDE.md`; the agent reads the grove-root `CLAUDE.md` instead, finds no `## Commands`, falls through to the four-manifest sniff, finds no Python manifest, and lands on empty. Layer 7 then skips the green gate on a project that has a perfectly good test suite. The skip is logged and surfaced, so it is not silent — but it is wrong, and it is the same class of miss (right stack, unread declaration) that 20.1 and this task exist to close.

Fix — pin the entry the way its siblings are pinned, e.g. `CLAUDE.md` at the same root as the `.ai-factory/` directory in play, so it co-resolves with the `ARCHITECTURE.md` read one bullet above. One clause; stays inside Layer 1 and inside the guard.

**2. The spec's "Layer 8 takes exactly one added line" guard is narrower than what the implementation correctly needed. (Low — spec text, not code)**
`.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md` § Guards vs. `SKILL.md` L372 + L377–378.

The implementation added the counts-block line *and* a two-line note stating it prints only on a skip. The note is not scope creep — it is required for correctness. Layer 8's counts block is a literal print template; without the conditionality statement an agent would emit `Existing-test gate: skipped (no test command resolved)` on every run, including runs where the suite executed and passed. That would be a real defect, and the implementer was right to prevent it. The plan authorized it explicitly ("and state that it prints only when Layer 7 skipped the gate"); only the spec's tighter "exactly one added line" wording fails to.

No code change wanted. The spec guard should be reworded to what was actually intended and implemented — one added counts-block line plus the sentence governing when it prints — so the next reader does not score the note as a violation.

### Positive Notes

- **The empty-command guard is placed correctly and is complete.** L288–292 sits ahead of the run block and closes every branch: skips the run, the classification, and the gate, and routes to Layer 8. Pairing it with the scoped re-run gate at L352–354 means there is no path left on which an empty `<$TEST_CMD>` reaches a shell — which was the whole defect.
- **The `$HANDOFF_LIST` exclusion is stated at the point of temptation.** L292 says plainly not to append, with the reason (not a task, no pointer). That is what keeps Layer 8's "Every handoff line resolves to a pointer" invariant intact, and stating it inline is better than leaving it to inference.
- **Grounding note 1 was carried into the text faithfully.** L53–56 rules against the `## Commands` *section* and names `| Tests | pytest |` as a typical shape rather than a parse contract — matching what `aif/SKILL.md` L37 actually mandates (nothing about a table or a `Tests` row). A literal-row rule would have fallen through on most real files.
- **The three-way resolution is exhaustive.** Primary / Fallback / Neither (L53–64), with the empty state named as *defined* and pointed at Layer 7 rather than left implicit — which is what makes the Layer 7 guard readable as a contract rather than defensive coding. The fallback trigger also covers `aif`'s documented "leave light if no scaffolding exists yet" case via "declares no test command".
- **Register preserved.** The new block mirrors the `$STACK` block's numbered Primary/Fallback shape and sentence voice; it reads as the same author, which was an explicit guard.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md` — The spec's Change bullet 1 still says the primary is "the `## Commands` table `aif` writes into `CLAUDE.md` (the `Tests` row…)", which overstates what `aif` mandates. Carried forward unchanged from plan-review-1; the skill text is correct, only the spec's own description of its upstream is inaccurate and will mislead a reader who consults it directly.
- Affects: phase 20 / `src/skills/roadmap-test-coverage/SKILL.md` — Running the skill against this repo now resolves `$TEST_CMD` to empty (neither grove `CLAUDE.md` has a `## Commands` section; no manifest at the `skills/` root), so Layer 7 skips the gate. That is correct behavior for a repo whose product is skill text with no test suite, and it exercises the new path end to end — noted as a useful observation, not a defect.

Finding 1 is a one-clause fix inside Layer 1 and should land before this task is considered done. Finding 2 is spec wording only and blocks nothing.
