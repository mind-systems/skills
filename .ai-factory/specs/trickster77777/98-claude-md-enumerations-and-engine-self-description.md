# CLAUDE.md's two skill enumerations, and an engine that misdescribes its own load

Three small gaps left open by the two paired-loop tasks of this phase. Two
are omissions from `CLAUDE.md`'s two parallel enumerations of our skills;
the third is one clause in `architect-editor-engine` that reads its own
`loads:` declaration as the mechanism that loads it. None breaks anything
today; each is a description that has drifted from what the tree holds.

## Current state (grounded, read fresh)

`active/skills/` contains symlinks for all three paired-loop skills:
`agent-architect`, `architect-editor-engine`, `architect-pairing-engine`.

`CLAUDE.md:74` — the active-set paragraph — ends its list of ours with
"… `orchestrator-artifacts`, `agent-architect`, `architect-pairing-engine`
— plus one upstream original we use as-is: `aif-skill-generator`."
`architect-editor-engine` is absent.

`CLAUDE.md:189` — "**Everything else in `src/skills/` is ours** — no
upstream counterpart to reconcile, sync never touches it: …" — ends its
list with "… `observe-logs`, `ui-ux-pro-max`, `agent-architect`." Both
engines are absent.

`src/skills/architect-editor-engine/SKILL.md:17`:

> "Load this skill once at birth — the architect via its own `loads:`
> frontmatter edge, the editor as the first action on spawn — so the
> contract is resident before any channel-message arrives."

The architect's actual load is the body instruction in
`agent-architect/SKILL.md`, which tells it to load the engine via the
`Skill` tool before the first channel-message. `loads:` declares the graph;
it does not perform a load — the repo's own rule is that the declarations
*are* the map, colocated with the depending skill.

## Defect A — the active-set paragraph omits an active skill

`CLAUDE.md:74` is the answer to "what does `~/.claude` actually load". It
names `architect-pairing-engine` but not `architect-editor-engine`, though
both are symlinked. A reader taking the paragraph as the working set gets a
false negative on a skill that is loaded on every paired-loop session.

## Defect B — the ownership list omits both engines

`CLAUDE.md:189` answers a different question: what in `src/skills/` is ours
and must never be overwritten by an upstream sync. Both engines are missing
from it. Nothing breaks today — `scripts/sync-upstream.sh` overwrites only
`upstream/ai-factory/` and never reads this list — but the list is the
written record of what a sync must not touch, and two of our own skills are
not in it.

The two lists are parallel enumerations of overlapping sets, which is why
they drift apart one at a time. They are corrected together, in one pass.

## Defect C — the engine reads its own `loads:` edge as a loader

`:17` attributes the architect's load to the `loads:` frontmatter edge.
`loads:` is a declaration of the forward graph, not a mechanism; the
architect loads the engine because its body instructs it to, via the
`Skill` tool. The sentence is harmless in practice and wrong in the one
place it matters: it is the only line in the repo that reads `loads:` as a
loader, and that reading is what would make an unpaired architect's "never
loads it" guard look self-contradictory.

## The change

Three edits, in two files:

1. `CLAUDE.md:74` — add `architect-editor-engine` to the active-set list,
   immediately before `architect-pairing-engine`, keeping the surrounding
   punctuation and the trailing "— plus one upstream original …" clause
   exactly as they are.
2. `CLAUDE.md:189` — add `architect-editor-engine` and
   `architect-pairing-engine` to the ownership list, after
   `agent-architect`, keeping the trailing "The same holds for
   `src/agents/` …" sentence exactly as it is.
3. `src/skills/architect-editor-engine/SKILL.md:17` — replace the clause
   "the architect via its own `loads:` frontmatter edge" so it attributes
   the architect's load to the instruction in the architect's own body.
   The corrected clause names no caller — the reverse-graph marker in the
   same sentence is how a reader finds them. The caller list already
   present in the `description:` field is outside this task's scope and
   stays exactly as it is.

## Files & types

- edit: `CLAUDE.md` — lines 74 and 189 only.
- edit: `src/skills/architect-editor-engine/SKILL.md` — one clause on line
  17 only.

## Guards

- The engine's body names no caller. The one-way graph rule holds there:
  the caller declares `loads:`, and the body carries only the reverse-graph
  marker that tells a reader how to find its callers by grep. The
  `description:` field is a separate matter — it already names both
  callers, and this task neither relies on that nor changes it.
- No other line of either file changes. In particular the reverse-graph
  `grep -l` command in the same sentence, the two channel-message formats,
  and the mode rule are untouched.
- No frontmatter changes anywhere: no `loads:` edge is added, removed, or
  reordered by this task.
- `src/skills/agent-architect/SKILL.md`,
  `src/skills/architect-pairing-engine/SKILL.md`, `src/agents/editor.md`,
  and `active/skills/` are untouched — the symlinks already exist and are
  correct; only the prose that describes them is wrong.
- The two `CLAUDE.md` lists stay two lists. They answer different
  questions — what is loaded, versus what is ours — and are not merged,
  cross-referenced, or reduced to one.

## Verification

- `grep -c "architect-editor-engine" CLAUDE.md` → at least one hit on line
  74 and one on line 189.
- `grep -c "architect-pairing-engine" CLAUDE.md` → hits on both lines 74
  and 189.
- Diff `CLAUDE.md` against `git show HEAD:CLAUDE.md`: exactly two lines
  differ, 74 and 189, and each differs only by the added skill names.
- Diff `src/skills/architect-editor-engine/SKILL.md` against its `HEAD`
  version: exactly one line differs, and the reverse-graph `grep -l`
  command inside it is unchanged.
- `sed -n '14,$p' src/skills/architect-editor-engine/SKILL.md | grep -c
  "agent-architect"` → 0. The body still names no caller. Scoped past the
  frontmatter deliberately: the `description:` field names both callers
  today and is not touched by this task, so a whole-file grep would return
  1 on correct work.
