# 68.2 — the prune gate names a phase as a route target

## What is true now

`src/skills/roadmap-prune/SKILL.md` § "Step 0 — Deferred-observations gate", in the item that stops on an unpinned entry, names the resolution in numbered parts. The second reads: "a **dedicated resolution session** works through the findings — fixing, routing into an **open** task's spec, or dismissing — and sets pins per `orchestrator-artifacts` § 6;". The text wraps in the file at a fixed column. It names one route target, an open task's spec.

`orchestrator-artifacts` § "6. Status-marker grammar", as the grammar task leaves it, admits a phase as a route target too, spelled `[routed → <roadmap path> § Phase N]`.

## What must be true after

The second resolution part reads: "a **dedicated resolution session** works through the findings — fixing, routing into an **open** task's spec or onto a phase, or dismissing — and sets pins per `orchestrator-artifacts` § 6;".

## What breaks on contact

**Rule:** a text breaks on this change if it restates the route target a resolution session may pin, or reads a routed pin's target.

**Sweep:**
```
grep -n -i "open\*\* task\|routing\|routed" src/skills/roadmap-prune/SKILL.md
grep -rn "open\*\* task" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the gate's second resolution part alone, the task's own target. The skill states the route target nowhere else: its gate cites the engine for the pinned definition and the grammar, and checks only that an entry line carries a bracketed marker, so a pin onto a phase passes the gate as any pin does. The second search reaches the same sentence and nothing else, so no other skill, command or doc restates "an open task's spec" as the only target. `task-rescue` § "Step 5.6 — Pin disposed observations" cites § 6 for the grammar and routes only into a spec, and `command-handoff` carries the unpinned entries into the handoff without naming a target; neither depends on this sentence.
