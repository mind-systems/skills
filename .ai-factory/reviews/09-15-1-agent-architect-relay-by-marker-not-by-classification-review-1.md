# Review — 15.1 agent-architect: relay by `::` marker, not by classification

**Artifacts reviewed:** `git diff HEAD`, `git status`, `src/skills/agent-architect/SKILL.md` (full), `src/agents/editor.md` (full), `.ai-factory/specs/70-architect-relay-marker.md` (full diff), plan `09-15-1`, handoff 22, `docs/reserved-words.md`
**Changed files in scope:** `src/skills/agent-architect/SKILL.md` (body), `.ai-factory/specs/70-architect-relay-marker.md` (amendment); the plan/plan-review/`.json` artifacts are pipeline output, not reviewed as product.
**Risk Level:** 🟢 Low

## Mechanical verification — all pass

| Guard | Result |
|---|---|
| `grep -n "brief" src/skills/agent-architect/SKILL.md` | exit 1, zero matches ✓ |
| `grep -n "standing judgment\|deciding which of the user" …` | exit 1, zero matches ✓ |
| Frontmatter byte-stable | ✓ — diff hunk opens at line 17; `name`, `description`, `argument-hint`, `user-invocable`, `disable-model-invocation`, `allowed-tools` untouched, no `loads:` introduced |
| `src/agents/editor.md` untouched | ✓ — `git status --porcelain` returns nothing |
| Body-only change | ✓ |

Every edit the plan ordered is present: the retitle (`## Relay on the marker; …`, :54), the marker rule with unconditionality and the mid-message-literal clause (:56–68), the why-trailing rationale (:70–74), the `/agent-architect` carve-out from skill-by-reference expansion (:81–84), the initiative-scoped skill guard with no warm-editor state check (:84–87), the work-order paragraph unchanged (:89–94), the two-channel contrast (:96–98), the review section re-keyed to an *arrived* relay (:110–112), the spawn lifecycle with `Agent` retained as the instrument (:33–39), loud death with no auto-replay (:43–52), the digest as an unsent recovery note (:41–43), and `"nothing drifted past the work-order"` (:125).

**The one interaction risk I went looking for is clean.** The spawn-by-work-order limb is new and `editor.md` was deliberately not changed, so I checked whether the editor assumes its first message is a relay. It does not: `editor.md:17–22` detects mode per round from what arrived, `:50–56` treats whatever arrives as the whole unit, and `:74–76` contracts every round self-contained. An editor spawned directly with a work-order lands in apply mode correctly. No change needed there, and adding one would violate the spec's rejection of editor-side discrimination.

## Findings

### 1. MEDIUM — The migrated scope-question rule has a gate but no path: the editor's question is unanswerable unless the user happens to know to append the marker

`SKILL.md:100–106`. The rule reads: carry the editor's scope question to the user verbatim, then *"the user's answer reaches the editor only if the user's own reply ends with `::` — you never append the marker to a message the user did not mark, and an unmarked answer is yours to hold, not to forward."*

The gate is correct and is exactly what plan-review round 1 asked for. What is missing is the other half. Consider the natural sequence:

1. Editor flags back "which skeleton pass?" and ends its round.
2. Architect carries the question to the user verbatim, as instructed.
3. The user — who is answering a question the *architect* just put to them, in conversation — replies "the second one", unmarked.
4. Architect holds it. The editor never receives the answer.

