# command-pin-gaps: walk the task's transformation, report where it fails to join

## Current state (grounded, read fresh)

`src/commands/command-pin-gaps.md` is 26 lines. `:19` states its premise — "Any question that would need an answer *during implementation* is space for the agent to fantasize. Close all of it now." `:21` and `:23` carry its two finding classes, value holes and meaning holes. `:25` gives scan mode's line format, `[file:line|spec-location] → value|meaning → what's missing → fix`; `:26` gives the default mode's report and is class-agnostic. `:10` reads `allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill`; `:11` reads `loads: roadmap-engine`. `grep -rl 'command-pin-gaps' src/` returns nothing — no callers, and the change is local to this one file.

The premise at `:19` is right and stays. What is missing is any method for answering it: the command interrogates the artifact's own text and improvises everything beyond it.

Nothing in the family checks how a task lands on the code that already exists. `src/skills/roadmap-decompose/SKILL.md` carries no instruction to read code at all. `src/skills/roadmap-decompose-skeleton/SKILL.md` Step 1 does read code, through three lenses — a skeleton where a shared or non-obvious surface needs to become testable, a tests-first task written against that skeleton and filtered by `test-philosophy`'s silent-failure discriminator, and a contract-task of invariants and scenarios for a heavy task touching two of three concurrency hazards. All three judge whether behavior can be verified. None asks where new code integrates with old.

Everything the command needs in order to know what a joined task looks like is already resident in every session of every project. `src/global/CLAUDE.md` § "Grounding claims" states that change moves one way — docs → roadmap → code — that the docs state desired behavior, the roadmap names what is not built yet, and the code is what is built; and it states how a reader reaches ground truth: down a chain of explicit references to the leaf, "Depth along named edges, never breadth across unrelated files". Nothing has to be fetched from anywhere for the command to hold this.

`command-pin-gaps` is a global command, symlinked into `~/.claude/commands` and invoked in any project. A path into a sibling repository resolves inside this coordination root and nowhere else, so no such path may appear in it.

## The change

One file, rewritten in place, keeping its question, its tool grant and `loads:` line, and its container.

1. **The walk.** The command walks the transformation the task claims: this governing spec, through this task, into that code. It reads the task and its spec, the documents the task and its phase name, and the code the task will land in — following named references to the leaf, never sweeping across unrelated branches. It reports every point where the three do not join. This is a restatement of the mechanism by which a governing spec becomes code, written into the command so it knows what it is looking for; it is not a reproduction of any other agent's prompt, and it names none. The unit of the walk is one behavior the task claims: each such behavior either ends at a `file:line` landing in the code or becomes a finding, and the walk descends into the code the named files themselves reference only as far as that behavior's landing requires, never past the question. Where the phase names no document — no `Governing spec:` on its header and no document linked from its preamble, the branch `src/skills/task-rescue/SKILL.md:61-63` already takes — the docs end is reported once per phase as a finding owned by `aif-docs`, and the walk proceeds from the task alone. The phase is located the way `src/skills/task-rescue/SKILL.md:58-63` already does it — the phase section the task's contract line sits under — and the walk reads both pointers on that header, `Governing spec:` and `Phase note:`: the first states how the phase must become, the second what diverges now, and a no-landing finding is judged against both. The no-document branch keys on `Governing spec:` and on links into `docs/` alone; a `Phase note:` is not a document and never satisfies it.

2. **Two ends, one hole.** A task states how the docs currently differ from the code and what it will change; a hole is wherever that statement fails to connect. **Toward the code:** desired behavior with no landing — no file named, no call site, an existing shape it must fit that nobody looked at, work already half-done, something that breaks on contact. This end is the one no other skill owns. **Toward the docs:** behavior the task assumes that no document states, because it surfaced during decomposition rather than during specification. The hole is then in the governing spec, not in the task, and the command points there — the same hole seen from the other end. The two ends are not classes. Every finding carries exactly one of the three classes: a missing file or call site is a value hole, an existing shape nobody looked at or work already half-done is a meaning hole, something that breaks on contact is a blast-radius hole, and behavior no document states is a meaning hole whose repair is routed rather than written. The end shows in the repair: closed in place, or `owner: <skill>` in the scan line's `fix` token.

3. **The classes.** Value holes and meaning holes keep their definitions and their in-place repairs; a meaning hole whose constraint no document states is routed to `aif-docs` instead of being written from the code, and `## Blocking decisions` stays reserved for genuine product decisions. Blast-radius joins them as a third class — what the repository already contains that this change breaks, closed by a `Grep`/`rg` sweep whose enumeration goes into the spec, never a sentence saying something may need updating. `:25`'s scan-mode middle token carries all three, and `:2-8`'s `description:` names all three and the walk: the description is always-loaded contract, not a summary, so a capability missing from it is one the invoking agent may never learn exists. The block stays inside the 1024-character cap `CLAUDE.md` sets for a `description:` — measured, not estimated; it holds 422 characters today. A sweep too large to enumerate is itself a finding: the command reports the search and its count with owner `roadmap-decompose`, and never files it under `## Blocking decisions`.

