# Plan Review: roadmap-decompose — always emit two-tier output by invoking aif-note

**Plan:** `.ai-factory/plans/03-roadmap-decompose-always-emit-two-tier-output-by-invoking-aif-note.md`
**Risk Level:** 🟡 Medium
**Verdict:** Solid intent and well-grounded in notes 09/13, but one mechanism-level gap (Skill tool not in `allowed-tools`) must be addressed or the feature may not fire reliably — which is the exact failure the plan exists to fix.

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): WARN — no `## Features` entry references `roadmap-decompose` or `aif-note`, so no boundary conflict. The change is internal to one skill file; no architectural boundary is crossed. Aligns with the meta-repo model (product = skills).
- **Rules** (`.ai-factory/RULES.md`): not present — gate skipped (WARN, non-blocking).
- **Roadmap** (`.ai-factory/ROADMAP.md` present): PASS — the work is explicitly linked: ROADMAP.md line 13 `roadmap-decompose: always emit two-tier output by invoking aif-note` with `Spec: .ai-factory/notes/13-task-decompose-two-tier-via-aif-note.md`. Plan, spec note, and roadmap entry are consistent.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project-specific review overrides to apply.

## Critical Issues

### 1. `Skill` is missing from `roadmap-decompose`'s `allowed-tools` — the plan never adds it
The plan's central mechanism (Task 1 step 3, Tasks 2–3) is: *"invoke the `aif-note` skill via the Skill tool."* But the target skill's frontmatter is:

```
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion
```

`Skill` is **not** in that list. The only skill in this repo that invokes sub-skills — `aif` — explicitly declares `Skill` in its `allowed-tools` (`.claude/skills/aif/SKILL.md:5`). No other skill invokes sub-skills, so `aif` is the precedent and it shows the required pattern. Without `Skill` in the allowlist, the very reliability the plan is chasing ("make the agent do it reliably every run", "the flakiness from manual chaining is gone") is undermined: the invocation may be blocked or trigger a permission prompt mid-run.

**Fix:** add a task (or fold into Task 1) to add `Skill` to `roadmap-decompose`'s `allowed-tools` frontmatter. This is a one-line change but it is load-bearing for the whole feature. It is currently absent from every task in the plan.

## Other Findings (non-blocking)

### 2. Frontmatter `description` will become stale (WARN)
The skill's `description` still reads *"each entry is a fully specified task: what exists today, what needs to change, which files and methods to touch, and explicit guard conditions."* After this change, the roadmap **entry** is a ~600-char contract line and the full spec lives in the note. The plan touches the body and the "Roadmap File Format" section but not the frontmatter description. Recommend a small wording update so the description reflects the contract-line + spec-note shape (the full detail now lives in the aif-note-written note). Not blocking, but it is user-facing skill-discovery text.

### 3. Sequential note numbering not stated explicitly (WARN)
aif-note allocates `<NN>` by scanning `.ai-factory/notes/` for the highest `[0-9][0-9]-*.md` and incrementing. This is collision-free **only if** decompose invokes aif-note sequentially (each note written to disk before the next invocation). The per-task procedure is inherently sequential, so in practice this holds — but a gate split producing "two invocations" should make clear they run one-after-another, not batched. Note 09 called this out ("allocate numbers sequentially across all tasks in one run so two tasks never collide"). Worth one sentence in the Two-Tier Output procedure block (Task 1) to prevent a future parallel-invocation regression.

### 4. Slug control is left entirely to aif-note (informational, acceptable)
aif-note derives its own slug from the topic (or `$1`). The plan correctly captures the path aif-note **reports back** rather than predicting it, so the `Spec:` tag will always be accurate. Good. Optionally, decompose could pass a slug as aif-note's `$1` argument for task-name/file-name consistency — but this is a nicety, not a requirement, and passing an arg does not "alter aif-note's behavior" (it is aif-note's documented input). Leave as-is unless consistency matters.

## Verified — assumptions that hold

- **aif-note is model-invocable now.** `.claude/skills/aif-note/SKILL.md:9` confirms `disable-model-invocation: false` and `user-invocable: true`. The plan's premise (the ban was lifted this session) is true in the current tree.
- **aif-note writes `<NN>-<slug>.md` with no `task-` prefix.** The plan's tag form `Spec: .ai-factory/notes/<NN>-<slug>.md` correctly matches aif-note's actual naming (notes 09/13 used a `task-` prefix, but since aif-note owns naming, dropping it is the right call — consistent with "do not alter aif-note's behavior").
- **aif-note reports the saved path** (Step 4: `Note saved: .ai-factory/notes/<NN>-<slug>.md`), so "capture the path aif-note reports back" is achievable.
- **File path is correct.** `.claude/skills/roadmap-decompose/SKILL.md` exists; all four tasks target it.
- **The touchpoints are accurate.** Step 1.3, Steps 2.4/2.5, the "Roadmap File Format" section, and "Critical Rules" all exist as described and currently contain the inline-spec instructions the plan replaces. Atomicity Gate steps 1.3.1/2.4.1 exist and the plan correctly leaves them intact.
- **Editing this skill is allowed.** `roadmap-decompose` is on CLAUDE.md's custom / never-overwrite-from-upstream list — safe to edit directly.
- **Mode 3 (`check`) correctly left untouched** — it only flips `[ ]`→`[x]` and is unaffected by the two-tier shape (matches note 09's analysis).
- **No migration needed.** The plan and spec note both correctly say *do not* bulk-migrate pre-existing legacy inline tasks — avoiding roadmap diff churn.

## Positive Notes

- Tightly scoped, surgical change with clear dependency ordering (Tasks 2–4 depend on Task 1's shared procedure block) — the right way to avoid four copies of the same procedure drifting.
- Excellent provenance discipline: the plan reconciles note 09 (concept kept) vs. its superseded inline-template mechanism, and inherits note 13's char-budget numbers consistently.
- Centralizing the procedure in one "Two-Tier Output" block and referencing it from each mode is good DRY design for skill instructions.
- Char-budget framed as guidance not a hard clamp — sensible, avoids brittle output rules.

## Recommended Action
Add the `Skill` tool to `roadmap-decompose`'s `allowed-tools` (Critical Issue 1) before implementation. Findings 2–3 are cheap to fold into the existing tasks. With those addressed, the plan is ready to implement.
