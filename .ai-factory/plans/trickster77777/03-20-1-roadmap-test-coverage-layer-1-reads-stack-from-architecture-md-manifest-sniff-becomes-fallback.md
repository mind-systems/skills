# Plan: 20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback

## Context
Layer 1 of `roadmap-test-coverage` already reads `.ai-factory/ARCHITECTURE.md` but resolves `$STACK` by re-deriving it from a closed four-manifest sniff. This task makes ARCHITECTURE.md's own `- **Tech stack:** ...` line the primary source for `$STACK` and demotes the manifest sniff to an unextended fallback, closing the class of "missing per-language detector" gaps instead of one instance.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Layer 1 stack resolution

- [x] **Task 1: Reorder `$STACK` resolution in Layer 1**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Edit **only** the Layer 1 block at `:25-37` (currently: the read-in-order list, the `Store: $STACK / $TEST_CMD / $ROADMAP_PATH` line, and the single-line `Infer stack from package.json / pubspec.yaml / go.mod / Cargo.toml.`).
  Rewrite the stack-resolution wording so it reads as an ordered two-source rule:
  1. **Primary** — if `.ai-factory/ARCHITECTURE.md` (already read at the first bullet of the same layer) has a `## Decision Rationale` → `- **Tech stack:** ...` line that is filled in, `$STACK` is that value verbatim.
  2. **Fallback** — only when the file is absent, the line is missing/empty, or the line still carries the unfilled template placeholder `[language, framework]`, infer the stack from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`.
  Carry an explicit sentence that the fallback list is never extended with new per-language detectors — a project needing a stack it cannot sniff is expected to declare it in `ARCHITECTURE.md`.
  **Keep `$TEST_CMD`'s manifest read unconditional.** Today's single line at `:37` is the only instruction in the whole skill that opens a manifest, and it is where `$TEST_CMD` implicitly comes from (`npm test` out of `package.json`'s scripts, `cargo test` out of `Cargo.toml`, …); `ARCHITECTURE.md` cannot cover for it — the template has a `Tech stack` field and no test-command field. Making the manifest read conditional on the `$STACK` branch would leave `$TEST_CMD` empty on the primary path, and Layer 7 both executes it (`:260`) and re-runs it as a hard gate (`:316`). So write the two resolutions as **independent**: the ordered primary/fallback rule governs `$STACK` only, and a separate sentence states that the manifest is still consulted for `$TEST_CMD` regardless of which source `$STACK` came from.
  Keep the four detectors in their current order and wording, four items only. Keep the `Store:` line and its example values intact. Match the file's existing register (terse imperative prose, no tables).
  Reference for the field name/shape (read-only, not edited): `src/skills/aif-architecture/references/architecture-template.md:11`.

- [x] **Task 2: Verify guards and behavior-baseline** (depends on Task 1)
  Files: `src/skills/roadmap-test-coverage/SKILL.md` (verification only, no further edits unless a check fails)
  - `git diff` on the file touches Layer 1 only — Layers 2–8 byte-identical; nothing in Layer 5's friction-axis prompt (`:155-234` — `$STACK` passed as `<stack>` at `:158`, verdict grammar at `:230-234`) changes.
  - `grep -n "Tech stack" src/skills/roadmap-test-coverage/SKILL.md` → at least one hit inside Layer 1, naming `ARCHITECTURE.md`'s field as the primary source.
  - `grep -n "package.json\|pubspec.yaml\|go.mod\|Cargo.toml" src/skills/roadmap-test-coverage/SKILL.md` → still the same single Layer 1 fallback line, four items, unreordered, unextended.
  - Placeholder guard: the rewritten text explicitly names the literal `[language, framework]` placeholder as a fall-through condition, so it is never stored as `$STACK`.
  - Behavior-baseline, three scratch fixtures outside the repo tree (discard all three afterwards; commit none). **DEVIATION from spec 79:33**, which specifies two live runs — fixture (3) is added on plan-review round 1, which found that neither of the spec's two fixtures exercises the ARCHITECTURE.md-plus-manifest combination where `$TEST_CMD` regresses: (1) a project with an `ARCHITECTURE.md` whose Tech stack line reads e.g. `Python, pytest` and no manifest file → Layer 1 resolves `$STACK` from that line; (2) a project with no `ARCHITECTURE.md` but a `package.json` → Layer 1 falls through to the manifest sniff, unchanged from today; (3) **both present** — a filled Tech-stack line *and* a `package.json` → `$STACK` comes from `ARCHITECTURE.md` while `$TEST_CMD` still resolves to `npm test`. Fixture (3) is the combination the other two never exercise and the one that regresses if the manifest read is nested under the `$STACK` branch.
