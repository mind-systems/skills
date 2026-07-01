# Code Review (pass 2): roadmap-decompose-skeleton (plan 19)

**Plan:** `.ai-factory/plans/19-roadmap-decompose-skeleton-new-skill-skeleton-tdd-concurrency-decomposition-lens.md`
**Changes reviewed:** `git diff HEAD` — new `src/skills/roadmap-decompose-skeleton/SKILL.md`, `CLAUDE.md` registration, plus incidental adjacent-milestone changes (`roadmap-engine` → `Read`-only, `roadmap-decompose` load-once wording, notes 27/31/32, `ROADMAP.md`).
**Risk Level:** 🟡 Low–Medium — no runtime-breaking bug; one design gap that will produce messy roadmap state, plus a nit.

## Status of review-1 findings (both resolved)

- **Finding 1 (validator FAIL on frontmatter word count) — FIXED.** The `description` was trimmed (715→612 chars; frontmatter 113→99 words). `validate.sh` now reports **PASSED** with 0 errors.
- **Finding 2 (Step 0 didn't explicitly read the roadmap) — FIXED.** Step 0 now has an explicit line (`SKILL.md:67–70`): "**Read the target roadmap** … and collect its open `- [ ]` tasks — this is the set the three lenses run over."

## New findings

### 1. Disposition of the *source* task after decomposition is unspecified (MEDIUM)

The skill splits an **existing open `[ ]` task** — one that, per the two-tier format, already has a contract line **and** a numbered `Spec:` note — into a skeleton/TDD/impl chain. But nothing states what happens to that original line and note. Step 4 (`SKILL.md:120–128`) says only: "produce the two-tier artifact (contract line + spec note) for **each resulting task**," and Step 2 (105–111) refers to "the impl milestone" without ever saying the impl milestone **is** the original task kept in place.

Two concrete failure modes at runtime:

- **Duplicate impl + orphaned note.** If "each resulting task" is read to include the impl task (and impl == the original), the skill renders a *new* contract line and a *new* `Spec:` note (fresh `<NN>`) for it — leaving the original line/note as a duplicate or orphan. The roadmap ends with two impl entries for one task and two notes.
- **Silent loss of the original spec.** Conversely, an agent that decides to "replace" the original line with the decomposed set may drop the original `Spec:` note reference without migrating its content.

The sibling this skill is modeled on handles exactly this: `roadmap-decompose` Mode 2.5 ("Decompose Existing") spells out the note-handling rule — "If the milestone already carries a `Spec:` tag, update the named note file in place with `Write`; the contract line's `Spec:` tag stays unchanged." This skill has **no** equivalent instruction, even though its whole job is decomposing already-spec'd tasks. Note 27 is also silent on it, so this is a genuine hole in both spec and implementation, not just a transcription miss.

**Fix:** add one explicit rule to Step 4 — e.g. "The original open task becomes the **impl** milestone: keep its existing line and `Spec:` note in place (update the note to reflect that the skeleton/tests are now separate milestones); **insert** the new skeleton/TDD/contract milestones immediately **before** it. Do not render a second contract line or a new note for the impl task." This removes the duplicate/loss ambiguity and mirrors `roadmap-decompose`'s in-place discipline.

### 2. `Bash(git *)` is granted but never used (NIT)

`allowed-tools` includes `Bash(git *)` (`SKILL.md:14`), but the body never invokes git — Step 0 reads `DESCRIPTION.md`/`ARCHITECTURE.md`/the roadmap via `Read`, and no step runs `git log`/`git diff` (unlike `roadmap-decompose`, whose exploration step does `git log --oneline`). Harmless over-grant carried from note 27's frontmatter; drop it, or add a git-based exploration step if one was intended. Non-blocking.

## Confirmed correct (spot-checks this pass)

- Tool grant carries `Write Edit` (plan's correction to note 27); `roadmap-engine` is now `Read`-only in the same diff, so the skill's own `Edit`/`Write` is the only path that writes `ROADMAP.md` — consistent, no permission-prompt gap.
- `test-engine` used throughout with the `test-philosophy` alias noted (body 36–38); no dangling reference to a non-existent skill.
- Renders only to `ROADMAP.md`, never `ROADMAP_TESTS.md` (Step 4); target-file selection kept with the caller.
- Critical Rules preserve every "do not" from note 27 (no `roadmap-tdd`, don't copy engine bodies, don't call `roadmap-decompose` at runtime, don't touch orchestrator, don't touch closed `[x]` tasks).
- CLAUDE.md: both the "never overwrite" list and the Repository Structure tree updated; validator passes.

## Conclusion

The two review-1 findings are fixed. The remaining item is Finding 1 — a decomposition-semantics gap (source-task disposition) that will duplicate milestones or orphan a spec note at runtime unless an in-place rule is added to Step 4. Recommend closing it before implementation; Finding 2 is a cosmetic over-grant.
