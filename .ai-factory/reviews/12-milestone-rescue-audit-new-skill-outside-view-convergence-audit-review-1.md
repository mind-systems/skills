# Code Review: milestone-rescue-audit — new skill — outside-view convergence audit

**Review round:** 1
**Scope:** New skill `src/skills/milestone-rescue-audit/SKILL.md` + registration in `CLAUDE.md`.

## What changed

- **New file** `src/skills/milestone-rescue-audit/SKILL.md` (172 lines) — read-only audit skill: frontmatter + Inputs block + Steps 1–6 + "What NOT to do".
- **Modified** `CLAUDE.md` — added `milestone-rescue-audit` to the "Custom skills — never overwrite from upstream" list.
- Plan/spec/sidecar/roadmap artifacts (`.ai-factory/…`) are process metadata, not product code — out of scope for correctness.

These are agent-instruction documents, not executable code, so the review checks spec conformance, frontmatter validity against repo authoring rules, and internal consistency of the procedure.

## Verification performed

**Frontmatter (against `CLAUDE.md` authoring constraints):**
- `name: milestone-rescue-audit` matches the directory name exactly ✓
- `description` is 634 chars — within the ≤ 1024 limit ✓; states both what it does and when to use it, with trigger phrases ✓
- `argument-hint: "[milestone slug | leave empty if artifacts already in context]"` — brackets are quoted, satisfying the "MUST quote brackets" rule ✓
- `allowed-tools: Read` — matches the spec's read-only / diagnoses-never-edits requirement ✓
- Body is 172 lines — within the ≤ 500 limit ✓
- YAML folded scalar (`>-`) is correctly indented; parses cleanly ✓

**Spec conformance (`.ai-factory/notes/22-milestone-rescue-audit-skill.md`):**
- Sibling-not-mode framing, "Convergence by Understanding or by Attrition" ✓
- Steps 1–6 present with the user's wording near-verbatim (finding→fix chain → central question → one-sentence root-cause test → discriminators → spectrum verdict → chat-only output) ✓
- Decisive one-sentence root-cause test with "default is NOT band-aid" guard ✓
- Discriminator signal lists (band-aid vs legitimate), including workaround-named state and reviewer-resignation language ✓
- `[Independent]—[Mixed]—[Band-aid]` spectrum with "Mixed" allowed and left-default ✓
- Output to chat only — no file, no ROADMAP edit — stated in Step 6 and reinforced in "What NOT to do" ✓
- Thin `Inputs` block names the artifacts and points to `milestone-rescue` for layout instead of re-documenting it ✓

**Internal consistency:**
- Control flow is coherent: Step 3 healthy branch → "stop at Step 5, skip Step 4"; band-aid branch → Step 4 → Step 5 → Step 6. No dead-ends or contradictory jumps.
- Step 4 is correctly gated ("run only when Step 3 found a candidate root-cause sentence") and explicitly subordinate to the test, matching the spec's "corroborate, don't replace."
- The body uses only the `Read` tool capability it declares; no step invokes Glob/Grep/Bash/Write.

**CLAUDE.md registration:**
- Single clean insertion of `milestone-rescue-audit` adjacent to `milestone-rescue`; no other list entries altered; placement is in the correct "never overwrite from upstream" list so the next sync preserves it ✓

## Observation (no action required — by design)

`allowed-tools: Read` means the cold-start path ("If run cold, locate and read them before Step 1") cannot programmatically discover artifacts via `Glob`/`Grep`/`git status` the way `milestone-rescue` does. In practice the agent derives artifact paths from the slug argument by the repo's consistent `<NN>-<slug>-…` naming and `Read`s them directly, and the primary flow runs warm (artifacts already in context). This tradeoff is intentional — the spec mandates read-only and its Open Questions already flag cold-start as a "revisit if it becomes common" item. Noting for traceability only; no change recommended.

## Conclusion

No bugs, security issues, or correctness problems. Frontmatter is valid, the procedure is internally consistent, the change is faithful to the spec, and the upstream-sync registration is correct. Nothing will break at runtime (the skill is read-only and writes nothing).

REVIEW_PASS
