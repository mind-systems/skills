# Handoff — position addresses, and the rulings that grew past their case

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

A long paired-loop session that landed four tasks, wrote two philosophy docs and six rescue reports, and ended with three tasks written but unrun and one blocker awaiting the user — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Unit A — task 31.1, the handoff's own mark (the next action)

#### Must-read now (minimal rehydration set)

- `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md` — the task spec; three changes, five guards. Four of the six pin-gaps findings below are repairs to *this* file. ← lead here.
- The `31.1` contract line under `### Phase 31` in `.ai-factory/roadmaps/trickster77777.md`.
- `src/commands/command-handoff.md` — the file all three changes land in. Note it emits **two** shapes, grid and prose; the spec addresses only the grid one. Its Step 2 passes the skeleton to `note` **blank**, which collides with a pre-filled mark line.
- `.ai-factory/handoffs/17-why-the-budget-fix-is-one-sentence.md` and `16-…`, `15-…` — the three files that already carry the mark verbatim. The form exists in the corpus; the spec never pins its literal.

#### Read on demand

- `src/skills/note/SKILL.md` — its `**Date:** <YYYY-MM-DD>` line is the precedent that a literal can sit beside placeholders in a template passed to it.

### Unit B — task 32.1, the character budget's method

#### Must-read now

- `.ai-factory/specs/trickster77777/107-character-budget-names-its-method.md` — two edits, five guards, numbers unchanged.
- `src/skills/roadmap-engine/SKILL.md` § "Rules for writing a contract line" — where the method sentence lands.

### Unit C — the two ratified philosophy docs

#### Must-read now

- `docs/reference-by-name.md` — naming must go as deep as reference; a `file:line` citation is a defect report against its target. Governs how everything above is written.
- `docs/always-loaded-discipline.md` — the two halves of the always-loaded layer, and the rule that a skill restates nothing the layer guarantees.

### Unit D — the open question about the architect

#### Must-read now

- `.ai-factory/handoffs/16-the-architect-extends-a-ruling-past-its-case.md` — **already marked processed.** Four specimens of one defect. The user chose its third option: write nothing.

## 3. Current state

**Done:**

- **28.1, 28.2, 29.1, 30.1 landed and committed.** `roadmap-outline-deep` exists; `roadmap-decompose` and `task-rescue` read both phase-header pointers; `command-pin-gaps` walks a task into the code; `task-rescue` writes one durable report per run.
- **`docs/reference-by-name.md`** written and wired into `CLAUDE.md`'s Guides table. Ratified by the user in words.
- **`docs/always-loaded-discipline.md`** written, with edges from `skill-description-field`, `context-tree`, `ARCHITECTURE.md` § Composition and the Guides table.
- **Six rescue reports** under `.ai-factory/rescue-reports/` — three for `skills`, three for `tradeoxy_core`. They are the only surviving record of attempts whose plans and reviews were deleted by the rescues that repaired them.
- **The architect-over-extension question closed with "write nothing."** The user's ruling.

**In-flight:**

