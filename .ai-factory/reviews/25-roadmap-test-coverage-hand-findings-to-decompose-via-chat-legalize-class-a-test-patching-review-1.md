# Code Review: roadmap-test-coverage — hand findings to decompose; legalize Class-A test patching

**Change:** `src/skills/roadmap-test-coverage/SKILL.md` (skill definition — executable agent instructions, not application code)
**Plan:** `.ai-factory/plans/25-roadmap-test-coverage-hand-findings-to-decompose-via-chat-legalize-class-a-test-patching.md`
**Spec:** `.ai-factory/notes/35-test-coverage-two-tier-handoff.md`

## Scope

The only product-affecting change is `src/skills/roadmap-test-coverage/SKILL.md`. Other staged files (`ROADMAP.md`, plan/plan-review/`.json` sidecar) are pipeline artifacts, not reviewed for logic. `ROADMAP.md` correctly drops the `---STOP---` marker and leaves the milestone unchecked — consistent with an in-flight run.

## Verification against plan + spec

All four planned tasks are implemented faithfully, and every spec-note constraint holds:

- **Task 1 (Layer 6 → "Refactor Collect"):** roadmap write removed; refactor verdicts now append to `$HANDOFF_LIST` with area name + description + note path. Step 2 (`## Refactor Required` note append) preserved verbatim. Log line reworded to "collect and continue". ✓
- **Task 2 (Layer 7 Class B):** `$ROADMAP_PATH` `## Bugs` write removed; Class B failures append to the same `$HANDOFF_LIST` with the **source file** fallback pointer and rationale. "Do NOT touch the test" retained. Classification table (lines 249–251), agent prompt, Class-A patch instruction (256–257), and re-run/all-green requirement all untouched. ✓
- **Task 3 (Layer 8):** handoff list printed as paste-ready `/roadmap-decompose` descriptions; summary lines changed to "Refactor items handed off / Class B items handed off"; per-item pointer rule (note path when researched, else source file) stated explicitly; "Do not run `/roadmap-decompose` automatically" kept. ✓
- **Task 4 (Critical Rule 1 + description):** Rule 1 now bans *new* test files and carves out the Class-A patch exception, matching Layer 7's wording — the self-contradiction is resolved. The single permitted `description` tweak ("emits refactor tasks" → "collects refactor findings") is applied; no other frontmatter field changed. ✓

Constraint checks:
- Layers 1–5 untouched — confirmed by diff. ✓
- No new file writes introduced; outputs remain Layer-4/6 notes + Layer-7 Class-A patches. ✓
- Body is 330 lines, well under the 500-line cap. ✓
- Critical Rule 2 ("Never write ROADMAP_TESTS.md") still accurate; the skill now writes *neither* roadmap file, which is more consistent, not less. ✓
- No stale references remain: grep finds no surviving "Test Infra", "## Bugs", "added to roadmap", or "Refactor Emit" strings. `docs/workflow.md` describes only the downstream `→ ROADMAP_TESTS.md` destination (via decompose) and never mentioned the removed `$ROADMAP_PATH` writes, so it is not made stale. ✓

## Non-blocking observations

None of these are correctness defects; they do not block.

- **Flat list, split printout.** `$HANDOFF_LIST` is a single list carrying both refactor and Class B entries, which Layer 8 renders under two headings ("Refactor:" / "Bugs (Class B …)"). The skill relies on the orchestrator distinguishing the two kinds by content (refactor description vs. failure reason) rather than an explicit type tag. An LLM orchestrator handles this correctly, but a one-word tag per entry would make the split unambiguous if this is ever revisited.
- **In-memory durability.** Class B handoff items live only in `$HANDOFF_LIST` until Layer 8 prints them (refactor items are additionally persisted to their Layer-4 note). If a run aborts between Layer 7 and Layer 8 they are lost — negligible for a single-session, user-present chat skill, matching the plan-review-2 note.
- **Minor redundancy.** The summary block ends with "Next step: /roadmap-decompose" and the following block again says "paste into /roadmap-decompose". Harmless.

## Verdict

The change implements the plan and spec exactly, resolves the two structural defects the milestone targeted (underspecified roadmap writes; Rule 1 ↔ Layer 7 contradiction), preserves every "keep intact" element, and introduces no runtime or consistency regressions.

REVIEW_PASS
