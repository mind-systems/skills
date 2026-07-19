# roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, not manifest-sniffing

Phase 20. Phase 8 (task 8.1, spec 61) rewrote Layer 5's testability axis to be stack-parametric, graded on substitution-friction in `$STACK`'s own idiom rather than a TS/NestJS-only DI check — and every one of its three review rounds flagged the same forward gap, correctly left out of that task's four-file boundary: on a Python repo `$STACK` arrives guessed or empty, so Layer 5 judges friction with no stack idiom to reason in. The reviewers framed this as "Layer 1 has no Python detector," but that framing is itself the defect: Layer 1's first bullet already reads `.ai-factory/ARCHITECTURE.md` for module boundaries and folder structure, and `aif-architecture` generates a `- **Tech stack:** [language, framework]` line in every project's `## Decision Rationale` for exactly this purpose — generic across whatever stack the project uses. Layer 1 ignores that already-read field and instead re-derives `$STACK` by grepping a closed, hard-coded list of package manifests (`package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`). Adding Python to that list would still leave the same gap open for the next stack not on it (Rust workspaces without a root `Cargo.toml`, Elixir, Java/Gradle, anything) — this is a generic-skill regression, not a Python-specific one, so the fix is generic: consult the project's own declared stack first, never grow the hard-coded list again.

## Current state (grounded, verified live)

- `src/skills/roadmap-test-coverage/SKILL.md:25-37` — Layer 1 ("Load Project Context") already reads `.ai-factory/ARCHITECTURE.md` at its first bullet (`:27`), then separately stores `$STACK`, `$TEST_CMD`, `$ROADMAP_PATH` and infers stack with one line (`:37`): "Infer stack from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`." The two reads are disconnected — ARCHITECTURE.md's own declared stack is never consulted for `$STACK`.
- `src/skills/aif-architecture/references/architecture-template.md:11` — every generated `ARCHITECTURE.md` carries `## Decision Rationale` → `- **Tech stack:** [language, framework]`, filled in for the project's actual stack, whatever it is (not a fixed language list).
- `SKILL.md:158` — Layer 5 passes `$STACK` from Layer 1 as `<stack>` into the per-file agent prompt; an unfilled or guessed `$STACK` here is exactly the failure mode 8.1's review flagged.

## Change

- Reorder Layer 1's stack resolution so the already-read `ARCHITECTURE.md` is the first source: if the file exists and its `## Decision Rationale` → `- **Tech stack:** ...` line is filled in (not the literal unfilled template placeholder), `$STACK` is that value, verbatim.
- The four-manifest sniff (`package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`) becomes the **fallback**, used only when `ARCHITECTURE.md` is absent or its Tech stack line is empty/still the placeholder — unchanged in every other respect (same four detectors, same order, same output shape).
- No new per-language detector is ever added to the fallback list again — a project that needs a stack the fallback can't sniff is expected to have an `ARCHITECTURE.md` (per this same repo's own harness doctrine that ARCHITECTURE.md is the entry map of space), which this fix now actually uses.

## Files & types

- edit: `src/skills/roadmap-test-coverage/SKILL.md` (Layer 1 only — `:25-37`)
- read-only: `.ai-factory/specs/61-test-coverage-l5-substitution-friction-axis.md` (Phase 8's spec, for the friction-axis contract this task must not touch); Layers 2–8 of the same file; `src/skills/aif-architecture/references/architecture-template.md` (confirms the field name/shape, not edited)

## Guards

- **Layer 1 only.** No change to Layer 5's friction-axis prompt, its verdict grammar, or any other layer.
- **No new hard-coded stacks.** The fallback's four detectors keep their current order and wording, unextended — this task closes the class of gap, not one instance of it.
- **Placeholder-aware.** A project whose `ARCHITECTURE.md` still carries the unfilled template line (`[language, framework]`) must fall through to the manifest sniff, not store the literal placeholder text as `$STACK`.
- **Don't fold into the friction axis.** This task is pure stack-resolution plumbing; it carries no opinion about what counts as friction in any stack (that is Layer 5's, already settled by spec 61).

## Verification

- `grep -n "Tech stack" src/skills/roadmap-test-coverage/SKILL.md` → at least one hit in Layer 1, naming `ARCHITECTURE.md`'s field as the primary source.
- The four fallback detectors are still present, unreordered, unextended: `grep -n "package.json\|pubspec.yaml\|go.mod\|Cargo.toml" src/skills/roadmap-test-coverage/SKILL.md` still resolves to the same Layer 1 fallback line, four items only.
- Behavior-baseline, two live runs: (1) a scratch project with an `ARCHITECTURE.md` whose Tech stack line reads e.g. `Python, pytest` and no `package.json`/etc. — Layer 1 resolves `$STACK` to that value, not empty; (2) a scratch project with no `ARCHITECTURE.md` but a `package.json` — Layer 1 falls through and resolves `$STACK` via the existing manifest sniff, unchanged from today. Discard both scratch fixtures after the check; neither is committed.
