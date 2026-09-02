# Handoff — Phase 26 for `agent-architect`, and the scope corrections that shaped it

## 1. Frame

Phase 26 in `.ai-factory/roadmaps/trickster77777.md` is decomposed down to three open tasks against three requirements the user named, and one work-order (R8) is out with the second architect and not yet applied — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `.ai-factory/roadmaps/trickster77777.md` — Phase 26 (lines 78–90): the direction, the intro, and the three open contract lines in file order 26.4, 26.1, 26.3 ← lead here
- `.ai-factory/notes/02-architect-buffer.md` — this architect's own buffer: the assigned role, the working configuration, the editor's handle, one open deferral
- `.ai-factory/specs/trickster77777/93-architect-state-survives-the-compact.md` — the spec R8 edits; the two edits land in its change list and its Verification section
- `src/skills/agent-architect/SKILL.md` — the file all three tasks edit; `:47-58` (handoff/liveness paragraph), `:120-126` (apply work-order), `:161-169` (buffer section)

### Read on demand

- `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` — task 26.4's spec; its `## The requirement` section was re-grounded this session and must not regain a handoff citation
- `.ai-factory/specs/trickster77777/92-nothing-closes-a-round-before-the-report.md` — task 26.3's spec; settled, untouched since it was written
- `src/agents/editor.md` and `src/skills/architect-editor-engine/SKILL.md` — the two files every task in this phase is guarded against touching
- `.ai-factory/handoffs/02-agent-architect-editor-field-report.md` — §2/§5.4 describe dual-independent cross-checking; they do **not** ground the pairing task, and a citation to them was removed from spec 95 for exactly that reason

## 3. Current state

**Done:**

- Phase 26 written, then repeatedly cut back to the three requirements the user actually stated.
- A failed orchestrator run of the old task 26.1 was rescued: plan, sidecar and three plan-reviews deleted; specs 90 and 91 retired; the surviving content merged into spec 93.
- Contract lines brought inside `roadmap-engine`'s length range: 26.4 = 983, 26.1 = 902, 26.3 = 906 characters.
- Spec 95's requirement re-grounded on the user's own decision after its handoff citation was found not to support it.

**In-flight:**

- Work-order **R8** is with the second architect, not yet applied. Two edits: (1) in the 26.1 contract line and spec 93, the handoff carries the **buffer's path alone** — a pointer, never a copy of the handle or role, which live in the buffer; (2) converge the three surviving "first non-deferral content" claims in spec 93 (lines 67, 134, 193) to the narrow wording change item 2 already uses, which currently contradicts item 1 of the same numbered list.

**Uncommitted working-tree state:**

- `M .ai-factory/roadmaps/trickster77777.md`
- `D .ai-factory/specs/trickster77777/90-architect-buffer-derivable-identity.md` (staged)
- `D .ai-factory/specs/trickster77777/91-architect-handle-survives-the-compact.md` (staged)
- `?? .ai-factory/specs/trickster77777/93-architect-state-survives-the-compact.md`
- `?? .ai-factory/specs/trickster77777/95-architect-pairing-roles.md`
- `?? .ai-factory/notes/` — two architect buffers, `01` (second architect) and `02` (this one)
- Last commit: `80ae03b` "Roadmap update". Nothing since is committed; every round R1–R8 sits in one working-tree diff, so per-round byte-identity claims are no longer verifiable after the fact.

## 4. Next step

Review the R8 result. The second architect is still executing it; when its report arrives, verify the two edits **against the files, not the report**: the 26.1 line's remedy clause now says the handoff carries the buffer's path alone, `grep -n "first non-deferral"` on spec 93 returns nothing, every remaining `handoff` line in spec 93 is consistent with a pointer rather than a copy, 26.4 (983) and 26.3 (906) are untouched, all twelve `[x]` lines keep their lengths, `---STOP---` is last, and `git diff -- src/` is empty. Relay the same target to the editor for an independent pass and reconcile before answering.

## 5. Working discipline

