# Review 1 — command-handoff: philosophy over the note engine

Scope: `git diff HEAD` — `src/skills/note/SKILL.md` and `src/commands/command-handoff.md`. This is an agent-instructions repo; "correctness" here means the prose an agent executes is internally consistent and cannot lead it into the explicitly-rejected behavior. Cross-checked against the spec note (`.ai-factory/notes/55-handoff-philosophy-over-note.md`) and the established caller convention in `src/skills/roadmap-engine/SKILL.md`.

## What is correct

- **`note` verbosity hook (Task 1).** Third hook added generically (no `command-handoff`/handoff mention), count updated "Two → Three". The Step-3 rebind is right: findings-focus / file-paths / English stay unconditional; concision is reframed as the *default* verbosity directive that a caller directive replaces. Standalone `/note` stays behavior-identical. `roadmap-engine` supplies only the destination hook (no verbosity) so it is unaffected — reverse-graph confirmed (only engine caller is `roadmap-engine`).
- **Frontmatter (Task 3).** `loads: note` added; `allowed-tools` is the exact union `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` (note's grants + command's own + `Skill`), per spec's "never a partial copy." `loads:` on a command matches repo convention (reverse-graph grep includes `src/commands/*.md`).
- **Hook-passing model matches the established convention.** `command-handoff` supplies destination/template/verbosity "in context" to `note`, the same way `roadmap-engine` does ("When invoking `note`, pass destination `.ai-factory/specs/` via `note`'s destination hook"). Same single-agent, prose-hook model — consistent.
- **No template/concision leak.** Template hook = the handoff skeleton passed verbatim, so `note`'s default Key-Findings/Details template and `**Date:**/**Source:**` header do not leak into handoffs; verbosity hook overrides default concision. Both spec "NOT to do" leaks avoided.
- **Map scoping (Task 2).** New proportionality-register paragraph plus in-skeleton guidance scope "must-read now" to the next action and state the multi-tree case explicitly; error-log and working-discipline sections untouched. Faithful to Edit 3.

## Findings

### 1. [Medium] Note mode: Step 2's "Populate every field" contradicts Step 3's "passed blank" — opens the door to the rejected pre-filled-template behavior

`src/commands/command-handoff.md`. Mode is determined at the top (line 13), but **Step 1 — Mine the session** and **Step 2 — Compose the handoff prompt** are written as unconditional imperatives. Step 2 ends (line 106): *"Populate every field from what you actually observed in the session — no placeholders, no invented content."* Only **Step 3 — Output** branches by mode, and its note-mode branch (line 119) says the template is *"passed **blank** … Do NOT pre-fill it: a filled-in skeleton would make `note`'s distillation a no-op."*

For a note-mode run these instructions are in direct conflict: Steps 1–2 tell the agent to mine the session and populate every field of the skeleton *now*; Step 3 tells it to hand `note` a blank skeleton and let `note` do the mining/distillation. An agent that executes the document top-to-bottom will compose the full body in Step 2, then in Step 3 either (a) pass that populated body as the template — which is precisely the pre-filled-template approach the spec explicitly rejects (note 55, "What NOT to do" #1; Key Finding #2), or (b) discard the just-composed body and re-delegate, doing the mining twice. Only an agent that reads the whole file first and lets Step 3 override Steps 1–2 lands on the intended behavior.

The spec's intent was that Steps 1–2 become the *shared lens/skeleton definition* referenced by both modes (note 55: "The skeleton and policy text live once in the command, shared by both modes; note mode must not restate them — it references them as the hooks' values"), with **execution** branching in Step 3: the agent performs the mining/compose itself in chat mode, whereas in note mode `note` performs it. The diff moved the note-mode *file mechanics* into Step 3 correctly but left Steps 1–2 framed as unconditional "do this now" imperatives, so the mode split is incomplete.

Failure scenario: user runs `/command-handoff note` after a large session. Agent follows Step 1 (mines) and Step 2 ("Populate every field … no placeholders"), producing a fully-written handoff body, then at Step 3 passes that populated skeleton to `note` as the Template hook. `note`'s distillation is now a no-op over an already-filled template — the exact inversion of the composition model the milestone exists to fix.

Suggested fix (wording, not mechanism): scope Steps 1–2 to their role in each mode — e.g. a one-line guard near Step 1/Step 2 stating that in **chat mode** the agent performs the mining and composition itself, while in **note mode** these steps define the lens and blank skeleton that `note` executes (the agent does not mine or populate the skeleton itself). That removes the contradiction without restating the skeleton in Step 3.

## Note (not a finding)

- The Step 3 note-mode bullet lists **Slug** alongside the three named hooks. `note` has no "slug" hook — it takes the slug via its `$1` argument / topic derivation. This is harmless in practice (the same agent runs `note`'s Step 2 and can set a semantic slug; `note`'s default derivation is from the session topic, never the literal word "handoff"), so it is a terminology imprecision, not a defect. Worth a word only if Finding 1 is being reworded anyway.
