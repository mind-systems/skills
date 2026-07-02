## Code Review Summary

**Files Reviewed:** 2 target files (`roadmap-engine/SKILL.md`, `roadmap-decompose/SKILL.md`) + governing note 38 + ROADMAP + ARCHITECTURE
**Risk Level:** 🟢 Low

The plan is a well-scoped boundary cleanup. All line references were verified against the live files, all four tasks map cleanly to real content, and the guards match spec note 38 exactly. Two non-blocking advisories below for the implementer.

### Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy")** — PASS. The plan makes the engine caller-agnostic and forbids a caller/"used by" registry, which is precisely what the architecture mandates ("the engine holds no policy and never drives … engines never list their callers"). Removing the two caller mentions aligns the code with the stated design.
- **Rules (`.ai-factory/RULES.md`)** — N/A (file not present).
- **Roadmap (`.ai-factory/ROADMAP.md`)** — PASS. Milestone linkage is intact: ROADMAP line 67 matches the plan heading verbatim and points to `Spec: .ai-factory/notes/38-engine-caller-boundary.md`, which the plan follows faithfully (both engine edits + both decompose edits + all three "What NOT to do" guards are carried into the plan's Notes).

### Verification performed

- **Task 1/2 targets exist and are exhaustive.** Grep of `roadmap-engine/SKILL.md` for `decompose|caller|outline|skeleton|used by|loaded by` returns exactly two hits — the description sentence (line 6) and the body parenthetical (line 19). These are the two the plan targets; no caller mention is missed.
- **Task 1 char budget is safe.** Current description body is ~357 chars; removing a sentence only shrinks it — comfortably under the 1024 limit.
- **Task 3 target block exists.** The fenced ```markdown``` roadmap-format block is present at decompose lines 93–102, and the "Rules for milestones" list (lines 104–108) the plan preserves is real and correctly identified as decompose's own philosophy.
- **Task 4 scope is correct.** Grep confirms the remaining `roadmap-engine` references in decompose (lines 6, 11, 17, 137, 188, 209, 292) are all by-name pointers, not inline format copies — so after Task 3 the only inlined format block is gone and Task 4's "verify nothing remains" is satisfiable.
- **Placeholder-tag nuance handled.** The engine's own roadmap file format (lines 42–52) uses real `Spec:` note paths, but the plan's replacement text uses placeholder `` Spec: `<note pending>`. `` tags for the 1.3 draft. This deviation is intentional and explicitly stated — good, and it stays consistent with the existing "Rules for milestones" placeholder (line 106) and the 1.4 real-render step (line 137).

### Critical Issues

None. Nothing here blocks implementation.

### Advisories (non-blocking WARN)

1. **The "format is available at 1.3" assumption is loose.** Task 3 (echoing note 38: "the engine is loaded at 1.3 anyway for drafting") justifies the pointer with "roadmap-engine is already declared in `loads:` and referenced elsewhere." Note that `loads:` in frontmatter is a *static declaration*, not an in-context load — decompose only actually invokes the Skill ("ensure `roadmap-engine` is loaded once this chat") at Steps 1.4/2.4/2.5, never at 1.3. So after this edit, the 1.3 drafting step points at a format that may not yet be in context. This is **acceptable and not a defect**: the 1.3 output is a loose in-memory draft shown to the user, and the authoritative format-conformant artifacts are rendered at 1.4 with the engine loaded. Recommendation: keep the pointer, but do **not** react by adding an early engine load at 1.3 (that would be an out-of-scope behavior change). Optionally have the replacement sentence make clear the format-conformant render happens at 1.4 — the draft only needs to approximate the shape.

2. **Avoid a duplicated "draft in memory" sentence.** Decompose line 91 already reads "Draft the roadmap **in memory (do not write `$TARGET_FILE` yet)**. The format to build toward:". The plan's replacement instruction repeats "draft the roadmap in memory (do not write `$TARGET_FILE` yet)". If the implementer deletes only the fenced block (lines 93–102) and leaves line 91, the result will have the dangling lead-in "The format to build toward:" followed by a near-duplicate sentence. Recommendation: replace lines 91–102 as a single unit (intro lead-in + fenced block) with the one new pointer sentence, so no redundant "draft in memory" phrasing survives.

### Positive Notes

- Line references throughout the plan are accurate against the live files — no drift.
- Scope is correctly confined to the engine + decompose; outline/skeleton slimming is deferred to the separate downstream milestones (notes 43/44/45), so no scope bleed.
- All three note-38 guards (don't change the two-tier format, don't move decomposition philosophy into the engine, don't add a caller registry) are carried verbatim into the plan's Notes, and "Never touch `upstream/ai-factory/`" is honored.
- Single-commit strategy with a clear message is appropriate for this boundary cleanup.

PLAN_REVIEW_PASS
