# Plan: roadmap-decompose-skeleton — skeleton/TDD/concurrency decomposition lens

## Context
Adds a new `aif-roadmap`-family skill that runs a second decomposition pass over **open** `[ ]` roadmap tasks along the spec-before-code axis (skeleton-first, TDD, concurrency contract), owning only the three lenses and delegating format to `roadmap-engine` and the silent-failure rule to the shared test-philosophy engine — copying neither.

**Assumption (naming):** The spec note (`27-…`) and roadmap line refer to the silent-failure engine as `test-philosophy`, but the skill actually installed in this repo is named **`test-engine`** (`src/skills/test-engine/`, `user-invocable: false`), and its own description already states it is "Loaded by roadmap-test-coverage and **roadmap-decompose-skeleton**". This plan therefore invokes `test-engine` at runtime and mentions the `test-philosophy` label only as an alias. If the intent was to rename `test-engine` → `test-philosophy`, that is out of scope for this milestone.

**Correction to note 27 frontmatter (`allowed-tools`):** Note 27 §Frontmatter lists `allowed-tools: Read Glob Grep Bash(git *) AskUserQuestion Skill` — with no write grant. But the skill's core behavior is to **render** skeleton/TDD/contract lines into an existing `ROADMAP.md`, which is an `Edit` (and, when the roadmap doesn't yet exist, a `Write`). No delegate performs that write: `roadmap-engine` is `Read`-only (describes the format), `aif-note` writes only the numbered spec-note files under `.ai-factory/notes/` and never touches `ROADMAP.md`, and this skill is forbidden from calling `roadmap-decompose` at runtime (the hand-off escape hatch `roadmap-test-coverage` uses). The sibling `roadmap-decompose`, which does the equivalent roadmap editing, carries `Read Write Edit …`. This plan therefore **adds `Write Edit`** to the grant, diverging from note 27 deliberately.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Author the skill

- [x] **Task 1: Create SKILL.md frontmatter, overview, and call graph**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Create the skill directory and `SKILL.md`. Frontmatter per note §Frontmatter with the corrected tool grant — `name: roadmap-decompose-skeleton` (must equal the directory name), the given multi-line `description`, `argument-hint: "[phase/slug or task description]"` (quoted brackets — required for YAML), `disable-model-invocation: true`, `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`. **Note:** `Write Edit` are added beyond note 27's list — the skill must edit `ROADMAP.md` to insert contract lines (and create it if absent); see the "Correction to note 27 frontmatter" assumption above. This matches the sibling `roadmap-decompose`'s grant. Follow the sibling `roadmap-decompose/SKILL.md` heading style. Write the intro (a *second* pass over already-atomic open `[ ]` tasks — splits on spec-before-code, not deliverability) and a **Load-once / dependencies** section: this skill owns no reusable body — it loads `roadmap-engine` (two-tier artifact format) and the silent-failure test engine (installed as `test-engine`; alias "test-philosophy") each **once per chat** via the Skill tool, and never re-invokes them per task. State the call graph (`roadmap-decompose-skeleton → roadmap-engine → aif-note`; `→ test-engine`) and that it does **not** call `roadmap-decompose` at runtime (the atomic list already exists) and never reads/modifies the orchestrator.

- [x] **Task 2: Write targeting, the three lenses, ordering/fusion, deliverability, and restraint** (depends on Task 1)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Append the working body (keep total ≤ 500 lines):
  - **Targeting:** optional arg = phase / slug / single task description; default = infer the target open-`[ ]` set from context; may operate on a single task; don't over-engineer.
  - **Step 0 — Load context:** read `.ai-factory/DESCRIPTION.md` and `.ai-factory/ARCHITECTURE.md` if present (mirror `roadmap-decompose` Step 0), operate only on **open** `[ ]` tasks — never closed `[x]` ones (prune / test-coverage territory).
  - **Lens 1 Skeleton (primary):** extract an interface/abstract/type **skeleton task** — no implementation bodies — only where it makes a shared (2+ task) or non-obvious single surface testable. Restraint: contracts are usually laid first anyway; do not blanket-cover with abstract classes.
  - **Lens 2 TDD:** insert a tests-first task against the skeleton's public surface; load `test-engine` and apply the silent-failure discriminator (test only silent-failure surfaces, skip loud-failure ones); not blanket coverage. Include the m36 `PassThroughIndicator` stateful-double canon.
  - **Lens 3 Concurrency:** for a **heavy** task touching **≥2 of** {async I/O, stateful buffer/event queue, lifecycle create/deactivate}, split a **contract-task** (invariant definition + per-concurrent-caller test scenarios, **no production code**) before impl. Restraint: never split a simple task even if it nominally touches two classes. Include the m37 `drainHeap()`/dedupKey canon.
  - **Ordering & fusion:** default order skeleton → TDD → impl; **fuse** skeleton + red specs into one "contract" milestone when skeleton:impl is 1:1 (compiles + red tests; impl turns them green); **exception:** skeleton shared across 2+ impl tasks → standalone shared-scaffold milestone, each impl gets its own TDD task.
  - **Deliverability:** "deliverable" shifts to "coherent reviewable artifact in the spec-before-code chain" (skeleton commit compiles/breaks nothing; TDD/contract commits are red tests).
  - **Rendering:** all outputs (skeleton, TDD, contract) render into the **same `ROADMAP.md`** the source tasks live in (never `ROADMAP_TESTS.md`), via `roadmap-engine`'s two-tier format; target-file selection is the caller's — the engine never infers it.
  - **Critical Rules / What NOT to do:** no `roadmap-tdd` middle skill; don't copy engine/test-rule bodies; don't call `roadmap-decompose` at runtime; don't touch the orchestrator; don't split simple tasks, blanket-cover with abstract classes, or test loud-failure surfaces; restraint is first-class.

### Phase 2: Register the skill

- [x] **Task 3: Register roadmap-decompose-skeleton in CLAUDE.md** (depends on Task 2)
  Files: `CLAUDE.md`
  Add `roadmap-decompose-skeleton` to the "Custom skills — never overwrite from upstream" list under **Upstream Sync**, and insert one line for it into the `src/skills/` block of the **Repository Structure** tree. Note: that tree uses an `aif-*/` catch-all and enumerates only a subset of the roadmap family (it does not currently list `roadmap-decompose` or `roadmap-test-coverage`) — just add one alphabetically-reasonable line; do not expect all siblings to be present. Keep the existing formatting.
