# Plan review — 58.1 the snapshot carries reasoning, not just residue, and is thick by default

## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/05-58-1-the-snapshot-carries-reasoning-not-just-residue-and-is-thick-by-default.md`
**Target:** `src/skills/agent-architect/SKILL.md` (one paragraph, two adjoining sentences)
**Risk Level:** 🟡 Medium

Every ground-truth claim the plan makes was re-verified against the files, and all of them hold:

- `src/skills/agent-architect/SKILL.md` is 371 lines; the memory-snapshot paragraph runs lines 65–81 of § "Spawn once, message thereafter".
- Sentence 1 begins at the start of line 73, directly after `…is never sent to the editor.` (58.2's anchor, line 72), and ends mid-line 76 with `never an inventory of the session.`; `Each new` does start on that same line. Sentence 2 ends mid-line 78 with `…a stale next action.` and `Of the` starts on that same line. The paragraph does open with the two-occasions sentence (58.4's anchor, line 65).
- The quoted "current" text of both sentences is byte-identical to the file.
- `src/skills/architect-editor-engine/SKILL.md` and `src/agents/editor.md` contain no occurrence of "snapshot" at all. The file's other four snapshot mentions (lines 40, 131, 328, 370) speak only of the buffer pointer, the recovery occasion, and the liveness fallback — line 328 even defers explicitly ("see 'Spawn once, message thereafter' for the rest of what is recorded"). No competing definition of snapshot content exists in the repository, exactly as the plan states.
- The frontmatter `description:` makes no claim about snapshot content — correctly left untouched.
- The wrap claim holds: the paragraph's non-terminal lines measure 63–76 columns, the file's body median is 72 and its widest body line is 81. The growth estimate is sound — the pinned replacement is roughly +400 characters over the sentence it replaces, ~+7 lines, landing near 378 and far inside the ≤ 500-line body constraint.
- The spec's sweep, run now, returns exactly seven paths: the target, the roadmap, this plan, spec `159-`, phase note `152-`, `.ai-factory/notes/07-architect-buffer.md`, and `.ai-factory/handoffs/29-…`. The plan's exception list covers all six non-target paths by category, with no unclassified remainder. The invariant (target drops out) is correct against the pinned replacement text: "only" is gone, "never an inventory of the session" is reworded, and "stale next action" is continued by a semicolon.
- `docs/paired-loop.md` § "How the memory begins, and how it survives" does carry both governing claims the change leans on — the break-destroys-the-reasoning paragraph and the "A newer snapshot supersedes the older one's next action, and nothing else" paragraph — so `Docs: no` is the right setting; nothing upstream needs amending.
- `Testing: no` is right: prose in a skill body has no silently-failing surface.

The task decomposition (two edits, second depending on the first because the first re-wraps the lines the second lands in, then a read-only sweep) is correct, and the restraint instructions — append-only on sentence 2, no citation aside, neighbouring sentences byte-stable — match both the spec and the contract line's "touch only these two sentences".

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" and its always-loaded-layer rule are not crossed: the change adds no skill, no `loads:` edge, and no restatement of an always-loaded guarantee. `docs/paired-loop.md` is a governing spec, not part of the always-loaded layer, so the rule "name the guarantee in one sentence at the point of reliance" does not fire and the plan's no-citation instruction is consistent with it.
- **Rules** — WARN (non-blocking): `.ai-factory/RULES.md` is absent in this repository, so no convention file could be checked. `.ai-factory/skill-context/aif-review/SKILL.md` is likewise absent.
- **Roadmap** — OK. The task is the first `[ ]` line of Phase 58 in `.ai-factory/roadmaps/trickster77777.md`, i.e. the seam, with 57.3 immediately above it as `[x]`. Linkage is complete: contract line → `Spec:` `159-…md` → phase note `152-…md` → `Governing spec: docs/paired-loop.md`, each walked and each consistent with the plan. Sibling tasks 58.2 and 58.4 own disjoint sentences of the same paragraph, as both the plan and the spec state.

### Findings

**1 — The enumeration of pinned wording changes omits the one the task is named for.** (`.ai-factory/plans/…05-58-1-….md`, Tasks → "Replace the residue sentence with the pinned replacement", bullet "Copy from the spec; do not paraphrase.")

