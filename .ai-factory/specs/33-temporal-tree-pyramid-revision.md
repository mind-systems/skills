# temporal-tree: pyramid revision — audit against the philosophy; "no change" is a legal outcome

## Current state

`src/skills/temporal-tree/SKILL.md` (157 lines) is borderline: not an inversion, but written before the philosophy was named. Untested against the pyramid: whether its walk procedure carries ceremony an executor performs unprompted, whether it restates the `## Features` table contract that `roadmap-prune`/`ARCHITECTURE.md` own, whether its register is two-reader clean.

## Change

A **revision, not a mandated rewrite**: audit the body against `docs/skill-pyramid.md`, `docs/skill-composition-model.md` (two-reader register, what-to-pin vs what-to-trust), and the walkable-tree rule. Fix only what the audit finds — restated shared contracts become links, procedural ceremony goes, pinned values stay pinned. **Restraint is first-class: if the audit finds the file already conformant, the task closes with "no change" and a one-paragraph audit report — padding a conformant skill is its own failure.**

## Guards

- Behavior-identical whatever the outcome; frontmatter unchanged.
- No mass moves to `references/` unless the audit names a rarely-read branch — do not invent structure.
- Live baseline only if the body changed: one walk on a real feature hash pre/post.

## Verification

- Audit report names each finding with its fix, or states conformance.
- If changed: baseline walk identical in output.
