---
name: roadmap-test-coverage
description: >-
  Orchestrates full test coverage planning for a project. Reads the roadmap,
  scans existing specs, filters areas by silent-failure risk, runs parallel
  deep-research agents per area, reviews testability, emits refactor tasks,
  runs existing tests and classifies failures (API drift vs silent bug), then
  hands off to /roadmap-decompose. Use when you want a complete test plan from
  a roadmap with no prior test strategy.
argument-hint: "[roadmap-file]"
disable-model-invocation: true
user-invocable: true
allowed-tools: Read Glob Grep Bash(find *) Bash(npm *) Bash(npx *) Bash(dart *) Bash(flutter *) Bash(python *) Bash(pytest *) Bash(go *) Bash(cargo *) Bash(mkdir *) Bash(git *) AskUserQuestion Agent Write
---

# roadmap-test-coverage — Test Coverage Orchestrator

Eight-layer pipeline. Layers 4, 5, and 7 run in isolated agents to protect
the main context. Agents write results to disk and return only one-line
summaries back to the orchestrator.

---

## Layer 1 — Load Project Context

Read in order (skip if absent):
- `.ai-factory/DESCRIPTION.md` — tech stack, test runner, conventions
- `.ai-factory/ARCHITECTURE.md` — module boundaries, folder structure
- `ROADMAP.md` (or `$ARGUMENTS` if provided) — all milestones

Store: `$STACK` (e.g. "NestJS/Jest"), `$TEST_CMD` (e.g. `npm test`),
`$ROADMAP_PATH`.

If no DESCRIPTION.md, infer stack from `package.json` / `pubspec.yaml` /
`go.mod` / `Cargo.toml`.

---

## Layer 2 — Coverage Scan

```bash
find . -name "*.spec.*" -o -name "*.test.*" | grep -v node_modules | grep -v dist | grep -v build
```

Read each completed and pending milestone in the roadmap. Group related
milestones into **candidate areas** — one area per logical component or
service. Each area maps to one or a few source files with a clear
responsibility boundary.

For each candidate area, classify:
- **No coverage** — no spec file for the target source file(s)
- **Partial coverage** — spec exists but visibly incomplete
- **Full coverage** — spec exists and appears thorough

Drop "Full coverage" areas. Carry forward "No coverage" and "Partial".

---

## Layer 3 — Silent-Failure Filter

This is the most important gate in the pipeline. It prevents Layer 4 from
wasting agent capacity on areas that already have automatic failure detection.

For each remaining candidate area, ask one question:

> **"If the logic here is wrong, does the system signal it immediately
> (TypeScript error, runtime exception, DI failure, 4xx/5xx response),
> or does it continue running and produce wrong output silently?"**

| Fails loudly → skip | Fails silently → keep |
|---|---|
| Mapper with wrong field type | Aggregator with off-by-one cursor |
| Controller missing route param | State machine with wrong transition |
| DI wiring missing a provider | Dedup logic with wrong key |
| Thin adapter with no branches | Flush threshold calculated incorrectly |
| gRPC interceptor that throws | Session expiry computed from wrong timestamp |

Apply the filter to every area. Drop loud-failure areas.

Present the result to the user:

```
After silent-failure filter: N areas remain (dropped M).

[Kept — fails silently]
  - AreaName — src/path/to/file.ts
  - ...

[Dropped — fails loudly]
  - AreaName — reason (e.g. "TypeScript catches type mismatch immediately")
  - ...

Research all N kept areas? (y / let me pick)
```

Store confirmed list as `$RESEARCH_AREAS`.

---

## Layer 4 — Deep Research (parallel agents)

Determine next note number:
```bash
mkdir -p .ai-factory/notes
find .ai-factory/notes -name "[0-9][0-9]-*.md" | sort | tail -1
```
Extract highest two-digit prefix + 1. If none, start at `01`.
Store as `$NEXT_NOTE_NUM`.

Launch one `Explore` agent per area in a **single message** (parallel).
Each agent writes its note to disk and returns one line to the orchestrator.
Do not read note contents back — one-line confirmations only.

**Agent prompt template:**

