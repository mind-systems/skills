---
description: >-
  Mine the live session and emit a dense, self-contained handoff prompt that
  lets the next agent (or yourself after /compact) rehydrate instantly.
  Run this BEFORE /compact — while context is still full. After compact there
  is nothing left to mine. Optionally persist the handoff as a durable note
  (pass "note" / "ноут" / "давай ноут" / "с ноутом" as the argument).
argument-hint: "[note]"
allowed-tools: Write Bash(ls *)
---

Read `$ARGUMENTS`. Determine the mode:

- **Note mode** — triggered when `$ARGUMENTS` contains any of: `note`, `ноут`, `давай ноут`, `с ноутом` (case-insensitive, substring match).
- **Chat mode** — everything else, including empty arguments.

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

Use the skeleton below exactly — do not change section names or order. Omit a section only if it is genuinely empty for this session (no invented content). Optional sections (7–11) appear only when the session produced material for them.

**Output length and granularity must track how much was actually done.** A session that touched many work-units (phases, modules, files, tasks) must enumerate each one individually with its specific state and the specific thing to re-check — never collapse a whole subsystem to summary bullets. A small session still yields a short handoff. Proportional, not maximal — a trivial session padded to migration-guide length is itself a failure.

~~~
# Handoff — <semantic slug derived from the session subject>

## 1. Frame
<one sentence: where we are in the project> — the chat is compacted but the
knowledge is durable in files; rehydrate from them, don't trust memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- `<path>` — <one line: what question this file answers> ← lead with the single best entry doc
- ...

### Read on demand
- `<path>` — <one line: what it covers>
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

Populate every field from what you actually observed in the session — no placeholders, no invented content.

Before emitting, apply this self-check to your draft: *Could a fresh agent, with only this note, (a) execute the next step, (b) avoid every mistake in the error log, and (c) for each subsystem touched, know what it became and what to re-check?* If a whole subsystem collapsed to one bullet, or the recurring contracts aren't listed — expand before emitting. Proportionality guard: if the session was small, a short handoff passes this check — do not pad. In **chat mode** this gate applies to the chat output. In **note mode** this gate applies to the content written to the note file; the chat pointer is intentionally minimal regardless of session size and is exempt from the proportionality gate.

---

## Step 3 — Output

**Chat mode:** Emit the handoff prompt directly to chat. Do not write any file. Do not use any tools.

**Note mode:** Write the full handoff to a file, then emit only a short pointer to chat.

1. Persist the handoff prompt as a note file — write it yourself using the Write tool, do **not** route through `/note` (that reshapes into a different template):

   a. Use Bash `ls .ai-factory/handoffs/` to list existing `[0-9][0-9]-*.md` files and find the highest `<NN>` prefix. The new file gets `<NN> + 1`, zero-padded to two digits. If the directory is empty or does not exist (a fresh project — `ls` may error with "No such file or directory"), treat it as no handoffs yet and start at `01`; the Write in step (c) creates the parent directory.

   b. Derive `<slug>` **semantically** from the session's subject matter — lowercase words joined by hyphens, specific to what was actually worked on. Do NOT use the literal word `handoff` as the slug.

   c. Write to `.ai-factory/handoffs/<NN>-<slug>.md` using the Write tool. The file content is the handoff prompt verbatim — no wrapper, no extra header, no reformatting.

2. Emit to chat **only a short pointer** — do **not** re-emit the full handoff body. The pointer must be paste-back-able (the user drops it into the next session to orient the fresh agent). It contains:

   - The path of the written file (e.g. `.ai-factory/handoffs/03-auth-refactor.md`)
   - The one-sentence frame from section 1 of the handoff
   - The next step from section 4 of the handoff
   - Optionally: the count of work-units covered (e.g. "5 tasks covered")

   Example shape (adapt wording to the actual session):

   > Handoff saved → `.ai-factory/handoffs/03-auth-refactor.md`
   >
   > **Frame:** We finished extracting the auth layer; chat compacted, knowledge is in files.
   > **Next:** Run the migration dry-run and confirm row counts match before applying.
   >
   > *Paste the path above into the next session to rehydrate.*
