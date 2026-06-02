# Plan: aif-docs: state-not-process docs (no-motivation rule + `3d`/`3д` mode)

## Context
Two coupled, surgical changes to the `aif-docs` skill so generated docs state factual *state*, not *process*: an always-on no-motivation/no-history Core Principle (Change A) and a `3d`/`3д` Document-Driven mode that authors docs for not-yet-built features as if already shipped (Change B). Plus registering the divergence in `CLAUDE.md` so an upstream sync does not wipe it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Change A — always-on state-not-process rule

- [x] **Task 1: Add the state-not-process Core Principle**
  Files: `.claude/skills/aif-docs/SKILL.md`
  In the `## Core Principles` section (currently 6 numbered items, lines ~17-24), add a new principle: documentation states the **factual state**, never the process or motivation behind it. Forbid phrasing like "we changed X to Y", "this replaces…", "previously…", "because we…", "was added", "this milestone". State what **is**, not how it came to be — history lives in commit messages. Word it as a hard rule that applies to **every run regardless of mode**. Keep it concise and in the same numbered style as the existing principles.

- [x] **Task 2: Wire the no-motivation rule into the Step 4 review** (depends on Task 1)
  Files: `.claude/skills/aif-docs/SKILL.md`, `.claude/skills/aif-docs/references/REVIEW-CHECKLISTS.md`
  In `## Step 4: Documentation Review` (SKILL.md ~line 468-476), add an explicit instruction that the review must **flag and remove** any motivation/history/process language (the patterns from Task 1) in every generated/modified file before presenting results. In `references/REVIEW-CHECKLISTS.md`, add a matching checklist item under the **Technical Checklist** (e.g. "No motivation/history/process language — docs state factual state only, no 'we changed / was replaced / previously / because we / this milestone'"). This makes the rule enforced, not just declared. Applies in both normal and 3D mode.

### Phase 2: Change B — `3d`/`3д` Document-Driven mode

- [x] **Task 3: Detect the `3d`/`3д` parameter and set MODE flag**
  Files: `.claude/skills/aif-docs/SKILL.md`
  In `### Step 0.1: Parse Flags` (~line 87-91), add detection: if the invocation arguments contain the token `3d` or `3д` (case-insensitive) → set `MODE = 3D` for the whole workflow; otherwise `MODE = normal` and behavior is byte-identical to today. Note that `3d`/`3д` is a standalone token, distinct from the existing `--web` flag (both can be present). State plainly that absence of the token means no behavioral change beyond Change A.

- [x] **Task 4: Add the "Document-Driven Development (3D)" explanation block** (depends on Task 3)
  Files: `.claude/skills/aif-docs/SKILL.md`
  Add a dedicated explanation block in the skill body (place it right after Step 0.1 or as a short subsection near the top of the workflow, before Step 1) that explains what 3D **is**, so the agent proceeds without arguing. State: 3D is the docs analogue of TDD — author the documentation as if the feature is **already shipped** (present tense, target behavior, end to end); the doc is the contract and code will be written to conform to it. Documenting APIs, columns, endpoints, or files that **do not exist yet is the intended behavior in this mode, never an error or staleness**. This block is the core of the fix — make it unambiguous and instruct the agent to honor it.

- [x] **Task 5: Branch Step 1 — "Current State" → "Target State" in 3D** (depends on Task 3)
  Files: `.claude/skills/aif-docs/SKILL.md`
  In `### Step 1: Determine Current State` (~line 93), add a `MODE = 3D` branch: instead of detecting what exists today, gather what the feature **will** do from the ROADMAP milestone / spec note / user intent. The State A/B/C detection still runs (a target-state doc may be new or an update), but the **content source** in 3D is intent, not existing code. Leave the normal-mode path unchanged.

- [x] **Task 6: Suppress the staleness audit in 3D** (depends on Task 3)
  Files: `.claude/skills/aif-docs/SKILL.md`
  In `#### 2.1: Audit current documentation` (State C, ~line 404-413), branch the **"Stale content — do docs reference files/APIs that no longer exist?"** check: in `MODE = 3D` this check is **suppressed** — absent code is expected, not stale. All other audit checks (README length, navigation, broken internal links, consistency, standards compliance) still run in 3D. Leave normal-mode behavior unchanged.

- [x] **Task 7: Suppress/invert the Technical Accuracy verify in 3D** (depends on Task 3)
  Files: `.claude/skills/aif-docs/SKILL.md`, `.claude/skills/aif-docs/references/REVIEW-CHECKLISTS.md`
  In `## Step 4` (SKILL.md ~line 474) and the **Technical Checklist** in `references/REVIEW-CHECKLISTS.md` (specifically "Code examples use the project's actual commands/syntax" and "Installation instructions are real and work (verified from package manager files)"), add a `MODE = 3D` carve-out: do **not** flag non-existent code/APIs/files as broken or stale; verifying docs against the live codebase is skipped in 3D. **Keep** the Readability & Completeness checklist and the Change-A no-motivation check fully active in 3D. Make clear 3D drops *current-state* and *verify*, but **keeps no-history** — target-state docs are pure present-tense behavior with no "was added / we changed / because / this milestone" language.

- [x] **Task 8: Reinterpret the "current state only" doc-style and add the conformance pointer** (depends on Task 4)
  Files: `.claude/skills/aif-docs/SKILL.md`
  (a) Where relevant in the 3D branch/explanation, reinterpret the "describe current state only" doc-style as "describe the **target shipped state**" — present tense, behavior-focused, still no history/rationale. Reaffirm that all formatting/navigation/language rules (README-as-landing, docs-dir split, prev/next nav, cross-links, scannability, language matching, no-file-trees, skill-context overrides) apply **unchanged** in 3D.
  (b) After authoring in 3D, **print** (do not auto-insert) a conformance pointer line the user can drop into the relevant ROADMAP milestone: `implementation must conform to \`<doc-path>\``. Lean print-for-user-to-place, mirroring the `Spec:` tag rhythm — never write it into ROADMAP automatically.

### Phase 3: Register the divergence

- [x] **Task 9: Register `aif-docs` as intentionally diverged in CLAUDE.md**
  Files: `CLAUDE.md`
  In the `## Upstream Sync` section, move `aif-docs` into the **"Intentionally diverged from upstream — review diff before updating"** list with a one-line reason (e.g. "3D / target-state docs mode + always-on no-motivation rule added downstream"). Ensure it is no longer implicitly covered by "all other skills — safe to overwrite directly from upstream". Without this, the next sync wipes both changes.

## Commit Plan
- **Commit 1** (after tasks 1-2): "Add always-on state-not-process rule to aif-docs"
- **Commit 2** (after tasks 3-8): "Add 3d/3д Document-Driven mode to aif-docs"
- **Commit 3** (after task 9): "Register aif-docs as intentionally diverged from upstream"
