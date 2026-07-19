# Plan Review — 15.1 agent-architect: relay by `::` marker, not by classification

**Artifacts reviewed:** plan `09-15-1`, spec `70-architect-relay-marker.md`, handoff `22`, target `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`, ROADMAP line 53, ARCHITECTURE.md
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture — PASS.** `.ai-factory/ARCHITECTURE.md:22` places `agent-architect` in `src/skills/` and `editor` in `src/agents/` as parallel categories; a body-only edit to one skill crosses no boundary. No `loads:` edge is created, so the forward graph is unchanged and no engine's reverse-graph marker needs touching (reverse-graph grep for `agent-architect` returns only the file itself and `editor.md`, which the plan correctly leaves untouched).
- **Rules — WARN (non-blocking).** No `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md` in this repo; skill-context overrides do not apply. The governing conventions were taken from the root CLAUDE.md language contract instead — the plan's prose is written in registry vocabulary (relay, work-order, channel, spec, phase) and treats `PLAN_REVIEW_PASS`/`grep` literals as protocol tokens, correctly.
- **Roadmap — PASS.** ROADMAP.md:53 carries task 15.1 under `### Phase 15 — \`::\` marks the relay; the architect stops guessing` with `Spec: .ai-factory/specs/70-architect-relay-marker.md`. The plan's title matches the contract line; the spec resolves and was read to the leaf (`SKILL.md`, `editor.md`).

### Mechanical claims — all verified against the file

The plan's grep predictions are exact, which is the main thing a plan of this kind can get wrong:

