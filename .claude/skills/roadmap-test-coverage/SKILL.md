---
name: roadmap-test-coverage
description: >-
  Analyzes a project roadmap to identify areas worth unit-testing, checks which
  areas already have test coverage, launches parallel explore agents to produce
  detailed test-case plans per area, and saves each agent's findings as a
  numbered note. Use when you want to plan test coverage for a project from its
  roadmap before writing any test files. Output: a set of notes ready for
  /roadmap-decompose to turn into ROADMAP_TESTS.md.
argument-hint: "[roadmap-file]"
disable-model-invocation: true
user-invocable: true
allowed-tools: Read Glob Grep Bash(find *) Bash(git *) Bash(mkdir *) AskUserQuestion Agent
---

# roadmap-test-coverage — Test Coverage Planner

Reads the project roadmap, identifies testable areas, checks existing coverage,
runs parallel research agents per area, and saves findings as notes.

## Workflow

### Step 0: Load Project Context

Read `.ai-factory/DESCRIPTION.md` if it exists — understand the tech stack,
test runner, and architecture conventions.

Read `.ai-factory/ARCHITECTURE.md` if it exists — understand module boundaries
and folder structure.

### Step 1: Determine Roadmap File

If `$ARGUMENTS` names a file — use it as the roadmap path.
Otherwise default to `.ai-factory/ROADMAP.md`.

Read the roadmap file in full.

### Step 2: Extract Testable Areas

Scan every completed (`[x]`) and pending (`[ ]`) milestone.

Group related milestones into **testable areas** — one area per logical
component or service (e.g. "TradeAggregator", "CandlePersistenceService",
"pure utility functions"). A good area maps to one or a few source files
that share a clear responsibility boundary.

Criteria for an area being worth testing:
- Contains non-trivial business logic, state transitions, or edge-case handling
- Is used by many downstream components (high blast radius if broken)
- Has hard-to-spot bugs: concurrency, time-based behavior, boundary conditions

Criteria for skipping:
- Pure wiring / DI configuration with no logic
- Thin pass-through adapters with no branches
- External library wrappers with no custom logic

### Step 3: Check Existing Test Coverage

For each area identified in Step 2, search the codebase for existing spec or
test files that cover it:

```bash
find . -name "*.spec.*" -o -name "*.test.*" | grep -v node_modules | grep -v dist
```

For each area, classify:
- **No coverage** — no spec file exists for the target source file(s)
- **Partial coverage** — spec file exists but visibly incomplete (read it briefly)
- **Full coverage** — spec file exists and appears thorough

### Step 4: Present Findings and Confirm

Show the user:

```
Found N testable areas:

[No coverage]
  - AreaName — src/path/to/file.ts
  - ...

[Partial coverage]
  - AreaName — src/path/to/file.spec.ts exists but missing: <what's visibly absent>
  - ...

[Full coverage — will skip]
  - AreaName
  - ...
```

Then ask:

```
AskUserQuestion: These areas have no or partial test coverage.
Which ones should I research in depth?

Options:
1. All of them (recommended)
2. Only "No coverage" areas
3. Let me pick manually
```

If the user picks manually — list areas and ask which to include.

Store the confirmed list as `$RESEARCH_AREAS`.

### Step 5: Determine Next Note Number

```bash
mkdir -p .ai-factory/notes
find .ai-factory/notes -name "[0-9][0-9]-*.md" | sort | tail -1
```

Extract the highest two-digit prefix and add 1. If no notes exist, start at `01`.
Store as `$NEXT_NOTE_NUM`.

### Step 6: Launch Parallel Research Agents

For each area in `$RESEARCH_AREAS`, launch one Agent with `subagent_type: Explore`
and the following prompt. Launch all agents in a single message so they run
in parallel — one Agent tool call per area.

**Agent prompt template:**

```
You are researching test coverage for one area of a codebase.

Area: <area name>
Source file(s): <file paths>
Existing spec file (if any): <path or "none">

Your task:
1. Read the source file(s) in full — understand every public method, constructor
   arguments, internal branches, error paths, and edge cases.
2. If a spec file exists, read it and identify what is already covered and what
   is missing.
3. Identify what dependencies need to be mocked (injected services, external
   libraries, timers, etc.).
4. Produce a structured list of test cases grouped by method or behavior.

For each test case write:
  - One-line description: "should <expected behavior> when <condition>"
  - Which method/function it exercises
  - Any gotcha or non-obvious setup needed

Format your findings as a markdown document with these sections:
## Source Overview
(2-3 sentences: what this class/module does, its role in the pipeline)

## Instantiation
(How to create an instance in tests: new X() directly, or NestJS Test.createTestingModule.
List what needs to be mocked and how.)

## Existing Coverage
(What is already tested if a spec file exists. "None" if no spec.)

## Test Cases
(Grouped by method or behavior. Use ### subheadings per group.)

## Gotchas
(Non-obvious things: timers, private method access, decorator bypass, invariants
that must not be violated even when inputs look empty.)

Return the full document as your response. Do not write any files.
```

### Step 7: Save Agent Results as Notes

For each agent result, save it to `.ai-factory/notes/<NN>-<slug>.md` where:
- `<NN>` is `$NEXT_NOTE_NUM` incremented per note
- `<slug>` is a lowercase-hyphenated name derived from the area name

Prepend the standard note frontmatter:

```markdown
# <Area Name> — Test Plan

**Date:** <YYYY-MM-DD>
**Source:** roadmap-test-coverage agent

<agent output here>
```

### Step 8: Report Summary

After all notes are saved, print:

```
Test coverage research complete.

Notes written:
  - .ai-factory/notes/<NN>-<slug>.md  (<area name>)
  - ...

Areas with no coverage: N
Areas with partial coverage: N
Areas skipped (already covered): N

Next step: run /roadmap-decompose to turn these notes into ROADMAP_TESTS.md
Reference the notes in each milestone description so the implementer has full context.
```

## Critical Rules

1. **Never write test files** — this skill only researches and plans
2. **Never write ROADMAP_TESTS.md** — that is the job of /roadmap-decompose
3. **One note per area** — do not merge multiple areas into one note
4. **Agent prompts must be self-contained** — the agent has no conversation context
5. **Always check existing specs before calling an area uncovered**
