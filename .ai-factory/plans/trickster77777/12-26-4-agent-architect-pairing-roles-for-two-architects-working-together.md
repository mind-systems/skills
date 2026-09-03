# Plan: agent-architect: pairing roles for two architects working together

## Context
Two architects running as a pair — one deciding, one applying — have no rule telling either its half, so the deciding one keeps addressing work-orders to its own editor and the applying one has nothing forbidding edits of its own. This task lands one new add-on engine, `architect-pairing-engine`, holding both halves, loaded only when the user assigns a role, plus the three wiring edges any new skill in this repo needs.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The new skill

- [x] **Frontmatter and load-trigger of `architect-pairing-engine`**
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Create the skill directory and file. Frontmatter mirrors its precedent `src/skills/architect-editor-engine/SKILL.md:1-13` field-for-field: `name: architect-pairing-engine` (must equal the directory name), `description: >-`, `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`. No `argument-hint` (the precedent has none, and it is only meaningful on a user-invocable skill).
  The `description:` carries the load-trigger, and this is load-bearing: per the spec's "Files & types", `agent-architect/SKILL.md` gets a frontmatter edit **only** — no body sentence there will ever tell an architect when to load this skill. The always-loaded skill description is therefore the sole trigger, so it must state (a) what the skill holds — the two pairing role halves for two architects working as a pair with no direct channel between them, and (b) that an architect loads it only when the user has assigned it one of the two roles for the session, never in an unpaired session. `disable-model-invocation: false` is what makes that self-load possible; do not set it to `true`.
  Body opens with an `#` title and a short preamble naming the arrangement: two architects, one deciding and one applying, every message between them carried by the user because they share no direct channel. The preamble also states the interpretive rule the rest of the file depends on — this skill states only the **departures** from `agent-architect`'s generic discipline; anything it does not name stays exactly as the generic skill has it.