Nothing hangs (subagent rounds don't block), but the sub-rule spec 70 §Edits calls "still-live" — *"an editor scope-question is carried to the user verbatim and the answer relayed back"* — does not actually complete in the common case. The answer reaches the editor only when the user independently remembers a marker they were not prompted for, in the one exchange where an unmarked reply is the most natural thing to type.

The fix is one clause and does not weaken the gate: when carrying the question, the architect says that a reply ending with `::` is what reaches the editor. That is the architect *informing*, with the user still deciding — not the architect classifying, so it does not reopen the drift surface. Without it, the body implements a prohibition where the spec specified a round trip.

Suggested: after "carry it to the user verbatim", add that you tell the user a marked reply is what goes to the editor — the decision stays theirs, you neither mark nor withhold silently.

### 2. LOW — The spawn lifecycle is stated normatively in two places and will drift

`SKILL.md:20–23` (intro) and `:33–35` (§"Spawn once") both state the same rule: the architect works alone until the first channel-message — a `::` relay, or the apply work-order where none arrived — spawns the editor. Both are normative statements of the same fact, not a framing plus a rule.

This is per-plan (Tasks 4 and 5 each ordered their edit independently) so it is not an implementation error, but it lands against the repo's own explicit constraint — CLAUDE.md § "Project CLAUDE.md authoring": *"One home per fact. Anything stated in two places will drift."* This file is a surface where that binds. The precise hazard is live: a future edit that revises the spawn rule in §"Spawn once" leaves the intro asserting the old lifecycle, which is the same class of defect as the `## Relay by default` heading this task existed to fix.

Cheapest resolution: keep the rule in §"Spawn once" (its home) and let the intro reference the editor as the hand that applies every change *once spawned*, without restating when the spawn happens.

### 3. LOW — "and you say so until it exists" has an unclear referent

`SKILL.md:22–23`: *"…spawns the **editor**, and you say so until it exists."* Read literally, "say so" has no clear antecedent (say *what* — that no editor exists? to whom? on every message?). The intent, from the plan's "and says so", is that the architect tells the user it is working alone before any channel-message. As written, an architect could equally read it as an instruction to repeat the disclaimer every turn, or skip it as decorative.

Naming the object closes it: "…and you tell the user you are working alone until it exists."

## Not findings — checked and clear

- **New compound "channel-message" is not in `docs/reserved-words.md`.** I checked whether this is vocabulary drift under the language contract. It is not: the registry has no paired-loop section at all — `relay`, `work-order`, `architect`, and `editor` are equally absent (the only `work-order` hit is `:23`, an unrelated gloss on *task spec*). The term is introduced in spec 70 and used consistently there and in the body, which is the correct pattern for a concept whose family is unregistered. Registering the paired-loop vocabulary is a separate concern, not this task's.
- **`description:` vs. the new body.** The description still says the architect "drives a persistent editor subagent". Under the new rule the ordinary invocation spawns nothing until a channel-message arrives — but the claim is not false (the editor does still apply every change), and spec 70's guard holds the frontmatter byte-stable. Correctly untouched. See deferred observation.
- **Spec amendment is complete and consistent.** All three warm-editor assertions (§Edits, §Guards, §Verification) are amended to the initiative-scoped form, each carrying its reasoning; the spec no longer asserts a rule the body deliberately omits, so the spec/implementation disagreement plan-review 2 flagged is closed rather than papered over with a deviation note.
- **No residual architect-initiated send.** Read the body end to end: §"Review in parallel" now keys off an arrived relay, §"Verify the editor's report by fact" and §"The user rules the forks" are architect↔user or file-check surfaces, and `AskUserQuestion` fork answers are structurally unmarked and therefore correctly never forwarded.

## Deferred observations

- Affects: Phase 14.1 / a follow-up description pass — `SKILL.md:3–9` frames the skill as one that "drives a persistent editor subagent", written when the invocation itself brought the editor up. Spec 70's frontmatter guard correctly forbids touching it here, but that guard's stated premise is that Phase 14.1 handles description altitude — and 14.1 is already `[x]` in ROADMAP.md with `agent-architect`'s description named in its own candidate list. The framing therefore has no scheduled reconciliation pass left. This is the third consecutive review to raise it; it needs an owner upstream of this task, not a fix inside it. [fixed — agent-architect's description now reads "channels every change through a persistent editor subagent — spawned on first contact, kept for the session", replacing the pre-15.1 framing]
- Affects: `docs/reserved-words.md` — the paired-loop vocabulary (relay, channel-message, work-order, architect, editor) is entirely unregistered while the two files that use it are surfaces where the language contract binds. Worth one deciding read on whether the registry should grow a paired-loop section; out of scope here. [fixed — added a "Paired loop" section to docs/reserved-words.md registering architect, editor, relay, channel-message, work-order]

Finding 1 is the only one I would ask to be fixed before this is considered done — it is a one-clause addition inside a section this task already rewrote, and without it the spec's round trip does not close. Findings 2 and 3 are wording-level and could ride a later pass without risk.
