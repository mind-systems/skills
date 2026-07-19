# Re-review — 15.1 agent-architect: relay by `::` marker, not by classification

**Prior review:** `09-15-1-…-review-1.md` (3 findings: 1 MEDIUM, 2 LOW)
**Artifacts re-read this pass:** `git status`, `git diff HEAD`, `src/skills/agent-architect/SKILL.md` (full, 154 lines), `src/agents/editor.md`, `.ai-factory/specs/70-architect-relay-marker.md` (diff), plan `09-15-1`
**Changed files in scope:** `src/skills/agent-architect/SKILL.md` (body), `.ai-factory/specs/70-architect-relay-marker.md` (amendment, unchanged since review 1)
**Risk Level:** 🟢 Low

## Verdicts on the previous review's findings

### Finding 1 (MEDIUM) — scope-question rule had a gate but no path → **Fixed**

Current `SKILL.md:100–107`:

> When the editor flags back a scope question ("which skeleton pass?", "what's
> the scope of phase 8?"), carry it to the user verbatim **and tell them a reply
> ending with `::` is what reaches the editor** — resolving the question
> yourself is the same contamination re-entering through the back door. The
> marker is the user's, on the user's own message; you only read it, never
> write it: the user's answer reaches the editor only if the user's own reply
> ends with `::` — you never append the marker to a message the user did not
> mark, and an unmarked answer is yours to hold, not to forward.

The round trip now closes. The architect informs the user what makes a reply reach the editor, and the user still decides — so the gate is intact (the architect neither marks the message nor forwards an unmarked one) while the failure case I traced is gone: a user answering the architect's relayed question is now told what a marked reply does, rather than being expected to remember a marker nobody mentioned.

Incidental improvement worth noting: the clause that followed was reworded "resolving **it** yourself" → "resolving **the question** yourself". With a second referent (the reply) now in the sentence, the bare pronoun would have been ambiguous. That is the kind of second-order effect an implementer often misses.

### Finding 2 (LOW) — spawn lifecycle stated normatively in two places → **Fixed**

Current `SKILL.md:20–23` (intro) — the lifecycle restatement is gone, replaced by a cross-reference:

> You reason, review, and
> decide; the **editor** — a persistent subagent you keep once spawned (see
> "Spawn once, message thereafter") — is the hand that applies every change and
> reports back; you check what landed against the files themselves, never
> against the report.

Current `SKILL.md:31–35` (§"Spawn once, message thereafter") — the rule now has exactly one home, and the "work alone" behavior moved here with it:

> Until the first channel-message arrives, you work alone on the unit named
> and tell the user you are working alone until it exists. The first
> channel-message is the spawn — the first `::` relay or, where none has
> arrived, the first authored apply work-order — and its content *is* the
> spawn prompt; there is no spawn before one exists.

This is the one-home-per-fact resolution done properly: the fact lives in §"Spawn once", and the intro reaches it by a link rather than a copy — the repo's own rule that a fact's second home is a link, never a copy. The cross-reference text matches the section heading exactly (`## Spawn once, message thereafter`), so it resolves.

### Finding 3 (LOW) — "and you say so until it exists" had an unclear referent → **Fixed**

The phrasing no longer appears anywhere in the file. Its replacement, in the §"Spawn once" quote above, names the object explicitly: *"**tell the user** you are working alone until it exists."* The instruction is now unambiguous about whom the architect addresses, which was the finding.

## Mechanical guards — all re-run, all pass

| Guard | Result |
|---|---|
| `grep -n "brief" src/skills/agent-architect/SKILL.md` | exit 1, zero matches ✓ |
| `grep -n "standing judgment\|deciding which of the user" …` | exit 1, zero matches ✓ |
| Frontmatter byte-stable | ✓ — diff hunk opens at line 18; no `loads:` introduced |
| `src/agents/editor.md` untouched | ✓ — absent from `git status --porcelain` |
| Spec amendment unchanged since review 1 | ✓ — same 10 insertions / 6 deletions |

## New-issue pass

I re-read the full body against the plan and against runtime behavior, with attention to what the fix itself could have broken.

- **The fix introduced no new contradiction.** Moving "work alone until spawned" from the intro into §"Spawn once" does not orphan it — it sits directly above the spawn rule it qualifies.
- **No residual architect-initiated send.** §"Review in parallel" (`:111`) keys off an arrived relay; §"Verify the editor's report by fact", §"Your buffer" (`:136`, "the editor is never told about it"), and §"The user rules the forks" are architect↔user or file-check surfaces; `AskUserQuestion` answers are structurally unmarked and therefore correctly never forwarded.
- **The new "tell them a reply ending with `::`" instruction does not reopen the drift surface.** It is the architect informing; the classification decision stays with the user's own keystrokes, which is the phase's whole thesis.
- **`editor.md` still needs no change.** Re-confirmed against the current body: mode detection per round (`editor.md:17–22`) and the self-contained-round contract (`:74–76`) hold under both the relay-spawn and work-order-spawn limbs.
- **Every path traced:** relay before spawn → that relay *is* the spawn; relay while editor dead → death-is-loud, report before anything is sent onward; unmarked message → held, never forwarded; slash-command in payload → expands unconditionally; `/agent-architect` invocation → explicitly carved out of expansion.

Two wording micro-nits I looked at and am deliberately **not** raising as findings, since neither changes behavior: `:31` reads "Until the first channel-message arrives … until it exists", a mild redundancy, and "the unit named" is slightly clipped from the intro's "whatever unit of work `$ARGUMENTS` names". Both readings converge on identical behavior.

## Deferred observations

These belong to other tasks and do not block this one; both are carried forward unchanged from review 1.

- Affects: Phase 14.1 / a follow-up description pass — `SKILL.md:3–9` frames the skill as one that "drives a persistent editor subagent", written when the invocation itself brought the editor up; the ordinary invocation now spawns nothing until a channel-message arrives. Not false (the editor does still apply every change), and spec 70's guard correctly holds the frontmatter byte-stable, so fixing it here would violate the spec. But that guard's premise is that 14.1 handles description altitude, and 14.1 is already `[x]` in ROADMAP.md with `agent-architect` named in its own candidate list — so the framing has no scheduled reconciliation pass left. Raised in three consecutive reviews now; it needs an owner upstream. [fixed — agent-architect's description now reads "channels every change through a persistent editor subagent — spawned on first contact, kept for the session", replacing the pre-15.1 framing]
- Affects: `docs/reserved-words.md` — the paired-loop vocabulary (relay, channel-message, work-order, architect, editor) is entirely unregistered, while the two files using it are surfaces where the language contract binds. `channel-message` is introduced in spec 70 and used consistently in both artifacts, which is the correct pattern for an unregistered family; whether the registry should grow a paired-loop section is a separate decision. [fixed — added a "Paired loop" section to docs/reserved-words.md registering architect, editor, relay, channel-message, work-order]

All three prior findings are fixed, the mechanical guards pass, and I found no new defects.

REVIEW_PASS
