# 65.3 — the prune handoff names the review file, not the entry's line

## What is true now

`src/skills/roadmap-prune/SKILL.md` § "Step 0 — Deferred-observations gate" has an item that begins "If any unpinned entry exists → stop the skill entirely". It prints one line per unpinned entry as `<file>:<line> — <entry text>`, states that pruning is blocked, and names the resolution in numbered parts. The first part reads: "the user runs `/command-handoff` on this session — the handoff carries every unpinned observation (gist, original reviewer text, `Affects:`, `file:line` of the entry) plus the gate context into `.ai-factory/handoffs/`;". The text wraps in the file at a fixed column.

The handoff is read by the resolution session, a different and later session, after the review file may have gained or lost lines above the entry, so a line taken now points somewhere else by then. `docs/reference-by-name.md` names that form the defect.

## What must be true after

The first resolution part reads: "the user runs `/command-handoff` on this session — the handoff carries every unpinned observation (gist, original reviewer text, `Affects:`, the review file the entry sits in) plus the gate context into `.ai-factory/handoffs/`;". The review file with the entry's own original reviewer text is enough to find the entry. The chat line the item prints just before, `<file>:<line> — <entry text>`, reads as it does now.

## What breaks on contact

**Rule:** a text breaks on this change if it names what the handoff carries per unpinned entry, or reads an entry's line from a handoff.

**Sweep:**
```
grep -rn "unpinned" src/ docs/ CLAUDE.md
grep -rn "command-handoff" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches this gate item, the task's own target, and the earlier item in the same step that collects the entries, which reads no line. It reaches `docs/reserved-words.md`, which defines deferred observations without a line, and `command-pin-gaps`, whose "unpinned" belongs to value holes and is unrelated. The second search reaches this item's own naming of `/command-handoff`; the handoff command itself, which mines the session for meaning and reads no field list from this item; a passage in `agent-architect` that names it as a different genre; and the description of the gate in `docs/sakshi-harness/skill-cycle.md`, which says the observations ride to the resolution session with their context and names no line. The field list appears once in `roadmap-prune`, in this item; the other places in that skill that print `<file>:<line> — <matched text>`, in its plan-layer citation scan and its summary report, are chat echoes no handoff carries and stay as they are. The resolution session finds an entry by opening the review file the handoff names and searching it for a short fragment of the entry's text, which stays findable because an entry's text and its `Affects:` target are never rewritten and only markers accumulate on the line; the dedup rule of `orchestrator-artifacts`, which has whoever pins an entry pin every occurrence across that task's review files by `Affects:` target and gist, reads no line and works unchanged. The chat line the gate prints holds the file, so the session that runs `/command-handoff` has the file and the entry's text in its own context. No file reads the entry's line from a handoff.
