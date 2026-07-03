# Engines carry a reverse-graph marker: the edit-time trigger lives in the engine file

**Date:** 2026-07-03
**Source:** conversation context (task-55 respec postmortem)

## Key Findings

- The dependency mechanism is one-way by design: a caller declares `loads: <engine>` in its own frontmatter; engines never list their callers (a `loaded-by:` list would be a cache that drifts). The reverse graph exists only via grep — and nothing triggers that grep at the moment it matters most: **editing the engine**. Live incident: during the task-55 respec, `note` was extended by spec without checking its callers; the rule "before touching an engine, grep for its callers" sits in CLAUDE.md — it was in context and still didn't fire, because the perception tree of the edit moment (rescue → artifacts → spec → engine file) contains no node mentioning that callers exist.
- Fix: put the trigger in the node the edit-time perception tree is guaranteed to pass through — the engine file itself. Not a caller list (names rot), a **genre marker without names**: one sentence stating this file is a load-once engine, callers depend on its exact behavior, and the reverse graph must be lifted (grep command inline) before editing. This cannot go stale — it names no caller.
- This completes the coupling-declaration rule ("cross-file invariants get one sentence at the coupling point in **both** files"): the caller side says *whom* it loads; the engine side now says *that it is loaded* and how to find by whom.

## Details

### Edit 1 — marker in each engine

The three engines are exactly the skills named in any `loads:` field today: `roadmap-engine`, `test-philosophy`, `note`. In each `src/skills/<engine>/SKILL.md`, add one sentence in the body near the load-once statement (or near the top where no such statement exists), adapted to the file's surrounding prose:

> This is a load-once engine: callers depend on its exact behavior, and edits to this file must honor their expectations as part of its contract — the reverse graph is `grep -l "<engine-name>" src/skills/*/SKILL.md src/commands/*.md`.

`<engine-name>` is the literal skill name (`note`, `roadmap-engine`, `test-philosophy`). One sentence (or two short ones), no caller names, no new section unless the file's structure demands one.

**The marker must be declarative, never imperative.** It loads into the context of every *user* of the engine, not just its editors — an imperative ("before editing, run grep …") reads as a runtime instruction and would make a using agent execute the grep and eagerly load every caller, exactly the context bloat the lazy model forbids. The grep appears as a *definition* of how the reverse graph is computed, addressed to a future editor; a skill-using agent finds nothing to execute in it.

### Edit 2 — the convention in CLAUDE.md

In `CLAUDE.md` → "Dependencies and the skill graph", add one line establishing the marker as part of the convention: every engine (any skill named in a `loads:` field) carries the reverse-graph marker in its body; a new engine gets the marker when the first `loads:` edge to it appears.

### Constraints

- The marker is genre-level only — if it ever names a specific caller, that is the drift the design forbids.
- `note`'s marker must not disturb the hooks section or default behavior; `test-philosophy`'s and `roadmap-engine`'s existing load-once sentences are the natural anchor.
- No `loaded-by:` field, no central map — the declarations plus the marker remain the whole mechanism.

## What NOT to do

- Do not list callers anywhere in an engine file.
- Do not add a frontmatter field for this — it is body prose, a note to the editor, not machine-read metadata.
- Do not restate the full editing rules from CLAUDE.md inside the engines — one marker sentence with the grep, nothing more.
- Do not phrase the marker as an instruction to run the grep — no imperative, no "before editing do X"; a using agent must find nothing executable in it.
