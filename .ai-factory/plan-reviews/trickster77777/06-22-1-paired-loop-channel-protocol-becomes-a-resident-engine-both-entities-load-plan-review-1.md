# Plan review — 22.1 paired-loop channel protocol becomes a resident engine

## Code Review Summary

**Artifacts reviewed:** plan (4 tasks) + its chain — contract line (`roadmaps/trickster77777.md` L46), task spec (`specs/trickster77777/84-paired-loop-channel-protocol.md`), and the two leaf files it edits (`src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`) plus the engine-shape model (`src/skills/test-philosophy/SKILL.md`, `roadmap-engine`, `roadmap-decompose`).
**Risk Level:** 🟡 Medium — one blocking omission (missing `Skill` in `allowed-tools`), otherwise the plan is faithful to the spec.

### Context Gates
- **Architecture** (`ARCHITECTURE.md`): WARN → PASS. The plan adds a leaf engine, one `loads:` edge, and a reverse-graph marker — consistent with "Composition: mechanism vs policy." The one novelty (an *agent* caller, so the reverse-graph grep line must include `src/agents/*.md`) is explicitly handled in Task 1 and is coherent with ARCHITECTURE L22, which already names the `src/agents/` category. No boundary violation.
- **Rules** (`.ai-factory/RULES.md`): WARN — file absent (optional). No convention source beyond CLAUDE.md; not blocking.
- **Roadmap linkage**: PASS. Plan title matches contract line 22.1 in `roadmaps/trickster77777.md`; the `Spec:` tag resolves to `specs/trickster77777/84-paired-loop-channel-protocol.md`; plan tasks map 1:1 onto the spec's "four artifacts, one atomic task." Design decisions the spec marks "do not re-litigate" are respected.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): WARN — absent; no project-specific review overrides to apply.

### Critical Issues

**1. Task 2 loads the engine "via the Skill tool" but never adds `Skill` to `agent-architect`'s `allowed-tools`.**
`src/skills/agent-architect/SKILL.md` L13 today reads:
`allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage` — **no `Skill`**.
Every skill in this repo that loads an engine at runtime lists `Skill` in its `allowed-tools` — this is universal, not incidental: `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-test-coverage`, `roadmap-outline`, `roadmap-prune`, `task-rescue`, `temporal-tree` all pair "Ensure `<engine>` is loaded once this chat (via the Skill tool …)" with `Skill` present in `allowed-tools`. The `loads:` frontmatter field is only the forward-graph *declaration* (per skills CLAUDE.md, "the declarations *are* the map"); it does not perform loading — the Skill tool does, at runtime. Task 2's frontmatter bullet stops at "add `loads: architect-editor-engine`" and the body bullet says "ensure the engine is loaded once this session via the Skill tool," but nothing adds `Skill` to the tool list.
Failure scenario: the architect reaches its load instruction, invokes the Skill tool, and it is not pre-approved (and may be unavailable) — the engine never becomes resident on the architect side, which is the exact "load at birth, not lazily" guarantee the whole task exists to deliver (spec L3). The task spec's own verification step (#4, grep for `loads:`) would pass while the runtime behavior silently fails.
Fix: Task 2's frontmatter bullet must also add `Skill` to `agent-architect`'s `allowed-tools`.

### Issues (should fix before implementing)

**2. The new enrich+parallel model contradicts surviving anti-contamination text that the plan neither retires nor reconciles.**
`agent-architect/SKILL.md` L58–61 currently mandates the relay add "**nothing** of your own on top: no findings, no inventory, no collision-hint, no checklist, no verdict, no method … so its agreement is real signal rather than manufactured echo." Task 2 changes the model to: the before-mark payload is "worked by **both** the architect and the editor in parallel," and "the architect enriches the before-mark payload with named context from its own chat before sending it on." That directly overwrites the "add nothing" rule — yet:
- L58–61 is **not** in the three-phrase retirement list (only "ending with `::`", "literal payload text", "apply it with arguments" are), and no verification grep catches it, so the contradictory sentence can survive the rewrite and leave the file internally incoherent; and
- the plan is silent on *how* "enrich with named context" (now allowed) stays distinct from "no findings / no verdict / no manufactured echo" (the property REPORT-ONLY still rests on — the engine format in Task 1 still says the receiver "reasons independently from the ground up"). Enriching with named *context* and injecting *conclusions* are different acts; the plan should say so explicitly so the implementer preserves the independent-reasoning guarantee instead of deleting it wholesale.
Fix: add L58–61 to the material Task 2 revises, and state the boundary — enrichment supplies context, never findings/verdict/method — so the anti-contamination property is retained under the new framing.

**3. The retirement grep for "ending with `::`" must also clear the scope-question carve-out at L100–107, and that paragraph needs the same mid-message-split rework.**
"ending with `::`" occurs twice — L56 **and L102** ("a reply ending with `::` is what reaches the editor"); the scope-question paragraph (L100–107) is also keyed on "the user's own reply **ends with** `::`" (L106). It sits inside the L54–107 span Task 2 says to "rewrite in place," so it is nominally in scope, but the plan never calls it out, and under the new mid-message-split model this carve-out's trailing-only phrasing is stale. If the implementer rewrites only the paragraphs Task 2 enumerates by name (L56, L76–87, L89–98) and misses L100–107, spec verification step #2 (`grep … "ending with \`::\`" → zero hits`) fails on L102. Fix: name the scope-question carve-out (L100–107) explicitly in Task 2 as part of the in-place rewrite.

### Positive Notes
- The engine's frontmatter is correctly pinned to the *engine baseline* (`user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, no `loads:`), matching `roadmap-engine` — the plan does not blindly copy `test-philosophy`'s `user-invocable: true`, and the spec justifies the choice (not a user-facing skill). The distinction between "follow the *shape* of `test-philosophy`" and "use the roadmap-engine frontmatter baseline" is handled cleanly.
- Editor side is sound: `src/agents/editor.md` already carries `Skill` in `tools` (L9) and the `editor` agent type exposes it, so Task 3's "load via the Skill tool as the first spawn action" is executable with no frontmatter change — the plan correctly notes agents carry no `loads:` field and uses a body instruction instead.
- The reverse-graph marker's grep line is correctly extended to `src/agents/*.md`, and the plan flags this as the family's one engine with an agent caller rather than silently diverging from the repo's documented reverse-graph command.
- Protocol-token discipline is right: `REPORT-ONLY` / `APPLY-EDIT` are treated as byte-exact tokens on the `PLAN_REVIEW_PASS` axis, and the engine is correctly kept free of all `::` grammar (Task 1 body + Guards), matching using-the-language.md § "Protocol tokens are a different axis."
- Symlink task (Task 4) matches the confirmed live pattern (`active/skills/<name> -> ../../src/skills/<name>`) with a concrete verify command.

## Deferred observations
- Affects: reserved-words.md `## Paired loop` maintenance (a separate planning edit named in spec L38, outside 22.1's file boundary) — the spec states the `relay`/`channel-message`/`work-order` registry entries "were removed … as a separate planning edit"; the current registry `## Paired loop` section indeed lists only `architect` and `editor`, so that edit appears already applied. Nothing for 22.1 to do; noted only so a downstream prune/verify pass does not re-open it as a gap.

Once issue **1** is resolved (and **2**/**3** tightened), the plan is implementation-ready.
