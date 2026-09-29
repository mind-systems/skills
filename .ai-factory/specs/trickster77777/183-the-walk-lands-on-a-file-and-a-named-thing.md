# 65.4 — the gap pass stops suggesting a line or a count

## What is true now

`src/commands/command-pin-gaps.md` suggests a position or a tally in three sentences, each inside a paragraph that is a single line of the file.

The walk paragraph opens "The unit of the walk is one behavior the task claims." Its second sentence reads: "Each such behavior either ends at a `file:line` landing in the code or becomes a finding; the walk descends into code the named files themselves reference only as far as that behavior's landing requires, never past the question."

The **Meaning holes** paragraph gives its repair as "write the missing constraint as a spec clause derived from the observed behavior of the actual code, citing the code that grounds it where a concrete source exists; when the code can't settle it (genuine product decision), don't fabricate it".

The **Blast-radius holes** paragraph ends: "A sweep too large to enumerate is itself a finding: report the search and its count with owner `roadmap-decompose`, never filed under `## Blocking decisions`."

The command's own **Value holes** repair already names a source as "the file and the name of the thing inside it that holds the value — a symbol, a heading, a bold lead-in — never a line number, because the spec outlives the numbering it was written against". The walk sentence asks for the form that repair forbids, the Meaning-holes clause leaves the form of a citation open, and the Blast-radius clause asks for a figure, which `docs/counts-go-stale.md` calls a measurement that is false as soon as a neighbour lands.

## What must be true after

The second sentence of the walk paragraph reads: "Each such behavior either ends at a landing in the code — a file and the named thing inside it that holds the behavior — or becomes a finding; the walk descends into code the named files themselves reference only as far as that behavior's landing requires, never past the question."

In the **Meaning holes** repair, the clause "citing the code that grounds it where a concrete source exists" reads "naming the code that grounds it — the file and the named thing inside it that holds the constraint — where a concrete source exists".

In the **Blast-radius holes** paragraph, the clause "report the search and its count with owner `roadmap-decompose`" reads "report the search, with owner `roadmap-decompose`", so the sentence reads: "A sweep too large to enumerate is itself a finding: report the search, with owner `roadmap-decompose`, never filed under `## Blocking decisions`." The sentence's first half already says the sweep is too large; the repair drops the number.

## What breaks on contact

**Rule:** a text breaks on this change if it depends on the wording of any of the three sentences, or describes a landing or a grounding citation as a line, or a too-large sweep as a count.

**Sweep:**
```
grep -rn "file:line" src/ docs/ CLAUDE.md
grep -rn "command-pin-gaps" src/ docs/ CLAUDE.md
grep -rn "and its count" src/ docs/ CLAUDE.md
grep -rn "citing the code" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the walk sentence, the task's own target, and, in the same command, the Value-holes repair, which reads as described above, and the scan-line form `[file:line|spec-location]`, chat output a report prints and no artifact keeps; the directive of `roadmap-outline-deep` and the handoff item of `roadmap-prune`, each owned by its own task in this phase; and the docs that name the form as the defect. It reaches `docs/sakshi-harness/skill-cycle.md`, whose description of value holes says the source is named as a file and the thing in it that holds the value, not a line, which agrees with the command's Value-holes repair.

The second search reaches no skill and no command: the command is named only in docs — the always-loaded-field explanation that uses it as an example of action without invocation, the pipeline order and the pins chapter of `docs/sakshi-harness/skill-cycle.md`, the harness explainer's account of the implementer, `docs/reference-by-name.md`, and the index in `CLAUDE.md` — each speaking of what the pass does and none of its walk's landing, its grounding citation or its report of a large sweep. The third and fourth reach the two sentences above and nothing else. The default-mode report line, `N closed from source · M blocking · K owned elsewhere`, counts the run's own outcomes and is chat output no artifact keeps, and the scan line and the rule, sweep and finding form of the Blast-radius repair are the command's own shape. No reader depends on the wording of any of the three sentences.
