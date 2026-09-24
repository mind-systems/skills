# Plan review — 58.4 a request phrased as a handoff routes correctly on both sides, or on neither

## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/07-58-4-a-request-phrased-as-a-handoff-routes-correctly-on-both-sides-or-on-neither.md`
**Targets:** `src/skills/agent-architect/SKILL.md` (one appended sentence), `src/commands/command-handoff.md` (one inserted paragraph)
**Risk Level:** 🟢 Low

Two prose additions, both pinned word for word upstream, both landing beside untouched anchors. Every factual claim the plan makes about the two files was re-measured against the files themselves; all of them hold.

### Ground truth verified against the files

- **Both pinned texts are copied, not re-derived.** Checked programmatically, newlines collapsed: the plan's `agent-architect` blockquote is character-identical to spec `162-…md` § "What must be true after"'s appended-sentence block, and the plan's `command-handoff` paragraph is character-identical to the spec's inserted paragraph. No paraphrase anywhere.
- **The anchor sentence in the destination matches what the spec quotes** — `agent-architect/SKILL.md` lines 65–67, newlines collapsed, are byte-identical to the spec's `## What is true now` quote, so the "existing sentence stays word-identical" instruction has a determinate referent.
- **The wrap hazard the plan names is real and correctly described.** Line 66 ends `— no` and line 67 opens `other handoff has any reason…`, so a single-line pattern containing "no other" does match nothing; the plan's instruction to match a fragment that does not span the break, and the spec's deliberately "no"-less sweep pattern, are both right and the plan explicitly forbids "fixing" the pattern.
- **Both wrap-width figures are measured, not guessed.** The memory-snapshot paragraph's full lines run 63–75 columns (line 90, the paragraph's last, runs 28) — exactly the range the plan states. `command-handoff.md`'s body paragraphs are single unwrapped lines of 140, 251, 342, 405 and 575 characters — the plan's "140–575" is exact, and its warning not to carry the wrapping habit across files is the right call for the folder's settled style.
- **The insertion point is structurally as described.** `command-handoff.md` line 14 is the opening paragraph (405 chars, unwrapped), line 15 is blank, line 16 is `---`. Inserting one paragraph with a blank line each side leaves both existing blocks untouched.
- **Line hints are disclaimed where they appear.** "around line 65–67" and "currently line 14" are each followed by an instruction to locate by text; neither is a state an earlier edit changes before it is used, since the two edits are in different files.
- **The reference style resolves by name.** `command-handoff.md` line 139 already carries the identical `<file> § "<heading>"` form (`the global CLAUDE.md § "Grounding claims"`), and `docs/paired-loop.md` § "How the memory begins, and how it survives" exists at line 21, its closing paragraph ("Two genres share the occasion and nothing else…", line 41) carrying exactly the reader/subject/lifetime claim both additions lean on. No line number anywhere.
- **Typography matches both destinations.** Both pinned texts use only U+2014 em dashes and U+00A7 section signs outside ASCII — ASCII apostrophes and ASCII double quotes throughout, the same forms both files already use.
- **One edit per file; no second surface.** `active/skills/agent-architect` is a directory symlink to `../../src/skills/agent-architect` and `active/commands/command-handoff.md` a file symlink to `../../src/commands/command-handoff.md` — both verified present, so editing `src/` is the whole job, exactly as the plan states.
- **Both sweeps, run now, return exactly what the plan predicts:** the first returns `src/skills/agent-architect/SKILL.md`, this plan, and spec `162-…md`; the second returns `src/commands/command-handoff.md`, this plan, and spec `162-…md`. No fourth path, and nothing outside the classes the plan enumerates. The plan is right that the count grows with its own artifacts and right to say the count is not the test.
- **No competing boundary exists anywhere.** Beyond the two targets, "handoff" appears in `src/skills/note/SKILL.md` (genre list in its description), `roadmap-prune` (invokes `/command-handoff` at its gate), `roadmap-test-coverage` (`$HANDOFF_LIST`, an unrelated use of the word), the global CLAUDE.md (handoff named among descriptions ground truth overrides) and four docs — none asserts a routing rule between the two genres. `agent-architect`'s own lines 119–120 ("an auto-compact that fired before any handoff was written, or a handoff addressed elsewhere") use the word loosely for recovery, not routing, and contradict nothing.
- **Downstream of the insertion point is clean, read end to end.** Step 1's lens prose, Step 2's `note` hooks, Step 3's paste-back pointer and "Holding a handoff" state nothing about handling every invocation regardless of the triggering request, and nothing re-opens the boundary. The plan's verification task asks for exactly this reading and asks that a contradiction be reported rather than edited — correct, since the spec's blast radius claims no such sentence exists and this review confirms it.
- **Growth is trivial and within constraints.** `agent-architect/SKILL.md` goes 382 → ~388 lines, far inside the ≤ 500-line body limit; `command-handoff.md` goes 139 → 141 and is a command, not a skill body.
- **The working tree is clean of code changes** — only plan artifacts, an untracked handoff, and a modified architect buffer note — so the edits start from precisely the text the plan quotes.
- **Settings are right.** `Testing: no` — skill-body prose has no silently-failing surface, per `test-philosophy`. `Docs: no` — `docs/paired-loop.md` already carries the governing claim, so the doc stands ahead of the skills, which is the intended direction.

