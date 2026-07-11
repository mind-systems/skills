# Review: 4.2 — writers route by the engine's resolution

Scope: `src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-decompose-skeleton/SKILL.md`. Documentation/skill-behavior edits only — no executable code, so no runtime/type/migration surface.

## What was checked
- **Diff confinement.** `git diff HEAD` shows edits limited to hook (c) (outline, decompose) and Step 0's target-roadmap parenthetical (skeleton). All surrounding philosophy — outline's 5–15 rule and hooks (a)/(b)/(d), decompose's Atomicity Gate and hooks (a)/(b)/(d), skeleton's three lenses — is byte-identical. Guard satisfied.
- **Single-home reference, no restatement.** All three sites reference `roadmap-engine`'s "Named roadmaps" section for slug/owner mechanics rather than restating them. The only `roadmaps/` literal added is decompose's `.ai-factory/roadmaps/<slug>-tests.md`, which is an explicit reference to the engine's "Test sibling" rule — consistent with the plan's grep verification (hits only resolution references, no restated derivation/owner mechanics).
- **Reference targets resolve.** Engine headings confirmed present: `## Named roadmaps` (`:49`), `**Resolution order**` (`:51`), `**Test sibling:**` (`:65`). The strings the three writers cite ("Named roadmaps" section, "Test sibling" rule) all point at real anchors — no dangling reference.
- **Resolution order fidelity.** All three now express argument → "my roadmap" → default `.ai-factory/ROADMAP.md`, matching the engine's order. Decompose correctly inserts "my roadmap" between explicit-argument and default. Outline preserves its strategic-tier restraint (no keyword branching on top of the resolution). Skeleton names the resolution instead of the bare literal.
- **Default-path stability.** With no `roadmaps/` directory, every site still resolves to `.ai-factory/ROADMAP.md` (and decompose's test branch to `.ai-factory/ROADMAP_TESTS.md`, "as today") — lazy-migration guard holds.
- **Test-sibling derivation.** Decompose's test-keyword branch now derives the sibling of the roadmap in play: default → `ROADMAP_TESTS.md`, named → `roadmaps/<slug>-tests.md`. Matches spec 44 and the engine's rule.

## Non-blocking observation (pre-existing, out of scope)
Decompose hook (c) leaves the interaction between an **explicit arbitrary filename argument** and **test-context keywords** unspecified: the test-sibling paragraph enumerates only "default roadmap" and "a named roadmap," not an arbitrary explicit-argument roadmap. If a user passed a non-roadmap explicit filename *and* a test keyword, the derived target is undefined. This ambiguity existed in the prior text too ("explicit filename argument wins" vs. "test keywords → ROADMAP_TESTS.md" had no stated precedence), is not introduced by this change, and is outside spec 44's scope. No action required for this task.

No correctness, security, or behavior-regression defects found.

REVIEW_PASS
