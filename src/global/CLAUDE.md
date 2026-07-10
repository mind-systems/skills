# Global Instructions

## User

Read `~/.claude/memory/user-personality.md` at the start of every conversation.

## Grounding claims

Ground truth (code, command output, the actual file) overrides any description of it (docs, CLAUDE.md, handoffs, memory) — descriptions drift. Before reasoning or acting on the artifact in front of you, read **down its chain of explicit references to the leaf** — every file it names (a task line names its spec note; a spec names its code), then every file those name: depth along named edges, never breadth across unrelated files. Reading a task's roadmap line while its named spec note sits unread is the failure this forbids — the direct references an artifact names are non-negotiable; only deeper branches genuinely irrelevant to the question may be pruned, and any reference you deliberately don't open you attribute ("per the spec…") rather than invent.

The session's opening task statement is itself the first artifact: raise its **map** first — which branches of the project are yours, one layer deep. Walk a branch **to the leaf at the moment you act on it**, not all branches up front — and the leaf is code, on both sides of the spec: docs are the crown, code is the root system, and a chain that stops at a doc has not reached ground truth. Never the whole tree — deep along the branch in your hands.

Held context decays: a file read hours ago is a description again, not the file. Before acting on a branch, re-read its leaf fresh — even when you "already know it"; the larger the context, the stronger the illusion that you don't need to.

When the project has `.ai-factory/ROADMAP.md`, it is the entry map of **time**: the seam between `[x]` and `[ ]` is where the project lives now — aim there. A `[x]` line is always history, never current state: it describes the moment of its own planning, a later line on the same surface supersedes an earlier one, and the present is verified only against the files. Its counterpart `.ai-factory/ARCHITECTURE.md` is the entry map of **space** — module boundaries, the chosen pattern, and the compacted history in `## Features`; the two maps together orient a cold session before any skill is invoked.

## Documentation style

- **Describe behavior, not code.** Docs explain what a feature does and how it works — not list methods, fields, event types, or endpoint tables. That's just copying the code.
- **No file/directory trees.** The only place a directory tree belongs is in ARCHITECTURE.md as a module template. Everywhere else — never.
- **Match the language of existing docs.** Before writing or editing a doc file, check what language neighboring docs use and match it — even if project instructions say otherwise.
- **No prev/next navigation links.** Never add `[← Previous](...)` / `[Next →](...)` header navigation to doc files — it's useless clutter.
- **No "See Also" sections.** Never add a "See Also" footer to doc files.
- **No README documentation table.** The documentation index belongs in the project's CLAUDE.md, not in README.md.
- **Describe current state only.** Never reference what was changed, removed, or added. No "X was replaced", "Y was added". History belongs in commit messages.
- **Docs form a walkable tree.** Inline links are the edges grounding walks: every doc links to the deeper docs and code it depends on, at the moment they are load-bearing. A fact's second home is always a link to its first, never a copy.

## Project CLAUDE.md authoring

- **One home per fact.** Anything stated in two places will drift. AGENTS.md is a one-line pointer to CLAUDE.md; the documentation index lives in CLAUDE.md (never in README); a module map lives in ARCHITECTURE.md or the code itself — CLAUDE.md points, it does not copy.
- **Monorepo roots route by ownership.** Tasks go to the sub-repo they belong to — into its `.ai-factory/` (contract line in `ROADMAP.md`, spec note in `specs/`). Resolution: an explicit sub-repo prefix at the start of the argument wins (strip it, process the rest); otherwise detect from the task description; if ambiguous — ask. The root CLAUDE.md holds only the project-specific prefix/keyword tables — this protocol is not restated there.

## Memory

- **Never write to memory.** Do not save anything to `~/.claude/memory/` or any memory files unless the user explicitly asks to remember something.
- **Allowed trigger phrases only.** Writing to memory is permitted only when the user uses one of these exact commands (in any language):
  - EN: "remember this", "save this", "save to memory", "add to memory", "memorize this"
  - RU: "запомни", "сохрани в память", "добавь в память", "запиши в память"
- **Explanations of workflow, process, or context are NOT a trigger.** If the user explains how something works or describes a process, do not interpret it as a request to save to memory.

## Git

- **NEVER commit without explicit permission.** If there are uncommitted changes, assume they are intentional or ask what to do. Do not auto-commit.

## Commit messages

- **Short noun phrase or imperative**, no trailing period.
- **Sentence case** — capitalize the first word and proper nouns only.
- **No type prefixes.** Never use `feat:`, `fix:`, `chore:`, `refactor:` or any other conventional-commit prefix.
- **No body** for single-concern commits. A body is acceptable when one commit covers multiple unrelated changes — use it to list them.

## Planning workflow

- **Chat plans; the orchestrator implements.** In a chat session, only plan and write planning artifacts (roadmaps, spec notes, docs) — don't touch application code unless the user directly and unambiguously asks for a specific change here. The default is plan-only; implementation is the orchestrator's job, run separately.
- **Do not drift into coding.** Never start editing code on your own initiative — not mid-session, not after a plan is "done". A vague or implied signal is not a request; if you think code needs changing, say so and ask.
- **Planning chain.** `/roadmap-outline` → `/roadmap-decompose` (plus `/roadmap-decompose-skeleton` on heavy tasks). Every task is two-tier: a contract line in `ROADMAP.md` plus a spec note in `.ai-factory/specs/` (older notes still resolve from `.ai-factory/notes/` via the contract line's `Spec:` tag).
- **Deferred questions mean unfinished planning.** If a session ends with questions "left for the planning stage", the tasks are not ready — keep decomposing and close every question before the roadmap is handed to the orchestrator.
