# Plan Review 2 — 15.1 agent-architect: relay by `::` marker, not by classification

**Artifacts reviewed:** plan `09-15-1`, spec `70-architect-relay-marker.md` (incl. its uncommitted amendment), handoff `22`, target `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`, ROADMAP.md:49–53, plan-review 1
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — PASS.** Body-only edit to one skill in `src/skills/`; no `loads:` edge created, forward graph unchanged, no engine reverse-graph marker touched. `src/agents/editor.md` correctly left untouched (spec `70:36` rejects adding discrimination on the editor side, and the plan honors that).
- **Rules — WARN (non-blocking).** No `.ai-factory/RULES.md`, no `.ai-factory/skill-context/aif-review/SKILL.md` in this repo. Governing conventions taken from the root CLAUDE.md language contract; the plan writes in registry vocabulary (relay, work-order, channel, task spec, phase) and treats `PLAN_REVIEW_PASS` / the grep literals as protocol tokens.
- **Roadmap — PASS.** ROADMAP.md:53 carries 15.1 under `### Phase 15 — \`::\` marks the relay; the architect stops guessing`, `Spec: .ai-factory/specs/70-architect-relay-marker.md`. Title matches; the spec resolves and was walked to the leaf (`SKILL.md`, `editor.md`).

### Round-1 findings — both closed

- **Marker direction (round-1 issue 1) — closed.** Task 2 (`:38`) now pins it explicitly: the marker is the user's, on the user's own message; the answer reaches the editor only if the user's own reply ends with `::`; the architect never appends the marker to an unmarked message. The reading that reintroduced the architect-initiated send is no longer available to an implementer.
- **Warm-editor / expansion collision (round-1 issue 2) — closed in the plan.** Task 2 (`:39`) scopes the guard to the architect's own initiative, forbids the state-tracking form outright, and grounds the reasoning in handoff 22's actual violation #2 (verified at `handoffs/22…md:13` — the message was the bare "go, phase 7" with no slash-command). See Critical Issue 1 below for the one loose end this leaves.

### Mechanical claims — re-verified against the file