- The user marks with `::`. Everything before the mark relays to the editor verbatim as a `REPORT-ONLY` channel-message; everything after it is the architect's alone and is never forwarded. No mark anywhere means the message is conversation, never relayed. The marker is unconditional — there is no judging whether it was "meant".
- **The editor is a research channel only.** It receives `REPORT-ONLY` and nothing else. Every apply work-order is authored for the **second architect** and travels through the user, who relays it and brings back the report. This architect holds the **first** of the two roles.
- **Nothing that closes a round — summary, verdict, or work-order — leaves before the editor's report on that round exists.** The architect's own parallel pass runs through the wait; what defers is the announcement. A couple of lines mid-flight are fine; the settled answer waits.
- Verification is the architect's own and is by fact: read the files, run the greps, never accept a report as proof.
- Never commit without explicit permission. Work-orders always end with "do not commit."
- Work-orders are English; conversation is Russian.
- The user wants small, surgical edits. When a requirement is unclear, ask about the *method*, never invent additional scope.

## 6. Error log

1. **A whole design was invented for a solved problem.** Spec 90 required the architect's buffer path to be "derivable from the environment" — a `<slug>/` key, a session-derived id, a fallback directory scan, an echo-to-user step. The buffer's identity was never at risk: the architect creates the file, and the handoff written before every compact carries its path. Three plan rounds were burned on the invented machinery, the task failed at planning, and the rescue retired the whole design. Correction: the path stays exactly `.ai-factory/notes/<NN>-architect-buffer.md` with `note`'s numbering — "retired and not reopened" is in 26.1's guard for this reason.
2. **A requirement was replaced by a design question, then lost with it.** The user's "teach the architect to work paired with another architect" was turned into a pitch about roles, actors and parameterizing the skill. The user rejected that framing (the configuration is external per-agent data; the skill is a generic engine and the roles are add-ons loaded on the user's word). Instead of returning to the requirement, it was dropped. Correction: task 26.4 now *is* the requirement — one add-on skill holding both halves.
3. **A task was built that nobody asked for.** The original 26.4 (a six-part work-order form plus a ban on irreversible operations) came from an incidental observation during the rescue. Its stated premise — "the recipient arrives with no shared context" — is false against this repo's own text: `agent-architect/SKILL.md:38-40` and `editor.md:85-87` both name the editor's accumulated history as the mechanism's value, and `::` exists so the editor works the same payload independently. The task was deleted, spec 94 with it.
4. **A citation was used that did not support the claim.** Spec 95's requirement was grounded in `handoffs/02` §2 and §5.4. Those describe *dual independent agents cross-checking the same question*, not a decide/apply split. Both the editor and the second architect caught it. Correction: the citation was removed entirely and the requirement re-grounded on the user's own decision — the fix was deleting the false grounding, not retargeting the task to match an available source.
5. **An invented length band cost real content.** Work-orders R3 and R4 set "target 800–900" on top of `roadmap-engine`'s actual range (~600 target, 400–1000). To hit it, the applying editor trimmed `and not reopened` from 26.1's guard — the two words that make it a prohibition rather than a statement. R5 restored it. Correction: the only length constraint is the 1000-character ceiling; state it as a ceiling, never as a target, and forbid compression in the rules block at the top of an order, not in its tail.
6. **Byte counts were reported as character counts.** `awk length()` and `wc -m` count bytes in this shell's locale; the em-dashes in contract lines make the numbers read high. Use `python3` `len()` on decoded text. The "623 and 163 characters" quoted for two long lines were bytes; the real values were 619 and 161.
7. **An anchor was off by one.** A work-order cited the apply-work-order paragraph as `:119-126`; line 119 is blank and the paragraph is `:120-126`. A related off-by-three (`:44-48` for `:47-48`) had already been caught in the failed plan.
8. **A verification expectation was unmeetable.** An order's self-verify block expected "two changed files" from `git diff --stat` while one of them (spec 93) was untracked and structurally invisible to it. Nothing has been committed since `80ae03b`, so all rounds fold into one diff.
9. **A summary sentence contradicted the design.** "We put nothing in the handoff" was written while the design says the handoff carries the buffer's path — the one thing it must carry, because that is what a compact destroys. The handle and the role are not copied there; they live in the buffer and the handoff points at it.