The bullet lists the deltas as: drops "only", drops the "and" before "what must not be resolved by inference", turns "because everything durable…" into "…so restating it is never the point", replaces "never an inventory of the session" with "a snapshot that drops the reasoning is an inventory, not a history", and adds the thickness default as its own sentence — closing with "Each of those is a pinned wording choice, not a stylistic one."

Missing from that list is the insertion that carries the whole task: `— and the reasoning that shaped it: why one option was taken over another, which premise proved false and how, what the user's own correction was and in what words`. It is the first thing the contract line demands ("require the stretch's reasoning") and the substance of the spec's replacement, yet the plan's own change set never names it. Worse, two entries in the list presuppose it without stating it: "a snapshot that drops the reasoning is an inventory" and "carrying the reasoning in full" both refer back to a requirement the enumeration never introduces.

An implementer who treats the enumeration as the change set — which its closing sentence invites — produces a replacement that removes "only", reflows the causal clause, and appends the thickness sentence while never adding the reasoning clause, and the task's own purpose is silently lost. The preceding instruction to copy from the spec is the only thing standing between that reading and the wrong output. Add the reasoning clause to the enumeration, in the position it occupies in the pinned text.

**2 — The verification task tests only the disappearance of the old wording, never the arrival of the new.** (`.ai-factory/plans/…05-58-1-….md`, Tasks → Verification → "Re-run the spec's sweep and confirm the invariant")

The step ends "That is the whole invariant." The sweep is a negative check: it confirms the three old anchors are gone. It cannot distinguish the pinned replacement from any other rewrite that happens to drop "only", reword the inventory phrase, and continue "stale next action" with a semicolon — including the truncated one finding 1 describes, which would pass cleanly.

Since the deliverable of this task is pinned verbatim text rather than a behavioural change, the plan should pair the sweep with a positive check that the destination paragraph reproduces the spec's § "What must be true after" wording word for word, ignoring newlines — for instance by reading the paragraph back and comparing it against the spec's two blockquotes, sentence by sentence. Without it, no step in the plan ever confirms the words that were the point of the task actually landed.

### Positive Notes

- The plan does not re-derive the pinned text and says so explicitly — "copy the words and their order from the spec" — and confines itself to what the spec leaves open: anchor positions, wrap convention, and the neighbours that must not move. That is the right division of labour with a verbatim-pinned spec.
- "Verbatim means the words and their order, never the newlines" is stated once, up front, and then relied on rather than repeated. It pre-empts the one real ambiguity of editing a hard-wrapped paragraph, and the consequence the plan draws from it — that later greps against this passage match per line, not per sentence — is precisely the property that makes the sweep in the verification step trustworthy.
- The sweep exception list is written as a *rule* with worked cases, not as a tally: "does this file quote one of the two passages as ground truth for a standing claim about the present?", followed by why each returned path answers no, and an explicit instruction to stop and report rather than edit an unclassified hit. Run against the repository now it classifies all seven returned paths with nothing left over, and it carries no count that could rot.
- The two restraint bullets are the kind that actually prevent damage: naming the adjoining sentences by their exact end and start text (58.2's and the pointer sentence's) rather than by line number, and forbidding the citation aside that a well-meaning implementer would otherwise add to a file that today cites no document at all.

## Deferred observations
- Affects: Phase 58 / `.ai-factory/specs/trickster77777/162-a-handoff-phrased-request-can-mean-the-snapshot.md` — This task deliberately leans on `docs/paired-loop.md` "by consequence" and forbids any citation aside, which matches the current state of `src/skills/agent-architect/SKILL.md`: the file contains no reference to `docs/` anywhere today. Sibling task 58.4's contract line, however, requires its new routing sentence in the same section to "cite `docs/paired-loop.md` § 'How the memory begins, and how it survives'". If both land as specified, one paragraph of § "Spawn once, message thereafter" ends up with an explicit doc citation in the sentence that opens it and a deliberate absence of one in the two sentences that follow — and the file gains its first `docs/` reference by way of the sibling rather than by a decision either spec states. Whether the skill body cites its governing spec is a phase-level call, not this task's; 58.1 is correct to follow its own spec here.