- `grep -n "brief"` → lines **37, 72, 91** — precisely the three the plan names, and each dies in the task it is assigned to (37 in Task 4, 72 in Task 2, 91 in Task 4's reword).
- `grep -n "standing judgment\|deciding which of the user"` → line 67, inside the paragraph Task 2 deletes. Post-edit zero is achievable.
- The Assumptions section is right on both counts: the frontmatter has **no** `loads:` field (the only occurrence is line 54, body prose about the *editor's* resolution of `loads:`), and the spec's line ranges are off by one (spec says relay section 42–63 / standing-judgment 65–74; the file has heading at 40, section body 42–62, standing-judgment paragraph 64–73). Instructing the implementer to locate by quoted opening words rather than line number is the correct mitigation and the ranges quoted in the task Files: lines resolve unambiguously.
- Task 4's citation of `editor.md` is accurate — lines 74–76 do contract *"every round is self-contained by contract, and a fresh editor picking up from the next round alone must succeed just the same"*, so the "respawned editor resumes through the two channels" claim rests on real ground truth, not on an assumption.
- The frontmatter field list in Task 6 (`name`, `description`, `argument-hint`, `user-invocable`, `disable-model-invocation`, `allowed-tools`) matches the file exactly.

The Decisions section is also doing real work: pinning the retitle (Decision 1), the spawn/respawn lifecycle including the work-order limb that closes the no-relay deadlock (Decision 2), and the `/agent-architect` carve-out from skill-by-reference expansion (Decision 4) each close a hole the spec left open. Decision 4 in particular catches something the spec does not state at all — that expanding the invoking command would hand the editor `agent-architect/SKILL.md` and spawn a second architect. That is a genuine catch, not restatement.

### Critical Issues

**1. Task 2's migrated sub-rule is ambiguous about who appends the marker — and the ambiguity reintroduces the architect-initiated send that Task 3 exists to delete.**
`plans/09-15-1…md:37` instructs: *"when the editor flags back a scope question, carry it to the user verbatim and relay the answer — under a trailing `::`, like any relay."*

The marker is something the **user** puts on their own message; the architect only reads it. But "relay the answer under a trailing `::`" reads equally as *the architect appends the marker to the user's answer and forwards it*. An implementer taking that second reading writes prose in which the architect decides that a scope-question answer is editor-bound and marks it as such — which is exactly the standing judgment Task 2 is deleting three sentences earlier, and directly contradicts Task 1's bullet 2 (`no trailing \`::\` → conversation aimed at you; **never** forwarded`) and Task 3's closing line (*"The architect never decides *when* something goes to the editor; the marker does"*). The failure is silent: the file would read coherently and still restore the drift surface.

Pin the direction in the task text: the architect carries the editor's scope question to the user verbatim, and the user's answer reaches the editor **only if the user's own reply ends with `::`** — the architect never appends the marker to a message the user did not mark, and an unmarked answer is the architect's to hold, not to forward.

**2. Task 2's "a warm editor is never re-sent a skill it already read" collides with Task 1's unconditional expansion rule, and the plan does not resolve which wins.**
Task 1 bullet 4 (`:31`) keeps skill-by-reference expansion as a *mechanical* transformation the relay carries, under a marker the plan repeatedly calls unconditional ("no check of whether the user 'meant' it"). Task 2 (`:37`) then adds: *"Also state that a **warm** editor is never re-sent a skill it already read."*

Concrete collision: round 1 the user sends `/roadmap-decompose phase 7 ::`; round 3 they send `/roadmap-decompose phase 8 ::`. Task 1 says expand and send, adding nothing, no judgment. Task 2 says don't re-send a skill the editor already read. The implementer must pick one, and either choice is defensible from the plan — so the resulting prose is unpredictable. Worse, the Task 2 form as written requires the architect to track *what the editor has already read* and gate a send on it, which is a per-message judgment of exactly the kind Phase 15 deletes; it is the classification surface re-entering through a different door than the one Task 2 is closing.

Note what handoff 22's violation #2 actually was (`handoffs/22…md:13`): the user's message was the bare *"go, phase 7"* with **no slash-command in it**, and the architect expanded a skill on its own initiative anyway. Under the marker design that failure is already structurally impossible — expansion is keyed to a slash-command present in the payload, and there is none to expand. The guard is satisfied by the mechanism, not by an added rule.

Scope the sentence to the architect's own initiative rather than to the editor's warmth: the architect never adds a skill reference the payload does not contain; where the user does type a slash-command, it expands unconditionally, warm editor or not. That keeps handoff 22's second violation closed, keeps Task 1's rule mechanical, and removes the state-tracking judgment.

### Positive Notes

- **The deadlock check is the plan's strongest move.** Decision 2 spots that deleting the brief channel while forbidding the architect's own hands leaves a greenlit work-order with no editor to receive it, and closes it by making the work-order a spawn limb. The spec states the same lifecycle (`70:22`) but does not name the deadlock as the reason; the plan reasoning it out independently is why the limb is stated as a rule rather than copied as a phrase.
- **The retitle decision is correctly argued and correctly bounded.** Recognizing that `## Relay by default` is the exact proposition being deleted — and that a heading contradicting its own section is this task's precise failure mode — is right; explicitly marking spec 70's and the plan's own use of the old heading as expected drift in already-written artifacts, not a defect to reconcile, prevents an implementer from "fixing" the spec.
- **Task 3 catches a contradiction the spec's Edits list misses entirely.** Spec 70 §Edits never mentions §"Review in parallel", yet line 76–78 (*"send the editor its (relayed) review target"*) is a standing instruction to initiate a send and would survive the spec's edit list intact, contradicting the rewritten relay gate. Finding it and keying the rule off an *arrived* relay is a real conformance catch.
- **Task 6 handles the handoff-22 conflict honestly.** Rather than quietly ignoring handoff 22's second "correct behavior" bullet (*"brief with context only when the editor is genuinely fresh or respawned"*), it names the bullet as deliberately superseded by spec 70 and instructs verification against the spec's phrasing — stating outright that the edited file is *supposed* to fail that bullet. That is the right resolution of a governing-spec/description disagreement, and stating it prevents a later reader from filing it as a regression.
- **Verification is proportionate.** No run-verification for a skill body change, two mechanical greps as backstops, plus a full end-to-end read for residual clauses "the edited sections are not the only place such a clause could sit" — which is the right instinct, since both surviving contradictions in this file (§"Review in parallel", the intro) sit outside the spec's own edit list.

## Deferred observations

- Affects: Phase 14.1 / a follow-up description pass — the `description:` field (`SKILL.md:3–9`) still frames the skill as one that "drives a persistent editor subagent", written when the invocation itself brought the editor up. After Task 5 the ordinary invocation spawns nothing until the first channel-message arrives. The claim is not false (the editor does still apply every change), so this is not a blocking inconsistency, and the spec's guard (`70:44`) explicitly holds the frontmatter byte-stable to stay clear of Phase 14.1 — correctly honored by the plan. Worth noting for whoever picks it up: 14.1 is already `[x]` in ROADMAP.md:43 and its candidate list named `agent-architect`'s description, so the "a later phase will handle it" premise behind that guard no longer holds; the description's framing has no scheduled reconciliation pass left. Fixing it here would violate the spec's explicit frontmatter guard, so it belongs upstream, not in this task. [fixed — agent-architect's description now reads "channels every change through a persistent editor subagent — spawned on first contact, kept for the session", replacing the pre-15.1 framing]

Both critical issues are wording-level pins inside task text the plan already owns — neither requires re-planning the task or amending spec 70.
