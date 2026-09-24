# Plan: 58.4 — a request phrased as a handoff routes correctly on both sides, or on neither

## Context
A request meaning "continue this same architect past a break" can currently reach either the architect's own on-request memory snapshot or a `command-handoff` run, because neither file states the boundary between the two genres — `src/skills/agent-architect/SKILL.md` says which occasions the snapshot has but not that a handoff-phrased request still means it, and `src/commands/command-handoff.md` opens on destination mechanics with no word about the sibling genre. Each file gains exactly one addition stating the boundary from its own side, both pointing at `docs/paired-loop.md` § "How the memory begins, and how it survives" for the distinction itself rather than restating reader, subject, and lifetime.

Both additions are pinned word for word in `.ai-factory/specs/trickster77777/162-a-handoff-phrased-request-can-mean-the-snapshot.md` § "What must be true after". They are copied from there, never re-derived — a paraphrase is a defect, not a variant.

A routing boundary exists only once both sides state it: this task is verified whole or not at all, and landing one edit without the other leaves the repository no better than before. Treat the two edits as one deliverable.

Both targets are reached through symlinks that already exist (`active/skills/agent-architect` → `../../src/skills/agent-architect`, `active/commands/command-handoff.md` → `../../src/commands/command-handoff.md`). Editing the `src/` files is the whole job — there is no second copy to update and no symlink to create.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The edits

