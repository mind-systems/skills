# roadmap-prune — Internal Rows Contradiction

**Date:** 2026-05-18
**Source:** conversation context — mind_api prune session

## Key Findings

- The skill has a direct contradiction: the outcome table says "Internal only → hash goes to drop history only, no feature row", but the formatting rules say "Internal rows always go under **Internal** at the bottom" and include an example with a named internal row. The agent follows the example and creates rows for every refactor.
- The correct behavior (confirmed by mind_mobile ARCHITECTURE.md) is: only one row exists under **Internal** — `Roadmap drop history`. All refactors, renames, cleanups, and doc changes go to the drop history hash only — never as named rows.
- The fix is to remove the contradictory example and add an explicit rule: "The only named row under Internal is Roadmap drop history."
- **A feature is "what the system can do" — the complete list of capabilities a user or another service can invoke.** This framing makes it immediately obvious whether something belongs: if you can call it, trigger it, or get a response from it — it's a feature. If it's an internal change that makes existing things work differently or not crash — it's drop history only.

## Details

### The Contradiction

In the outcome classification table:

> | **Internal only** | No new e2e behaviour — refactor, cleanup, dep fix, arch change | Hash goes to drop history only — no feature row |

But later in the formatting rules:

> Internal rows (refactors, arch cleanup, dep fixes) always go under **Internal** at the bottom.

And the example shows:

```
| **Internal** | |
| <Refactors / arch changes with no new e2e behaviour> | f04bb91 |
| Roadmap drop history | 5d1284c |
```

The agent sees a concrete example of a named internal row and follows it — creating rows like "Migration consolidation", "UUID schema fixes", "Transport cleanup", "Documentation sync" — none of which pass the e2e test criterion.

### What Triggered This

During a `roadmap-prune` run on `mind_api`, the agent produced:

```
| **Internal** | |
| Transport cleanup | 738076a db50793 |
| Proto contract cleanup | 39f560b 747dc8e |
| Presence removal | b26832f |
| Migration consolidation | 615cc70 |
| UUID schema fixes | 7b6035c |
| Documentation sync | 44fd26e 749c1bd |
| Roadmap drop history | a5959dc |
```

The correct output (after correction, matching mind_mobile pattern):

```
| **Internal** | |
| Roadmap drop history | a5959dc |
```

### The Fix

In the skill, under `## Step 2 — Classify, then group tasks into features`:

1. Remove the example internal row from the table template — replace it with just `Roadmap drop history`.
2. Add an explicit rule: **"Internal-only items (refactors, renames, cleanups, doc fixes, migration changes) go to the drop history hash only — they do not get a named row in the Features table. The only row under Internal is Roadmap drop history."**
3. Change the formatting example to show:
   ```
   | **Internal** | |
   | Roadmap drop history | 5d1284c |
   ```

### Reference

- Correct example: `/Users/max/projects/mind/mind_mobile/.ai-factory/ARCHITECTURE.md` — Features table has no internal rows except Roadmap drop history.
- Skill file: `/Users/max/.claude/skills/roadmap-prune/skill.md` (or equivalent path).
