# Test Coverage — Full Workflow (Session Record)

**Date:** 2026-05-18
**Source:** conversation context — mind_api project

## Key Findings

- Writing tests for a real codebase is a 5-step pipeline, not a single command. Each step gates the next.
- "Which areas to test" requires a silent-failure filter, not a "has logic?" filter — otherwise you get near-exhaustive lists.
- Testability review must happen before task decomposition, not after — an untestable class breaks the entire test spec before a single assertion is written.
- Architecture refactors that unblock testability should be tracked as explicit roadmap tasks so they don't get lost or done inline during spec writing.
- Existing tests should be run before creating new test tasks — broken tests reveal API drift that would otherwise corrupt all new specs.

## Details

### The Full Workflow (inputs and steps in order)

This is the exact sequence of user inputs and agent actions that produced a clean, ready-to-implement test roadmap from a codebase with no test plan.

---

#### Step 1 — `/roadmap-test-coverage` (no args)

**User input:** run the skill.

**What happened:**
- Read `.ai-factory/DESCRIPTION.md`, `ARCHITECTURE.md`, `ROADMAP.md`
- Ran `find . -name "*.spec.*"` to map existing coverage
- Identified 12 testable areas (services and controllers with no spec or partial spec)
- Presented the list to user with coverage classification (no coverage / partial / full)

**Output:** list of 12 areas.

---

#### Step 2 — Apply the silent-failure filter

**User input:** read `/Users/max/projects/skills/.ai-factory/notes/05-roadmap-test-coverage-filter-redesign.md` before proceeding.

**What happened:**
- Read the note, which introduced the decisive filter question:
  > *"If the logic here breaks, will the system signal it immediately, or continue silently?"*
- Re-evaluated all 12 areas through this lens
- Dropped 3 that fail loudly: `GrpcAuthInterceptor` (throws UNAUTHENTICATED), `grpc-mappers` (TypeScript catches type errors), `DeviceService` (upsert failures are visible)
- Kept 9 that fail silently: cursor off-by-one, missed sync events, wrong session state, etc.

**Output:** filtered list of 9 areas.

**Key rule:** do not skip this filter step. Without it, the agent produces ~exhaustive lists that contradict the "test what matters" philosophy.

---

#### Step 3 — Launch parallel research agents

**User input:** "давай 9" (all 9).

**What happened:**
- Determined next note number (existing notes 01–05 in mind_api → next is 06)
- Launched 9 `Explore` subagents in parallel, one per area
- Each agent: read source file + dependency files, identified mocks needed, produced test case list
- 6 agents returned immediately; 3 hit rate limits → re-launched
- Saved 9 notes: `06-changelog-service-test-plan.md` through `14-stats-worker-test-plan.md`

**Output:** notes 06–14 in `mind_api/.ai-factory/notes/`.

**Each note contains:**
- Source overview (role in the system)
- Instantiation instructions (mocks needed, constructor pattern)
- Existing coverage summary
- Test cases grouped by method, with description + method + non-obvious setup
- Gotchas (timer faking, private fields, fire-and-forget async, etc.)

---

#### Step 4 — Testability review

**User input:** "давай посмотрим, везде ли архитектура получилась готовой к тестированию"

**What happened:**
- Read all 9 source files in parallel
- Assessed each for: injectable dependencies, hidden global state, hard-to-mock imports, async patterns that complicate teardown assertions

**Findings:**

| Class | Status | Issue |
|---|---|---|
| `ActiveStreamRegistry` | ✅ clean | no deps |
| `SyncStreamService` | ✅ clean | fake timers needed |
| `ActivitySessionStore` | ✅ clean | ConfigService mock + fake timers |
| `SyncService` | ✅ clean | one dep |
| `StatsWorker` | ✅ clean | one dep |
| `ChangelogService` | ✅ clean | QueryBuilder chainable mock (standard pattern) |
| `PersonalAccessTokenService` | ✅ clean | crypto — let real run, no mock needed |
| `ModuleStateGrpcController` | ⚠️ refactor needed | user extracted from `(metadata as any)[GRPC_USER_KEY]` |
| `SyncStreamGrpcController` | ✅ clean | user via `@GrpcCurrentUser()` typed param |

**The one issue:** `ModuleStateGrpcController.trackActivity(request, metadata?)` extracts the user manually from `(metadata as any)[GRPC_USER_KEY]`. In tests this requires constructing a fake `Metadata`-shaped object with the constant as a key — awkward and fragile. `SyncStreamGrpcController` already uses `@GrpcCurrentUser()` which makes `user` a plain typed second argument — clean to test.

