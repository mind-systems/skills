# global CLAUDE.md: comments never cite the plan layer

Origin: [handoff 15](../handoffs/15-code-cites-fluid-plan-layer-false-resolution.md) — the class analysis. The orchestrator's own repo carries the operational half (its task 1.1 / spec `18-implementer-forbid-plan-layer-cites.md`); this task lands the single authoritative home of the rule on the skills side.

## Current state

`src/global/CLAUDE.md` (the user-level instructions loaded into every session of every project, symlinked from `~/.claude/CLAUDE.md`) has no rule forbidding a durable comment from citing the fluid plan layer. The leak is **emergent**: an implementer handed a plan file titled `Phase N.M` and a spec note numbered `NN` narrates its current task into a code comment — `// Phase 9.3.1`, `// note 39`, an `.ai-factory/specs/…` path — with no instruction asking it to. It is worse than a dead link: `roadmap-prune` reuses freed phase/note numbers (globally-sequential numbering, holes from pruning refilled by later directions), so a stamped citation later resolves to an *unrelated live phase* — a confident false pointer, not an honest dangling one. `ARCHITECTURE.md ## Features` anchors pruned work only at feature→one-hash grain, so `Phase 8.1.2` has no correct resolution path anywhere once its phase is pruned.

The rule is family-universal, not a per-project counter-default, so it does **not** belong in the generated `rules/base.md` (see `src/skills/aif/references/rules-generation.md` — that file is for code-evidence counter-defaults, the costliest instruction surface per line). Its home is the global instructions, beside the sibling doc-discipline rules "Describe behavior, not code" and "One home per fact".

## Change

Append **one bullet** to `src/global/CLAUDE.md` § "Documentation style", after the "Describe behavior, not code." bullet. Exact text:

```markdown
- **Comments never cite the plan layer.** No code or test comment carries a phase/note number, a `ROADMAP`/`Plan` reference, or an `.ai-factory/` path.
```

That is the whole edit — a pure prohibition, no second sentence.

## Files & types

- edit `src/global/CLAUDE.md` only (one bullet appended in § "Documentation style").

## Guards

- **Pure prohibition — no positive limb.** Do not add "…explains behaviour or links a `docs/` file" or any "what to do instead": a positive limb reads as an instruction to *add* doc-linking comments and floods code with them. The "instead" is operational and already lives in the orchestrator's implementer prompt (spec 18, "`docs/` is the only reference target allowed in code") — that prompt is this rule's operational **projection**, never a second home.
- **One home for the fact.** This bullet is the single authoritative statement; nothing else in the skills repo restates it. Anything enforcing it (task 6.2's prune scan, the orchestrator prompt) points at or projects from here, never copies the wording.
- **Directional boundary is implicit, not spelled out.** A comment is always outside `.ai-factory/`, so the bullet needs no "the plan layer may cite itself" clause — that clause matters only to the plan layer's own artifacts, which this rule does not govern. Keep it to the one sentence.
- **Additions only** — every existing line in the file byte-identical; the 1.16 / 4.5 append pattern. No skill edits, no docs edits.

## Verification

- `grep -n "Comments never cite the plan layer" src/global/CLAUDE.md` → one hit, inside § "Documentation style".
- `git diff src/global/CLAUDE.md` → exactly one bullet added, no other line changed.
- The bullet has no positive/"link docs" clause and no provenance sentence.
