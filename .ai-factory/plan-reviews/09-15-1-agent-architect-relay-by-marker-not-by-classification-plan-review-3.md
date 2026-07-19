# Plan Review 3 — 15.1 agent-architect: relay by `::` marker, not by classification

**Artifacts reviewed:** plan `09-15-1`, spec `70-architect-relay-marker.md` (incl. its uncommitted amendment), handoff `22`, target `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`, ROADMAP.md:49–53, `docs/philosophy/skill-cycle.md`, `.ai-factory/ARCHITECTURE.md`, plan-reviews 1 and 2
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — PASS.** `.ai-factory/ARCHITECTURE.md:22` places `agent-architect` in `src/skills/` and `editor` in `src/agents/` as parallel categories; a body-only edit to one skill crosses no boundary. No `loads:` edge created, forward graph unchanged, no engine reverse-graph marker touched. `active/skills/agent-architect → ../../src/skills/agent-architect` verified — editing `src/` is what surfaces through `~/.claude/skills`, so the plan targets the right layer and needs no `active/` step.
- **Rules — WARN (non-blocking).** No `.ai-factory/RULES.md`, no `.ai-factory/skill-context/aif-review/SKILL.md` in this repo. Governing conventions taken from the root CLAUDE.md language contract; the plan writes in registry vocabulary (relay, work-order, channel, task spec, phase) and holds the grep literals and `PLAN_REVIEW_PASS` as protocol tokens.
- **Roadmap — PASS.** ROADMAP.md:53 carries 15.1 under `### Phase 15 — \`::\` marks the relay; the architect stops guessing`, `Spec: .ai-factory/specs/70-architect-relay-marker.md`. Title matches the contract line; the spec resolves and was walked to the leaf (`SKILL.md`, `editor.md`).

### Round-2 findings — both closed

- **Critical 1 (warm-editor rule asserted in spec, overridden only in plan) — closed at the spec.** All three spots are amended in the working tree, verified by `git diff .ai-factory/specs/70-architect-relay-marker.md`: §Edits (`70:31`) now reads *"The skill-re-send guard survives in initiative-scoped form… The warm-editor phrasing does **not** survive"*; §Guards (`70:47`) *"Not phrased as a warm-editor rule: that form requires tracking what the editor already read"*; §Verification (`70:57`) *"no skill reference appears that the payload did not contain"*. The plan's Decision 5 (`:19`) records the amendment and its reason — the review stage now checks the edited body against a spec that agrees with it, so the conformance-failure loop round 2 forecast cannot fire.
- **Critical 2 (`Agent` traded away in Task 4's lifecycle rewrite) — closed.** Task 4 (`:55`) now carries an explicit paragraph: the rewritten rule *"must still name `Agent` as what performs the spawn"*, with the reason stated (the replaced sentence at `SKILL.md:30` is the body's only mention, `allowed-tools` being frontmatter held byte-stable). `SendMessage` survives in the same `Keep:` list. The mechanic rides through the lifecycle change.

### Mechanical claims — re-verified against the file this round

- `grep -n "brief" src/skills/agent-architect/SKILL.md` → **37, 72, 91**, exactly Task 6's prediction; 72 dies in Task 2, 37 and 91 in Task 4.
- `grep -n "standing judgment\|deciding which of the user"` → **67**, inside Task 2's deleted paragraph. Post-edit zero is achievable.
- No `loads:` in frontmatter — the only occurrence is body prose at line 54 about the *editor's* resolution. Assumption 1 holds; "still absent" is the right reading of the spec's byte-identical clause.
- Spec ranges are off by one (spec: relay 42–63, standing-judgment 65–74; file: heading 40, section 42–62, paragraph 64–73). Assumption 2 holds, and every task's `Files:` quotes opening and closing words that resolve unambiguously — Task 1 (`heading` → *"over-told steps only drift."*) = 40–62, Task 2 (*"Relay is scoped to editor-bound work…"* → *"…re-brief it from the digest first."*) = 64–73. Both exact.
- Frontmatter field list in Task 6 matches the file exactly; `editor.md:74` does contract every round self-contained, so Task 4's respawn claim rests on ground truth.

### Retitle and propagation — checked repo-wide this round

