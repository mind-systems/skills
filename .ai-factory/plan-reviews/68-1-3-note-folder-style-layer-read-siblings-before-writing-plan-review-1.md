## Code Review Summary

**Files Reviewed:** 1 plan (`.ai-factory/plans/68-1-3-note-folder-style-layer-read-siblings-before-writing.md`), verified against spec `.ai-factory/specs/21-note-folder-style-layer.md`, roadmap line 155, phase header (ROADMAP.md §"Phase 1"), and the target file `src/skills/note/SKILL.md`.
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap (WARN→clean):** Plan heading maps cleanly to ROADMAP.md line 155 (`1.3 — note: folder-style layer`). Spec tag `.ai-factory/specs/21-note-folder-style-layer.md` resolves and matches. No milestone-linkage gap.
- **Phase governing spec:** Phase 1 header (lines 147–149) states no separate `Governing spec:` tag; the phase's binding hard rules ("rewrites are behavior-first — unverified until a live run compares output to the pre-rewrite baseline") are prose in the direction/phase intro (lines 145, 149). See finding below.
- **Architecture/Rules:** No `.ai-factory/RULES.md`. The change respects the composition model (mechanism stays in the engine; no new hook; no caller edits) and one-home-per-fact (Task 2 explicitly makes the Hooks line *point at* the Step 3 rule rather than restate the mechanism). Aligned.

### Critical Issues
None. The plan is implementable as written and faithful to the spec.

### Issues

**1. Plan Verification drops the spec's live behavioral check (`Verification`, plan lines 28–31).**
Spec 21's Verification has three bullets; the plan carries two and omits the middle one:
- spec ✓ "Step 3 contains the sibling-read rule…" → plan bullet 1 ✓
- spec ✗ **"Live check: write a note into a folder whose existing files use a distinct register … the new file matches the folder's register where the hook is silent; caller hooks still shape structure"** → **absent from the plan**
- spec ✓ "Callers unchanged" → plan bullet 2 ✓

The two surviving plan bullets only confirm the *text was added* and that *unset-hook output stays byte-identical* — neither exercises the new mechanism. Whether the folder-style layer actually produces folder-matched output where hooks are silent is exactly what the dropped live check verifies. This matters more than usual here because the phase's stated hard rule is behavior-first: "a rewritten skill is unverified until a live run compares its output to the pre-rewrite baseline" (ROADMAP.md line 145), and "each rewrite then passes its live baseline before the next starts" (line 149). `Settings → Testing: no` correctly means no automated test file, but it does not discharge the spec-named live check — that is orchestrator/manual verification, not a unit test. Recommend adding the spec's live check as a third Verification bullet so the implementer/orchestrator does not treat "text present + byte-identical" as full verification.

### Positive Notes
- **Line references are accurate.** Hooks section (27–33), Step 3 numbering scan (50–55), and the 48–98 Step-3 register span all match the current `src/skills/note/SKILL.md` exactly — the plan was written against the live file, not a stale copy.
- **Resolves a spec ambiguity.** The spec says "most recent" neighbors; Task 1 pins this to "highest-numbered neighbors … reuse that scan," binding it to the existing `[0-9][0-9]-*.md` numbering scan and removing any mtime-vs-number ambiguity for the implementer.
- **No `allowed-tools` change needed.** Sibling reading uses `Read`, already present in the frontmatter (`Read Write Bash(ls *) Bash(mkdir *) Glob`); the always-on mechanism introduces no new tool surface. The plan correctly treats this as pure mechanism with no new hook/parameter.
- **Drift-proof precedence.** Task 2's "single source of truth — the Hooks line points at the layer, the Step 3 rule holds the mechanism" prevents the three-level precedence from being duplicated across two sections, honoring one-home-per-fact.
- **Byte-identical guards restated correctly** at both task and verification level, matching the spec's engine-edit guard.

The plan is otherwise sound; the only actionable item is restoring the spec's live behavioral check to the Verification section.
