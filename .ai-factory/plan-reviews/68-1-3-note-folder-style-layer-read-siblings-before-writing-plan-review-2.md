## Code Review Summary

**Files Reviewed:** 1 plan (`.ai-factory/plans/68-1-3-note-folder-style-layer-read-siblings-before-writing.md`), verified against spec `.ai-factory/specs/21-note-folder-style-layer.md`, ROADMAP.md line 155 (milestone 1.3) + Phase 1 hard rules (lines 145/149), the reverse graph, and the target file `src/skills/note/SKILL.md`.
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap:** Plan heading `1.3 — note: folder-style layer — read siblings before writing` maps cleanly to ROADMAP.md line 155. Spec tag `.ai-factory/specs/21-note-folder-style-layer.md` resolves and matches the plan's Context/Tasks. No milestone-linkage gap.
- **Phase governing spec:** Phase 1 (lines 147–149) declares no separate `Governing spec:`; its binding rule is the direction-level "behavior-first — unverified until a live run compares output to the pre-rewrite baseline" (line 145) and "each rewrite passes its live baseline before the next starts" (line 149). The plan's Verification now honors this (see below). Aligned.
- **Architecture / Rules:** No `.ai-factory/RULES.md`. The change respects the composition model (mechanism stays in the `note` engine; no new hook; no caller edits) and one-home-per-fact (Task 2 makes the Hooks line *point at* the Step 3 rule, not restate the mechanism). Aligned.

### Resolution of prior review
Plan-review-1's single actionable finding — the plan's Verification dropped the spec's live behavioral check — is **resolved**. Plan line 30 now carries the live check as an explicit bullet ("Live behavioral check … write a note into a folder whose existing files use a distinct register … the new file matches the folder's register where the hook is silent, while the caller hook still shapes structure"), and correctly pins that `Settings → Testing: no` does not discharge it (it only means no automated test file). All three spec-Verification bullets are now present, plus the byte-identical guard.

### Critical Issues
None. The plan is implementable as written and faithful to the spec.

### Verification against codebase (confirmed accurate)
- **Reverse graph is correct.** The only genuine delegating callers are `roadmap-engine` (`loads: note`) and `command-handoff` (`loads: note`); both drive `note` via its hooks. The plan/spec claim that these two need no edits holds. The plan's re-check grep is `note`'s own documented reverse-graph command (SKILL.md line 23), so it is the canonical check even though it returns lexical noise.
- **No tool-surface change.** Sibling reading uses `Read`/`Glob`, both already in the frontmatter (`Read Write Bash(ls *) Bash(mkdir *) Glob`). Correctly treated as pure always-on mechanism, no new hook/parameter.
- **Callers stay inert by design.** `roadmap-engine` (spec-note template) and `command-handoff` (grid skeleton) both supply strong template hooks that fully determine structure; the plan's Task 1 guard "a hook that already fully determines the body → skip silently" plus the precedence "hooks win, neighbor fills only what hooks leave unsaid" means the layer cannot alter their structural output. No caller-facing contract break.
- **Line references match the live file.** Hooks 27–33, Step 3 numbering scan 50–55, Step-3 register span 48–98 are all accurate against the current `src/skills/note/SKILL.md`.
- **"Most recent" disambiguated.** Task 1 binds it to "highest-numbered neighbors … reuse that [numbering] scan," removing the mtime-vs-number ambiguity for the implementer.

### Positive Notes
- **Drift-proof precedence split.** Task 2 keeps the three-level precedence's single home in Step 3 and has the Hooks line point at the layer rather than re-hold the mechanism — honors one-home-per-fact while still satisfying the spec's "one line in the Hooks section stating the precedence order."
- **Byte-identical scope stated precisely.** The plan scopes the byte-identical guarantee to "unset-hooks standalone output rules," with the only new observable behavior being ≤2 sibling reads — no over-claim.
- **Guards fully carried.** Empty folder / hook-covers-everything → skip silently, max 2 reads, style *matched* never content-copied — all three spec guards land inline in Task 1.

The plan is sound, faithful to the spec, and accurately grounded in the current codebase. No findings.

PLAN_REVIEW_PASS
