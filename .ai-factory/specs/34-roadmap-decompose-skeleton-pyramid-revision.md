# roadmap-decompose-skeleton: pyramid revision — audit the three lenses; "no change" is a legal outcome

## Current state

`src/skills/roadmap-decompose-skeleton/SKILL.md` (157 lines) is a philosophy top over two engines (`loads: roadmap-engine test-philosophy`) — structurally already the pyramid shape. Untested against the written philosophy: whether the three lenses (skeleton / TDD / concurrency) carry ceremony, whether any engine content leaked inline (format fragments, discriminator restatement), whether the register is two-reader clean.

## Change

A **revision, not a mandated rewrite**: audit against `docs/skill-pyramid.md` and the composition model. Fix only findings — inline engine restatements become loads/links, ceremony goes; the three lenses' decision content (fuse-at-1:1, standalone-scaffold-at-2+, heavy ≥2-of-{async I/O, buffer, lifecycle}) is contract text and stays pinned verbatim. **"No change" plus a one-paragraph audit report is a legal, complete outcome.**

## Guards

- Behavior-identical; frontmatter and `loads:` unchanged; restraint-first-class wording stays.
- Live baseline only if changed: one skeleton pass over a real heavy task pre/post, compare the produced splits.

## Verification

- Audit report names findings+fixes or states conformance; if changed, baseline splits identical.
