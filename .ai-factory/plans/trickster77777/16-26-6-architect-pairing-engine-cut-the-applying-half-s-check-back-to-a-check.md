# Plan: 26.6 — architect-pairing-engine: cut the applying half's check back to a check

## Context
Task 26.5 added the applying half's work-order check plus three powers past what was asked — a correction licence, the sentence reconciling that licence with `:52`'s "never to its own judgment", and a round-closing clause. This task replaces that whole paragraph with the check and the report alone, resolving the internal contradiction and mooting 26.5's open deferred observation about the deciding half's unwritten mirror.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Cut the paragraph back

- [x] **Replace the applying-half check paragraph**
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Replace lines `58-70` — the whole paragraph bounded by the blank lines at `:57` and `:71` — word-for-word with the text pinned in the task spec (`.ai-factory/specs/trickster77777/97-applying-half-check-cut-back.md` § "The change"):

  ```
  Applying exactly is not obeying blindly. Read the arriving work-order
  against the files before you touch them: where it is underspecified,
  contradicts itself, or would break something it never named, report that
  back instead of guessing your way through it, and name in your report every
  decision the work-order left unpinned. The deciding half verifies what
  landed against the files, so an unflagged judgment call is the one thing
  its check cannot see.
  ```

  Reproduce the pinned wrapping exactly; do not re-wrap, re-word, or re-order it. What disappears with the paragraph: the correction licence (`:61-64`), the reconciliation sentence (`:65-67`), and the round-closing clause (`:67-68`). Nothing else in the file changes.

  Guards (all verified untouched by the diff): the `description:` frontmatter block — its applying clause already carries the check alone; `## The deciding half` in full; the load-only-when-assigned rule (`:27-30`); the originates-no-edit paragraph (`:52-56`) and the supersession paragraph (`:72-75`) of `## The applying half`. No pointer is added to `src/agents/editor.md` — the correction discipline stays where it lives, in the editor's own definition, neither restated nor referenced here. No new channel-message format, no third mode, no round-closing rule.

### Verify

- [x] **Check the result against the spec's verification list** (depends on Replace the applying-half check paragraph)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Read `## The applying half` and confirm it holds exactly three paragraphs — originates-no-edit, the replacement, the supersession note — and that the replacement is byte-identical to the pinned text.

  Run the spec's greps against `src/skills/architect-pairing-engine/SKILL.md`:
  - `grep -c "Correcting an order while executing it"` → 0
  - `grep -c "closes the round"` → 0
  - `grep -c "Applying exactly is not obeying blindly"` → 1

  Caveat on one spec check: `grep -c "correct it inside the change"` reads 0 on the *pre-change* file too, because the phrase wraps across `:62-63`. Use a wrap-tolerant form instead — e.g. `grep -c "correct$"` → 0, or `grep -Pzo "correct\s+it inside the change"` → no match — so the check actually witnesses the removal.

  Then `git diff --stat`: exactly one file under `src/` changed, and `git diff` must not show the `description:` block.
