# Code Review: 1.4 — command-handoff: rewrite to a lens over `note`

**Scope reviewed:** `git diff HEAD` — only `src/commands/command-handoff.md` is a code change (the other staged files are planning artifacts: plan `.md`/`.json`, three plan-reviews). Reviewed the rewritten command in full against spec `20-command-handoff-destination-always-handoffs.md`, the plan's Task 1 byte-equivalence checklist, and `note/SKILL.md`.

## Verdict
No blocking bugs. The rewrite faithfully implements the spec: the destination invariant is correct, the frontmatter grant set is preserved, the grid skeleton is byte-identical, and every policy element on the plan's survivor checklist is present. Two non-blocking items below.

## Verification performed
- **Grid skeleton byte-identity:** `diff` of the old skeleton (HEAD lines 47–103) against the new (lines 29–85) → identical. Section names, order, and placeholder descriptions unchanged — the mining-lens payload is intact.
- **Destination fix (spec 20 core):** line 13 states the invariant correctly — `$ARGUMENTS` names the project **root** only (not a file, not the destination), `<root>/.ai-factory/handoffs/` is always the destination, current project when unset, "never `notes/`, never the bare argument path." Passed to `note`'s destination-directory hook at line 97. Mechanically sound against `note/SKILL.md:31` (`<destination>` used verbatim for mkdir/scan/path).
- **Frontmatter (prior-review blocker):** `allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob Skill` preserved unchanged (line 9) — `Write`/`Bash(mkdir *)` not stripped, correct since `note` runs its mkdir/Write inline in the same agent. `loads: note` intact. `argument-hint: ""` retained. `Read $ARGUMENTS` opener dropped as required.
- **Byte-equivalence checklist (Task 1):** meaning-tree mandate (21), next-step-scoped read-map (23 + skeleton §2), both shapes (grid 29–85, prose 87), tree-completeness gate + pointer exemption (91), verbosity/Rule-2 override (99), semantic-slug "never `handoff`" (100), minimal pointer contract (104–113), "Write in English" directive (21) — all present.
- **Body has no restated file mechanics:** the only `mkdir`/`Write`/`numbering` mentions are inside the "do not … yourself" negation (95) and the "`note` performs its own numbering, directory creation, and file write" attribution (102) — no engine mechanics re-enter as command procedure.
- **Internal cross-references after the Step renumber (was 1/2/3 with 2=Compose; now 1=Shape, 2=Delegate, 3=Pointer):** "hook `note` receives in Step 2" (13), "populate via `note` in Step 2" (89), "pointer below" (91, 102), "self-check gate above" (113) — all resolve correctly.

## Non-blocking observations

No finding rises to a bug, security issue, or runtime correctness defect. Two documentation notes, neither blocking:

**1. `note (its own Step 3)` mislabels where `note` mines.**
`command-handoff.md:19` — "`note` (its own Step 3) performs mining and population, not the agent here." In `note/SKILL.md`, mining is **Step 1: Analyze Context** (`:37`); Step 3 is Save Note to File (compose body + write). Population/composition is Step 3, but mining is Step 1, so attributing *mining* to "its own Step 3" is inaccurate. The original phrasing `note (Step 3)` referred to *command-handoff*'s own former Step 3 (the delegation step); the rewrite re-pointed it at `note`'s internal Step 3 and picked the wrong internal step for "mining." Impact: none at runtime — the executing agent loads all of `note` via the Skill tool regardless of which internal step is cited; a documentation-accuracy nit. Optional fix: drop the parenthetical ("`note` performs mining and population, not the agent here") or cite Step 1 for mining.

**2. Prose-shape mining lens is now thinner than the grid shape's.** The original Step 1 carried an explicit 11-point extraction checklist (project/domain, every file touched, decisions+why, done-vs-in-flight, uncommitted state, next action, working discipline, mistakes+corrections, traps/collisions, don't-re-litigate points, hard rules) that the original said was "folded into the free-form body directive for the prose shape." That list is removed. For the **grid** shape this is fully covered — the skeleton's section placeholders (§3 uncommitted state, §6 error log, §8 domain spine, §9 hard rules, etc.) are the mining lens, exactly as the spec intends ("its placeholders are the mining lens"). For the **prose** shape there is no skeleton, so the prose directive (line 87 — causal thread, decisions+rationale, inline refs, next step + working discipline) is now the entire lens, and it does not explicitly name error-log / uncommitted-state / don't-re-litigate / traps as extraction targets. This removal is **sanctioned by the spec** ("cut everything `note` already does"; "the prose directive likewise" is named as the prose mining lens) and by the plan's checklist (which did not list the 11-point list as a survivor), so it is not a defect against the contract. Flagging it only so the required live pre/post baseline check pays attention to whether a prose-shape handoff still surfaces the error log and uncommitted state — the two highest-value, most-easily-dropped sections — as richly as the pre-rewrite version did.

## Notes
- Line count 122 (was 140); ~57 lines are the legal skeleton payload. Within the "~80 aspiration, never a clamp" guidance.
- The spec's live-session pre/post baseline (same tree at same depth, identical pointer structure) and the foreign-path destination check are user-run against a real mineable session; they cannot be exercised from this static review and are not asserted here.

REVIEW_PASS
