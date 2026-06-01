# Document-Driven Development — target-state docs mode for aif-docs

**Date:** 2026-05-31
**Source:** conversation context (recurring workflow request)

## Key Findings

- **3D = Document-Driven Development**, the docs analogue of TDD: author the documentation page **as if the feature is already shipped** (present tense, target/current-state, behavior-focused), then implement the code to conform to the doc. The doc becomes the contract / source of truth; the implementation must match it, not the other way around.
- This is a **recurring** request — the user has spelled out the same instruction more than once ("write it as if the feature is already done; don't describe the task or why we changed anything; describe the target state").
- The default `aif-docs` skill is **wrong** for this: its Core Principles mandate "Describe current state only" and it audits for "stale content referencing files/APIs that no longer exist." Under 3D, a doc that describes not-yet-built behavior is intentional, not stale — a normal `aif-docs` run would flag or refuse it.
- The user wants a **dedicated command** (or a flag/mode) that switches `aif-docs` into target-state authoring behavior.

## Details

### The behavior the new command must have
Same output conventions as `aif-docs` (behavior-not-code, no file trees, match neighboring docs' language & style, obey project doc rules such as "no prev/next nav, no See Also" when present), **plus** these overrides:

1. **Write target state as if shipped.** Present tense, the feature works now. Describe how it behaves, end to end.
2. **Do NOT describe the task, the change, or the rationale.** No "was added", "we changed", "this milestone", no history. Pure target behavior.
3. **Do NOT verify against the live codebase / do NOT flag not-yet-existing APIs, columns, endpoints as stale or broken.** The whole point is documenting ahead of implementation. The skill's audit/standards-compliance steps that assume shipped code must be suppressed in this mode.
4. **Optionally wire the doc as the conformance target**: emit a pointer the user can drop into the relevant ROADMAP milestone ("implementation must conform to `<doc>`"), so the implementing task treats the doc as the spec.

### Worked example from this session (mind_api)
- `docs/auth/rate-limiting.md` was authored in Russian describing OTP send-cooldown + per-code verify lockout + per-IP REST throttle **as current behavior**, before Phase 27 (the implementing milestone) exists in code.
- `ARCHITECTURE.md` gained a target-state invariant (client IP = TCP peer, `trust proxy` off).
- The ROADMAP milestone (Phase 27) was annotated: "implementation must conform to `docs/auth/rate-limiting.md`."
- Net: the doc + architecture invariant are the contract; the code will be written to match them.

### Design options for the command
- **(a) A flag/mode on `aif-docs`** — e.g. `/aif-docs --target` (a.k.a. `--3d` / `--spec`). Lightest: reuses all existing templates and topic structure; just flips the "current-state + verify" assumptions to "target-state + no-verify". Best fit for "change the behavior of the docs skill".
- **(b) A separate skill** — e.g. `/aif-doc-first` or `/aif-docs-spec`. More discoverable as a distinct workflow, but duplicates most of `aif-docs`.
- Leaning toward **(a)**: a documented mode inside `aif-docs` that branches the Core Principles and skips the codebase-verification / staleness-audit steps. The user's phrasing ("спец команда, которая будет менять поведение докс скила") explicitly frames it as altering `aif-docs` behavior.

### Where it changes aif-docs internals (for the implementer of this skill)
- `aif-docs` SKILL.md Core Principle "Describe current state only" → in target mode becomes "Describe the target state as if shipped".
- Step 2.1 audit / Step 4 review "stale content referencing files/APIs that no longer exist" and "Technical Accuracy" checks → suppressed or inverted in target mode (do not treat absent code as an error).
- Keep all formatting/navigation/language rules and the project skill-context overrides intact.

## Open Questions

- **Command vs flag** — dedicated `/aif-doc-first` skill, or a `--target`/`--3d` flag on `aif-docs`? (Leaning flag/mode.)
- **Marking aspirational docs so a later *normal* `aif-docs` audit doesn't flag them.** Between authoring and shipping, a standard audit would see the doc as describing non-existent behavior. Need a convention — e.g. a transient front-matter marker (`status: target`), or relying on the ROADMAP conformance link — that the audit step recognizes and skips until the milestone is marked done. Without this, the two modes fight each other.
- **Should the command auto-insert the ROADMAP conformance pointer**, or just print it for the user to place?
