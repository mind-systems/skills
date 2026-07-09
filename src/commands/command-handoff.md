---
description: >-
  Mine the live session and emit a dense, self-contained handoff prompt that
  transfers context to a future agent or session. Run this while the
  originating session's context is still live — that is the only moment
  there is something to mine. Always persists the handoff as a durable note
  under `.ai-factory/handoffs/`.
argument-hint: ""
allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob Skill
loads: note
---

Read `$ARGUMENTS`.

---

## Step 1 — Define the mining lens

`note` (Step 3) performs the mining and population, not the agent here. The following is the lens the agent hands `note` via the template hook — blank 11-section placeholders for the grid shape, folded into the free-form body directive for the prose shape — so `note` knows what to extract from the session:

- What project / domain / problem we are working on
- Every file that was read, edited, or created
- What decisions were made and why
- What is done vs still in-flight
- Any uncommitted working-tree state (modified files not yet committed)
- The one concrete next action
- How the user wants decisions made (confirm-before-execute, show-diff-first, when to stop and ask)
- Any mistakes made and their exact corrections
- Any traps, naming collisions, or "two of a kind" confusions that came up
- Any settled domain model points that must not be re-litigated
- Hard rules: commit/permission policy, file language, memory-write triggers, conventions

---

## Step 2 — Compose the handoff prompt

Every handoff is verbose and transfers the full **tree of meanings** the session built — the leaf→branch→trunk perception the successor would otherwise re-derive — rehydrating the next agent to the whole session's understanding, minus the dross: irrelevant tool-calls and dead-end file reads are stripped, only the load-bearing tree is carried.

Write **in English** regardless of the conversation language.

Compose in the shape inferred from the session's type.

**Grid shape.** Use the skeleton below exactly — do not change section names or order. Omit a section only if it is genuinely empty for this session (no invented content). Optional sections (7–11) appear only when the session produced material for them.

**The read-first map scopes to the next step, not the session.** "Must-read now" lists only what a fresh agent must read to execute the next concrete action and avoid every mistake in the error log — not an inventory of everything touched. A subsystem that was touched but requires nothing from the successor's next action does not belong under "must-read now" (it may still appear under "Read on demand" if genuinely useful later, or be dropped from the map entirely). When a session spanned several independent work-units, the handoff hands off several small cross-linked trees — one lean must-read set per unit — not one merged inventory tree; keep cross-linking between them, just don't flatten them into a single list.

~~~
# Handoff — <semantic slug derived from the session subject>

## 1. Frame
<one sentence: where we are in the project> — the originating session's
context isn't available here; trust these files, not memory.

## 2. Read-first map
<Scoped to the next step: "must-read now" is what a fresh agent needs to execute
the next action and avoid the error log — not every file touched this session.
If the session covered several independent work-units, repeat this pair of
subheadings once per unit (small, cross-linked trees) instead of merging
everything into one inventory.>

### Must-read now (minimal rehydration set)
- `<path>` — <one line: what question this file answers, specific to the next action> ← lead with the single best entry doc
- ...

### Read on demand
- `<path>` — <one line: what it covers — touched this session but not required for the next action>
- ...

## 3. Current state

**Done:**
- ...

**In-flight:**
- ...

**Uncommitted working-tree state:**
- <list modified/untracked files, or "none">

## 4. Next step
<The one concrete thing to do next. Who does what.>

## 5. Working discipline
<How the user wants decisions made: confirm-before-execute, show-diff-first, stop-and-ask triggers, etc.>

## 6. Error log
<Actual mistakes made this session and their exact corrections — each named with the specific symbol, file, or decision involved. Not "some issues were fixed." This is the first thing thin handoffs drop and the cheapest repeat-failure to prevent. Empty → omit section.>

## 7. Orientation
<"Two of a kind" traps, naming collisions, confusable concepts. Only if session produced these.>

## 8. Domain model spine
<Settled model points with "don't re-litigate" + a file pointer per point. Only if session produced these.>

## 9. Hard rules
<Commits/permission policy, file language, memory-write triggers, naming conventions. Only the ones that came up.>

