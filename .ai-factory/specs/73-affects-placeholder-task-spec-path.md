# The `- Affects:` placeholder speaks task spec — scanner side of the lockstep pair

Task 17.5 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Task 17.1 certifies `orchestrator-artifacts` conformant while deliberately freezing the jointly-owned `- Affects:` entry line at `:55` — the retired synonym `spec-note` survives there on the protocol axis, retirable only by a paired change. This is that change. The emitter side — orchestrator task 17.1 (`orchestrator/.ai-factory/specs/trickster77777/29-affects-placeholder-task-spec-path.md`) — has **already landed** (commit `8f34644`): `reviewer.md:108` reads `task-spec path`, and `orchestrator-artifacts:55` is the last surviving `spec-note` occurrence in the pair. Only this scanner half remains; the pair was order-free by design — neither side touches the scanned bytes, and both pin the identical target field.

## Current state

`src/skills/orchestrator-artifacts/SKILL.md:55` documents the deferred-observations entry as:

```
- Affects: <phase / spec-note path / "unknown"> — <observation>
```

The emitter (`orchestrator/orchestrator/prompts/reviewer.md:108`) already writes `task-spec path`, with the tail `— <one-paragraph observation>` — the tails differ between the sides, harmlessly: the bytes actually scanned are the `## Deferred observations` heading and the `- Affects: ` prefix, never the placeholder tail.

## Change

One field on one line — `SKILL.md:55`: `spec-note path` → `task-spec path`. Target:

```
- Affects: <phase / task-spec path / "unknown"> — <observation>
```

The field string `<phase / task-spec path / "unknown">` is pinned identically in the emitter-side spec — that shared pin, not execution order, is what makes the pair converge.

## Guards

- **Scanned literals byte-identical.** The `## Deferred observations` heading and the `- Affects: ` prefix stay untouched.
- **The tail stays `— <observation>`.** Here it is a format description; the emitter's `— <one-paragraph observation>` is a length instruction to the reviewer. A recorded per-side difference, not drift — both specs state it.
- **Ordering: after 17.1** — same file: 17.1's pass edits other lines of `orchestrator-artifacts` and freezes this one; this task is the sanctioned unfreeze of the one field, nothing else. No constraint against the emitter task — the cross-repo pair is order-free.
- **Reverse-graph marker, `loads:`, the `[fixed]`/`[routed → <path>]`/`[dismissed]` marker literals, and every other protocol token untouched.**

## Verification

- `grep -n 'task-spec path' src/skills/orchestrator-artifacts/SKILL.md` → line 55 only.
- `rg -in 'spec-note' src/skills/orchestrator-artifacts/SKILL.md` → zero.
- `grep -c '## Deferred observations' src/skills/orchestrator-artifacts/SKILL.md` → 2, unchanged.
- `git diff src/skills/orchestrator-artifacts/SKILL.md | grep -c '^[-+]- Affects: '` → 0 — no diff hunk touches a line beginning with the `- Affects: ` prefix, the mechanical check for "byte-identical pre/post" rather than an assumption from the surrounding counts.