- [x] **The reverse-graph marker** (depends on Frontmatter and load-trigger of `architect-pairing-engine`)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Per CLAUDE.md § "Dependencies and the skill graph", every engine named in a `loads:` field carries a reverse-graph marker in its body. Follow the precedent's one-sentence form at `src/skills/architect-editor-engine/SKILL.md:17`: state that the skill is loaded on the user's role assignment (not at birth — that is the editor engine's rule, not this one) and give the reverse-graph command `` grep -l "architect-pairing-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``.

- [x] **The two role halves** (depends on Frontmatter and load-trigger of `architect-pairing-engine`)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Two `##` sections, one per half, each naming what changes about work-order **addressing** and **origination** for that half.
  *The deciding half* — its editor becomes research-only: every `REPORT-ONLY` relay still goes to it exactly as `src/skills/agent-architect/SKILL.md:71-91` has it, and no `APPLY-EDIT` work-order does. The architect still authors the work-order as it does today (`:120-126`) — same `APPLY-EDIT` format, same pinned values, guardrails, self-verify commands and "do not commit" — but addresses it to the paired architect and delivers it through the user, who carries or confirms the relay. The applying architect is the one that acts on shared artifacts.
  The deciding half must also resolve the spawn trigger, or the file contradicts itself on the most ordinary session shape. Generic `:33-36` makes the first channel-message the spawn and offers two alternatives for it — "the first `::` relay or, where none has arrived, the first authored apply work-order". This half deletes the second alternative: in a session that runs without a single `::` relay, the architect would have to spawn its editor with the very message it is forbidden to send there. Add one sentence naming the departure — for the deciding half the spawn trigger is the first `::` relay alone, since the apply work-order no longer travels to the editor. This is a consequence of the rule the spec already pins ("no `APPLY-EDIT` work-order does"), not new policy: state it, do not extend it.
  *The applying half* — it originates no edit: every change it makes to a shared artifact traces to an arriving work-order, never to its own judgment. It applies exactly what that work-order pins, as an editor would, and does not route it onward to its own editor — its hands are its own, not delegated a second time. State plainly that for this half the generic default at `src/skills/agent-architect/SKILL.md:25-26` ("You never touch the shared artifacts … that hand is always the editor's") is superseded, since the override lives here and that line is not edited.
  Write only what the spec pins. In particular: say nothing about whether the applying half still relays `REPORT-ONLY` to an editor, and nothing about whether it spawns one at all — the spec pins neither, its generic spawn behaviour stays coherent because it can still receive `::` relays, and the preamble's interpretive rule already resolves the silence. Do not invent a third channel-message format, a new marker, or any `::` mechanic; the two formats stay byte-identical. No deployment-specific fact — no agent name, session, user, or project — enters the file; the role assignment is a runtime fact the user states each time.
  English, present tense, registry vocabulary per `docs/reserved-words.md`; body well under the 500-line cap (the precedent runs 28 lines — this file is a small one).

### Wiring

- [x] **The `loads:` edge on `agent-architect`** (depends on The two role halves)
  Files: `src/skills/agent-architect/SKILL.md`
  Line 14 today reads `loads: architect-editor-engine`. Extend it to name `architect-pairing-engine` as well (space-separated, per CLAUDE.md). This is the whole edit to this file — the frontmatter line and nothing else. The body stays byte-identical: the unpaired default at `:19-28` and `:25-26`, the spawn paragraph at `:30-40`, the `::` mechanics at `:60-140`, and the two-format statement at `:128-131` are all guarded. The spawn-trigger departure belongs in the new skill only; it is never written into this file.

- [x] **The `active/` symlink** (depends on The two role halves)
  Files: `active/skills/architect-pairing-engine`
  `ln -sfn ../../src/skills/architect-pairing-engine active/skills/architect-pairing-engine` — the relative form every existing entry uses (`active/skills/architect-editor-engine -> ../../src/skills/architect-editor-engine`). Verify with `ls -la active/skills/architect-pairing-engine`.

- [x] **The active-set paragraph in CLAUDE.md** (depends on The `active/` symlink)
  Files: `CLAUDE.md`
  Line 74, the `**The active set**` paragraph. Insert `` `architect-pairing-engine` `` into the "our skills —" enumeration immediately after `` `agent-architect` `` (the last item before the "— plus one upstream original we use as-is" clause), keeping the existing comma style and leaving the rest of the sentence untouched.
  Guard, from the spec: `architect-editor-engine` is symlinked under `active/skills/` but is missing from this same paragraph. That is a pre-existing defect this task explicitly does **not** fix — add the new skill only, and do not add `architect-editor-engine` while in the line. The same applies to the second enumeration of our skills at `CLAUDE.md:189` ("**Everything else in `src/skills/` is ours** … sync never touches it: …"), which omits `architect-editor-engine` today: leave it alone, and do not add the new skill there either. Both gaps are on record for whoever closes them in one pass; neither is in this diff.

- [x] **Verify the four edges and the diff boundary** (depends on The active-set paragraph in CLAUDE.md)
  Files: none
  Run the spec's own verification: `grep -n "architect-pairing-engine" src/skills/agent-architect/SKILL.md` (the `loads:` edge), `ls -la active/skills/architect-pairing-engine` (resolves to `../../src/skills/architect-pairing-engine`), `grep -n "architect-pairing-engine" CLAUDE.md` (named in the active-set paragraph).
  Then check the diff boundary with `git status --porcelain -- ':!.ai-factory'`, which excludes the orchestrator's own artifact tree (that path is where the plan, sidecar, plan-review and review live; it was clean under this pathspec before implementation began). Expect exactly these four entries and nothing else:
  `?? active/skills/architect-pairing-engine`, `?? src/skills/architect-pairing-engine/`, ` M CLAUDE.md`, ` M src/skills/agent-architect/SKILL.md`.
  Two of the four are new untracked paths, so `git diff --stat` reports only the two modified files — that is correct, not a missing-file symptom. Any **fifth** entry under this pathspec is out of scope and must be reverted; never revert or delete anything under `.ai-factory/`. In particular `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, `docs/reserved-words.md`, and the `docs/sakshi-harness/` guides are untouched by this task.
