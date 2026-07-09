## Code Re-Review — milestone 61 (command-handoff single path + note verbosity hook)

Re-review after fixes to `review-1`. Re-read both changed files via `Read` (not session memory) and re-ran every verification grep against the current working tree.

### Prior-finding verdicts

**1. [Low] `note` SKILL.md:62 stale "skeleton verbatim" sibling of the broadened template hook — FIXED.**
Current `src/skills/note/SKILL.md:62` (re-read):
> "When the template hook is set, the note body follows the caller's **directive (section skeleton or free-form)** verbatim instead."
The word "skeleton" was replaced by "directive (section skeleton or free-form)", now aligned with the hook definition at `:32` ("a section skeleton **or** a free-form (non-skeleton) body directive"). The prose-shape handoff's free-form directive is no longer described by narrower "skeleton" wording. `git diff` confirms this is the only change since the prior pass (`-…caller's skeleton verbatim instead.` → `+…caller's directive (section skeleton or free-form) verbatim instead.`).

### Full re-review for new issues

**Verification gates — all pass** (grepped against current files):
- #2 `<NN>|highest existing prefix|zero-padded` (command-handoff) → empty. ✓
- #4 `compact` → empty (boundary-neutral intact). ✓
- #5 `always apply|other Important Rules` (note) → the two hits name only "file paths, English"; findings-focus no longer asserted always-on. ✓
- #7 `proportional` → empty. ✓
- #8 `register|note mode|chat mode|destination axis|note destination|Write.*(direct|itself)` → empty. ✓
- `skeleton` in command-handoff → two hits, both legitimate: `:43` grid shape uses a literal skeleton; `:118` prose branch explicitly says "not a section skeleton." No stale mode residue. ✓

**Additivity / load-once contract — holds.** `note` diff is confined to the two hook descriptions (`:32`, `:33`) and the one template sentence (`:62`); Rule text 1–5, the default template block, and Steps 1–4 mechanics are untouched. Unset case still reads "Unset → the current default (Rule 1 … and Rule 2 …)", so the only other caller, `roadmap-engine` (passes destination hook only, no verbosity directive — `roadmap-engine/SKILL.md:35-36`), is byte-identical. The Rule-2 broadening is inert for it.

**Caller correctness — sound** (unchanged from review-1 and re-confirmed): Step-1 reframed as `note`'s lens (no double-mining), fixed invariant at the Step-2 opener governs both shapes, the verbosity directive passed to `note` (`:119`) exercises the Rule-2 override that makes the prose path viable, self-check tests tree-completeness, paste-back-pointer exemption quotes it consistently. `allowed-tools` retains now-unused `Write Bash(mkdir *)` per spec.

No new issues found. The one prior finding is resolved and the change faithfully implements spec 15.

REVIEW_PASS