4. **It names owners and wields none.** A task that cannot be planned coherently belongs to `roadmap-decompose` or `roadmap-decompose-skeleton`; behavior no document describes belongs to `aif-docs`; a surface that fails silently, by `test-philosophy`'s discriminator, owes a test. The command names which one and performs none of them: it does not decompose, does not write documentation, does not author tests, and loads none of these four — naming an owner needs no load. A hole it can close in place it closes, exactly as today; a hole whose repair belongs elsewhere is reported, in both modes. `:26`'s report gains a third count, `N closed from source · M blocking · K owned elsewhere`, so a routed hole is counted rather than lost; in scan mode the `fix` token of a routed hole reads `owner: <skill>`.

5. **Tool grant and `loads:` unchanged, and no reach outside the project.** The `description:` block is rewritten per item 3; nothing else in the frontmatter moves. No `Write`, no `AskUserQuestion`, no `Agent`; `loads:` stays `roadmap-engine`; it stays a command in `src/commands/`. No path under `orchestrator/` and no reference to another repository's files appears anywhere in it.

## Files & types

- edit: `src/commands/command-pin-gaps.md` — rewritten in place, same path, same `allowed-tools:` and `loads:` lines, `description:` block rewritten

## Guards

- The question is the identity and does not change: where would the implementing agent have to invent? The walk is a method for answering it, not a replacement for it, and no pass/fail verdict displaces the finding list.
- The command gains no authority. Any wording that has it split a task, write a document or author a test is wrong.
- **No path into a sibling repository, and no dependence on one existing.** The command runs in projects that have no `orchestrator/` beside them. If a rule seems to need one of that repository's files, restate the rule or drop it.
- No frontmatter growth. If a capability seems to require `Write`, `Agent` or a new `loads:` entry, it has been written as an action instead of a finding — rewrite the finding, do not grow the grant.
- **A task spec may repeat a paragraph from a document instead of linking to it, and that is not a finding.** An agent does not reliably walk to the leaf; it guesses a file's content from its name. Such a copy goes stale, and that is proper to this tier: the roadmap is the perishable seam between the documentation and the code, pruned as it closes, unlike the two surfaces it sits between.
- Judging a task too large, and judging a behavior undocumented, are comparative: from inside one task every task looks normal-sized. They are made where the whole roadmap is readable, which is where the command runs.
- The repair verb is `Grep` or `rg`, never bare `grep` — fixed by `:10`'s grants.
- The third class's paragraph has the shape of `:21` and `:23`: a bold name, the definition of what it looks for, then `Repair:`. The file grows no second register.
- Do not touch Phase 28, task 28.1, or spec 102.

## Verification

Counts against a whitespace-normalized read of the named file — never a line-oriented `grep` — with `**` normalized out of both sides before any quoted span is compared.

- the `allowed-tools:` line and the `loads:` line are byte-identical to the same two lines in `git show HEAD:src/commands/command-pin-gaps.md`, whatever line numbers they now sit on
- the words `Write`, `AskUserQuestion` and `Agent` do not appear in that file's `allowed-tools` line → each 0
- **the string `orchestrator/` does not appear in the file → 0**, and no path in it names a file outside this repository
- the file states the direction change moves in, docs → roadmap → code → ≥ 1
- the file states both ends of the hole: a landing missing in the code, and behavior the task assumes that no document states → each ≥ 1
- all three class names appear inside the frontmatter's `description:` block (blast-radius and blast radius counted together) → each ≥ 1, and the block states that the command walks the task's transformation → ≥ 1; the block measures ≤ 1024 characters (`wc -m`, UTF-8 locale)
- the scan-mode line format carries three alternatives in its middle token → the two-alternative form `value|meaning →` → 0
- the file names `roadmap-decompose`, `roadmap-decompose-skeleton`, `aif-docs` and `test-philosophy` → each ≥ 1, contains no instruction to invoke any of them, and lists none of them in `loads:`
- the file still lives at `src/commands/command-pin-gaps.md`; no new file under `src/skills/` and no new symlink under `active/`
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/commands/command-pin-gaps.md` and nothing else
- the token `Repair:` appears exactly three times in the body → 3
- the default-mode report line carries the three counts, and the phrase `owned elsewhere` appears → ≥ 1
- the scan-mode description states the `owner: <skill>` form of the `fix` token → ≥ 1
- the file states the no-document branch: `Governing spec:` → ≥ 1, and `aif-docs` is named as its owner in the same sentence; the file names `Phase note:` as the second pointer the walk reads → ≥ 1, byte-exact
- the file states what a sweep too large to enumerate becomes: a finding owned by `roadmap-decompose` → ≥ 1
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section