## 7. Orientation

- **26.2 does not exist and its number is retired.** The original 26.2 was merged into 26.1; the new task took the next free ordinal, 26.4. Do not reuse 26.2 for anything.
- **Numbers are identity, not order.** Tasks execute in **file order** — currently 26.4, then 26.1, then 26.3. Do not renumber to make the sequence read tidily.
- **`ListAgents` and `SendMessage` are different subsystems.** The listing is built from the live task registry, which drops a completed subagent about a minute after its round; a send resolves a handle from the on-disk sidecar under `~/.claude/projects/<project-key>/<session-id>/subagents/agent-<id>.meta.json` and resumes the agent from its transcript. Absence from the listing is never evidence of death. This is the failure that opened the session.
- **Two buffers, two owners.** `.ai-factory/notes/01-architect-buffer.md` is the second architect's; `02` is this one's.

## 8. Domain model spine

- The applying hand is not the editor in this deployment, and which agent applies is **external per-agent data** — it never enters the generic skill. Settled; do not re-litigate by proposing to parameterize `agent-architect`. Pointer: `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` § "Why an add-on, not a change to the generic skill".
- The generic skill keeps today's default for an unpaired session (`agent-architect/SKILL.md:25-26`, "that hand is always the editor's"). Settled; the add-on overrides it only when a role is assigned.
- One home per fact: the buffer holds the handle and the role; the handoff carries a pointer to the buffer, never a copy of its contents. Settled this session and is the subject of R8.

## 9. Hard rules

- Planning only. No file under `src/` is edited by any round of this work — the orchestrator implements the tasks in a separate run. Every work-order carries `git diff -- src/` must be empty.
- `---STOP---` stays the last line of the roadmap file.
- `[x]` contract lines are history: never edited, never renumbered, never re-measured against a length rule.
- Task specs live in `.ai-factory/specs/trickster77777/` (named roadmap → per-slug subdirectory).
- No commit without the user's explicit word.

## 10. Cross-cutting contracts / invariants checklist

- Contract-line ceiling: **1000 characters**, measured in characters. There is no narrower target. Current: 26.4 = 983, 26.1 = 902 (R8 may change it), 26.3 = 906.
- Guard phrase that must survive in 26.1: `retired and not reopened`.
- The buffer path form stays `.ai-factory/notes/<NN>-architect-buffer.md`; no slug key, no session-derived id.
- Every `Spec:` tag resolves to a file that exists; after R8 the tags in file order are 95, 93, 92.
- Spec 93's Verification section must agree with its own change list — the contradiction R8 closes is exactly a mismatch between items of that list and the Verification text.
- Files no task in this phase may touch: `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, `src/skills/note/SKILL.md`, `src/commands/command-handoff.md`, `src/skills/roadmap-engine/SKILL.md`.

## 11. Per-unit map with watch-points

- **26.4 — pairing roles (spec 95).** Became one add-on skill holding both halves, loaded only when the user assigns a role. Watch: its `## The requirement` section stands on the user's decision alone — if a later reader re-adds a `handoffs/02` citation, the section is wrong again. Also unresolved by design: the new skill needs a `loads:` edge, an `active/skills/` symlink and an entry in `CLAUDE.md`'s active-set paragraph, where `architect-editor-engine` is already missing (recorded as a deferral in `02-architect-buffer.md`).
- **26.1 — the architect's state survives the compact (spec 93).** Became: the handoff names its addressee and carries the buffer's path; the handle and any assigned role live in the buffer and its section says so; a failed delivery is the only death signal. Watch: R8's two edits are the open part; verify the change list and the Verification section agree afterwards.
- **26.3 — nothing closes a round before the report (spec 92).** Became a standalone `##` section between `## Relay on the marker…` and `## Review in parallel…`, naming summary, verdict and work-order as the three closing artifacts. Watch: it is settled and byte-identical since it was written — any diff touching it is unintended.
