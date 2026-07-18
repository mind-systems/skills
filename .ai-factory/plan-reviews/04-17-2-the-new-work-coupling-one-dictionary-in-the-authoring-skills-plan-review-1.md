# Plan Review: 17.2 — The "new work" coupling: one dictionary in the authoring skills

## Code Review Summary

**Files Reviewed:** 1 plan + 7 target files + spec 63 + ROADMAP + ARCHITECTURE
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is untouched by this task: no `loads:` edge, no engine/lens boundary, no reverse-graph marker is in scope. Naming-only conformance does not move the graph.
- **Rules** — WARN (non-blocking). No `.ai-factory/RULES.md` in this repo; conventions live in CLAUDE.md and `docs/reserved-words.md`, both of which the plan cites correctly.
- **Roadmap** — OK. `ROADMAP.md:28` is the contract line for 17.2 and names `Spec: .ai-factory/specs/63-new-work-coupling-reserved-words-conformance.md`. Read that spec and its own governing spec [reserved-words](../../docs/reserved-words.md). The plan conforms to the contract line on every pinned decision: `milestone`→**phase** in outline's `description:`, `milestone`→**task** in decompose/skeleton, outline's `Use when` trigger word retained, aif-docs:70 `ROADMAP milestone`→`ROADMAP phase`, detection-list "this milestone" left. No drift from the contract line.
- **Skill-context** — no `.ai-factory/skill-context/aif-review/SKILL.md` present; no project overrides to apply.

### Critical Issues

None. Nothing here breaks behavior or loses a site. The findings below are correctness defects in the plan's own assumptions and gates.

### Findings

**1. Assumption 1's byte-length-preservation claim is false for the majority of the sweep — and Task 3 contradicts it outright.** (`plans/04-17-2…md:16`, `:38`)

Assumption 1 justifies freezing line counts by asserting the substitutions are length-preserving: "`spec` → `task` and `note` → `spec` are both 4 chars, and `spec note` → `task spec` is 9 → 9, so the wrapped sites are byte-length preserving." That holds only for the contiguous `spec note` → `task spec` swaps. It does **not** hold for the bare-note sweep the plan itself mandates in Tasks 5 and 7, where bare `note` → `task spec` is +5 chars per site, nor for Task 3's chosen rewrite, which is +7. Measured against the live files:

| Site | Now | After |
|---|---|---|
| `roadmap-decompose:6` | 93 | ~100 |
| `roadmap-decompose:79` | 85 | 90 |
| `roadmap-decompose:81` | 87 | 92 |
| `roadmap-decompose-skeleton:122` | 89 | ~96 |
| `roadmap-decompose-skeleton:123` | 84 | 94 |
| `roadmap-decompose-skeleton:126` | 90 | 95 |

Line *counts* still hold, so the frozen-count discipline survives — the consequence is ragged lines up to ~100 cols in files hard-wrapped at ~85. That is tolerable, but the plan should say so deliberately rather than resting on a premise that is arithmetically wrong for six of its sites.