**Both gRPC controllers note:** `replay().catch()` / `setup().catch()` pattern (fire-and-forget async inside Observable) means teardown assertions need `await new Promise(r => setTimeout(r, 0))` or `jest.runAllTimersAsync()` to settle microtasks. Not a bug, inherent to streaming.

---

#### Step 5 — Add refactor task to roadmap

**User input:** "давай этот рефакторинг зафиксируем как таск в роадмап"

**What happened:**
- Added Phase 15 to `mind_api/.ai-factory/ROADMAP.md`:
  > Replace `metadata?: Metadata` with `@GrpcCurrentUser() user: JwtPayload | null` in `trackActivity`
- Updated note 12 (`module-state-grpc-controller-test-plan.md`) to reflect the post-refactor API:
  - Removed references to `GRPC_USER_KEY` and metadata construction
  - Simplified auth test cases to `controller.trackActivity(request$, null)` and `controller.trackActivity(request$, mockUser)`

**User then performed the refactor** and confirmed it was done.

---

#### Step 6 — `/roadmap-decompose` to create test tasks

**User input:** `/roadmap-decompose таск выполнен, давай таски на тесты`

**What happened:**
- Skill detected "тесты" keyword → `$TARGET_FILE = .ai-factory/ROADMAP_TESTS.md`
- File didn't exist → Mode 1: Create
- Marked Phase 15 in ROADMAP.md as `[x]`
- Created `ROADMAP_TESTS.md` with 11 milestones ordered by ascending complexity:

| # | Milestone | Why this order |
|---|---|---|
| 1 | StatsWorker — add missing tests | additive to existing spec, fastest win |
| 2 | ActiveStreamRegistry spec | zero deps |
| 3 | SyncService spec | one dep, no timers |
| 4 | PersonalAccessTokenService spec | two repos, crypto ok |
| 5 | ChangelogService spec | QueryBuilder mock |
| 6 | SyncStreamService spec | fake timers, no deps |
| 7 | ActivitySessionStore spec | fake timers + config |
| 8 | ModuleStateGrpcController — lifecycle | Observable + async setup |
| 9 | ModuleStateGrpcController — routing | 5 command branches |
| 10 | SyncStreamGrpcController — replay | cursor logic, hasMore loop |
| 11 | SyncStreamGrpcController — buffer/live/teardown | gap prevention, dedup |

Controllers are split into 2 tasks each because stream lifecycle and command routing can be implemented and reviewed independently.

---

#### Step 7 — Run existing tests

**User input:** "давай теперь запустим уже существующие тесты и посмотрим, все ли они выполняются"

**What happened:**
- Ran `npm test`
- 113/114 passed
- 1 failure: `auth.service.spec.ts` — `toHaveBeenCalledWith('valid-code')` but `exchangeCodeForProfile` was called with `('valid-code', undefined)` (second arg `redirectUri` added to the method signature but test not updated)
- Fixed: added `undefined` as second expected arg
- All 114 tests pass

---

### Why this can't be collapsed into one command

The workflow requires distinct human judgment at three points:

1. **After coverage scan** — deciding which areas are worth testing (silent-failure filter). An agent can apply the filter mechanically, but the first run without the filter instruction produced a near-exhaustive list.

2. **After testability review** — deciding whether to refactor first or work around the architectural issue in tests. Working around it (fake metadata objects) is possible but creates fragile tests. Refactoring first is better but costs a sprint item.

3. **After creating test tasks** — running existing tests before starting new spec work. If existing tests are broken, the new specs may mask or duplicate the breakage.

### What a future autonomous agent would need

To run this workflow without human checkpoints:

1. Always apply the silent-failure filter (encoded in the skill prompt) — done via note 05
2. Always run a testability review pass before decomposing into tasks
3. Emit refactor tasks to ROADMAP.md before creating test tasks in ROADMAP_TESTS.md
4. Always run `npm test` (or equivalent) before saving test task plans, and fix broken specs as part of the workflow

## Open Questions

- Should the testability review be a named sub-step inside `roadmap-test-coverage`, or a separate skill that runs between `roadmap-test-coverage` and `roadmap-decompose`?
- Should refactor tasks emitted during testability review go into ROADMAP.md (main roadmap) or a separate ROADMAP_REFACTOR.md? Currently they went into ROADMAP.md which is correct — they're real implementation work, not just test scaffolding.
- The split of large controller specs into 2 tasks each (lifecycle + routing) was done manually. Should the atomicity gate in `roadmap-decompose` automatically detect "more than N test cases → split"?