## 10. Cross-cutting contracts / invariants checklist
<The concrete names, types, signatures, and rules that recur across the work and must stay identical everywhere — e.g. "type X stays `Foo[]`, never `Bar[]`"; "method renamed `a()`→`b()`"; "field Z lives on the entity, not in params". Densest, highest-leverage section for consistency-heavy efforts. Only if the session produced recurring cross-cutting concerns.>

## 11. Per-unit map with watch-points
<For each work-unit touched: one line of what it became + one line of the non-obvious thing to verify (where the work was tricky or a mistake nearly happened). Distinct from the flat "Current state" list. Only if the session covered many work-units.>
~~~

**Prose shape.** Write flowing prose carrying the causal thread: the path walked, the false turns, the decision made and its rationale. References to files, specs, and notes appear inline at the moment they are load-bearing, not catalogued in a separate read-map. End by making the durable next step and the working discipline explicit — woven into the prose, not sectioned away.

Both shapes populate via `note` in Step 3 — do not populate here. The agent's job in this step is to shape the lens and directive `note` will use; `note` fills the grid or composes the prose from what the session actually produced — no placeholders, no invented content.

Before emitting, apply this self-check to your draft: *Could a fresh agent, from this handoff alone, hold the same perception tree — leaf→branch→trunk — the session ended with, without the irrelevant exploration? Could it execute the next step, avoid every mistake in the error log, and for each subsystem touched, know what it became and what to re-check?* If a whole subsystem collapsed to one bullet, or the recurring contracts aren't listed — expand before emitting. This gate applies to the content written to the note file; the paste-back pointer is intentionally minimal and is exempt from the tree-completeness gate — the full tree lives in the persisted file.

---

## Step 3 — Output

**Delegate to `note`.** Delegate composition and file mechanics to `note` (loaded via `loads: note` above) — do not mine, number, slug, `mkdir`, or `Write` yourself. Invoke `note` once this chat, supplying only hooks:

- **Destination directory** = `.ai-factory/handoffs/`
- **Template** = the chosen shape: for the grid shape, the skeleton from Step 2 above passed **blank** — its placeholder descriptions are the mining lens `note` uses to distill the session (do NOT pre-fill it: a filled-in skeleton would make `note`'s distillation a no-op); for the prose shape, a free-form body directive through the same template hook — the causal-thread structure from Step 2's prose guidance, not a section skeleton.
- **Verbosity directive** = "verbose; carry the full meaning-tree and its causal thread; strip irrelevant tool-calls and dead-end reads" — this exercises `note`'s Rule-2 override so the causal thread survives distillation.
- **Slug** (`note`'s `$1` / topic derivation, not a named hook) = derived semantically from the session's subject matter — lowercase words joined by hyphens, specific to what was actually worked on. Do NOT use the literal word `handoff`.

`note` performs its own numbering, directory creation, and file write. Its own Step 4 report is **not** surfaced — once `note` completes, emit only the minimal paste-back pointer below.

**Minimal paste-back pointer:** exactly one chat block, not the full handoff body re-emitted. The pointer must be paste-back-able (the user drops it into the next session to orient the fresh agent). It contains:

- The path of the written file (e.g. `.ai-factory/handoffs/03-auth-refactor.md`)
- The one-sentence frame (grid shape: section 1 of the handoff; prose shape: the opening framing line of the prose)
- The next step (grid shape: section 4 of the handoff; prose shape: the closing next-step sentence of the prose)
- Optionally: the count of work-units covered (e.g. "5 tasks covered") — grid shape only

This pointer stays consistent with the self-check gate above ("the paste-back pointer is intentionally minimal … exempt from the tree-completeness gate") for both shapes.

Example shape (adapt wording to the actual session):

> Handoff saved → `.ai-factory/handoffs/03-auth-refactor.md`
>
> **Frame:** We finished extracting the auth layer; the originating session's context isn't available here — trust these files, not memory.
> **Next:** Run the migration dry-run and confirm row counts match before applying.
>
> *Paste the path above into the next session to rehydrate.*