### Verification apparatus

The three verification tasks cover the whole deliverable and are ordered correctly:

- The **positive half exists and is named as such** — the word-for-word comparison runs first, states the right comparison mode per destination (newlines collapsed for the hard-wrapped file, line-as-written for the unwrapped one), and says plainly why the sweeps cannot stand in for it: "they prove survival and scope, both of which a paraphrase of either addition would also satisfy".
- It also carries the **negative check the spec asks for** — that neither addition restates reader, subject, or lifetime — which is the one requirement an obedient copy could satisfy and a well-meaning expansion could not.
- The **both-sides rule is enforced as a verification step, not just asserted in Context**: "a check of one file alone is not a check of this task" mirrors the spec's own whole-or-nothing rule, and the plan repeats it up front by treating the two edits as one deliverable.
- The **sweep task classifies by rule, never by list**, routes an unclassified competing-boundary hit to stop-and-report, and explicitly forbids tidying matching artifacts — closing the failure mode where an apparatus check starts editing what it was meant to read.
- **Markup is checked separately from words** ("the spec's blockquote is the authority on the words; the file is the authority on the markup"), which matters here because the spec's blockquote renders the backticks and the comparison is word-and-order only.

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is not crossed: no new skill, no `loads:` edge, no mechanism moved between engine and policy. Each side of the boundary is stated in the file that owns that side's policy, and both point at the governing spec rather than copying it — one home per fact, second home a pointer.
- **Rules** — WARN (non-blocking). Neither `.ai-factory/RULES.md` nor `.ai-factory/skill-context/aif-review/SKILL.md` exists in this repository, so no project convention file could be applied.
- **Roadmap** — OK. 58.4 is the seam: the first `[ ]` line in `.ai-factory/roadmaps/trickster77777.md` file order (line 37), with 58.1 and 58.2 landed above it. Linkage walked to the leaf: contract line 58.4 → `Spec:` `162-…md` → phase note `152-…md` → `Governing spec: docs/paired-loop.md` § "How the memory begins, and how it survives" → the two target spans. The contract line's scope — append to the two-occasions sentence, insert one paragraph before the first `---`, cite rather than restate, Steps 1–3 and "Holding a handoff" untouched, no thickness policy — is honoured clause by clause by the plan, and each clause has a matching verification entry. Phase 58 has no 58.3; nothing is missing between 58.2 and 58.4. The next task in file order, 59.1, reopens the same section (§ "Spawn once, message thereafter") but for the buffer's zone-split clause in the paragraph at lines 39–45 — a different span, no collision with the sentence this task appends to.

### Findings

None. The plan is implementable as written: both texts are pinned upstream and copied verbatim, both anchors are addressed by their own words, the opposite wrapping conventions of the two files are each named with the reason, verification has a positive half, an anchor half, a scope half and a rule-based sweep, and no number anywhere is asserted as a test.

### Positive Notes

- The plan names the one hazard its own two-file shape invites — carrying the first file's hard-wrapping habit into the second — and resolves it against each folder's measured style rather than a figure.
- "A routing boundary exists only once both sides state it: this task is verified whole or not at all" is lifted into the Context and then enforced again inside verification, so a half-landed change cannot read as done.
- The restraint instructions are stated with their reasons, not as prohibitions: the `command-handoff` paragraph names the genre rather than `agent-architect` because "the pointer is to the documented genre, not to a specific carrier", and the no-expansion rule is grounded in the pointer being the whole mechanism. An implementer meeting an unenumerated case can still rule correctly.
- The sweep task pre-empts the misreading that grows counts into a test, and pre-classifies the artifact classes the task's own run will add.

## Deferred observations
- Affects: Phase 58 / `.ai-factory/specs/trickster77777/162-a-handoff-phrased-request-can-mean-the-snapshot.md` — The boundary this task lands in `command-handoff.md` is body prose, so on that side it is read only *after* the command has been invoked; the layer that actually decides which of the two genres a phrased request reaches is the always-loaded skill-description-field, and the command's `description:` — "transfers context to a future agent or session … persisted under `.ai-factory/handoffs/`" — is exactly the surface the field evidence in `152-`/`29-` shows the misrouted request matching, and it stays unchanged here. The architect side is genuinely covered, since `agent-architect/SKILL.md` is resident for the whole of an architect session and the appended sentence is read before any routing happens; the handoff side degrades to a stop-after-invocation, which costs an invocation rather than a wrong artifact, and is the only place the boundary can be read at all in a session where no architect is rehydrated. So the pair does cover the observed case and the plan is right not to touch the frontmatter — the spec pins "No other sentence changes in either file" and the contract line scopes the task to the two additions. If the phase later wants the genre decided before invocation rather than after, the `description:` field is where that would live, and it belongs to a task that owns it.

PLAN_REVIEW_PASS
