## Code Review (round 2, re-review) — milestone-rescue-audit: two modes

Re-read `src/skills/milestone-rescue-audit/SKILL.md` in full. `git status` confirms the only behavior change is that file; the rest is planning artifacts (plan, plan-reviews, review-1, sidecar).

### Verdicts on round-1 findings

**Finding 1 (Medium) — frontmatter `description` claimed "chat only (no file writes)" and omitted prune mode.** → **Fixed.**
Current lines 7–16:
> "Two modes: `rescue` (default) emits a diagnosis plus one upstream recommendation to chat, appending only status marks on evaluated deferred observations — no content rewrites, no ROADMAP edits; `prune` runs when `roadmap-prune`'s gate refused, pinning every unpinned observation via the same marks plus promotion appends into existing files. Run `rescue` right after `milestone-rescue` while artifacts are warm, or cold on any looped/outlier task; run `prune` when a roadmap prune is blocked on unpinned observations."

The stale "no file writes" claim is gone; the description now names both modes, states the append-only write behavior accurately, adds prune-mode trigger phrases (line 15–16: "prune gate blocked", "pin deferred observations"), and stays within the frontmatter budget (folded description = 993 chars < 1024).

**Finding 2 (Low) — `$1` dispatch undefined when the argument is present but neither `rescue` nor `prune`.** → **Fixed.**
Current lines 33–37:
> "`$1` selects the mode. The dispatch is total: `$1 == "prune"` selects prune mode; everything else — absent, `rescue`, or any other token (including a bare task slug from the historic invocation form) — selects rescue mode. When `$1` selects rescue mode but is neither absent nor `rescue`, treat it as the cold-rescue slug (the `$2` role in `## Inputs` below) rather than an error."

Dispatch is now total and the historic bare-slug form is absorbed as the cold-rescue slug. The Inputs block (lines 57–61) was updated to match — it reads the slug "as `$2` when `$1` is `rescue`, or as `$1` itself per the `## Run mode` dispatch rule (the historic bare-slug invocation)", consistent with the Run mode section. No contradiction between the two.

### New issues

None. The two fixes are internally consistent with the rest of the body (Write contract, What-NOT-to-do, Step 3 marking, Prune mode steps all still align), the spec mapping (Edits 1–4 + Constraints) remains faithful and complete, and the `loads`/`allowed-tools`/`argument-hint` mechanics are unchanged and correct (`Edit` present, `Write` correctly absent).

Non-blocking FYI (not a finding): the folded `description` sits at 993 chars against the 1024 cap — compliant with ~31 chars of headroom; worth keeping in mind if trigger phrases are added later.

REVIEW_PASS
