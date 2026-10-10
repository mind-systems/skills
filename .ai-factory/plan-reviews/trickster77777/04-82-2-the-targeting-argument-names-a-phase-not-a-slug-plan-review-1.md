# Plan Review: 82.2 — the targeting argument names a phase, not a slug

**Plan:** `.ai-factory/plans/trickster77777/04-82-2-the-targeting-argument-names-a-phase-not-a-slug.md`
**Task spec:** `.ai-factory/specs/trickster77777/0237-the-targeting-argument-names-a-phase-not-a-slug.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap:** OK. The plan heading matches the 82.2 contract line in `.ai-factory/roadmaps/trickster77777.md` (Phase 82, "the user's placeholder is `<user-slug>`"). 82.1 is `[x]`, so 82.2 is next at the seam. The phase preamble says "The targeting hints … offer a slug neither defines; it goes, and they take a phase", and the plan does exactly that.
- **Governing spec:** `docs/philosophy/multiuser-roadmaps.md` is named on the phase. The task removes a misuse of "slug" and adds no new user-slug semantics, so nothing in this plan goes against it.
- **Rules:** No `.ai-factory/RULES.md` exists. I checked the project CLAUDE.md rule that `argument-hint` values with brackets must be quoted. The plan keeps both values quoted and asks for a YAML parse check. OK.
- **Architecture:** No boundary is touched. These are text edits inside two lens skills. OK.
- **Skill-context:** There is no `.ai-factory/skill-context/aif-review/SKILL.md` (WARN, informational only).

### Verification against ground truth

- `src/skills/roadmap-outline-deep/SKILL.md`: frontmatter line `argument-hint: "[phase or slug]"` is present. § "Targeting" opens "Optional arg — a phase or slug (matching `argument-hint`). Default: infer the target phase set from conversation context." The plan's before-texts match the file exactly, and its after-texts match the spec's pinned after-texts exactly.
- `src/skills/roadmap-decompose-skeleton/SKILL.md`: `argument-hint: "[phase/slug or task description]"` and "Optional arg — a phase, slug, or single task description." are both present. The before-texts and after-texts match the file and the spec.
- The rest of each Targeting paragraph is preserved word for word. Reflowing the hard-wrapped lines is allowed, which is right, because the new first lines get shorter.
- The slug's removal leaves no orphaned meaning. The `roadmap-outline-deep` paragraph still points the roadmap selection at `roadmap-engine`'s resolution order. That order's "explicit argument" is a *path or filename* (`roadmap-engine` § "Named roadmaps", **Resolution order**), not a slug. Dropping "slug" from the hint therefore cuts off no documented way to pass a named roadmap.
- The `<user-slug>` and `<NN>-<slug>.md` path placeholders elsewhere in `roadmap-outline-deep` are correctly left out of scope. They come from 82.1 and do not offer a target.
- The sweep runs on today's tree. It returns exactly the four lines the spec's Finding predicts and nothing in `docs`, `CLAUDE.md` or `README.md`. The plan's contact check (all three greps empty after the edits) is the correct exit condition.

### Critical Issues

None.

### Positive Notes

- Before-texts and after-texts are quoted literally from the spec, so the edits leave no wording to interpret.
- The plan states explicitly that nothing past the first sentence changes. That respects the "the rest of each sentence and of each section stands" contract.
- The read-only sweep step reuses the spec's own breakage rule instead of inventing a new check, and it adds the YAML-quote check the project rules require.

## Deferred observations
- Affects: Phase 82 / `.ai-factory/specs/trickster77777/0237-the-targeting-argument-names-a-phase-not-a-slug.md` — After this task, `roadmap-outline-deep`'s `argument-hint` reads `"[phase]"`. Its Targeting paragraph still says the roadmap in play resolves from an "explicit argument" (a path or filename, per `roadmap-engine`). So the hint does not advertise the roadmap-path argument the body accepts. The same holds for `roadmap-decompose-skeleton`, which has no roadmap-resolution sentence at all. The spec pins the hint verbatim, so changing it here would contradict the plan's contract. Whether the hints should name a roadmap argument is a separate decision for a later task.

PLAN_REVIEW_PASS