- `grep -n "brief"` → **37, 72, 91**, exactly as Task 6 predicts, each assigned to the task that kills it.
- `grep -n "standing judgment\|deciding which of the user"` → **67**, inside Task 2's deleted paragraph. Post-edit zero is achievable.
- No `loads:` in `agent-architect` frontmatter (the sole occurrence is body prose at line 54 about the *editor's* resolution) — Assumption 1 holds.
- Spec ranges are off by one against the file (spec says 42–63 / 65–74; file has heading 40, section 42–62, standing-judgment paragraph 64–73) — Assumption 2 holds, and locating by quoted opening words is the right mitigation.
- `editor.md:74` does contract *"every round is self-contained by contract"*, so Task 4's respawn claim rests on ground truth.
- Frontmatter field list in Task 6 matches the file exactly.
- The spec's uncommitted amendment (death-is-loud, the brief sweep, spawn-on-first-channel-message) is now upstream of the plan, so Decisions 2 and 3 restate spec text rather than inventing it — correctly attributed to spec 70.

### Critical Issues

**1. The plan overrides spec 70 on the warm-editor rule but leaves the spec unamended in three places — the implement→review stage will read that as non-conformance.**
Task 2 (`:39`) instructs, in bold: *"Do **not** write 'a warm editor is never re-sent a skill it already read'."* Spec 70 still states that rule three times: §Edits (`70:31`, closing sentence), §Guards (`70:47`, *"A warm editor is never re-sent a skill it already read (the second handoff-22 violation)"*), and §Verification (`70:57`, *"…and a warm editor is not re-sent a skill"*).

The plan's reasoning is sound and I agree with the outcome — the rule as phrased requires tracking what the editor has already read, which is the per-message judgment Phase 15 exists to delete, and it collides with the unconditional expansion rule. But the resolution is recorded only inside the plan. The spec was already amended in this working tree for the other round-1 gaps (`git diff` shows the death-is-loud paragraph, the spawn-on-first-channel-message rule, and the brief-sweep bullet all added), which establishes that amending the spec is in this task's hands. Leaving one clause out of that pass means the review stage checks the edited body against `70:57` and finds the warm-editor bullet unimplemented — a conformance failure with no artifact explaining why, i.e. exactly the loop shape `task-rescue` gets called for.

Close it one of two ways: amend `70:31`, `70:47`, and `70:57` to the initiative-scoped form (the architect never adds a skill reference the payload does not contain; a slash-command in the payload expands unconditionally), or add an explicit `DEVIATION:` note in the plan naming the three spec lines superseded and why — the same treatment Task 6 already gives handoff 22's second "correct behavior" bullet, which is handled exemplarily. The first is preferable: a task spec that still asserts a rule the implementation deliberately omits is a defect to reconcile, not stale description.

**2. Task 4 replaces the only sentence that names the spawn mechanic, without instructing that the mechanic be kept.**
`SKILL.md:30` — *"Spawn the editor with `Agent` at the start of the work"* — is the sole place in the body naming the `Agent` tool as the spawn instrument (the `Agent` and `SendMessage` entries in `allowed-tools` are frontmatter, which this task holds byte-stable). Task 4 (`:52`) directs the implementer to *"State instead: the first channel-message is the spawn…"*, replacing that sentence. Its `Keep:` list (`:54`) preserves *"one spawn, then every subsequent round into the same conversation via `SendMessage`"* — `SendMessage` survives by name, `Agent` does not.

An implementer following the task literally can land a body that says when the spawn happens but no longer says what performs it, leaving the architect to infer the tool. Add `Agent` to Task 4's `Keep:` list — the rewritten rule should read as *the first channel-message is what you spawn the editor with via `Agent`*, so the lifecycle change carries the mechanic through instead of trading it away.

### Positive Notes

- **The round-1 fixes are pins, not patches.** Task 2's marker-direction paragraph does not merely assert the rule — it names the misreading it forecloses ("relay the answer under a trailing `::`" reading as *the architect marks and forwards*) and ties it back to the standing judgment being deleted three sentences earlier. Prose that carries its own why survives an implementer's paraphrase; prose that only asserts does not.
- **The warm-editor override is argued from the mechanism, not from preference.** Task 2 shows the failure it guards against is *structurally impossible* under the marker design (expansion keys off a slash-command present in the payload; handoff 22 had none), rather than arguing the rule is inconvenient. That is the right shape of argument for deleting a stated guard — and it is why Critical Issue 1 is a bookkeeping gap, not a disagreement.
- **The retitle decision is correctly argued and correctly bounded.** `## Relay by default` is the exact proposition Phase 15 deletes; a heading asserting the opposite of its own section is this task's precise failure mode. Marking spec 70's and the plan's own use of the old heading as expected drift in already-written artifacts prevents an implementer from "fixing" the spec by re-titling backwards.
- **Task 3 catches a contradiction the spec's Edits list misses entirely.** Spec 70 §Edits never mentions §"Review in parallel", yet `SKILL.md:77` (*"send the editor its (relayed) review target"*) is a standing instruction to initiate a send that would survive the spec's edit list intact and contradict the marker gate. Keying the rule off an *arrived* relay is a real conformance catch, found by reading the file rather than the edit list.
- **Task 6's handling of the handoff-22 conflict is exemplary.** It names the superseded bullet, states the file is *supposed* to fail it, and directs verification against the spec's phrasing. This is the pattern Critical Issue 1 asks to be applied one more time.
- **Verification is proportionate.** No run-verification for a body change, two mechanical greps with pre-edit line numbers stated (and verified correct), plus a full end-to-end read for residual clauses — the right instinct, since both contradictions found beyond the spec's edit list (§"Review in parallel", the intro) sit outside it.

## Deferred observations

- Affects: Phase 14.1 / a follow-up description pass — `SKILL.md:3–9` still frames the skill as one that "drives a persistent editor subagent", written when the invocation itself brought the editor up; after Task 5 the ordinary invocation spawns nothing until the first channel-message arrives. The claim is not false (the editor does still apply every change), so this is not blocking, and spec 70's guard (`70:44`) explicitly holds the frontmatter byte-stable — correctly honored by the plan. Worth noting for whoever picks it up: 14.1 is already `[x]` in ROADMAP.md and named `agent-architect`'s description in its candidate list, so the "a later phase will handle it" premise behind that guard no longer holds and the framing has no scheduled reconciliation pass left. Fixing it inside this task would violate the spec's explicit frontmatter guard, so it belongs upstream. [fixed — agent-architect's description now reads "channels every change through a persistent editor subagent — spawned on first contact, kept for the session", replacing the pre-15.1 framing]

Both issues are contained: issue 1 is a three-line spec amendment (or one `DEVIATION:` note) in artifacts this task already edits, issue 2 is one word added to a `Keep:` list. Neither requires re-planning a task or rethinking the design.
