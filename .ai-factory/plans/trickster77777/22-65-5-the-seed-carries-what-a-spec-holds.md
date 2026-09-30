# Plan: 65.5 — the seed carries what a spec holds

## Context
A newly founded architect buffer copies `src/skills/agent-architect/templates/buffer-seed.md` whole, and the head re-reads that buffer all session. Its `## Method` section today holds only the counts rule, so the rule on what a spec holds (the one `roadmap-engine`'s **What a task spec holds** and `docs/what-a-task-carries.md` state) never reaches a buffer. This task adds it to `## Method` as a second standing entry, word-for-word as the task spec pins it.

Ground truth checked: the seed's `## Method` holds, in order, the angle-bracket placeholder ("A mistake as the pattern behind it … never the episode that revealed it."), then **Standing entry — the counts rule.**, whose body ends "ask which member is missing.", then a blank line, then `## Orientation`. That is what the spec describes, so 65.2 has already landed.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Seed edit

- [x] **Add the "what a spec holds" standing entry to `## Method`**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  Put a new paragraph right after the counts-rule entry, which ends "ask which member is missing.", and before `## Orientation`. Leave one blank line between it and the counts rule, and one blank line between it and `## Orientation`. It has the same shape as the counts rule: a bold lead-in, then the body in the same paragraph. The text must be exactly this, word for word:

  > **Standing entry — what a spec holds.** A spec states what is true now, what must be true after and what breaks on contact, and nothing else. It carries no check that the instruction was carried out: the orchestrator plans, builds and reviews on its own, and a check written into a spec comes back as plan steps and review rounds. It names no position in a file, only what the artifact must hold. It puts no fence around a neighbour; scope is what the task changes.

  Hard-wrap the paragraph the way the counts-rule entry is wrapped: lines of about 72–76 characters, breaking only between words, with the wording and punctuation unchanged. Use the em dash `—` in the lead-in, the same character the counts rule uses. Do not add a pointer to any doc or skill.

  Change nothing else: not the counts-rule entry, the placeholder, the file's opening paragraph, or any other section. No other file changes. Per the spec's sweep, the only reader of the seed is the founding passage in `agent-architect/SKILL.md`, which copies the seed whole, so no caller needs an update. Buffers founded from earlier seeds are records and stay as they are.
