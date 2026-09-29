# 65.1 — the phase-note directive names a file and a heading, never a line

## What is true now

`src/skills/roadmap-outline-deep/SKILL.md` § "Step 1: Write the phase note" hands `note` its caller hooks, each a bullet led by a bold name. The third, **Verbosity directive**, reads: "short: a few sentences more than the preamble, grounded in the docs and code read at Step 0, a `file:line` where a claim needs one, never a transcript of the conversation." The text wraps in the file at a fixed column.

`note` takes the directive as free text through its verbosity hook and follows it, so a phase note written under it can ground a claim by a line number. `docs/reference-by-name.md`, at its bold lead-in "A `file:line` reference is a defect report against its target", calls that form the defect: the thing needed had no name.

## What must be true after

The **Verbosity directive** bullet reads: "short: a few sentences more than the preamble, grounded in the docs and code read at Step 0 — a claim that rests on a file names the file and the heading, symbol or quoted fragment that holds it, never a line number — and never a transcript of the conversation." The bullet's bold lead-in and dash stay as written, and the sentence wraps at the file's own column. The old clause applied "where a claim needs one", so the new one keeps that reach: it governs the claims that rest on a file, and leaves a statement about the user's rulings or about an absence to stand without a source.

## What breaks on contact

**Rule:** a text breaks on this change if it depends on the directive's wording, or if it asks a reader to ground a claim by a line and so pulls against the new sentence.

**Sweep:**
```
grep -rn "file:line" src/ docs/ CLAUDE.md
grep -rn "erbosity directive" src/ docs/
```

**Finding.** The first search reaches this directive, the task's own target. It also reaches the walk paragraph of `command-pin-gaps` and the handoff item of `roadmap-prune`, each a request for a line and each owned by its own task in this phase. It reaches the scan-line form of `command-pin-gaps`, `[file:line|spec-location]`, which is chat output no artifact carries and reads as intended. The global CLAUDE.md's reference rule, `docs/reference-by-name.md` and `docs/counts-go-stale.md` name the form as the defect and read as intended. `docs/sakshi-harness/skill-cycle.md` describes value holes as pinned by a source named as a file and the thing in it that holds the value, not a line, which agrees with what `command-pin-gaps` does. Phase notes, handoffs and buffers that carry a `file:line` are records of a past moment and stay true as records.

The second search reaches `note`'s hook definition and `docs/sakshi-harness/skill-graph.md`'s account of the hooks, which treat the directive as free text and read no wording of it; `command-handoff` and `task-rescue`, each holding its own directive for its own register, unrelated to this one; and the re-run rule in this same Step 1, which refers to "the verbosity directive above" by name and so takes the new sentence with no edit. The rest of `roadmap-outline-deep` holds no request for a position: its template asks for links to docs, its pointer and path forms name a file, and its budget is a decision. Under a caller's directive `note` keeps its rules on file paths and English, which ask for paths and never lines, and its folder-style step matches sibling notes' register only where the hooks are silent, which the new sentence is not. No caller depends on the directive's wording.
