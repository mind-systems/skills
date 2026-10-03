## Plan Review Summary

**Plan:** 53.1 — three skill sentences agree with the shape they describe
**Files targeted:** 3 (`src/skills/roadmap-decompose/SKILL.md`, `src/commands/command-pin-gaps.md`, `src/skills/roadmap-decompose-skeleton/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** Contract line 53.1 in `.ai-factory/roadmaps/trickster77777.md` (Phase 53) sits at the seam. Its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0205-three-skill-sentences-agree-with-the-shape-they-describe.md`, and the phase note `147-sentences-that-outlived-their-shape.md` is linked from the phase header. The plan's three edits match the contract line's "Change:" clause one-for-one.
- **Governing spec — OK.** The phase note says outright that no document governs these sentences ("a skill is its own documentation"). The plan's `Docs: no` matches that.
- **Rules — WARN (informational).** `.ai-factory/RULES.md` does not exist, which I confirmed. No conventions to check against.
- **Architecture — OK.** These are text edits inside skill bodies. No `loads:` edge changes, and no boundary is crossed. The skeleton's `loads:` frontmatter already names `polymorphism-philosophy`, so the new bullet brings the body's list into line with the frontmatter. It does not add a dependency.

### Verification against ground truth

- **Hook (d), `roadmap-decompose`.** The current two-line text is exactly as the plan quotes it. The replacement drops only ", how to verify" and keeps "guards", which matches the spec's after-text word for word, wrap included.
- **`command-pin-gaps`.** Each of the two before-substrings appears exactly once in the file, so the in-line swaps can't hit the wrong place. The after-texts match the spec. The plan correctly keeps § "Blast-radius holes" ("never the sweep's own enumeration of what it found") untouched.
- **Skeleton list.** § "Load-once / dependencies" currently has the two bullets the plan describes, followed by a blank line and the "does **not** call `roadmap-decompose`" paragraph. The proposed bullet is the spec's sentence, split across two lines with the file's two-space continuation indent. The plan says the lines are 85 and 84 characters; I got the same measurement. The section's existing lines run up to about 88, so the bullet fits the column. The plan correctly leaves the count word and its gloss parenthesis, the `loads:` field, and Lens 1 alone.
- **Blast radius.** I re-ran all three of the spec's sweeps. The hits are the same as the ones the plan and spec list: `docs/what-a-task-carries.md`, the hook's name cited in `roadmap-decompose`, the two "Load-once / dependencies" sections, and `roadmap-engine`'s description word "Load-once". None of them quotes a target sentence, so nothing outside the three targets needs to change.

### Critical Issues

None.

### Positive Notes

- Every edit carries its exact before-text and after-text, anchored by heading or bold lead-in rather than by line number, so the implementer has nothing to guess.
- The plan tells the implementer which file is hard-wrapped and which is not, so the edits keep each file's existing layout.
- The plan's own re-run of the blast-radius sweep checks the spec's finding instead of copying it.

PLAN_REVIEW_PASS
