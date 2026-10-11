## Code Review Summary

**Files Reviewed:** 1 plan, its task spec (`.ai-factory/specs/trickster77777/0238-what-a-snapshot-carries-lives-in-the-engine.md`), contract line 78.1 and the Phase 78 header in `.ai-factory/roadmaps/trickster77777.md`, the governing spec `docs/paired-loop.md` (§ "How the memory begins, and how it survives"), and both target files: `src/skills/architect-editor-engine/SKILL.md` and `src/skills/agent-architect/SKILL.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — OK.** The change moves a genre from a lens (`agent-architect`) into its engine (`architect-editor-engine`). Both of the engine's callers (`agent-architect` and `src/agents/editor.md`) load it, so the genre ends up with a single home where both halves of the pair can read it. This matches the mechanism-versus-policy split, and 78.2 and 78.4 rely on it because the hand will also write snapshots.
- **Rules — WARN (missing optional file).** There is no `.ai-factory/RULES.md`. The conventions in the project CLAUDE.md are met: no engine content is inlined into the lens, the lens points to the engine instead of restating it, and spec text marked verbatim is copied as written.
- **Roadmap — OK.** The plan's heading matches contract line 78.1 in the named roadmap `roadmaps/trickster77777.md`. The task sits at the seam: 76.x is `[x]` and 78.1 is the first `[ ]`. The contract line's `Spec:` tag resolves to the spec the plan copies from. The phase's governing spec is `docs/paired-loop.md`. The text the spec adds to the genre (how the knowledge was got, the shape of what was studied when its source is out of reach, pointers to the detail, and "a conclusion kept without its method cannot be re-checked or redone") matches § "How the memory begins, and how it survives" of that doc. The plan correctly sets `Docs: no`, because the doc is already ahead of the code.

### Verification against the files

- **Engine, § "The architect's buffer":** I checked the insertion point the plan names. The first paragraph defines the folder, `buffer.md`, `address.md`, the snapshot files and their numbering, and it ends with "…the architect's own skill points here rather than restating them." The paragraph after it opens with "The head is the memory's only writer." The section is written one paragraph per unwrapped line, as the plan says. The spec says only "in § 'The architect's buffer', a paragraph reads" and does not fix a position. The plan places the genre beside the definition of the snapshot files, which is a sound choice and conflicts with nothing in the spec.
- **Engine frontmatter:** The `description:` names the folder ("its buffer, its snapshots and its address file, with their path and numbering") and does not describe a genre. That agrees with the spec's finding, so leaving the description untouched is correct.
- **`agent-architect`, § "Spawn once, message thereafter":** The paragraph that opens "The memory snapshot continuing this same architect has two occasions" contains the "Either occasion writes the snapshot into your own folder —" tail exactly as the plan describes, including the odd line break after "folder —". The sentences before it ("…no command is invoked and no template is consulted.") are the ones the spec says must stay as they are. Everything from "Either occasion" to the end of the paragraph is the replaced span, and it holds the three sentences that leave this skill ("What a snapshot carries is the volatile residue…", "It is thick by default…", "Each new snapshot supersedes the last by name…").
- **Sweep, run against the current tree:** each of the three greps hits only the target paragraph in `agent-architect` (`volatile residue`, `supersedes the last` and `thick by default`). No other doc, `CLAUDE.md` text or skill appears. This confirms the spec's finding.
- **Other references stay true:** I grepped for `snapshot` across `src/agents/editor.md`, `src/commands/` and `docs/`:
  - `command-handoff` only separates its own genre from the architect's snapshot.
  - `editor.md` names no snapshot.
  - `agent-architect` § "On every invocation" only reads the latest snapshot.
  - § "Relay on the marker…" points back to "Spawn once, message thereafter" for the editor ban, and the after-text keeps that ban ("never delegated to the editor to compose").

  None of these states what a snapshot carries, so none needs to change.

### Critical Issues

None.

### Positive Notes

- The plan copies the after-texts from the spec rather than restating them, so the wording has one home, as "One home per fact" requires.
- It gives exact opening and closing anchors for both edits and the boundary of the span left unchanged. This leaves the implementer no room to guess where a paragraph starts or ends.
- It names each file's style (unwrapped paragraphs in the engine, ~72-char hard wrap in the lens) and limits re-wrapping to the replaced tail, which keeps the diff minimal.
- The sweep is judged by the spec's rule ("a pointer, not a restatement"), so the hit left in the lens is classified correctly instead of being treated as leftover text.
- The dependency order (engine first, then the lens pointer, then the sweep) keeps the pointer from ever pointing at a genre that does not exist yet.

PLAN_REVIEW_PASS
