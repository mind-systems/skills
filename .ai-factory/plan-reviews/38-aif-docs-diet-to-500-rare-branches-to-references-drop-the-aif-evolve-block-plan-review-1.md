## Code Review Summary

**Artifact reviewed:** `.ai-factory/plans/38-aif-docs-diet-to-500-rare-branches-to-references-drop-the-aif-evolve-block.md`
**Target skill:** `src/skills/aif-docs/SKILL.md` (587 lines) + new `references/*.md`
**Files Reviewed:** plan (1), target SKILL.md, spec note 49, roadmap line, REVIEW-CHECKLISTS.md (extraction-pattern baseline)
**Risk Level:** 🟢 Low — the plan is solid, faithful to spec note 49, and every line range it cites resolves correctly in the current file. The findings below are all non-blocking (WARN).

### Context Gates

- **Roadmap linkage (WARN → informational):** Milestone is line 87 of `ROADMAP.md`, `Spec: .ai-factory/notes/49-aif-docs-diet-references.md` — both exist and the plan matches the spec's three moves verbatim (topic-guides / html-generation / consolidation + drop skill-context block). Dependency on task 48 (line 85, done — Step 2.2b / State B/C CLAUDE.md-index edits are present in the current file) is correctly honored: the plan's Task 5 explicitly checks task 48's edits are preserved. ✅
- **Architecture / authoring norm:** The ≤500-line body norm (CLAUDE.md "Body ≤ 500 lines — move details to references/") is the governing constraint; the plan's progressive-disclosure approach matches the established `references/REVIEW-CHECKLISTS.md` + `templates/html-template.html` on-demand pattern. Ownership respected: upstream mirror (`upstream/ai-factory/aif-docs`) explicitly untouched. ✅
- **RULES.md / ROADMAP_TESTS.md:** not present — gate skipped. Testing is off per plan Settings, consistent with a skill-text-only change verified by a live run.

### Critical Issues

None. No missing migrations, no security surface, no incorrect file paths (all four cited targets — SKILL.md and the three new `references/*.md` — are correct and relative). Line ranges verified against the live file: Task 1 → 55–74 (skill-context block ✅), Task 2 → 337–369 (per-topic guidelines ✅), Task 3 → 467–488 (Step 3.1–3.4 ✅), Task 4 → 156–197 (table + stays-in-root list + sample dialog ✅).

### Findings (non-blocking — WARN)

1. **Stale baseline line count; the "~450" target is unreachable, though ≤500 still holds.**
   The plan (Context, Task 5), the roadmap line, and spec note 49 all say the file is **574** lines. `wc -l` reports **587** (the file grew when task 48 added the CLAUDE.md-index content). The four extractions remove roughly: Task 1 ≈ 21, Task 2 ≈ 32, Task 3 ≈ 19, Task 4 ≈ 28 → **≈ 100 lines**, landing at **≈ 487**. That satisfies the hard `≤ 500` constraint (the real goal) but will **not** hit the advertised "~450". Recommend Task 5's acceptance read "≤ 500" as pass and treat "~450" as aspirational, so the verifier doesn't loop chasing 37 phantom lines.

2. **"Byte-identical runtime behavior" is imprecise for Task 1.**
   The Context framing ("byte-identical runtime behavior") is accurate for Tasks 2–4 (pure relocation behind pointers) but **not** for Task 1: deleting the skill-context / aif-evolve block *removes a live capability branch* (loading `.ai-factory/skill-context/aif-docs/SKILL.md`), it does not relocate it. This is deliberate and justified — `aif-evolve` exists only in `upstream/ai-factory/` and is **not** in the active set, so the skill-context file is never populated in the way these skills are deployed, and spec note 49 records it as "Confirmed removable by the user." No change needed; just name it precisely (behavior *removal*, not *preservation*) so a future reader doesn't reintroduce it expecting the diet was inert. Note also this *widens* the src↔upstream `aif-docs` divergence (upstream keeps the block) — the next reconciliation diff will surface it; acceptable under the repo's "src is authoritative" model.

3. **Task 4's example pointer omits the when-to-read condition that Task 5 requires.**
   Task 5 verifies "every body pointer names its reference with a correct relative path **and a when-to-read condition**." Tasks 2 ("when generating State A pages") and 3 ("when `--web` is passed") satisfy this, but Task 4's suggested pointer — *"Consolidation targets and the sample proposal dialog → read `references/consolidation.md`."* — has no condition. Recommend the implementer append one, e.g. "…read `references/consolidation.md` **when scattered root `.md` files were found in Step 0**," so Task 4 and Task 5 don't disagree.

4. **Task 4 requires splitting a single fenced code block — the trickiest edit; the plan flags it but call it out sharply.**
   In the current file the sample dialog and the AskUserQuestion options are **one contiguous fenced block (lines 177–197)**: the "Found [N] markdown files…" example (178–190) *and* "AskUserQuestion: Would you like to apply the consolidation?" + options 1/2/3 (191–196). The plan moves the example to the reference but keeps the options in the body — so the implementer must **split that block**, not move it wholesale, and re-anchor the retained options under an introducing sentence (the plan's "Ensure the retained AskUserQuestion options are not orphaned" covers this). Same care applies to the file-mapping one-liner in Task 3 (currently inside subsection 3.3, line 484): it must be lifted into the body while 3.1–3.4 are removed, and should not be duplicated verbatim in the reference. Low risk, but this is where a careless move would silently drop the contract dialog — worth an explicit re-read after editing.

### Positive Notes

- Faithful decomposition: the plan mirrors spec note 49's three moves exactly, and its "keep in body / move to reference" carve-outs (rule + procedure + AskUserQuestion options stay; concrete mapping tables + sample narrative move) correctly distinguish *behavior* from *reference material*.
- Contract text protected: verbatim AskUserQuestion dialogs are explicitly not compressed; Core Principles, 3D mode, Step 4 (incl. no-motivation pass), Step 4.1, Step 5, Artifact Ownership, and Important Rules are named as untouched and verified in Task 5.
- Correct guardrails: upstream mirror off-limits, task-48 edits preserved, dependency ordering explicit, and a live State C run chosen as the verification method (right call for a text-only skill change with no automated test surface).
- Sensible commit plan; messages comply with the repo's no-prefix / sentence-case convention.

Overall: the plan is implementable as written. The findings above are refinements — update the target from "~450" to "≤500", add the missing when-condition to Task 4's pointer, and edit the consolidation block surgically. None block execution.

PLAN_REVIEW_PASS
