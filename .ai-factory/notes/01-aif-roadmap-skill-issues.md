# aif-roadmap Skill: Design Issues

**Date:** 2026-04-11
**Source:** conversation context — tradeoxy_gui history pagination planning session

## Key Findings

- The skill is designed for "strategic high-level milestones" but the actual use case is an orchestrator queue where each milestone = one git commit and the description is the primary agent input.
- The skill actively resists granularity via explicit rules ("high-level goal, not a granular task"), which directly conflicts with how the orchestrator consumes ROADMAP.md.
- Every time `/aif-roadmap` is used to add tasks, the user must manually correct the output to be more atomic and descriptive — the skill never produces this on its own.
- The format example (`— short description`) reinforces the wrong behavior; the core ROADMAP.md shows what descriptions should actually look like (paragraph-length, file paths, API contracts, guard conditions).

## Details

### The root tension

The skill was designed as a two-level planning tool:

```
ROADMAP (strategic)  →  /aif-plan (detailed)  →  /aif-implement (code)
```

But the actual workflow with the orchestrator is:

```
ROADMAP milestone description
        │
        ▼ (primary input)
  PlannerAgent (Opus) — reads milestone title + description, explores codebase, writes plan
```

The Planner gets the milestone description as its main brief. If that description is vague ("Add history pagination"), the Planner has to guess intent and make assumptions. If it's specific (files to change, RxJS operators to use, API contract, guard conditions), the Planner produces a much better plan with fewer review iterations.

### What the skill currently enforces (wrong)

In `SKILL.md`, section "Rules for milestones":
```
- Each milestone is a high-level goal, not a granular task (that's /aif-plan)
- 5-15 milestones is the sweet spot
```

And Critical Rule 1:
```
Milestones are high-level — each represents a major feature or capability, not a task
```

The format template:
```
- [ ] **Name** — short description
```

The word "short" is the problem. The core ROADMAP.md entries are 3-10 sentences each, with file paths, method names, and explicit constraints.

### What good milestone descriptions look like (from tradeoxy_core ROADMAP)

```
- [x] **Add `count + to` query mode to candles endpoint** — Currently
  GET /api/candles supports two mutually exclusive modes: `count` (latest N
  candles) and `from + to` (date range). Neither supports pagination...
  Changes required: (1) GetCandlesQueryDto ... relax the cross-field validator
  to allow `count + to` together; (2) CandleController.getCandles() ... add a
  third branch; (3) CandleRepository ... add findLatestBefore(symbol, timeframe,
  count, before: Date)...
```

Key properties:
- Describes the **current state** (what exists, what's wrong/missing)
- Describes the **target state** (what needs to change)
- Lists **specific files** to touch
- Lists **specific methods/types** to add or modify
- States **guard conditions** (what to skip, when to stop)
- One focused responsibility — not a bundle of loosely related changes

### One milestone = one commit

The orchestrator (`main.py:_git_commit`) calls `git add -A && git commit` once per milestone, after all tasks in the plan are done. So milestone granularity directly determines commit granularity. Bundling unrelated things into one milestone produces a noisy, hard-to-revert commit.

### Correct mental model for milestone descriptions

> The milestone description is the specification that a capable AI agent will read with zero prior context to produce a working implementation. It must be complete enough that the Planner does not need to guess intent, invent constraints, or ask clarifying questions.

## Right Granularity (crystallized definition)

> Each milestone maps to one git commit. The right granularity is one conceptual step with a single reason to revert — one layer of responsibility. The description is the primary input for a Planner agent that has no prior context: it must name the specific files to change, the exact APIs or operators to use, and explicit "do NOT do X" guards for non-obvious pitfalls. Vague descriptions produce bad plans. Overly granular milestones waste agent time on trivial changes. Aim for the size of a bridge, a service method, or a reactive pipeline — not a feature, not a line.

Note: "do NOT do X" gotchas are not expected upfront — they emerge from failed orchestrator runs and get added to notes. The task description improves retroactively. The system self-corrects over time.

## Open Questions

- Should the skill distinguish between "roadmap for human planning" (high-level OK) and "roadmap as orchestrator queue" (must be atomic + descriptive)? Or should it always assume orchestrator use?
- Should the skill read the orchestrator's presence (`.ai-factory/orchestrator-state.json` or similar) and adjust its behavior accordingly?
