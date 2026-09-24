# 165 — the buffer is seeded from a template at founding

## What is true now

`src/skills/agent-architect/` has no `templates/` directory. Its `SKILL.md` § "Spawn once, message thereafter" states the buffer-creation moment in one paragraph, ending: "no such pointer means you are a new architect and create your own buffer first, at the path and numbering the engine defines. Either way the buffer exists before any editor does." Nothing in that paragraph, or anywhere else in the file, seeds the new file's content — a newly created buffer starts from nothing, and the pair reinvents the same shape by memory at every founding, per `.ai-factory/handoffs/29-the-architects-snapshot-is-a-history-not-a-telegram.md`, cited in this phase's own note. `src/skills/aif-docs/templates/html-template.html` is the family's one existing precedent for a skill-local, once-only `templates/` file, cited only from `references/html-generation.md` § "3.2: Generate HTML files" and read only on the invocation that needs it.

## What must be true after

A new file `src/skills/agent-architect/templates/buffer-seed.md` exists, holding the memory's starting shape — one flat set of seven rubrics, per this phase's corrected note (no zones, no eighth *live* heading, *rescues* dropped since `task-rescue` already owns rescue reports):

```markdown
# Buffer seed — the architect's memory at founding

This is the starting shape of a newly founded architect's buffer, read once
by `agent-architect/SKILL.md`'s "Spawn once, message thereafter" step at the
moment a new buffer is created — never reread for a buffer that already
exists, which is simply resumed. Copy it whole into the new buffer file; the
headings below are filled over the session, not left as placeholder prose.

## Where things stand

<Rewritten each time, never appended — the session's current position, not a log.>

## Rulings in force

<Rulings the user has made about how the pair works, in the user's own words.>

## Method

<A mistake as the pattern behind it and the reason that pattern holds, never
the episode that revealed it.>

**Standing entry — the counts rule.** Keep a contract, delete a census: a
number stays in a durable artifact only where the sentence would still read
true after someone adds a member without touching it; where it would not,
state the rule instead of the tally. Date a measurement instead of asserting
it as permanent. Two counts that disagree are not reconciled against each
other — ask which member is missing.

## Orientation

<Where the skills still lag the practice, and traps a reader would otherwise re-discover.>

## Ledger

<Deferrals not yet resolved: what, why deferred, and the trigger that resolves it.>

## Candidates — not tasks

<Ideas not yet promoted to a task, each with the trigger that would promote it.>

## Current thread

<The architect's own read of an open question, a diagnosis still forming —
as readable to the hand as everything else here.>
```

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" gains one sentence, appended at the end of the buffer-creation paragraph, after "Either way the buffer exists before any editor does." (no existing sentence in the paragraph is altered):

> A newly created buffer is seeded in full from `templates/buffer-seed.md` at
> the moment of its founding — read once, copied whole, never reread for a
> buffer that is merely resumed.

## What breaks on contact

The new template file has no existing citation anywhere to update — it is a wholly new file, and no `templates/` directory previously existed under `agent-architect/`. The one sentence added to `agent-architect/SKILL.md` is an append at the very end of the buffer-creation paragraph; sibling task 59.1 (spec `164-`) edits the same paragraph's mid-paragraph clause ("your buffer's path and rules are defined") and nothing else in it — the two edits are non-overlapping spans of one shared paragraph, landing either first leaves the other's anchor text intact, and this task's appended sentence does not restate anything 59.1 puts in its own span.

**Rule:** any file that references `agent-architect/templates/` or `buffer-seed.md` by path is either this task's own artifact set (the roadmap's own contract line for this task, and this task's own spec, both of which name the path as the thing being created) or a genuine second reference this task would need to account for.

**Sweep (re-runnable):**
```
grep -rln "agent-architect/templates\|buffer-seed" src/ docs/ .ai-factory/
```

**Invariant:** after the change, the roadmap's own contract line for this task and this task's own spec are the only artifacts naming `agent-architect/templates/` or `buffer-seed.md` by path, and each names it as what this task creates, not as a prior claim on it. This corrects an earlier version of this section, which claimed "no other file references `agent-architect/templates/` or a buffer-seed file" without exempting the task's own two planning artifacts, which do. The sweep locates candidates; reading decides.