The sharper problem is that Task 3 then licenses the opposite: "Re-wrap **within the folded block only** if a line overruns; the block's line count should stay at 5." Assumption 1 says "do not rewrap"; Task 3 says rewrap if it overruns — and line 6 *will* overrun, to ~100 chars. Two directives, opposite outcomes, on the one line where the question actually arises. An implementer cannot produce a deterministic result. Pin it: either state explicitly that `roadmap-decompose:6` is left long and unwrapped (consistent with 17.1's landed discipline and with the fact that line 6 is *already* a 93-char outlier), or pin the exact 5-line rewrap byte-for-byte. Do not leave it to judgment — every other site in this plan is pinned.

**2. Task 10's second verification gate expects the wrong number — it will read as a false failure.** (`plans/04-17-2…md:77`)

The gate reads: `rg -U -in '[^-]milestones?' …` → "**exactly two survivors**: `roadmap-outline:3`'s user-trigger word and `aif-docs`' detection-list `"this milestone"` (26, 182)". Those are two *kinds* of survivor but **three** matching lines — `rg` reports per line, and `aif-docs` carries the phrase at both 26 and 182 (confirmed in the live file). An implementer running the gate gets 3 hits against a stated expectation of 2 and must either report the gate failed or "fix" a line the plan explicitly protects. Since this is the task's own acceptance criterion, state it as three matching lines across two exempt categories.

**3. Task 3 quotes a fragment that straddles the line break it attributes it to.** (`plans/04-17-2…md:38`)

Task 3 says: "line 6 `with the full spec persisted as a note` → `with the full detail persisted as a task spec`". In the live file, `with` is the **last word of line 5** (`…naming the key files, types, and guards, with`); line 6 begins `the full spec persisted as a note`. The intended edit is entirely inside line 6 and is unambiguous in substance, but an implementer doing an exact-string `Edit` on the quoted text will fail to match. Requote to the line-6 text alone. (Contrast Task 5, which handles the analogous wrap at 29–30 precisely and correctly.)

**4. Tasks 6 and 7 both edit skeleton lines 122 and 124, with no "apply both" note.** (`plans/04-17-2…md:53`, `:58`)

Task 6 edits line 122 (`**impl** milestone` → `**impl** task`) and line 124 (`are now separate milestones` → `tasks`); Task 7 edits the *same two lines* (`` `Spec:` note `` → `` `Spec:`-tagged task spec ``; `a new note` → `a new task spec`). The plan flags exactly this collision for `roadmap-decompose:83` — "same line as Task 4's edit — apply both" — but omits the equivalent note here. The sequential dependency makes the right outcome likely, not guaranteed; an implementer re-reading line 122 after Task 6 may not recognize Task 7's quoted pre-edit text. Add the same cross-reference on both lines. Note also that the net change on 124 is length-neutral (−5/+5), which is worth stating given finding 1.

**5. Task 10's third gate lists expected residue categories that do not exist in the files it scans.** (`plans/04-17-2…md:78`)

The gate expects `\bnotes?\b` survivors to be "only backticked `` `note` `` (the skill name), `loads:` values, quoted section titles, and `aif-docs:41`'s `**Note:**`". Verified against the live files: none of the four edited files contains a backticked `note` skill reference, and all three roadmap skills declare `loads: roadmap-engine` / `roadmap-engine test-philosophy` — `note` appears in no `loads:` value here. After the sweep the only legitimate survivor is `aif-docs:41`. The gate is not wrong, but it is loose enough to wave through a genuine residue as one of the phantom categories. Sharpen the expected value to the one line.

### Positive Notes

- **The site inventory is verified, not inherited.** I re-ran the greps against the live files: every `milestone`, `spec note`, and bare artifact-`note` occurrence in the four edited files is accounted for by a task — decompose 6/18/30/78/79/81/83/93, skeleton 35/117/122/123/124/126/127/132, outline 40/41, aif-docs 41/70. **Zero missed sites.** The plan's decision to re-ground on a fresh 2026-07-18 grep rather than trust the spec's 2026-07-13 inventory is exactly right, and it paid off.
- **The certification is real.** `rg -U -in 'spec\s+notes?|milestones?' src/skills/agent-architect/SKILL.md src/agents/editor.md` returns zero (exit 1), confirming Task 9's expectation before the work starts.
- **All five `wc -l` baselines are correct** as stated (outline 75, decompose 97, skeleton 148, aif-docs 271).
- **Cross-file consistency is handled.** `roadmap-decompose-skeleton:126` references `roadmap-decompose`'s "in-place note-update discipline" — the plan renames both sides in lockstep (Task 5 renames the discipline, Task 7 updates the reference). This is the kind of coupling a per-file sweep silently breaks, and it was caught.
- **The `Spec:` tag / artifact distinction is pinned per site, not left to judgment** (Assumption 2), including the genuinely subtle call at skeleton:132 where `note tag` means the tag and the noun is dropped rather than substituted.
- **The mention-vs-use distinction at `aif-docs:26/182` is correctly reasoned**: rewriting a phrase inside a forbidden-phrase detection list would change behavior by making the detector miss what it exists to catch. Correctly identified as behavior, not naming.
- **Scope restraint is exercised and surfaced, not silently expanded** — `command-pin-gaps:17`'s bare artifact-`note` is left alone per spec 63 § Guards and reported to the reviewer.

---

None of the five findings is a blocker on approach — the plan's substance, scope, and site coverage are sound. All five are fixable within the plan file itself without touching the task's boundary: correct the gate arithmetic (2), tighten the two loose gate expectations (1, 5), requote one fragment (3), and add one cross-reference (4).
