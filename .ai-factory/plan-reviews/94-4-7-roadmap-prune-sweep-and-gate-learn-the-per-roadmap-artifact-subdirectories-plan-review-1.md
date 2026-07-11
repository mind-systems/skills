## Plan Review Summary

**Plan:** 4.7 — roadmap-prune: sweep and gate learn the per-roadmap artifact subdirectories
**Files planned to change:** `src/skills/roadmap-prune/SKILL.md` (only)
**Risk Level:** 🟢 Low

Reviewed against the full reference chain: the plan → spec `.ai-factory/specs/49-prune-sweep-per-roadmap-subdirs.md` → layout owner `orchestrator-artifacts` §1 → governing doc `docs/multiuser-roadmaps.md` § «Разрешение целевого файла», and the target file `src/skills/roadmap-prune/SKILL.md` read in full. The ROADMAP.md contract line (219) matches the plan.

### Context Gates
- **Architecture / composition**: PASS. The plan honors the `loads: orchestrator-artifacts` edge — it explicitly forbids restating the layout in detail (Tasks 1–3 all defer to `orchestrator-artifacts` §1). Consistent with the mechanism/policy split.
- **Rules**: PASS. "Instructions only, no rationale prose" is preserved (Task 2 caps the one allowed divergence sentence; Tasks 1 & 3 are instruction-only). 3.1's ledger text and 4.4's two policy sentences are called out as untouched. Commit policy untouched.
- **Roadmap alignment**: PASS. Plan title matches ROADMAP.md line 219; predecessor 4.6 (line 217) is `[x]` and did land the subdir layout + `patches/` retirement in `orchestrator-artifacts` §1, so the layout this plan references exists.

### Line-reference & grounding accuracy (verified against the file)
- The four flat dirs incl. `patches/` are at line 267 — Task 1's target. Confirmed the file has exactly **one** `patches` hit, so Task 3's "grep → zero" verification is achievable.
- Task 3's three "Step 5 deletes" premise sites (lines 43, 67, 327) are all real and all matched by the stated grep `"Step 5 delet\|deleted them\|before Step 5"`. No fourth site exists. Accurate.
- Step 0 item 2 hand-off clause (lines 42–44), item 6 margin capture (lines 63–68), and the Step-8 parenthetical (line 327) are correctly located.
- The `-tests` stem-stripping decision is soundly grounded: `orchestrator-artifacts` §1 places the test partner's runs under the *same* stem segment as the main roadmap (`…test-runs/` under `kg-wmservice`, not `kg-wmservice-tests`), so pruning must strip `-tests` to match what the orchestrator wrote. The plan pins this explicitly rather than leaving the implementer to derive it from the raw basename — a genuine fantasy-hole closure.

### Findings

**Finding 1 (Low — clarity, Task 1 test-runs sentence).**
The Task 1 bullet updating the tests-mode sentence reads: *"…so `test-runs/` follows the same branch … `test-runs/<stem>/` in the named case (the same shared `<stem>` derived above, so pruning **either partner** of a named pair sweeps the one `test-runs/<name>/` the orchestrator wrote)."*

The parenthetical "pruning either partner … sweeps the one `test-runs/<name>/`" is at odds with the gate it is updating. The current sentence (file line 274) sweeps `test-runs/` **only in tests mode** — i.e. only when the pruned target is the test roadmap. The main roadmap's prune (`roadmaps/<name>.md`) sweeps `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/` but must **not** touch `test-runs/`, exactly as the default `ROADMAP.md` prune does not. "Either partner" invites an implementer to broaden the test-runs sweep to the main-roadmap prune, dropping the "in that mode only" gate.

The author's actual intent is almost certainly path-disambiguation (the shared stem means the test-runs subdir is unambiguously `test-runs/<name>/` regardless of which partner's name you started from), not a change to which prune triggers the sweep. Recommend rewording so the two concerns are separated: keep the tests-mode gate explicit ("`test-runs/` is swept only when the pruned target is the test roadmap"), and state the stem-sharing only as path resolution (`test-runs/<name>/`, `-tests` stripped). This lives entirely within the milestone's single-file boundary, so it is a finding rather than a deferred observation, but it is low severity — a careful implementer working from the retained "in that mode only" phrasing will likely gate correctly.

### Positive Notes
- Excellent reference discipline: every task cites the layout owner and refuses to duplicate it, keeping the `loads:` contract intact.
- The three "Step 5 deletes these files" premises are each individually reconciled with the new sweep-scoped capture (Task 2 items 2 & 6, Task 3 Step-8), and the plan supplies a concrete grep to prove no blanket premise survives — this is the kind of cross-clause coherence that usually gets missed.
- The gate-scope vs. margin-capture-scope divergence (gate repo-wide; capture follows the sweep) is called out with an explicit instruction to prevent the implementer from "fixing" one to match the other — a real trap, pre-empted.
- Byte-stability of the default-pair path is preserved and stated (three flat dirs minus `patches/`), matching the spec's solo-repo invariant.
- Verification section is executable and matches the spec's own verification, including the `-tests` dry-read case.

## Deferred observations
- Affects: unknown (out of milestone scope) — the working tree carries an uncommitted 1-line edit to `docs/multiuser-roadmaps.md` (the `-tests` slug hard-stop sentence) from a different task. It does not touch `roadmap-prune/SKILL.md` and is outside this milestone's file boundary; noting only so it is not mistaken for part of this plan's diff at implement time.
