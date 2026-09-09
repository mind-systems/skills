# Plan: 34.2 — `command-pin-gaps` closes holes and writes no checks

## Context
`src/commands/command-pin-gaps.md` carries three finding classes that already are the three parts a task spec holds (34.1 landed that shape in `roadmap-engine`), but the command never says so, and its mandate "Close all of it now" (line 22) has no stopping rule — so a pass closes past its own classes and writes verification bullets. Three edits in one file: two new paragraphs at one seam naming the shape and the register the pass never writes, and one clause of the value-hole repair replaced so a `file:line` citation stops entering the spec.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Name the shape and the stopping rule

- [x] **The seam before `**Value holes:**` gains the shape paragraph**
  Files: `src/commands/command-pin-gaps.md`
  Insert one new paragraph after the "A task spec that repeats a paragraph from a document…" paragraph (line 34, ending `unlike the two surfaces it sits between.`) and before the `**Value holes:**` paragraph (line 36) — a blank line on each side. It opens with a bold lead-in, matching the file's habit of bold-leading every addressable paragraph (`**Value holes:**`, `**Meaning holes:**`, `**Blast-radius holes:**`, `**scan mode**`) so the fact is addressable by name — and it adds **no heading**: the file carries none, and `docs/reference-by-name.md` cites that as the reason its classes are cited by name. Pinned text, as one unwrapped line — every body paragraph from line 20 onward is a single long line (120–887 columns), and that is the stretch this insertion sits in; the file's one hard-wrapped body paragraph is the opening "Ensure `roadmap-engine` is loaded once this chat…" at lines 17–18, which is not the model here. Do not hard-wrap:

  ```
  **The shape it repairs toward:** a task spec holds three parts — *what is true now*, *what must be true after*, *what breaks on contact* — defined in `roadmap-engine`'s "What a task spec holds" paragraph and not restated here; each hole class supplies exactly one of them. A class is named by the part its repair supplies, never by the part that went unread: a value hole is closed by pinning *what is true now*, a meaning hole by deciding *what must be true after* — which is why an existing shape nobody looked at is a meaning hole, the fit it must satisfy being what is undecided — and a blast-radius hole by enumerating *what breaks on contact*. The three classes are therefore the whole of what "all of it" means above: with none of them left open the spec is whole and the pass stops.
  ```

  The "named by the part its repair supplies" clause is load-bearing and must not be dropped to shorten the paragraph: line 32 (`an existing shape nobody looked at, or work already half-done, is a meaning hole`) and the last two members of line 38's enumeration route by repair, not by which part went unread, and a bare identity mapping would contradict them six lines apart. The pinned text keeps line 32's routing correct and names the principle behind it; line 32 and line 38 are themselves untouched.

  The command already declares `loads: roadmap-engine`, so naming the engine's paragraph is a pointer to the shape's one home, not a second home — do not paraphrase the engine's elaborations ("read from the code with exact values", "in the code's own terms: which file, which text, which value", "enumerated rather than hedged") into this file.

- [x] **A second paragraph states the register the pass never writes** (depends on the shape paragraph)
  Files: `src/commands/command-pin-gaps.md`
  Immediately after the paragraph above, still before `**Value holes:**`, insert a second bold-led paragraph as one unwrapped line. Pinned text:

  ```
  **What the pass never writes:** it pins values and enumerates breakage, and it never authors a verification check — no step, command, or bullet whose only job is to confirm the instruction was carried out. Such a check can only fail where the instruction was ignored, and by `test-philosophy`'s discriminator that is a loud failure, which is not written. A surface that fails silently still owes a test, routed to its owner as below.
  ```

  This names `test-philosophy` the way line 42 already names it — as a discriminator and an owner, never a load. Do **not** add `test-philosophy` to the frontmatter `loads:` field, and do not touch line 42's sentence ("A task that cannot be planned coherently belongs to `roadmap-decompose`… and loads none of the four"): its "does not author tests" is ownership routing, this paragraph is the artifact register, and both stand.

### Pin the value, not the line number

- [x] **The value-hole repair names its source instead of citing a position**
  Files: `src/commands/command-pin-gaps.md`
  In the `**Value holes:**` paragraph (line 36), the repair clause currently reads `Repair: read the code/proto and pin the **exact** value with a `file:line` citation — never invent.` Replace that clause with:

  ```
  Repair: read the code/proto and pin the **exact** value, naming its source as the file and the name of the thing inside it that holds the value — a symbol, a heading, a bold lead-in — never a line number, because the spec outlives the numbering it was written against; never invent.
  ```

  The enumeration of what a value hole *is* (`TODO/TBD/«решим по ходу»`, unpinned symbols, magic numbers, a missing file or call site) is untouched — only the `Repair:` clause changes. Do not cite `docs/reference-by-name.md` in the command: no skill or command under `src/` references a `docs/*.md` file of this repository, and this command runs inside arbitrary projects where that path does not exist — the rule is stated inline and the doc stays reachable from `CLAUDE.md`, as it is today.

## Guards

- **The two other `file:line` occurrences stay.** Line 26 (`Each such behavior either ends at a `file:line` landing in the code or becomes a finding`) describes where the walk lands while reasoning, not a citation written into an artifact. Line 44's scan-mode report format (`[file:line|spec-location] → value|meaning|blast-radius → what's missing → fix`) is printed to chat and thrown away — the exemption `docs/reference-by-name.md` grants a work-order. Neither is a sweep target; leaving them is the deliberate outcome of this landing.
- **No new hole class, none removed.** The three classes, their contents, both modes, and the owner routing to `roadmap-decompose`, `roadmap-decompose-skeleton`, `aif-docs` and `test-philosophy` all survive unchanged.
- **Frontmatter untouched.** The `description:`, `argument-hint:`, `allowed-tools:` and `loads:` fields keep their current text — the three classes it advertises are unchanged, and no load edge is added.
- **The mandate line stays.** Line 22 ("Any question that would need an answer *during implementation*… Close all of it now.") is not rewritten; the new shape paragraph is what bounds "all of it".
- **Siblings in this phase are out of scope.** 34.3 (`agent-architect` / `architect-pairing-engine` / `editor.md` dropping the self-verify component) and 34.4 (`docs/reserved-words.md` dropping "the implementation-tier work-order") are separate tasks — do not anticipate either.
- **Docs are not updated.** `docs/sakshi-harness/skill-cycle.md` and `docs/reference-by-name.md` describe this command and stay correct after the change; neither is edited here.
- **Diff scope:** `git diff HEAD --stat` lists `src/commands/command-pin-gaps.md` and nothing else. `active/commands/command-pin-gaps.md` is a symlink to it — never write through the symlink path or replace it with a copy.
