# roadmap-test-coverage: emit findings via decompose handoff; legalize Class-A test patching

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- `src/skills/roadmap-test-coverage/SKILL.md` breaks the pipeline's two-tier invariant in two places: **Layer 6** writes refactor tasks into `$ROADMAP_PATH` as plain text ("Task text = the refactor description from the verdict") under a `## Test Infra` phase, and **Layer 7** writes Class B bug tasks the same way ("Task text = area name + reason") under a `## Bugs` phase. Neither gets a contract line or a `Spec:` note — these tasks reach the orchestrator underspecified, which is exactly the failure mode the rest of the pipeline exists to prevent.
- The skill also contradicts itself: **Critical Rule 1** says "Never write test files — research and planning only", while **Layer 7** instructs "For each Class A failure: patch the failing test". Patching Class-A (API-drift) tests is intentional and stays — the rule must carve out the exception instead of banning it.
- Design intent (from the user): this skill should not write roadmap tasks at all — it hands control to `/roadmap-decompose` via chat, so the decompose skill's full two-tier machinery is not duplicated here.

## Details

### Edit 1 — Layer 6 (Refactor Emit)

Remove the write to `$ROADMAP_PATH` (step 1 of Layer 6). Instead, collect each `needs-refactor` verdict into an in-memory handoff list: area name + one-sentence refactor description + pointer to its Layer-4 note. **Keep** step 2 unchanged — appending the `## Refactor Required` section to the corresponding Layer-4 note is note content and stays. Rename the layer accordingly (e.g. "Refactor Collect").

### Edit 2 — Layer 7 (Class B escalation)

Remove the write to `$ROADMAP_PATH` for Class B failures. Instead, add each Class B failure to the same handoff list: area name + reason from the classification. The "Do NOT touch the test" instruction for Class B stays. The classification table stays as-is (per user: tables about code are fine here).

### Edit 3 — Layer 8 (Hand Off)

Extend the final printout: after the existing summary, print the handoff list as concrete task descriptions to feed `/roadmap-decompose` — refactor items and Class B bug items, each one line with its source note path. Keep "Do not run `/roadmap-decompose` automatically" — the handoff is via chat, the user triggers decompose. Update the summary lines ("Refactor tasks added to roadmap: M" / "Silent bugs escalated to roadmap: J") to reflect that items are handed off, not written.

### Edit 4 — Critical Rule 1

Reword to legalize the existing Layer 7 behavior: never write **new** test files — research and planning only; the single allowed write is Layer 7's patching of existing Class-A failures (tests broken by API drift, not by implementation bugs), keeping assertions intact and updating only call signatures.

### Constraints

- Layers 1–5 untouched. Agent prompt templates in Layers 4/5/7 untouched except the Layer 7 table stays.
- No new writes anywhere: after this change the skill's only file outputs are Layer-4/6 notes and Layer-7 Class-A test patches.
- Frontmatter unchanged. Body ≤ 500 lines.

## What NOT to do

- Do not auto-invoke `/roadmap-decompose` from Layer 8 — hand off via chat only.
- Do not remove the Layer 7 classification table or convert it to prose.
- Do not ban Class-A patching — legalize it as the explicit exception.