The heading retitle (Decision 1) strands nothing. `grep -rn "Relay by default"` across the repo returns only the plan itself, spec `70:30`, ROADMAP.md:53, and the target line `SKILL.md:40` — no doc, skill, or command indexes the section by heading, so no cross-reference breaks. Nor is there a propagation gap outside the target: the only other files naming `agent-architect` are `editor.md` (correctly untouched — spec `70:36` rejects editor-side discrimination), `.ai-factory/ARCHITECTURE.md:22` (category placement only, no behavior claim), and `docs/philosophy/skill-cycle.md:25` (describes the pair generically — architect reasons and issues work-orders, editor applies and reports by fact, skills passed by reference — none of which the marker gate contradicts; the skill-by-reference sentence stays true, and Decision 4's carve-out narrows only which command expands, not the mechanism). `Docs: no` is therefore correct, not an omission.

### Critical Issues

None.

### Positive Notes

- **The spec was amended rather than deviated from.** Round 2 offered two closes — amend the spec, or file a `DEVIATION:` note — and the plan took the stronger one. That matters beyond bookkeeping: a task spec is a governing spec, so a rule it asserts that the implementation deliberately omits is a defect to reconcile, not a stale description, and Decision 5 says exactly that in those terms. The amendment also carries the *reason* into `70:47` (the warm form requires tracking what the editor read), so a later reader of the spec cannot restore the rule without meeting the argument.
- **Decision 4 remains the plan's sharpest independent catch.** Spec 70 nowhere states that skill-by-reference expansion must exclude the `/agent-architect` invocation itself; the plan reasons out that expanding it would hand the editor this very file and spawn a second architect. That hole would have shipped unnoticed — the spec's edit list says only "keep the existing expansion rule".
- **The lifecycle limbs are argued from deadlock, not from symmetry.** Decision 2 keeps the apply-work-order spawn limb because deleting the brief channel while forbidding the architect's own hands would otherwise leave a greenlit work-order with no editor to receive it. Task 4 restates the same reasoning at the point of edit, so the limb survives paraphrase.
- **Task 2's marker-direction pin names the misreading it forecloses.** It does not merely assert that the marker is the user's — it spells out that *"relay the answer under a trailing `::`"* would otherwise read as the architect marking and forwarding, which is the standing judgment deleted three sentences earlier. Prose carrying its own why is what survives an implementer's rewrite.
- **Task 3 still covers a section the spec's edit list never mentions.** `SKILL.md:77` (*"send the editor its (relayed) review target"*) is a standing instruction to initiate a send; it would have survived the spec's edits intact and contradicted the new gate. Keying it off an *arrived* relay is a conformance catch found by reading the file, not the edit list — as is Task 5's intro reconciliation.
- **Task 6 is proportionate and honest.** No run-verification for a body change (spec `70:49`), two mechanical greps with pre-edit line numbers stated and now verified correct, a full end-to-end read for residual clauses the edited sections wouldn't cover, plus a `git diff` frontmatter check. It also names handoff 22's second "correct behavior" bullet as deliberately superseded and states the edited file is *supposed* to fail it — the right way to resolve a governing-spec/description disagreement so a later reader doesn't file it as a regression.

## Deferred observations

- Affects: Phase 14.1 / a follow-up description pass — `SKILL.md:3–9` still frames the skill as one that "drives a persistent editor subagent", phrasing written when the invocation itself brought the editor up; after Task 5 the ordinary invocation spawns nothing until the first channel-message arrives. The claim is not false (the editor does still apply every change), so this is not blocking, and spec `70:44` explicitly holds the frontmatter byte-stable to stay clear of Phase 14.1 — a guard the plan correctly honors (Task 5 `:63`, Task 6 `:76`). Carried forward from reviews 1 and 2 because the premise behind that guard has expired: 14.1 is already `[x]` in ROADMAP.md and named `agent-architect`'s description in its candidate list, so no scheduled reconciliation pass remains. Fixing it inside this task would violate the spec's own frontmatter guard, so it belongs to whoever opens the next description-altitude pass. [fixed — agent-architect's description now reads "channels every change through a persistent editor subagent — spawned on first contact, kept for the session", replacing the pre-15.1 framing]

Both round-2 issues are closed at the artifact level rather than papered over in the plan, every mechanical prediction re-verifies against the file, and the retitle and propagation sweeps come back clean.

PLAN_REVIEW_PASS
