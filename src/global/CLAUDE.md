# Global Instructions

## Grounding claims

Ground truth (code, command output, the actual file) overrides any **description** of it — a description doc, CLAUDE.md, a handoff, memory. Descriptions drift; code wins. A **governing spec** (a ТЗ) is the other doc mode: it states intended behavior ahead of code, and code is built and verified against it. When a governing spec and its code disagree, that is a defect to reconcile — not a stale doc.

Before acting on an artifact, read **down its chain of explicit references to the leaf**: every file it names, then every file those name. A contract line names its task spec; a spec names its code. Depth along named edges, never breadth across unrelated files. Reading a contract line while its named task spec sits unread is the forbidden failure. Direct references are non-negotiable; prune only branches irrelevant to the question. A reference you don't open, you attribute ("per the spec…") — never invent.

The opening task statement is the first artifact: raise its **map** — your branches, one layer deep. Walk a branch **to the leaf at the moment you act on it**, not all branches up front. The leaf is code, on both sides of the spec — docs are the crown, code the root system. A chain that stops at a doc has not reached ground truth — when the question is what the system *does now*. A governing spec answers what the system *must do*; for unbuilt code it legitimately ends at the doc — the ground truth of intent. Never the whole tree — deep along the branch in your hands.

Held context decays: a file read hours ago is a description again. Re-read the leaf fresh before acting — even when you "already know it". The larger the context, the stronger the illusion that you don't.

`.ai-factory/ROADMAP.md` is the entry map of **time**: aim at the `[x]`/`[ ]` seam — `[x]` lines are history, only the files verify the present. `.ai-factory/ARCHITECTURE.md` is the entry map of **space**: module boundaries, the chosen pattern, `## Features`. The two maps orient a cold session. Named roadmaps under `.ai-factory/roadmaps/` branch the time map — per-developer buffers with an `> Owner:` line; multiuser entry starts by enumerating that directory.

## Documentation style

- **Describe behavior, not code.** Docs explain what a feature does and how it works — not list methods, fields, event types, or endpoint tables. That's just copying the code.
- **Comments never cite the plan layer.** No code or test comment carries a phase/note number, a `ROADMAP`/`Plan` reference, or an `.ai-factory/` path.
- **No file/directory trees.** The only place a directory tree belongs is in ARCHITECTURE.md as a module template. Everywhere else — never.
- **Match the language of existing docs.** Before writing or editing a doc file, check what language neighboring docs use and match it — even if project instructions say otherwise.
- **No README documentation table.** The documentation index belongs in the project's CLAUDE.md, not in README.md.
- **Present tense, not change history.** A doc states behavior in the present tense — a governing spec states *intended* behavior whether the code exists yet or not, a description states *existing* behavior. Neither narrates change history: no "X was replaced", "Y was added" — that belongs in commit messages.
- **Docs form a walkable tree.** Inline links are the edges grounding walks: every doc links to the deeper docs and code it depends on, at the moment they are load-bearing. A fact's second home is always a link to its first, never a copy.

## Project CLAUDE.md authoring

- **One home per fact.** Anything stated in two places will drift. AGENTS.md is a one-line pointer to CLAUDE.md; the documentation index lives in CLAUDE.md (never in README); a module map lives in ARCHITECTURE.md or the code itself — CLAUDE.md points, it does not copy.
- **Monorepo roots route by ownership.** Tasks go to the sub-repo they belong to — into its `.ai-factory/` (contract line in `ROADMAP.md`, task spec in `specs/`). Resolution: an explicit sub-repo prefix at the start of the argument wins (strip it, process the rest); otherwise detect from the task description; if ambiguous — ask. The root CLAUDE.md holds only the project-specific prefix/keyword tables — this protocol is not restated there.

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

- **Chat plans; the orchestrator implements.** In a chat session, only plan and write planning artifacts (roadmaps, task specs, docs) — don't touch application code unless the user directly and unambiguously asks for a specific change here. The default is plan-only; implementation is the orchestrator's job, run separately.
- **Do not drift into coding.** Never start editing code on your own initiative — not mid-session, not after a plan is "done". A vague or implied signal is not a request; if you think code needs changing, say so and ask.
- **Planning chain.** `/roadmap-outline` → `/roadmap-decompose` (plus `/roadmap-decompose-skeleton` on heavy tasks). Every task is two-tier: a contract line in `ROADMAP.md` plus a task spec in `.ai-factory/specs/` (older notes still resolve from `.ai-factory/notes/` via the contract line's `Spec:` tag).
- **Deferred questions mean unfinished planning.** If a session ends with questions "left for the planning stage", the tasks are not ready — keep decomposing and close every question before the roadmap is handed to the orchestrator.
- **Interface names declare their kind.** When a planning artifact — a contract line, a spec, a skeleton, a work-order, a plan — names a new abstraction, the name carries the language's own interface marker (`I` prefix, `Protocol` suffix, or whatever form the language's convention uses), so a reader tells a contract from a class by the name alone. Where the project's rules pin a specific form, that form is mandatory.
