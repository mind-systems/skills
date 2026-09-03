# Review: agent-architect — pairing roles for two architects working together

**Plan:** `.ai-factory/plans/trickster77777/12-26-4-agent-architect-pairing-roles-for-two-architects-working-together.md`
**Governing spec:** `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md`
**Changed:** new `src/skills/architect-pairing-engine/SKILL.md`; `src/skills/agent-architect/SKILL.md` (L14); new symlink `active/skills/architect-pairing-engine`; `CLAUDE.md` (L74)
**Risk Level:** 🟢 Low

## Diff boundary

`git status --porcelain -- ':!.ai-factory'` returns exactly the four expected entries and nothing else:

```
M  CLAUDE.md
A  active/skills/architect-pairing-engine
M  src/skills/agent-architect/SKILL.md
A  src/skills/architect-pairing-engine/SKILL.md
```

`src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, `docs/reserved-words.md` and the `docs/sakshi-harness/` guides are untouched, as the plan's guards required.

## Mechanical verification (all run against the live tree)

- **`loads:` edge** — `src/skills/agent-architect/SKILL.md:14` is now `loads: architect-editor-engine architect-pairing-engine`, space-separated per CLAUDE.md § "Dependencies and the skill graph".
- **The rest of `agent-architect` is byte-identical.** Confirmed structurally, not by eye: deleting line 14 from both `HEAD:src/skills/agent-architect/SKILL.md` and the working copy leaves files that `diff` reports as identical. The guarded regions — the unpaired default `:19-28`/`:25-26`, the spawn paragraph `:30-40`, the `::` mechanics `:60-140`, and the two-format statement `:128-131` — are therefore provably unchanged.
- **Symlink** — `active/skills/architect-pairing-engine -> ../../src/skills/architect-pairing-engine`, git mode `120000`, resolves to a directory containing `SKILL.md`; the relative form matches every existing entry.
- **CLAUDE.md** — one line changed (one `+`, one `-`), `architect-pairing-engine` inserted after `agent-architect` in the active-set enumeration. The pre-existing `architect-editor-engine` gaps at `:74` and `:189` were correctly left alone, as instructed.
- **Frontmatter parses and the skill loads.** Stronger than a lint: `architect-pairing-engine` appears in this review session's own available-skills listing, with a description folding byte-for-byte to the file's `description:` block. That proves the YAML is valid and `disable-model-invocation: false` genuinely makes the skill model-invocable — the mechanism the plan identified as the sole load trigger.
- **Reverse graph** — the command documented at `:28` returns `agent-architect` (plus the file itself), so the marker is accurate.
- `name` matches the directory; body is 59 lines, far under the 500-line cap; no `argument-hint` (correct — the skill is not user-invocable, mirroring the precedent).

## Guards held

- **No third format, no new marker.** The body uses only `REPORT-ONLY` (`:32`) and `APPLY-EDIT` (`:33`), both byte-exact. The deciding half changes the work-order's *recipient*, never its format — consistent with generic `:128-131`.
- **No deployment-specific fact** — no agent name, session id, user, or project anywhere in the file; the role assignment is left as a runtime fact the user states.
- **Spawn departure is stated, not extended** (`:41-46`). This closes plan-review 1's issue 2: the generic rule's second spawn alternative (the first authored apply work-order) is explicitly deleted for the deciding half, so a session that runs without a `::` relay no longer requires spawning an editor with a message that half is forbidden to send it. The half correctly stops there and does not invent further spawn policy; a deciding architect with no relay simply works alone, which is generic `:32-33` unchanged.
- **The applying half's silence is preserved** (`:48-59`) — it names origination, no-onward-routing, and the supersession of `:25-26`, and says nothing about `REPORT-ONLY` or whether it spawns an editor, exactly as the plan directed.

## Findings

### 1. Low — the load trigger assigns the role to "the session" rather than to the architect, and doubles the qualifier

`src/skills/architect-pairing-engine/SKILL.md:9-11` (the `description:`) and `:25-26` (the body) both read:

> "Load only when the user has assigned **the session** one of these two roles **for the session**; never in an unpaired session."

The spec's pinned sentence is: *"An architect loads this skill only when the user has assigned **it** one of these two roles for the session."* The pronoun for the architect was replaced by "the session", which produces two problems in one clause: the redundant "assigned the session … for the session", and — the substantive part — the loss of the spec's explicit framing that *"The role is per-agent, per-session data … assigned per agent and per session by the user."* The per-agent half is what the sentence now drops.

Why it matters more here than ordinary prose: the plan established that because `agent-architect` takes a frontmatter-only edit, this description is the *sole* trigger that will ever fire the load — it is the always-loaded text an architect reads to decide whether the roles apply to it. The whole point of the skill is telling two agents which half each holds; a trigger phrased as a property of "the session" is ambiguous about *which agent* holds the role at precisely the moment that distinction is being established. Two paired architects are two agents, and the user assigns each its own half.

Failure scenario: the user assigns roles by naming them in one place ("you decide, the other applies"). An architect reading a trigger keyed to "the session" having a role can conclude the condition is met without resolving which half is *its own* — the exact confusion the skill exists to delete.

Fix — one word, in both places: "…when the user has assigned **it** one of these two roles for the session" (`:9-11`), and "…when the user has assigned **you** one of the two roles below" (`:25-26`). No other text needs to move.

## Positive notes

- The byte-identity of `agent-architect` outside line 14 is not merely plausible here — it is verifiable, which is the right property for a change whose main risk was collateral edits to a heavily-guarded file.
- The spawn-trigger departure is written as a consequence of the rule the spec pins, with the generic rule quoted before it is narrowed. A future reader sees both the old rule and why this half departs, which is what makes the override safe to leave in the add-on rather than in the generic file.
- The applying half names the supersession of `:25-26` explicitly (`:56-59`) instead of silently contradicting it — the one place where the add-on genuinely inverts the generic discipline is the one place it says so out loud.
- Carrying both `architect-editor-engine` enumeration gaps forward untouched keeps the diff to exactly the spec's four edges.

## Deferred observations

- Affects: Phase 26 / `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` — the applying half's "does not route it onward to an editor of its own" (`:52-54`) meets the generic `::` rule (`src/skills/agent-architect/SKILL.md:93-96`: *"The marker is unconditional: there is no check of whether the user 'meant' it to relay"*) without either file saying which wins. If the user relays the deciding architect's work-order to the applying architect with a `::` marker — a plausible habit, since the marker is how a user normally hands work to an architect's pair — the generic rule says forward the payload as `REPORT-ONLY`, while the pairing half says never route the work onward. Nothing corrupts (a `REPORT-ONLY` relay writes no files, so the edit is still applied exactly once, by the applying architect's own hands); the cost is one wasted editor round and a contradiction the architect must resolve by guess. The spec deliberately left the applying half's relay behaviour unstated and the plan directed that silence, so this is correctly out of scope for 26.4 — recorded for whoever specifies the applying half's relay handling. [dismissed]
