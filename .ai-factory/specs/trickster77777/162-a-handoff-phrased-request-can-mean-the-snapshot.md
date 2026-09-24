# 162 — a request phrased as a handoff routes correctly on both sides, or on neither

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" reads, in the memory-snapshot paragraph:

> The memory snapshot continuing this same architect has two occasions:
> before a compact, and whenever the user asks for one mid-session — no
> other handoff has any reason to mention the buffer or the handle.

`src/commands/command-handoff.md` opens with:

```
A handoff always lives in `<root>/.ai-factory/handoffs/`. `$ARGUMENTS`, when present, names the project **root** only — not a file to read, not the destination itself. `<root>` is that named project, or the current project when no argument is given. The resolved `<root>/.ai-factory/handoffs/` is the destination-directory hook `note` receives in Step 2 — never `notes/`, never the bare argument path.

---

## Step 1 — Shape the mining lens
```

Neither file states the boundary between the two genres `docs/paired-loop.md` now names, so a request meaning "continue this same architect past a break" can reach either artifact with nothing redirecting it. Field evidence shows this happens in practice, not just in theory: a request phrased as "write a detailed handoff of what we did and what came of it" — the phrasing named in phase note `152-`, sourced from `.ai-factory/handoffs/29-the-architects-snapshot-is-a-history-not-a-telegram.md` — was routed to a `command-handoff` run instead of the on-request snapshot it actually meant. `docs/paired-loop.md` § "How the memory begins, and how it survives" now carries the governing claim both changes below lean on, in its closing paragraph beginning "Two genres share the occasion and nothing else...": a memory snapshot's reader is the same head after a break and its subject is the stretch's reasoning; a project handoff's reader is another agent, its subject the project's state, its lifetime ending when read.

## What must be true after

`src/skills/agent-architect/SKILL.md`'s sentence above gains one appended sentence:

> The memory snapshot continuing this same architect has two occasions:
> before a compact, and whenever the user asks for one mid-session — no
> other handoff has any reason to mention the buffer or the handle. A
> request that means continuing this same head past a break reaches this
> capability even when it is phrased as asking for a handoff; a request
> meant for whoever comes next, on the project rather than on this
> conversation, is the different genre `command-handoff` writes, and does
> not reach here (`docs/paired-loop.md` § "How the memory begins, and how
> it survives" draws the line by reader, subject, and lifetime).

`src/commands/command-handoff.md` gains one new paragraph, inserted between its opening paragraph and the `---` that follows it:

```
A handoff always lives in `<root>/.ai-factory/handoffs/`. `$ARGUMENTS`, when present, names the project **root** only — not a file to read, not the destination itself. `<root>` is that named project, or the current project when no argument is given. The resolved `<root>/.ai-factory/handoffs/` is the destination-directory hook `note` receives in Step 2 — never `notes/`, never the bare argument path.

A request meant to continue the same architect's own memory across a break is a different genre — the architect's own on-request snapshot, not this command — and never reaches here, however it is phrased; `docs/paired-loop.md` § "How the memory begins, and how it survives" draws that line by reader, subject, and lifetime.

---

## Step 1 — Shape the mining lens
```

No other sentence changes in either file. Neither addition restates reader, subject, or lifetime — both point at `docs/paired-loop.md` for the distinction itself. The `command-handoff.md` paragraph does not name `agent-architect` or any other skill by file path, since the pointer is to the documented genre, not to a specific carrier.

## What breaks on contact

**Rule:** a routing boundary exists only once both sides state it, so this task is verified whole or not at all — confirming one file's change without the other is not a check of what this task delivers, only of half of it. Neither insertion replaces any existing wording (both add a new sentence or a new paragraph beside untouched text), so nothing here goes stale the way a replaced clause would; the concern is whether any *other* file asserts a competing boundary, not whether these two go out of date.

**Sweep (re-runnable):**
```
grep -rln "other handoff has any reason to mention the buffer or the handle" src/ docs/ .ai-factory/
grep -rln "A handoff always lives in" src/ docs/ .ai-factory/
```
(the first anchor drops the leading "no" on purpose — in the actual file the sentence wraps a line between "no" and "other", so "no other handoff has any reason" as a single-line pattern silently matches nothing at all; this is the re-runnable form that actually works.)

**Invariant:** after the change, both targets still carry their anchor phrases untouched — `agent-architect/SKILL.md`'s "no other handoff has any reason to mention the buffer or the handle" stands as before, now followed by the new appended sentence; `command-handoff.md`'s "A handoff always lives in..." opening stands as before, now followed by the new inserted paragraph. This task's own spec quotes both anchors permanently, under `## What is true now`, as history. Corrected from an earlier version of this section, which claimed the same searches also return `.ai-factory/handoffs/29-` and this phase's own note `152-` — checked directly, neither file contains either phrase; `152-` and `29-` are cited elsewhere in this spec's `## What is true now` for a different phrase entirely (the field-evidence quote, "write a detailed handoff of what we did and what came of it"), unrelated to this sweep. No other live skill, command, or document quotes either passage or asserts a competing boundary. No sibling task of this phase addresses either span this task now owns. The sweep locates candidates; reading decides.

The `command-handoff.md` insertion point is checked structurally, not by search: it sits between two existing, unchanged blocks (the opening paragraph, the `---` that follows) and touches no other line. Downstream of it — Step 1's lens-shaping prose, Step 2's `note` hooks, Step 3's paste-back pointer, and "Holding a handoff" — none states or implies that every invocation of this command is handled regardless of what request triggered it; none names or excludes the sibling genre either, and none would still process a same-architect continuation request if one reached this command despite the new paragraph. The boundary is stated once, at the top, and nothing downstream re-opens or contradicts it.
