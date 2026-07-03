# Code Review — Engines carry a reverse-graph marker

**Scope:** `git diff HEAD` + `git status`
**Files changed:** `CLAUDE.md`, `src/skills/note/SKILL.md`, `src/skills/roadmap-engine/SKILL.md`, `src/skills/test-philosophy/SKILL.md` (milestone substance); `.ai-factory/ROADMAP.md` (unstaged); plan/plan-review/sidecar artifacts.
**Risk level:** 🟢 Low — the milestone edits are correct and faithful to the spec. One out-of-scope roadmap change and two trivial nits.

## Summary of the substantive changes

All three engines gained a declarative genre marker and CLAUDE.md gained the convention line. Verified against the spec (`.ai-factory/specs/01-engine-reverse-graph-marker.md`):

- **Declarative, not imperative** — required by the spec's core design (the marker loads for every *user* of the engine, so it must contain nothing executable). All three markers pass: "callers depend on its exact behavior — edits here must honor their expectations … the reverse graph resolves via `grep …`". This states a *property* of edits and *how the reverse graph is computed*; there is no "before editing, run grep" imperative. ✓
- **No caller names** — the grep literals are generic (`grep -l "<engine>" src/skills/*/SKILL.md src/commands/*.md`); no caller is enumerated. ✓
- **No new section, no frontmatter field** — every marker is prose appended to the existing intro paragraph; nothing added to YAML. ✓
- **Anchors correct** — `roadmap-engine` and `test-philosophy` append to their existing "Load this skill once per chat" sentences; `note` (which had no load-once statement) places the marker after its one-line intro, before `## Workflow`, leaving `### Hooks (caller inputs)` and the default template untouched. ✓
- **CLAUDE.md convention** — the added line completes the both-ends coupling rule (caller declares *whom* it loads; engine declares *that it is loaded* and how to find by whom) and states a new engine gets the marker with its first `loads:` edge. Matches spec Edit 2. ✓
- **Markdown rendering** — the double-backtick code spans render correctly and (importantly) protect the `*` glob characters from being parsed as emphasis. ✓

Declaring `note` a "load-once engine" in prose is accurate (roadmap-engine and command-handoff both load it once per chat) and does not alter its standalone default behavior.

## Findings

### 1. Out-of-scope ROADMAP.md change: `---STOP---` moved past `observe-logs` (Low–Medium — verify intent)

The unstaged `ROADMAP.md` diff moves the `---STOP---` boundary from *above* the `observe-logs: remote Loki auth` entry to *below* it:

```
before:  … milestone-rescue │ ---STOP--- │ observe-logs
after:   … milestone-rescue │ observe-logs │ ---STOP---
```

This pulls `observe-logs` into the orchestrator's active region (tasks above STOP). It is unrelated to this milestone, whose scope is strictly the three engine markers + the CLAUDE.md line — nothing here should touch the STOP fence. Note also that no task was marked `[x]` (engine-marker, milestone-rescue, and observe-logs all remain `[ ]`), so this is not the usual "advance the frontier after completing a task" bookkeeping.

**Impact:** if committed as-is, the orchestrator will treat `observe-logs` as the next in-scope task, which may not be intended.
**Action:** confirm whether advancing STOP here was deliberate; if not, restore the marker to its position above `observe-logs`. It is unstaged, so it is trivially separable from the milestone commit.

### 2. Dangling modifier in the marker sentence (Trivial — style)

Each marker opens "As a load-once engine, its callers depend on its exact behavior …". The introductory phrase "As a load-once engine" grammatically attaches to the subject "its callers," so it literally reads as "the callers are a load-once engine." Meaning is unambiguous in context. If polished, rephrase to e.g. "This is a load-once engine: its callers depend on its exact behavior …" (which also matches the spec's own suggested wording verbatim). Non-blocking.

### 3. `grep -l "note"` is a noisy reverse-graph literal (Informational — inherent to the convention)

`"note"` is a common substring, so the marker's grep will also match files that merely mention the word rather than only true `loads: note` callers. This is a property of the pre-existing documented convention (CLAUDE.md already uses this form) and the spec explicitly requires reproducing the literal — so it is correct as written, flagged only for awareness.

## Verdict

The milestone implementation is correct and faithfully implements the spec — no bugs in the four target-file edits. The only item warranting action before commit is Finding 1 (the unrelated `---STOP---` move), which should be verified and most likely reverted since it is unstaged and outside this milestone's scope.
