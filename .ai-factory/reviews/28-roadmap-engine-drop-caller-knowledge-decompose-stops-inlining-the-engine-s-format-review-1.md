# Review: roadmap-engine drop caller knowledge; decompose stops inlining the engine's format

## Scope
Reviewed `git diff HEAD` and `git status`. Two source files changed:
- `src/skills/roadmap-engine/SKILL.md`
- `src/skills/roadmap-decompose/SKILL.md`

(Plus planning artifacts under `.ai-factory/` — not code.)

Both files read in full. This is a skill-content (documentation) change with no runtime, type, migration, or concurrency surface.

## Verification against plan + spec note 38

**Task 1 — engine frontmatter description**
The stale sentence "Currently loaded by roadmap-decompose; retained as forward-looking shared-format infra for the rest of the roadmap family." is removed. Replacement — "Caller-agnostic: holds no decomposition philosophy of its own. Load-once." — describes only what the engine holds, names no caller, and stays well under the 1024-char limit. Matches spec note 38's "describe only what the engine holds (the two-tier format) and that it is load-once, caller-agnostic." ✅

**Task 2 — engine body**
"The calling philosophy skill (currently `roadmap-decompose`) stays in control" → "The calling philosophy skill stays in control". Parenthetical caller name removed; load-once rule and format-vs-philosophy boundary intact. The `## The two-tier artifact` and `## Roadmap File Format` sections are byte-identical (the reflow of lines 17–20 is whitespace only, no content change). No caller/"used by" registry added. ✅

**Task 3 — decompose Mode 1.3**
The fenced ```markdown``` block duplicating the engine's roadmap file format is removed and replaced with a by-name pointer: "Draft the roadmap **in memory (do not write `$TARGET_FILE` yet)**, per `roadmap-engine`'s roadmap file format, using placeholder `` Spec: `<note pending>`. `` tags on the contract lines." The **Rules for milestones** list (atomic/one-concern, per-milestone spec draft → Atomicity Gate → draft contract line, ordering, `[x]` marking) is preserved verbatim. Mode 1.3.1 (Atomicity Gate) and Steps 1.4/2.4/2.5 untouched. `roadmap-engine` is already declared in the file's `loads:` frontmatter, so the pointer resolves. ✅

**Task 4 — no residual inline format restatement**
Grepped decompose for `# Project Roadmap`, `## Milestones`, `project vision`, `Task Name`, and ```` ```markdown ````. No format template or contract-line rule list remains. The surviving `**Task Name**` hits (lines 165/220/250/253/256/269) are Mode 3 check/progress-review example output, not a copy of the engine's roadmap file format — correct to leave. Remaining format references are all by-name pointers to `roadmap-engine`. ✅

## Guardrails (spec note 38 "What NOT to do")
- Two-tier format itself unchanged. ✅
- No decomposition philosophy moved into the engine. ✅
- No caller/"used by" list added anywhere. ✅
- `upstream/ai-factory/` untouched (only `src/skills` modified). ✅

## Findings
None. The change is correct, complete, and matches the spec and plan. No correctness, security, or runtime concerns.

REVIEW_PASS
