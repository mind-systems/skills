# detangle: pyramid revision — reconcile with the context tree; "no change" is a legal outcome

## Current state

`src/skills/detangle/SKILL.md` (125 lines) predates `docs/context-tree.md` yet describes the same motion from the other end: the context tree raises from the session input down to the leaf; detangle climbs from a leaf up through branch and trunk to the forest. The two must read as one model, not two competing ones. Untested: whether detangle's wording now duplicates what the context-tree doc (and the global grounding rule) already carry, and whether its register is two-reader clean.

## Change

A **revision, not a mandated rewrite**: audit against `docs/context-tree.md` and the pyramid. Fix only findings — where detangle restates what the doc/global rule now owns, replace with a link and keep only detangle's own contribution (the leaf-upward climb, the shared-contract multi-tree raise); ceremony goes. **"No change" plus a one-paragraph audit report is a legal, complete outcome.**

## Guards

- Behavior-identical; frontmatter unchanged; the multi-tree shared-contract raise is detangle's own content — never reduced to a doc link.
- Live baseline only if changed: one detangle run on a real shared-contract element pre/post, compare the raised context set.

## Verification

- Audit report names findings+fixes or states conformance; if changed, baseline raise identical.
