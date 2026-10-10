## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-engine/SKILL.md`). The other staged files are pipeline artifacts: the plan, its sidecar and the plan-review.
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap gate: OK.** Contract line 83.2 in `.ai-factory/roadmaps/trickster77777.md` is the first open task after 83.1, which is done. Its `Spec:` tag points to `.ai-factory/specs/trickster77777/0234-the-engine-says-the-slug-is-given-not-how-to-derive-it.md`, and the diff implements that spec's "What must be true after".
- **Governing spec gate: OK.** Phase 83's governing spec is `docs/sakshi-harness/sakshi-harness.md`. It says the session gets the slug line from `roadmap-engine`'s `user-slug.sh` through a `SessionStart` hook, a session without the line runs the script itself, and the agent does not compute the slug. The rewritten paragraph says the same thing.
- **Architecture gate: OK.** The engine still holds only its own mechanism and now points to a script in its own directory. No `loads:` edge changes.
- **Rules gate: WARN (non-blocking).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`, so no project-specific rules apply.

### Verification against ground truth

- **Verbatim match.** With the line breaks joined, the new paragraph reads "**Slug derivation:** the user's slug is given at session start, as the line `The user's slug: <user-slug>`; a session that holds no such line runs `scripts/user-slug.sh` and takes its output as the slug." This matches the spec's pinned text exactly. The line breaks fall between words and outside every backtick span, and the paragraph keeps the same three-line, roughly 85-column wrapping as its neighbours.
- **Removal.** `grep -n "local-part\|john-doe\|user.name"` finds nothing in the engine any more. The rule, the example and the fallback are gone.
- **Rest of the section unchanged.** The diff touches only the three lines of the paragraph. **Resolution order**, **Owner line**, **Test sibling** and **Spec destination** are byte-identical.
- **Script target exists.** `src/skills/roadmap-engine/scripts/user-slug.sh` exists and is executable (`-rwxr-xr-x`). It prints the bare slug, which matches "takes its output as the slug".
- **Contact sweep.** `grep -rn "Slug derivation" src docs CLAUDE.md` matches only the engine's paragraph. `grep -rln "slug/owner mechanics"` matches the six expected pointers (`command-pin-gaps`, `roadmap-decompose`, `temporal-tree`, `roadmap-test-coverage`, `task-rescue`, `roadmap-outline`). Each one points to the section as a whole, which still holds the resolution order and the owner line, so all six stay true. No other text under `src/` tells the agent how to derive the user's slug. The other "slug derivation" hits are about title slugs (`note`, `aif-plan`, `command-handoff`, `roadmap-prune`), which are a different concept.

### Critical Issues

None.

### Positive Notes

- The change is as small as it can be: one paragraph, matched word for word against the spec, with the surrounding text untouched.
- The wrapping keeps `The user's slug: <user-slug>` on one line, so a reader can copy the exact form the hook will emit.
- The script path is relative to the skill directory, as the skills' `CLAUDE.md` § "Key constraints" requires.

REVIEW_PASS
