# Code Review — 1.3 note: folder-style layer

**Change under review:** `src/skills/note/SKILL.md` (two additions). Verified against plan `.ai-factory/plans/68-1-3-…md`, spec `.ai-factory/specs/21-note-folder-style-layer.md`, and the reverse graph.
**Nature of change:** skill-instruction prose (engine mechanism), not executable code — "runtime" here is how an implementing agent interprets the added rules. No migrations, types, or concurrency surface.
**Risk Level:** 🟢 Low

## Scope confirmation
- `git diff HEAD --name-only` (excluding `.ai-factory/` artifacts) → only `src/skills/note/SKILL.md` changed. No caller edits, matching the spec's "callers untouched."
- True delegating callers via `loads: note`: `src/skills/roadmap-engine/SKILL.md:11` and `src/commands/command-handoff.md:10`. Both unchanged. The broad `grep -w note` reverse-graph command returns lexical noise (any file mentioning the word "note"); the `loads:` grep is the authoritative check and confirms exactly the two the spec names.

## Faithfulness to spec (all requirements met)
- **Sibling read (Step 3, line 59):** reads 1–2 most-recent (highest-numbered) `[0-9][0-9]-*.md` neighbors in `<destination>`, reusing the existing numbering scan. Matches spec's "read the 1–2 most recent … neighbors."
- **Three-level precedence:** stated explicitly — (1) caller hooks always win, (2) neighbor style fills only what hooks leave unsaid, (3) engine defaults last. Matches spec precedence exactly.
- **Guards:** empty `<destination>` or hook-covers-everything → skip silently; at most 2 sibling reads; style *matched*, never content-copied. All three spec guards land inline.
- **No new hook / always-on:** correctly framed as mechanism, no parameter, no `allowed-tools` change (sibling reading uses `Read`/`Glob`, both already present).
- **Hooks semantics byte-identical:** the three hook bullets (lines 31–33) are unchanged; the new line 35 is additive and only points at the layer.
- **Spec "Files & types":** "one rule in Step 3 + one line in the Hooks section stating the precedence order" — satisfied by lines 59 and 35 respectively.

## Correctness observations (non-blocking)

1. **"Most recent" resolved to "highest-numbered."** The spec says "most recent"; the implementation binds this to highest `NN` prefix (reusing the numbering scan). This is correct for these folders because numbering is a monotonic append sequence, so highest-numbered = most recently created — no mtime/number divergence in practice. The disambiguation removes an ambiguity rather than introducing one. Not a defect.

2. **Precedence order appears in two places (lines 35 and 59), near-verbatim.** This is a mild one-home-per-fact tension, but it is **spec-mandated**: spec "Files & types" explicitly asks for the precedence in *both* the Step 3 rule and the Hooks line. Line 35 is scoped as a pointer ("folder style (Step 3) …") with the mechanism's full detail (which siblings, the guards, "matched not copied") living only in Step 3, so the duplication is limited to the ordering statement the spec requires in both. Acceptable; flagged only so a future editor keeps the two ordering statements in sync if either is reworded.

3. **Standalone (unset-hooks) behavior — no regression.** In the default `.ai-factory/notes/` case the layer is now active and may nudge register/density where the default template is silent. This is within the spec's guard ("byte-identical in output *rules* — the only new observable behavior is up to 2 extra sibling reads"): the default template still governs structure; register-matching where the template is silent is the intended always-on feature applied uniformly, not a change to the output rules. Confirmed consistent with spec design intent ("mechanism, always-on … any caller-supplied dir").

## Runtime / breakage check
Nothing to break: no code path, no tool-surface addition, no schema. The only new runtime action is ≤2 extra `Read` calls on already-listed sibling files, bounded and guarded against the empty-folder case. Callers that supply a fully-determining template hook (both real callers do) are inert by the precedence rule.

No correctness, security, or breakage findings.

REVIEW_PASS
