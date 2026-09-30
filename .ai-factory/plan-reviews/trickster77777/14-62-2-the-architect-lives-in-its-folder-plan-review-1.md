## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/14-62-2-the-architect-lives-in-its-folder.md`
**Task:** 62.2 in `.ai-factory/roadmaps/trickster77777.md`. Spec: `.ai-factory/specs/trickster77777/175-the-architect-lives-in-its-folder.md`. Governing spec: `docs/paired-loop.md` § "Where the memory lives"
**Files targeted:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟡 Medium. One sentence the plan keeps would contradict the new text.

### Context Gates

- **Architecture:** OK. The skill still points at `architect-editor-engine` for the folder's path and numbering instead of restating them, which matches the mechanism/policy split. 62.1 has landed (commit `1a25ea9`), and the engine's § "The architect's buffer" defines `.ai-factory/architects/<NN>/` with `buffer.md`, `address.md` (`session-id:` / `session-name:`) and `<NN>-<slug>.md` snapshots. The pointers the plan writes will therefore resolve.
- **Rules:** WARN. There is no `.ai-factory/RULES.md`, so nothing could be checked against it.
- **Roadmap:** OK. The plan covers every item in the 62.2 contract line: founding, seeding `buffer.md`, `address.md`, the nonce probe, the `ListAgents` session name and its `allowed-tools` entry, rewriting on every start and rehydration, the snapshot destination, the recovery passage, and § "Your buffer is shared; you alone write it". The line is sequenced after 62.1, which is `[x]`.
- **Spec conformance:** OK apart from the finding below. I checked each quoted target sentence in the plan against the spec's § "What must be true after" and they match word for word. I checked each anchor ("no such pointer means you are a new architect and create your own buffer first", "Either occasion records your buffer's path (defined in `architect-editor-engine`)", "you are a new architect and create your own buffer at the path and numbering", "The buffer's path and numbering, the rule that the hand reads it in full…", and the `allowed-tools` line) against the current file, and each exists exactly once.
- **Ground-truth checks:** `ListAgents` currently opens with `This session is skills-4e [c0eb43] — …`, which is the form the spec's probe paragraph parses. This session's transcript directory is `-Users-max-projects-sakshi-skills`, which fits the "every non-alphanumeric → hyphen" definition. I re-ran the spec's sweeps: `create your own buffer` hits only lines in the founding and recovery passages; `AskUserQuestion Agent SendMessage` hits only the frontmatter line; `project-key` hits only the recovery fallback; `Spawn once` hits the seed and the skill's own internal cross-references, and none of the plan's steps renames a heading.

### Critical Issues

1. **The plan keeps "It is the one file you edit directly", which the new text makes false.**
   *Where:* the plan's task "§ 'Your buffer is shared; you alone write it': closing sentence points at the folder", which says: *"the tail '— this section points there and restates none of them. It is the one file you edit directly: you are its only writer.' stays."*
   *Why it is wrong:* after this task the head writes `address.md` with its own hands. At a founding it does so before any editor exists ("…and write `address.md`. Either way the buffer exists before any editor does."). The new paragraph also has the head rewrite that file on every start and rehydration ("Write both into `address.md`… replacing what was there"). The snapshot clause now says the head "writes the snapshot into your own folder", and the snapshot paragraph already forbids delegating a snapshot to the editor. So the head directly edits at least three kinds of file in its folder: the buffer, `address.md` and its snapshots. Yet the closing sentence of the very paragraph this plan edits would still say the buffer is *the one* file the architect edits directly. A later reader would get two answers from the same skill about which files the head may write, which is the kind of stale-on-contact statement the spec's § "What breaks on contact" rule covers ("any file that states where a new architect's memory is founded, where a snapshot is written… reads stale once these passages change").
   *Fix, inside the task's boundary:* the spec pins the sentence only up to "loaded at birth", so the plan is free to rewrite the tail, and it should. For example:
   > "— this section points there and restates none of them. It and the rest of your own folder — `address.md` and your snapshots — are the only files you edit directly: you are their only writer."

   Any wording works if it keeps the "only writer" rule for the buffer (from `docs/paired-loop.md`: "The head is the memory's only writer") and stops claiming the buffer is the head's only direct write. Add the new tail to the plan as verbatim target text so the implementer does not invent it.

### Positive Notes

- Every changed sentence is pinned verbatim from the spec, and each anchor is quoted from the current file, so the implementer has nothing to guess about text or position.
- The founding step replaces a correctly bounded span ("no such pointer…" through "…merely resumed."), which absorbs the old separate seeding sentence and moves "Either way the buffer exists before any editor does." to the end of the paragraph. This matches the spec's quoted paragraph exactly.
- The plan deliberately leaves the handle-recovery fallback (the `meta.json` path, the separators-only `<project-key>` definition, the re-pointing) and § "On every invocation" for 63.1, which matches the spec and the phase split.
- Keeping the existing `ListAgents` liveness sentence apart from the new session-name reading follows the spec's finding that the two do not meet.
- The last task re-runs the spec's sweeps and confirms that the headings the seed cites still resolve.

## Deferred observations

- Affects: 63.1 (`.ai-factory/roadmaps/trickster77777.md`, "the architect comes back on a bare invocation"). Once 62.2 lands, `agent-architect/SKILL.md` will carry two different definitions of `<project-key>`. The new probe paragraph's definition ("every character that is not a letter or a digit replaced by a hyphen") matches how Claude Code actually names the directory. The handle-recovery fallback's definition ("separators replaced by hyphens") gives the wrong directory for any working directory whose path contains `_` or `.` (for example `mind_api` → `-mind-api`). The spec gives removal of that fallback to 63.1. If 63.1 keeps any part of that fallback instead of removing it, it should adopt the probe paragraph's definition, or point at it, rather than leave the separators-only wording.