```
You are researching test coverage for one area of a codebase.

Area: <area name>
Source file(s): <file paths>
Existing spec file (if any): <path or "none">
Note to write: .ai-factory/notes/<NN>-<slug>.md

Your task:
1. Read the source file(s) in full — every public method, constructor args,
   internal branches, error paths, edge cases.
2. If a spec file exists, read it and identify what is covered and what is
   missing.
3. Identify dependencies that need to be mocked or faked.
4. Produce a structured list of test cases grouped by method or behavior.

For each test case write:
  - "should <expected behavior> when <condition>"
  - Which method/function it exercises
  - Any non-obvious setup needed

Write the following document to .ai-factory/notes/<NN>-<slug>.md:

# <Area Name> — Test Plan

**Date:** <YYYY-MM-DD>
**Source:** roadmap-test-coverage agent

## Source Overview
(2–3 sentences: what this class/module does, role in the system)

## Instantiation
(How to construct in tests: direct new X(), NestJS Testing module, etc.
List what needs to be mocked and how.)

## Existing Coverage
(What is already tested, or "None".)

## Test Cases
(Grouped by method. Use ### per group.)

## Gotchas
(Timers, private fields, fire-and-forget async, decorator bypass, invariants.)

After writing the file, return exactly one line:
saved: .ai-factory/notes/<NN>-<slug>.md
```

Collect all one-line confirmations. Proceed to Layer 5.

---

## Layer 5 — Testability Review (parallel agents)

Launch one `general-purpose` agent per area in a **single message** (parallel).
Each agent reads the source file and returns a one-line verdict only.

**Agent prompt template:**

```
Testability review for: <area name>
Source file: <file path>

Read the source file. Assess four things:
1. Are all dependencies injected (constructor params, not module-level
   singletons or static imports)?
2. Any hard-coded globals: process.env reads without injection, Date.now()
   calls that cannot be overridden, fs calls without abstraction?
3. Any fire-and-forget async patterns (unawaited promises inside observable
   pipes, setTimeout without returned handle) that complicate teardown
   assertions?
4. Any metadata extraction via unsafe casts ((req as any).user,
   (metadata as any)[KEY]) that makes test setup awkward vs. a typed
   decorator param?

Return exactly one line in this format:
  clean | <area name>
  OR
  needs-refactor | <area name> | <one sentence: what to refactor and why>
```

Collect all verdicts. Do not read source files back into orchestrator context.

---

## Layer 6 — Refactor Emit

For each `needs-refactor` verdict from Layer 5:

1. Add a task to `$ROADMAP_PATH` under a `## Test Infra` phase (create the
   phase if absent). Task text = the refactor description from the verdict.
2. Open the corresponding Layer 4 note and append a `## Refactor Required`
   section: what to refactor, and what the post-refactor API will look like
   so the test implementer knows what to expect.

Log what was added. No user confirmation needed — emit and continue.

---

## Layer 7 — Existing Tests Run

Run the test suite:
```bash
<$TEST_CMD>
```

If all tests pass: log "All existing tests pass." and continue to Layer 8.

If any tests fail, launch one `general-purpose` agent with the full test
output. The agent classifies failures only — it does not write any files.

**Agent prompt:**

```
A test suite was run and some tests failed. Classify each failure.
Do not fix anything. Do not write any files.

Test output:
<paste full test runner output>

For each failing test:
1. Read the test file to understand what it asserts.
2. Read the source file it tests to understand the current implementation.
3. Run: git log --oneline -10 <source file>
   Look for recent changes that could explain the failure.

Classify each failure:

  Class A — API drift: the source API changed (renamed method, new required
  arg, changed return shape) but the test was not updated. The test is
  outdated, not meaningful. Safe to patch.

  Class B — Silent bug: the source behavior changed in a way the test was
  designed to catch. The system would produce wrong output. The test is
  doing its job. Do NOT patch — escalate.

Return a markdown table only:

| Test (describe > it) | Source file | Class | Reason | Action |
|---|---|---|---|---|
| ... | ... | A or B | one sentence | patch test / escalate |
```

Present the classification table to the user.

**For each Class A failure:** patch the failing test to match the current
source API. Keep assertions intact — only update the call signature.

**For each Class B failure:** add a task to `$ROADMAP_PATH` under a `## Bugs`
phase. Task text = area name + reason from the table. Do NOT touch the test.

Re-run `$TEST_CMD`. All tests must be green before Layer 8.

---

## Layer 8 — Hand Off

Print:

```
Test coverage research complete.

Notes written: N
  - .ai-factory/notes/<NN>-<slug>.md  (<area name>)
  - ...

Refactor tasks added to roadmap: M
Existing tests patched (API drift): K
Silent bugs escalated to roadmap: J

Next step: /roadmap-decompose
```

Do not run `/roadmap-decompose` automatically.

---

## Critical Rules

1. **Never write test files** — research and planning only
2. **Never write ROADMAP_TESTS.md** — that is `/roadmap-decompose`'s job
3. **Layer 4 and 5 agents return one line** — never read note contents back
   into the orchestrator context
4. **Layer 7 agent classifies only** — the orchestrator patches, never the
   agent
5. **Class B failures are wins** — the test caught a silent bug; escalate,
   never suppress
6. **One note per area** — never merge multiple areas into one note