- [x] **Append the routing sentence to the two-occasions sentence**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the memory-snapshot paragraph opens with a sentence ending `— no other handoff has any reason to mention the buffer or the handle.` (around line 65–67 — locate it by matching that text, never by the number; note the sentence is hard-wrapped and the words "no" and "other" sit on different lines, so match on a fragment that does not span the break). Append the sentence given in the task spec's `## What must be true after`, so the passage reads:

  > The memory snapshot continuing this same architect has two occasions: before a compact, and whenever the user asks for one mid-session — no other handoff has any reason to mention the buffer or the handle. A request that means continuing this same head past a break reaches this capability even when it is phrased as asking for a handoff; a request meant for whoever comes next, on the project rather than on this conversation, is the different genre `command-handoff` writes, and does not reach here (`docs/paired-loop.md` § "How the memory begins, and how it survives" draws the line by reader, subject, and lifetime).

  The existing sentence stays word-identical — the appended sentence sits beside it, replacing nothing. The anchor phrase "no other handoff has any reason to mention the buffer or the handle" must survive verbatim; other artifacts' sweeps key on it.
  Keep the two inline references backticked exactly as quoted: `` `command-handoff` `` (the genre's carrier, named as the skill it is) and `` `docs/paired-loop.md` `` followed by the section named in quotes — the file already uses this quoted-heading style for cross-references, and a line number here would be a defect.
  Hard-wrap the appended sentence to the width the paragraph already uses (its lines run 63–75 characters; the surrounding body sits at roughly 72). The wrap points are the implementer's own — the spec pins the words and their order, never the line breaks.
  Nothing else in this paragraph changes. The sentences following it — "The on-request one is the architect's own capability…", and the digest/delegation sentence ending "only the head that held it can write what happened there." — are 58.1's and 58.2's landed work and stay word-identical. The file's frontmatter, including its `description:` field, is untouched.

- [x] **Insert the sibling-genre paragraph into the handoff command**
  Files: `src/commands/command-handoff.md`
  Insert one new paragraph between the opening body paragraph (the one beginning `A handoff always lives in` — currently line 14, a single unwrapped line) and the `---` that follows it, separated by a blank line on each side, so the top of the file reads:

  > A handoff always lives in `<root>/.ai-factory/handoffs/`. …never `notes/`, never the bare argument path.
  >
  > A request meant to continue the same architect's own memory across a break is a different genre — the architect's own on-request snapshot, not this command — and never reaches here, however it is phrased; `docs/paired-loop.md` § "How the memory begins, and how it survives" draws that line by reader, subject, and lifetime.
  >
  > ---

  Write the new paragraph as **one unwrapped line**: this file's prose is not hard-wrapped (its paragraphs are single long lines of 140–575 characters), and wrapping this one would break the folder's settled style. This is the opposite convention from the first task's file — do not carry the wrapping habit across.
  The paragraph names the *genre* and the document, deliberately not `agent-architect` or any other skill file path: the pointer is to the documented genre, not to a specific carrier. Do not "improve" it by adding the skill name.
  The paragraph does not restate what reader, subject, or lifetime the two genres have — `docs/paired-loop.md` holds that, and the pointer is the whole mechanism. Do not expand it.
  Nothing else in the file changes: the frontmatter (including `description:`, `allowed-tools:`, `loads:`), the opening paragraph, Step 1, Step 2, Step 3, and the "Holding a handoff" section all stay byte-identical. In particular, add no thickness or verbosity policy — Step 1 already states its own ("Every handoff is verbose…") and this task does not touch it.

### Verification

- [x] **Compare both additions against the spec's pinned wording, word for word** (depends on both edits)
  Files: none — read-only check
  Read both additions back off disk and set each beside its block in `.ai-factory/specs/trickster77777/162-…md` § "What must be true after". For the `agent-architect` sentence, compare **words and order only, newlines collapsed to spaces** — that paragraph is hard-wrapped and was re-wrapped by this task, so the comparison is never of lines. For the `command-handoff` paragraph, compare the line as written, since it is unwrapped on both sides.
  This is the positive half of verification and the sweeps below cannot stand in for it: they prove survival and scope, both of which a paraphrase of either addition would also satisfy. Check, in order:
  - **The `agent-architect` sentence** is present in full, ending "draws the line by reader, subject, and lifetime).", with `command-handoff` and `docs/paired-loop.md` backticked and the section title in double quotes. The spec's blockquote is the authority on the words; the file is the authority on the markup.
  - **The `command-handoff` paragraph** is present in full, ending "draws that line by reader, subject, and lifetime.", with `docs/paired-loop.md` backticked, and sits between the opening paragraph and the first `---` with a blank line on each side.
  - **Neither addition restates the distinction** — check that no sentence added by this task defines who the reader is, what the subject is, or when the lifetime ends; both must point rather than explain.
  - **Neither anchor was disturbed**: `agent-architect`'s "…no other handoff has any reason to mention the buffer or the handle." and `command-handoff`'s "A handoff always lives in…" opening paragraph read exactly as they did before this task, only their line breaks possibly differing in the first.
  A mismatch in the first two is a defect in this task's own edits — fix it against the spec. A mismatch in the last is a neighbour that was disturbed and must be restored.

- [x] **Confirm the boundary is stated on both sides and nothing downstream re-opens it** (depends on the comparison above)
  Files: none — read-only check
  The spec's own rule for this task: *a routing boundary exists only once both sides state it.* Confirm both, in one pass — a check of one file alone is not a check of this task.
  Then read the rest of `src/commands/command-handoff.md` — Step 1's lens-shaping prose, Step 2's `note` hooks, Step 3's paste-back pointer, and "Holding a handoff" — and confirm none of them states or implies that every invocation of this command is handled regardless of what request triggered it, and none re-opens or contradicts the new paragraph. The boundary is stated once, at the top. Report anything that contradicts it rather than editing it; the spec's blast radius states no such sentence exists.
  Confirm by reading (not by diff alone) that the untouched spans really are untouched: `command-handoff.md`'s Steps 1–3 and "Holding a handoff", and every sentence of `agent-architect`'s memory-snapshot paragraph other than the one this task appended to.

- [x] **Re-run the spec's two sweeps and classify every hit by rule** (depends on the comparison above)
  Files: none — read-only check
  ```
  grep -rln "other handoff has any reason to mention the buffer or the handle" src/ docs/ .ai-factory/
  grep -rln "A handoff always lives in" src/ docs/ .ai-factory/
  ```
  The first pattern deliberately drops the leading "no": in the file the sentence wraps between "no" and "other", so a single-line pattern including it silently matches nothing. Do not "fix" the pattern by restoring the word.
  **The two paths that must still appear are `src/skills/agent-architect/SKILL.md` (first sweep) and `src/commands/command-handoff.md` (second)** — both edits add beside the anchors rather than replacing them, so a disappearance means an anchor was rewritten and must be restored.
  Everything else returned is a hit by design and **the count is not the test** — it grows with every artifact this task produces. Judge each returned path by the rule, never by a list: *does this file quote the passage as ground truth for a standing claim about the present, and does it assert a competing boundary?*
  - This task's own spec (`162-…md`) quotes both anchors permanently under `## What is true now`, as history — a spec describes a moment, not the present. Correct as it is.
  - The roadmap's contract line for this task states the problem it describes, permanently. Correct as it is.
  - This plan file, and any plan-review or review artifact of this task, quote the passages and the sweep commands self-referentially rather than asserting them as live claims. Runtime working communication, not findings.
  - A path that is none of the above **and** asserts a competing boundary: stop and report it, do not edit it. The spec's blast radius states no such file exists.
  Do not edit any matching artifact to make the output tidier.