- **31.1** — written, not run. A pin-gaps scan returned six findings: four repairs to spec 106 (the mark's literal is unpinned; the prose shape is unaddressed; the blank-template collision; a verification bullet that assumes a clean tree), one blocker for the user, and one I rejected on evidence.
- **32.1** — written, not run. No findings against it yet.

**Uncommitted working-tree state:** the roadmap (phases 31 and 32), specs 106 and 107, `ARCHITECTURE.md`, `CLAUDE.md`, `docs/philosophy/context-tree.md`, `docs/skill-description-field.md`, both new docs, handoffs 15–18, the six rescue reports, and the architect buffers. Nothing staged. Nothing may be committed without the user saying so.

## 4. Next step

Put the 31.1 blocker to the user, then repair spec 106.

**The blocker.** Spec 106 has the `description:` state that no document and no task references a handoff. The shipped corpus contradicts it: `roadmap-outline` explicitly *permits* handoff links in preamble prose, `roadmap-engine`'s format template names "source handoff/spec links" in the direction preamble, and `roadmap-prune`'s safety rationale leans on that permission by name — it keys deletion on the literal `Phase note:` token *because* unrelated handoff links are allowed in the same prose and it holds `Bash(rm *)`. Live instances: task specs 87 and 88 cite handoffs in their first line; three direction preambles in this roadmap carry `Source handoff:`. Spec 106's own guards forbid touching those skills, so shipping as written leaves the family self-contradictory. Reconciling them is a second reason to revert, therefore a separate task. **The user decides:** narrow the rule to "not cited as authority or confirmation" (which leaves `roadmap-outline` true), or keep the rule as stated and open a second task for the corpus.

**Then the four repairs to spec 106**, all closable from the code:
1. Pin the mark's literal verbatim — `**Processed:** \`[ ]\` — whoever reads this marks it; a marked handoff is spent.` — naming handoffs 15–17 as the source of the form, and require byte-exact reproduction. Both state literals must appear.
2. Say what the **prose shape** does — it has no `# Handoff` title and no `## 1. Frame`, so either it carries the same line directly under its title, or it is excluded and the spec says why.
3. Resolve the blank-template collision: `command-handoff` Step 2 passes the grid skeleton to `note` **blank** and forbids pre-filling, because a filled skeleton makes distillation a no-op. The mark is a pre-filled literal. `note`'s own default template holds `**Date:** <YYYY-MM-DD>` beside placeholders, so it is feasible — the clause must live at the template hook, since a guard forbids touching `note`.
4. Narrow the last verification bullet to `-- src/commands/command-handoff.md`, or state a clean-tree precondition. As written it fails on unrelated uncommitted files that are in the tree right now.

## 5. Working discipline

**The pairing.** This session ran as the **applying half** of a two-architect pair (`architect-pairing-engine`). Orders arrive as `APPLY-EDIT` through the user from the deciding architect; the applying half originates no edit of its own, composes each arriving decision into an `APPLY-EDIT` to its own editor, and verifies what landed **against the files, never against the report**. Read the arriving order against the files first: where it is underspecified, self-contradicting, or would break something it never named, report back instead of guessing, and name every decision it left unpinned.

**The exception, learned this session:** what the architect authors from its own reading — handoffs, its buffer, rescue reports, and a mark an artifact addresses to its own reader — it writes with its own hands, no work-order. The user also directs edits straight to the architect ("сам вставь, без редактора", "запиши это как ратифицированное"); a direct instruction from the user is not an arriving order and is acted on.

**Measure, never estimate — and price the measurement first.** The user's standing complaint, verbatim: «эти вечные подсчёты строк… занимают 30% времени рассуждения и чата. И это такой мусор, который засоряет и мой мозг и твой контекст». The test that came out of it: **will anyone act on this number?** Existence checks and anchor-uniqueness pay; cardinality mostly does not. Of roughly fifteen contract-line measurements this session, none changed a decision.

**Report only what breaks.** The user rejected four findings as «шлак» — a broken path in a closed task, a registry entry the spec's own guard already deferred, handoffs already resolved, a wording quibble. The bar he set: report what will give a wrong result or a loss, keep inconsequential inconsistencies to yourself.

**Do what was asked, nothing more.** «это такая задача, где я боюсь ты опять насуёшь того, что я не просил». And, on an explanation being mistaken for a clause: «это не призыв прописывать это в скиле!!!» A ruling is a sentence; where it seems to imply more, the implication is a question for the user, not an artifact.

**Never commit.** Nothing was committed this session by the architect; every commit in the log was the user's.

## 6. Error log

Mistakes actually made here, each with its correction. These are cheap to repeat.

- **Inverted the direction of evidence.** Measured the existing roadmap's preambles and argued a proposed 200–500-character budget was wrong because half the corpus exceeded it. A corpus written before a norm cannot falsify the norm — and large preambles were evidence *for* the task. The user caught it; the finding was withdrawn in full. **Before measuring a corpus against a proposed rule, ask which direction the evidence runs.**
- **Shipped a 1022-character contract line**, over the 400–1000 band, having estimated "roughly 850" without measuring — in the same order that required the editor to measure with Python. Authored text needs the same three checks as a received anchor: path resolves, length measured, anchor unique.
- **Wrote sibling-repo paths one segment short** (`orchestrator/prompts/planner.md`) in spec 57 and contract line 24.1. The real path is `orchestrator/orchestrator/prompts/…`; the short form resolves to nothing from the family root. Repaired a round later.
- **Relayed a boundary check stale by one round.** `git diff HEAD -- src/ active/ docs/` "must be empty" was passed through verbatim after the previous round had deliberately written under `docs/`. A check that fails on correct work. **Re-derive a relayed check against what the preceding rounds actually wrote.**
- **Wrote an unreachable check for an untracked file.** Required `git diff --stat` to show one insertion and one deletion for a handoff that git does not track. The editor reported the measurement instead of forcing it.
- **Verified inputs, not outputs — twice.** Checked that token positions were where an order claimed, but did not simulate the post-edit text; the pinned bullet reintroduced the very tokens whose count was required to be zero. The fix that has worked since: **simulate every edit in memory and run the order's own self-verify against the simulated result before sending.**
- **Numbering collision on a handoff.** Scanned the directory at the start of the round, wrote `16-…` at the end, and collided with a parallel session's `16-…`. Renamed mine to 17. **Re-scan at the moment of write, not at the start of the round.** The `handoffs/` directory is flat with one counter and several writers; `multiuser-roadmaps` predicts exactly this and no per-stem split exists for handoffs.
- **Nearly filed two fabrication charges.** Once against a preamble-size figure of "1200–1900" that this repository could not produce — it is grounded in `tradeoxy_broker`, which holds 1892 and one at 2861. Once against an order's anchors for the orchestrator roadmap, from a grep that had shown only half the file. **Measure the corpus the claim is about, not the one in front of you.**

## 7. Orientation

Two-of-a-kind traps that cost time here:

- **Bytes vs characters.** This machine sets no locale, so `wc -m` returns bytes and `awk`'s `length` returns bytes whatever the locale says. A 991-character line reads as 995. Even `LC_ALL=en_US.UTF-8 wc -m` adds one for the trailing newline. Use a Python code-point count on the line with its newline stripped. Eight measurements were reported wrong before this was pinned; task 32.1 exists to write the method next to the budget.
- **Substring containment.** `orchestrator/agents.py` is a substring of `orchestrator/orchestrator/agents.py`. A global substitution meant to fix the short form would have tripled the segment in a file already holding the long one. Likewise a count of `orchestrator/prompts/` can never reach zero once the corrected path exists — count the difference, not the substring.
- **Two `aif-docs` rows** in `skill-cycle.md`'s `## Схема` diagram — the ТЗ step and the final verification pass. Match by the full line, never by the skill name.
- **`plan-reviews/` and `reviews/` are different sets.** A rescue at spec+plan depth deletes the first; at spec+plan+code, the second.
- **`Governing spec:` and `Phase note:`** both sit on a phase header and are not interchangeable: the first states how the phase must become and is never swept, the second states what diverges now and is captured by `roadmap-prune` before an emptied phase's header is deleted.
- **A verification bullet that names the token it requires to be absent** always fails against itself. This happened; report the measured value rather than rewording the pinned text.

## 8. Domain model spine

Settled. Do not re-litigate.

- **A reference addresses by name or by position; only the name survives.** Naming must go as deep as reference — a heading, a bold lead-in, a numbered item, anything that will be depended on. `docs/reference-by-name.md`.
- **A `file:line` reference is a defect report against its target.** The repair belongs in the target — a name added, or an existing name used. Position addresses live in a work-order, which is thrown away when applied; they never enter a spec, a roadmap line or a document.
- **Documents are split by their reason to change, never by length.** Measured: docs in this repository and both sibling projects are already small and subject-split; citation density does not track file size. There is no doc-restructuring project, and inventing one would be the defect described in handoff 16.
- **A handoff is a temporary buffer, spent once read.** Its reader marks it. A marked handoff is never edited and never cited as confirmation. `.ai-factory/specs/trickster77777/106-…`.
- **The always-loaded layer produces behavior with no skill invoked**, and a skill restates nothing that layer already guarantees; where it leans on such a guarantee, it names it at the point of reliance. `docs/always-loaded-discipline.md`.
- **A rescue report is the only durable record of a failed attempt**, because the repair deletes the plan and reviews it repaired. One report per run, written once, at the end.

## 9. Hard rules

- **Never commit without explicit permission; never push.** Two repositories, two permissions.
- **All artifacts in English.** The user's own words may be quoted verbatim in Russian where the words themselves are the ruling.
- **No new term, token, class, owner or task unless the user asked for it in words.**
- **A contract line is 400–1000 characters, counted in Unicode code points.**
- **`docs/reserved-words.md` is final and is not subject to update** — its own first line, added this session by the user's ruling.
- The applying half never touches a shared artifact through its own hands, except handoffs, its buffer, rescue reports, and a mark an artifact addresses to its reader.

## 10. Cross-cutting contracts / invariants checklist

- `Phase note:` — protocol token, byte-exact, capital P, lowercase n, colon. Its pointer form is `Phase note: [<title>](<path>)`, with the path repo-root-relative and beginning `.ai-factory/`, exactly as a `Spec:` tag's path.
- `**Processed:** \`[ ]\`` / `\`[x]\`` — the handoff mark, two states and nothing else. No date, no author, no third status. Nothing scans it.
- The phase-note destination is the roadmap's own spec directory — `.ai-factory/specs/<slug>/` for a named roadmap, flat `.ai-factory/specs/` for the default.
- A cross-repo path names the repository and resolves from the family root: `orchestrator/orchestrator/prompts/planner.md`, `skills/src/skills/…`.
- `roadmap-engine` is a load-once engine with eight callers; any edit to it is part of their contract.
- The rescue report's destination is `<skills repo root>/.ai-factory/rescue-reports/<project>/`, resolved at write time by `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` — verified working through the double symlink — and never stored or cached.

## 11. Per-unit map with watch-points

- **31.1 — the handoff mark.** Became a three-part change to one file: the `description:` names the entity and forbids citation, the emitted template carries the mark, the body carries the rule. **Watch:** the blocker above, and that `command-handoff` emits two shapes.
- **32.1 — the budget's method.** Became one sentence in `roadmap-engine` plus a pointer from `roadmap-outline-deep`, which loads it. **Watch:** the numbers must not move — `~600`, `400–1000`, `~200–500` stay exactly as they are.
- **`docs/reference-by-name.md`.** Became a ratified discipline doc. **Watch:** its five `:N` occurrences are quotations of the defect as evidence, not uses; do not "fix" them.
- **The rescue reports.** Became a new genre with six entries. **Watch:** a report states what was true when written and is never rewritten — report 02 describes a two-moment design that report 03 records as deleted, and that contradiction is the record working, not a defect.
- **The architect question.** Became handoff 16, marked processed, with the user's ruling to write nothing. **Watch:** the cheapest counter already works — the user asking what a task is for caught three of four specimens within minutes.
