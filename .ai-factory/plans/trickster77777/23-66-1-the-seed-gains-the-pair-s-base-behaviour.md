# Plan: 66.1 — the seed gains the pair's base behaviour

## Context
Every new architect buffer is a whole copy of `src/skills/agent-architect/templates/buffer-seed.md`. The hand, which writes the artifacts, reads that buffer whole. `docs/paired-loop.md` § "Where the pair's behaviour lives" says the behaviour both halves must keep holding lives in the buffer and gets there through the seed as standing entries. Today the seed's `## Method` has only the counts rule and the entry on what a spec holds. This task adds the reading half of the counts rule (the rule in `docs/counts-go-stale.md` that a figure is read as an order of magnitude) and three new standing entries, word for word as the task spec pins them.

Ground truth checked: `## Method` holds, in this order, the angle-bracket placeholder, then **Standing entry — the counts rule.**, then **Standing entry — what a spec holds.**, whose body ends "scope is what the task changes.", then a blank line, then `## Orientation`. The spec describes this same state. The entry paragraphs are hard-wrapped at no more than 76 characters per line.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Seed edit

- [x] **Add the reading-half sentence to the counts-rule entry**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  In **Standing entry — the counts rule.**, put this sentence right after "…and the orchestrator cannot execute a spec whose facts no longer hold." and right before "Two counts that disagree are not reconciled against each other; ask which member is missing." Use this exact text:

  > A number met in a spec, a plan or a report is read as an order of magnitude; one that has gone stale is not a defect to correct, count again or stop on.

  Nothing else in the entry changes. Re-wrap the paragraph from the insertion point to its end so every line stays within 76 characters and breaks only between words. Keep the wording and punctuation exactly as given.

- [x] **Append three standing entries after "what a spec holds"** (after the counts-rule edit, since both edit `## Method`)
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  After the **Standing entry — what a spec holds.** paragraph and before `## Orientation`, add these three paragraphs in this order. Use the same shape as the existing entries: a bold lead-in, then the body in the same paragraph. Put exactly one blank line between neighbouring paragraphs, and keep one blank line before `## Orientation`. Use the em dash `—` in each lead-in, the same character the existing entries use. The text must be exactly this:

  > **Standing entry — state the behaviour and stop.** A rule says what happens and ends there: no sentence for each case it excludes, no guard against its own misuse. A rule or a fix that needs guards against its own machinery is the wrong one.

  > **Standing entry — a task is not retold in the code.** A spec's reasons are for whoever plans, and the code keeps none of them. A task says what must be true and what to delete or link; it never asks for a comment carrying its reasoning, a skeleton's contract or its scope. A comment in code says only what a reader would get wrong from the code alone, where the reader meets it, in a line or three.

  > **Standing entry — the orchestrator's commit takes the whole tree.** While it runs a queue in a repository, leave nothing uncommitted there, or it lands inside a task's commit.

  Hard-wrap each paragraph the way the existing entries are wrapped: no line longer than 76 characters, breaking only between words, wording and punctuation unchanged, with straight apostrophes as written above. Do not add a pointer to any doc, skill or code file.

  Change nothing else: not the file's opening paragraph (task 66.2 owns it), not the placeholder, not the "what a spec holds" entry, not any other section. No other file changes. Per the spec's sweep, the only reader of the seed is the founding passage in `agent-architect/SKILL.md`, which copies the seed whole. The editor reads the founded buffer, not the seed. So no caller needs an update. Buffers founded from earlier seeds are records and stay as they are.
