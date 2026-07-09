---
description: >-
  Mine the live session and emit a dense, self-contained handoff prompt that
  transfers context to a future agent or session. Run this while the
  originating session's context is still live — that is the only moment
  there is something to mine. Optionally persist the handoff as a durable
  note (pass "note" / "ноут" / "давай ноут" / "с ноутом" as the argument).
argument-hint: "[note] [narrative]"
allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob Skill
loads: note
---

Read `$ARGUMENTS`. Determine two orthogonal axes — do not collapse them into one four-way enum.

**Destination axis:**
- **Note mode** — triggered when `$ARGUMENTS` contains any of: `note`, `ноут`, `давай ноут`, `с ноутом` (case-insensitive, substring match).
- **Chat mode** — everything else, including empty arguments.

**Register axis:**
- **Skeleton register** (state-transfer) — the existing 11-section skeleton (Step 2). Fits sessions of mechanical progress across many work-units, where the successor needs what's done / what's next / what to re-check.
- **Narrative register** (understanding-transfer) — flowing prose carrying the causal thread to one or two decisions (Step 2).

Selection: an explicit user cue wins — *narrative* / *повествование* / *story*, or a rejection of the numbered form (e.g. "not the numbered skeleton"). Otherwise infer from session shape: many mechanical units mid-flight → skeleton; a reasoning journey to one or two decisions → narrative. When genuinely ambiguous, default to skeleton (safe for state-transfer) and name the choice.

**How Steps 1–2 apply:** the agent performs the mining (Step 1) and composition (Step 2) itself for **chat destination** (either register) and for **narrative + note destination**, producing the full handoff body now. **Only skeleton + note destination** instead has Steps 1–2 define the lens and blank skeleton that `note` executes in Step 3 — the agent does not mine the session or populate the skeleton itself there; it hands the skeleton and policy text to `note` as hooks, and `note` performs the mining and population.

---

## Step 1 — Mine the session

Review the entire visible conversation context. Extract:

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

Write **in English** regardless of the conversation language.

Compose in the register selected above.

**Skeleton register.** Use the skeleton below exactly — do not change section names or order. Omit a section only if it is genuinely empty for this session (no invented content). Optional sections (7–11) appear only when the session produced material for them.

**Output length and granularity must track how much was actually done.** A session that touched many work-units (phases, modules, files, tasks) must enumerate each one individually with its specific state and the specific thing to re-check — never collapse a whole subsystem to summary bullets. A small session still yields a short handoff. Proportional, not maximal — a trivial session padded to migration-guide length is itself a failure.

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

**Narrative register.** Write flowing prose carrying the causal thread: the path walked, the false turns, the decision made and its rationale. References to files, specs, and notes appear inline at the moment they are load-bearing, not catalogued in a separate read-map. End by making the durable next step and the working discipline explicit — woven into the prose, not sectioned away.

The proportionality principle applies to both registers: a small session yields a short narrative; padding a trivial session to migration-guide length is still a failure.

**Chat destination** (either register): populate every field (skeleton register) or compose the full narrative (narrative register) from what you actually observed in the session — no placeholders, no invented content. **Narrative + note destination:** the agent composes and populates the narrative itself here too — it `Write`s the result directly in Step 3, not via `note`. **Skeleton + note destination:** do not populate the skeleton here — pass it blank to `note` in Step 3; `note` performs the mining and population itself.

Before emitting, apply this self-check to your draft: *Could a fresh agent, with only this note, (a) execute the next step, (b) avoid every mistake in the error log, and (c) for each subsystem touched, know what it became and what to re-check?* If a whole subsystem collapsed to one bullet, or the recurring contracts aren't listed — expand before emitting. Proportionality guard: if the session was small, a short handoff passes this check — do not pad. In **chat mode** this gate applies to the chat output. In **note mode** this gate applies to the content written to the note file; the chat pointer is intentionally minimal regardless of session size and is exempt from the proportionality gate.

---

## Step 3 — Output

**Chat destination** (either register): Emit the handoff prompt directly to chat. Do not write any file. Do not use any tools.

**Note destination — skeleton register:** unchanged. Delegate composition and file mechanics to `note` (loaded via `loads: note` above) — do not mine, number, slug, `mkdir`, or `Write` yourself. Invoke `note` once this chat, supplying only hooks:

- **Destination directory** = `.ai-factory/handoffs/`
- **Template** = the skeleton from Step 2 above, passed **blank** — its placeholder descriptions are the mining lens `note` uses to distill the session. Do NOT pre-fill it: a filled-in skeleton would make `note`'s distillation a no-op.
- **Verbosity directive** = the proportionality policy from Step 2 ("Output length and granularity must track how much was actually done…") plus the self-check gate above, both applied to the note-file content before `note` writes it.
- **Slug** (`note`'s `$1` / topic derivation, not a named hook) = derived semantically from the session's subject matter — lowercase words joined by hyphens, specific to what was actually worked on. Do NOT use the literal word `handoff`.

`note` performs its own numbering, directory creation, and Write to `.ai-factory/handoffs/<NN>-<slug>.md`. Its own Step 4 report is **not** surfaced — once `note` completes, emit only the minimal paste-back pointer below.

**Note destination — narrative register:** the agent composes the prose itself (Step 2) and `Write`s it directly to `.ai-factory/handoffs/<NN>-<slug>.md` — **explicitly not** via `note`. `note` distils, and distillation flattens the exact causal thread the narrative exists to carry. Because there is no `note` call on this path, the agent owns the numbering mechanic `note` would otherwise handle:

- `<NN>` is a zero-padded **two-digit** sequence number (`01`, `02`, `03` …) — the same rule `note` uses for this directory. Scan `.ai-factory/handoffs/` (via `Bash(ls *)` or `Glob`) for files matching `[0-9][0-9]-*.md`; `<NN>` is the highest existing prefix + 1. If no numbered files exist yet, start at `01`.
- `<slug>` is derived semantically from the session's subject — lowercase words joined by hyphens, and never the literal word "handoff".
- `mkdir -p .ai-factory/handoffs/` first if it does not already exist, then `Write` the composed narrative to `.ai-factory/handoffs/<NN>-<slug>.md`.

Once the file is written, emit only the minimal paste-back pointer below — do not re-emit the full narrative in chat.

**Minimal paste-back pointer (both note-destination paths):** exactly one chat block, not the full handoff body re-emitted. The pointer must be paste-back-able (the user drops it into the next session to orient the fresh agent). It contains:

- The path of the written file (e.g. `.ai-factory/handoffs/03-auth-refactor.md`)
- The one-sentence frame (skeleton register: section 1 of the handoff; narrative register: the opening framing line of the prose)
- The next step (skeleton register: section 4 of the handoff; narrative register: the closing next-step sentence of the prose)
- Optionally: the count of work-units covered (e.g. "5 tasks covered") — skeleton register only

This pointer stays consistent with the self-check gate above ("the chat pointer is intentionally minimal … exempt from the proportionality gate") for both registers.

Example shape (adapt wording to the actual session):

> Handoff saved → `.ai-factory/handoffs/03-auth-refactor.md`
>
> **Frame:** We finished extracting the auth layer; the originating session's context isn't available here — trust these files, not memory.
> **Next:** Run the migration dry-run and confirm row counts match before applying.
>
> *Paste the path above into the next session to rehydrate.*
