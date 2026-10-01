## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/14-62-2-the-architect-lives-in-its-folder.md`
**Task:** 62.2 in `.ai-factory/roadmaps/trickster77777.md`. Spec: `.ai-factory/specs/trickster77777/175-the-architect-lives-in-its-folder.md`. Governing spec: `docs/paired-loop.md` § "Where the memory lives"
**Files targeted:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture:** OK. The skill keeps pointing at `architect-editor-engine` for the folder's path and numbering and does not restate them, which fits the mechanism/policy split. 62.1 is `[x]`. The engine's § "The architect's buffer" defines `.ai-factory/architects/<NN>/` with `buffer.md`, `address.md` (`session-id:` / `session-name:`, read by a peer and never the buffer), and `<NN>-<slug>.md` snapshots numbered inside the folder. Each pointer the plan writes ("the path and numbering the engine defines", "numbered as `architect-editor-engine` defines", "what `address.md` holds and who reads it") therefore resolves to text that exists.
- **Rules:** WARN. There is no `.ai-factory/RULES.md`, so nothing could be checked against it.
- **Roadmap:** OK. The plan covers every item on the 62.2 contract line: founding the folder, seeding `buffer.md`, writing `address.md`, the nonce probe, `ListAgents` for the session name and its `allowed-tools` entry, rewriting on every start and rehydration, writing snapshots into the folder, the recovery passage, and § "Your buffer is shared; you alone write it". The line is sequenced after 62.1, which has landed.
- **Governing spec:** OK. `docs/paired-loop.md` § "Where the memory lives" says a new head "founds its own folder, seeds its buffer, and writes its keeper", that the head "rewrites it on every start", and that "the head is the memory's only writer". The planned text holds to all three.

### Spec conformance and anchors

I checked every quoted target against the spec's § "What must be true after" and each matches word for word:
- the founding tail;
- the `address.md` paragraph's required content (nonce probe over top-level `.jsonl` files, the letter/digit `<project-key>` definition, the not-exactly-one fallback, and the bare name taken from `ListAgents`'s first line);
- the snapshot clause;
- the recovery clause;
- the closing sentence of the buffer section;
- the frontmatter line.

I also checked every anchor against the current file, and each occurs exactly once:
- `allowed-tools:` line 13;
- the founding span running from "no such pointer means you are a new architect and create your own buffer first" through "…never reread for a buffer that is merely resumed.";
- "Either occasion records your buffer's path (defined in `architect-editor-engine`)";
- "you are a new architect and create your own buffer at the path and numbering";
- "The buffer's path and numbering, the rule that the hand reads it in full…";
- the tail "It is the one file you edit directly: you are its only writer.".

The new paragraph's insertion point is immediately before the paragraph that opens "Until the first channel-message arrives", which is where the spec places it.

The Critical Issue from review 1 has been resolved. The plan now replaces the tail "It is the one file you edit directly: you are its only writer." with pinned text: "The buffer, `address.md` and your snapshots — your own folder — are the only files you edit directly: you are their only writer." That tail is outside the span the spec pins, because the spec pins only up to "loaded at birth". The new text agrees with three other statements:
- the head writes `address.md` itself at a founding, before any editor exists;
- the snapshot is never delegated to the editor;
- the skill's opening paragraph, "You never touch the shared artifacts — roadmap, specs, code, docs — with your own hands", which does not list the folder.

Other ground-truth checks:
- `Bash` is already in `allowed-tools`, so the nonce probe needs no new tool.
- Both `create your own buffer` hits (lines 43 and 137) fall inside spans this plan rewrites.
- `AskUserQuestion Agent SendMessage` still matches only the updated frontmatter line, so the final step's sweep expectation is correct.
- No step renames a `##` heading, so the seed's citation of "Spawn once, message thereafter" still resolves.

### Critical Issues

None.

### Positive Notes

- Every changed sentence is pinned verbatim from the spec, and every anchor is quoted from the file, so the implementer has nothing to compose or locate by guesswork.
- The plan explains why the out-of-pin tail rewrite is inside the task's boundary, and pins its exact wording so the implementer does not have to invent it.
- The scope for 63.1 is fenced correctly. The plan leaves untouched the `meta.json` fallback, the separators-only `<project-key>` definition, the re-pointing block, and § "On every invocation", and it keeps the editor-liveness `ListAgents` sentence separate from the new session-name reading.
- The final step re-runs the spec's sweeps and holds the neighbouring files (`buffer-seed.md`, `command-handoff`, `roadmap-prune`, `docs/`, `CLAUDE.md`) untouched.

## Deferred observations

- Affects: 63.1 (`.ai-factory/roadmaps/trickster77777.md`, "the architect comes back on a bare invocation"). After 62.2 lands, `agent-architect/SKILL.md` will define `<project-key>` in two different ways:
  - The new probe paragraph says every character that is not a letter or a digit is replaced by a hyphen. This matches the transcript directory Claude Code actually uses.
  - The handle-recovery fallback says only separators are replaced. That gives the wrong directory for any path containing `_` or `.`.

  The spec assigns removal of that fallback to 63.1. If 63.1 keeps any part of it, it should adopt or point at the probe paragraph's definition. [dismissed]

PLAN_REVIEW_PASS
