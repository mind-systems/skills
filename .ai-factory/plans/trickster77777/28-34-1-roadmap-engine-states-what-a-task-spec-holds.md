# Plan: 34.1 — `roadmap-engine` states what a task spec holds

## Context
`roadmap-engine` § "The two-tier artifact" gives the task spec a path, a numbering scheme, a `Spec:` tag and the phrase "holds the full implementation detail" — never what that detail is, so the shape comes from whoever writes it. Two edits in one file: the section gains one paragraph naming the three parts, and the contract-line bullet's four-part enumeration is brought into line with it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### State the shape at its home

- [x] **§ "The two-tier artifact" gains the three-part paragraph**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Insert one new paragraph immediately after the **Why two tiers:** paragraph (currently lines 42–44, ending `is guidance, not a hard clamp.`) and before the `**Never write a full spec inline in the roadmap**` paragraph — a blank line on each side. It names the three parts and nothing else; write it as prose, not a bulleted list (both the contract line and the task spec say "one paragraph"), and open it with a bold lead-in, matching the section's existing habit of bold-leading its paragraphs so the fact is addressable by name per `docs/reference-by-name.md`. Pinned text:

  ```
  **What a task spec holds:** three parts and nothing else — *what is true now*, read
  from the code with exact values, so the implementer does not re-derive it; *what must
  be true after*, in the code's own terms: which file, which text, which value; and
  *what breaks on contact*, enumerated rather than hedged.
  ```

  Hard-wrap the paragraph at ≤90 columns as the pinned text already is — the section's prose lines run 59–90 columns and no line in it is left unwrapped. Nothing else in the section moves: the path/numbering/`Spec:`-tag paragraph, the `note`-format paragraph, the **Why two tiers:** paragraph and the "Never write a full spec inline" paragraph all keep their current text and line breaks, including the existing phrase "the task spec holds the full implementation detail" on line 43 — the new paragraph says what that detail is, it does not replace the sentence.

- [x] **The contract-line bullet's enumeration matches the paragraph** (depends on the three-part paragraph)
  Files: `src/skills/roadmap-engine/SKILL.md`
  In **Rules for writing a contract line:**, the last bullet (line 105) reads `- Full current-state / target / guards / verify detail lives in the task spec, not the contract line`. Rewrite that one line to `- Full current-state / target / blast-radius detail lives in the task spec, not the contract line`. Verified at plan time, string-level only: the literal enumeration `current-state / target / guards / verify` occurs exactly once in the repository outside `.ai-factory/`, at this line. That is a claim about the string, not about the concept — one direct caller restates the same four parts in prose: `src/skills/roadmap-decompose/SKILL.md` § "(d) Extra update action — 'Decompose existing'" describes a full spec as "(what exists today, the exact change, files/types/methods to touch, guards, how to verify)". That restatement is known and deliberately out of scope here — this task's contract line names only `roadmap-engine`, and no task in Phase 34 owns `roadmap-decompose`; it is raised as a deferred observation for a follow-up, not repaired in this landing. So the family is **not** reconciled when this task lands: the engine will say three parts while that caller still asks for guards and how to verify. The other six bullets in the list are untouched, in particular the third (`Name guard conditions ("do not touch X", "skip Y") only for real pitfalls…`) — it is a rule about the contract line's own content, not the dropped enumeration, and the word `guards` leaving this bullet is not a sweep of the word from the file.

## Guards

- **No skill gains a template.** `note`'s template hook stays unset for task specs — do not add a template argument at the `note` invocation in the `note`-format paragraph, and do not edit `src/skills/note/SKILL.md` (its Key Findings / Details / Open Questions default stays the standalone-note default).
- **Task specs already on disk are not rewritten.** Nothing under `.ai-factory/specs/` is touched; the paragraph states the shape for what is written next.
- **Siblings in this phase are out of scope.** `src/commands/command-pin-gaps.md` naming the three parts is task 34.2; `docs/reserved-words.md` dropping "the implementation-tier work-order" from its task-spec entry is task 34.4. Do not anticipate either, and do not restate the new paragraph anywhere outside `roadmap-engine` — the engine is its one home.
- **Do not repair `roadmap-decompose`.** Its hook (d) parenthetical contradicts the new paragraph and is a real defect, but it is outside this task's file boundary; leaving it standing is the deliberate outcome of this landing, not an oversight to fix in passing.
- **Diff scope:** `git diff HEAD --stat` lists `src/skills/roadmap-engine/SKILL.md` and nothing else.
