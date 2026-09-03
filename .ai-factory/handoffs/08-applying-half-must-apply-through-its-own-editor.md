# Handoff — the applying architect must apply through its own editor, not its own hands

## 1. Frame

Phase 26 is fully landed and committed (six tasks, `27ab9cb` … `88f1e35`, working tree clean), and code review of the whole phase found one real defect shipped by the phase itself: `architect-pairing-engine`'s applying half was written to touch shared artifacts with its own hands, which the user never asked for and has now rejected outright — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `src/skills/architect-pairing-engine/SKILL.md` — the file to fix; `## The applying half` at `:50-69` is the whole subject ← lead here
- `src/skills/agent-architect/SKILL.md` — the generic discipline the applying half wrongly overrides; `:25-26` ("that hand is always the editor's") and the `description:` field are correct as they stand and must NOT be edited
- `.ai-factory/roadmaps/trickster77777.md` — Phase 26 at lines 82–96, all six tasks `[x]`; the fix becomes a new task at the end of the phase
- `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` — where the defect entered: `:67` and `:73` carry the own-hands language verbatim from the first draft

### Read on demand

- `.ai-factory/specs/trickster77777/97-applying-half-check-cut-back.md` — the most recent spec; its check paragraph is the part of the applying half that stays
- `src/agents/editor.md` — the editor's own definition; `:39-48` apply mode, `:71-83` the check-and-flag-back discipline. Never edited by this phase and not to be edited now
- `docs/reserved-words.md`, `docs/using-the-language.md` — imported into every session via the root CLAUDE.md; the vocabulary the skill bodies are bound to
- `.ai-factory/handoffs/07-agent-architect-phase-26-scope-correction.md` — the previous handoff, covering the same phase before it was implemented

## 3. Current state

**Done:**

- Phase 26 shipped in six commits: 26.4 (pairing roles → new `architect-pairing-engine`), 26.1 (architect state survives a compact), 26.3 (nothing closes a round before the editor's report), 26.5 (the applying half checks the order), 26.6 (26.5 cut back to the check alone), 26.7 (CLAUDE.md's two enumerations + the engine's load self-description).
- All deferred observations on 26.4 and 26.5 are pinned: two `[routed → …98…]`, four `[dismissed]`, zero unmarked. A prune is no longer blocked by them.
- Full code review of the phase completed, by the architect and by an independent editor pass.

**In-flight:**

- One defect found and confirmed, no task written for it yet. The applying half of `architect-pairing-engine` claims the architect's own hands act on shared artifacts. The user's ruling: **neither architect ever touches artifacts; the applying architect applies the arriving work-order through its own editor.** The intended next task is 26.8 with spec 99.

**Uncommitted working-tree state:**

- none. Tree is clean at `88f1e35`.

## 4. Next step

Write task 26.8 (spec 99) and its work-order. The change is confined to `src/skills/architect-pairing-engine/SKILL.md` § "The applying half": delete the clause "and does not route it onward to an editor of its own — its hands are its own, not delegated a second time" (`:54-56`) and the entire "This half supersedes the generic default…" paragraph (`:66-69`). What replaces them: the applying half authors an ordinary `APPLY-EDIT` channel-message to its own editor, exactly as an unpaired architect does. Its only departure from generic behavior is **where the work-order's content comes from** — a peer architect's decision arriving through the user — never who touches the files. The check paragraph (`:58-64`) survives; adjust only "before you touch them", since the editor is the hand. `agent-architect`'s `description:` and `:25-26` need no edit — they were never wrong.

## 5. Working discipline

- The user marks with `::`. Everything before the mark relays to the editor verbatim as a `REPORT-ONLY` channel-message; everything after it is the architect's alone and never forwarded. No mark anywhere means the message is conversation. The marker is unconditional — never judge whether it was "meant".
- **Nothing that closes a round — summary, verdict, or work-order — leaves before the editor's report on that round exists.** The architect's own parallel pass runs through the wait; what defers is the announcement.
- Verification is by fact: read the files, run the greps, never accept a report as proof.
- The user wants small, surgical edits. Ship exactly the sentences of the request — nothing past them. When a requirement is unclear, ask about the method; never invent additional scope.
- Never commit without explicit permission. Work-orders always end with "do not commit."
- Work-orders are English; conversation is Russian.

## 6. Error log

1. **The defect the next task fixes was invented, three tasks ago, and never reopened.** The user's requirement was one sentence: the second architect "не собирается делать правки сам, а только через таск от первого" — originates no edit, acts only on an arriving work-order. It was written into 26.4's contract line as "…and never routes it onward to its own editor", into spec 95 (`:67`, `:73`), and shipped into the skill. Nothing in the request bypassed the editor. 26.5 built on top of it; 26.6 trimmed only 26.5's own additions.
2. **A whole design was invented for a solved problem.** Spec 90 required the architect's buffer path to be "derivable from the environment" — slug key, session-derived id, fallback directory scan. The buffer's identity was never at risk. Three plan rounds burned, the task failed at planning, the rescue retired the design. The path stays `.ai-factory/notes/<NN>-architect-buffer.md`; "retired and not reopened" sits in 26.1's guard for this reason.
3. **A task was built that nobody asked for** — a six-part work-order form plus a ban on irreversible operations, on the false premise that the recipient arrives with no shared context. Deleted; spec 94 retired.
4. **26.5 shipped three powers past its one-sentence requirement** — a licence to correct an outright-wrong order, a sentence existing only to reconcile that licence with the paragraph above it, and a round-closing clause. 26.6 exists solely to undo them.
5. **A citation was used that did not support the claim.** Spec 95's requirement was grounded in `handoffs/02` §2/§5.4, which describe dual independent cross-checking, not a decide/apply split. Fixed by deleting the citation, not by retargeting the task.
6. **Six self-verify checks asserted an absolute repository state instead of deriving the round's own delta** — R10 (stale staged-path count, defeated by an orchestrator commit landing mid-round), R12 ("exactly three files, 3+3" against `git diff --stat`, which shows the whole uncommitted tree), R13 (`[dismissed]` assumed unique; nine pre-existing instances), R16 (three at once). None was a defect in the edit; every one was a false alarm manufactured by sixteen rounds of accumulated uncommitted state. **The working form: diff each file against `git show HEAD:<path>` and name the delta in words, never a number the order predicts.** Also: derive the expectation from the order's own NEW blocks — R15's "exactly two hits" was defeated by its own first edit.
7. **Byte counts reported as character counts.** `awk length()` and `wc -m` count bytes in this locale; em-dashes read high. Use `python3 len()` on decoded text.
8. **An invented length band cost real content.** Orders R3/R4 set "target 800–900" on top of `roadmap-engine`'s actual 400–1000, and the guard clause `and not reopened` was traded away to hit it. The only length constraint is the 1000-character ceiling, stated as a ceiling.
9. **Spec 96 pinned new text word-for-word and simultaneously guarded the line above it as untouched**, without stating how the two read together. That is what made 26.5's first plan round unresolvable at plan level.
10. **A review's finding was relayed as substantive when it was not.** The `::`-relay "fork" conflates two different objects: the pairing rule governs the arriving work-order, the generic `::` rule governs the user's marked message. They never address the same thing.
11. **26.1's commit touched three hunks while spec 93 pinned two regions** — the third at "## On every invocation". The change was correct and necessary; the boundary violation was not caught by any plan-review.

## 7. Orientation

- **26.2 does not exist and its number is retired.** Numbers are identity; tasks execute in file order. Never renumber.
- **`ListAgents` and `SendMessage` are different subsystems.** The listing comes from the live task registry and drops a completed subagent within about a minute; a send resolves the handle from the on-disk sidecar and resumes the agent from its transcript. Absence from the listing is never evidence of death. This is the failure that opened the whole phase.
- **Two buffers, two owners.** `.ai-factory/notes/01-architect-buffer.md` belongs to the applying architect; `02` to the deciding one.
- **`loads:` declares the graph; it does not load.** 26.7 fixed exactly this misreading in `architect-editor-engine:17`. The same gap is still open for `architect-pairing-engine` — see § 10.

## 8. Domain model spine

- **Neither architect ever touches shared artifacts.** The editor is always the hand — for the unpaired architect, for the deciding half, and for the applying half. Settled by the user this session; do not re-litigate. This is what task 26.8 restores.
- **Which agent plays which role is external per-agent data.** It never enters the generic skill; it lives in `architect-pairing-engine`, loaded only when the user assigns a role. Settled at 26.4.
- **One home per fact.** The buffer holds the editor's handle and any assigned pairing role; the handoff carries the buffer's path alone — a pointer, never a copy. Settled at 26.1.
- **The two halves are the architect's internal implementation, not vocabulary.** The user ruled they need no entry in `docs/reserved-words.md`. Do not add one.

## 9. Hard rules

- Planning only in a chat session. The orchestrator implements roadmap tasks in a separate run; a work-order that plans must carry `git diff -- src/` must be empty.
- `---STOP---` stays the last line of the roadmap.
- `[x]` contract lines are history: never edited, never renumbered, never re-measured.
- Task specs live in `.ai-factory/specs/trickster77777/` (named roadmap → per-slug subdirectory). Next free number is 99.
- Contract-line ceiling is 1000 characters, measured in characters. There is no narrower target. Note that the orchestrator appends a `[Nm Ns]` timing suffix when it closes a task, so a closed line is ~10 characters longer than when written.
- No commit without the user's explicit word.
- Never edit `src/commands/command-handoff.md`, `src/skills/note/SKILL.md`, or `src/skills/roadmap-engine/SKILL.md` as part of this work.

## 10. Cross-cutting contracts / invariants checklist

- `agent-architect/SKILL.md:25-26` — "that hand is always the editor's" — is **correct and stays**. Every pairing rule must be consistent with it.
- `agent-architect`'s `description:` — "the architect never touches shared artifacts itself" — is **correct and stays**. It was briefly misdiagnosed as stale; it is not.
- `architect-editor-engine`'s two format tokens `REPORT-ONLY` and `APPLY-EDIT` are protocol tokens, byte-exact wherever produced or consumed. Mode is keyed strictly off the token that opens a message.
- `architect-editor-engine`'s `description:` names both callers (`:8-9`). That is a known exception to "engines never list their callers", deliberately left alone by 26.7 and recorded as such in spec 98. Do not "fix" it as a side-effect.
- The engine's body names no caller — verify with `sed -n '14,$p' … | grep -c "agent-architect"` → 0, never a whole-file grep, which returns 1 because of the frontmatter.
- **Still open, no task written:** `agent-architect` declares `loads: architect-pairing-engine` but its body never instructs loading it — the only mentions are the frontmatter edge and a parenthetical at `:61-62`. The sibling engine gets an explicit body instruction at `:42-45`. The load condition currently lives only inside the file being loaded. Failure mode: a role is assigned, the architect never loads the skill, and proceeds on the generic default. Worth folding into 26.8 or a task beside it — the user has not ruled on it yet.

## 11. Per-unit map with watch-points

- **26.4 — pairing roles (spec 95, `27ab9cb`).** Became the new `architect-pairing-engine` with two role halves. Watch: its applying half carries the own-hands defect from the first draft; that is what 26.8 removes. Its deciding half is correct and must not be touched.
- **26.1 — architect state survives the compact (spec 93, `451c6b3`).** The handoff names its addressee and carries the buffer's path alone; the handle and role live in the buffer; a failed delivery is the only death signal; `ListAgents` explicitly ruled out. Watch: the commit touched a third hunk beyond the spec's two pinned regions.
- **26.3 — nothing closes a round before the report (spec 92, `6cc8e5b`).** A standalone `##` section at `:176`, between "Relay on the marker" and "Review in parallel". Watch: `:184-186` says an apply work-order "is addressed to the editor" — for the deciding half it is addressed to the paired architect. A wording inaccuracy, not a broken rule; nobody has ruled on whether to fix it.
- **26.5 — the applying half checks the order (spec 96, `d59b004`).** Watch: it shipped three additions past the requirement; 26.6 removed them. Do not reintroduce a correction licence or a round-closing clause.
- **26.6 — cut back to the check (spec 97, `57c6c63`).** The check paragraph as it now stands is what the user actually asked for. Watch: 26.8 must keep it and change only "before you touch them".
- **26.7 — CLAUDE.md enumerations and the engine's self-description (spec 98, `88f1e35`).** Both lists now name both engines; `:17` says "per the instruction in its own body". Watch: `CLAUDE.md:74` and `:189` are two parallel enumerations answering different questions and drift apart one at a time — check both whenever a skill is added.
