# The character budget names how a character is counted

## Current state (grounded, read fresh)

Two budgets in this family are stated in characters. `src/skills/roadmap-engine/SKILL.md` § "Rules for writing a contract line" reads "Target ~600 characters (range 400–1000)". `src/skills/roadmap-outline-deep/SKILL.md`'s **Budget** bullet reads "rewrite the phase preamble down to ~200–500 characters". Neither names how the count is taken. These two are the only length budgets in the repository, but the `~600` figure is named again in two `description:` blocks — `roadmap-engine`'s own and `roadmap-decompose`'s, both reading "a ~600-char contract line" — where it carries the vocabulary and not the rule, and so takes no unit and no method.

The environment cannot be relied on. Whether `wc -m` counts characters or bytes depends on the locale of the shell it runs in, and that varies between shells on this machine: with `LANG`, `LC_ALL` and `LC_CTYPE` all unset it returns 22 on the eleven-character line `тест — тире`, and with `LC_CTYPE=UTF-8` exported it returns 12. `awk`'s `length` returns 21 on that line either way. A code-point count returns 11. `en_US.UTF-8` is installed here, so the locale-forced `wc -m` is available — but on that same line it returns 12 for eleven characters, counting the trailing newline the rule excludes, so it cannot be the pinned command without an off-by-one correction every caller has to remember.

The cost is not hypothetical. A contract line of 991 characters was reported as 995 by `awk`, and eight separate measurements this session reported bytes as characters before being caught and redone.

`roadmap-outline-deep` declares `loads: roadmap-engine`, so a rule stated in the engine already reaches it; what it lacks is a sentence at its own budget naming where that rule lives.

## The change

1. `src/skills/roadmap-engine/SKILL.md` gains one named paragraph immediately below the `**Rules for writing a contract line:**` bullet list, separated from the seventh bullet by one blank line: a paragraph under the list, never a bullet inside it, and never lazily continuing the bullet above. Its text, verbatim:

   **Counting characters:** every character budget in these skills — the contract-line budget above, and the phase-preamble budget in `roadmap-outline-deep` — counts Unicode code points with the trailing newline excluded. The command that yields them here is `python3 -c "import sys;print(len(sys.stdin.read().rstrip('\n')))"`.

   The paragraph names its scope by naming the two budgets it governs. It does not use the word `family`: that word is already spent in the same section for the task-number family, ten lines below, and the engine names no family of its own. The numbers — `~600`, `400–1000` — do not change, and no bullet of the list is edited.

2. `src/skills/roadmap-outline-deep/SKILL.md`'s **Budget** bullet names the method's home by its address — `roadmap-engine`'s "Roadmap File Format" § "Counting characters" — in the shape this same file already uses once for an engine rule — the passage routing the spec destination through `note`'s hook: the engine named, its place named in quotes, and the restatement explicitly refused, as in "This is `roadmap-engine`'s "Named roadmaps" § "Spec destination" routed through `note`'s destination hook — do not restate its mechanics here". Neither the method nor the command is restated, and `~200–500` does not change.

## Files & types

- edit: `src/skills/roadmap-engine/SKILL.md` — the contract-line budget bullet
- edit: `src/skills/roadmap-outline-deep/SKILL.md` — the **Budget** bullet

## Guards

- The numbers do not move. `~600`, `400–1000` and `~200–500` stay exactly as they are; this task adds a unit and a method, not a new budget.
- One home for the method. It is stated in `roadmap-engine` and pointed at from `roadmap-outline-deep`, never written twice.
- The two `description:` blocks naming `~600-char` are not edited. A sweep for the figure finds three files; only the engine's rule is a home of the method, and the other two carry the number as vocabulary. Editing them would put the method in three places and break the two-file scope this task keeps.
- No verification step anywhere gains a count. This task makes an existing count correct; it does not add one.
- No new skill, no new `loads:` edge, no new tool grant.
- `roadmap-engine` is a load-once engine with eight callers. This edit adds a paragraph beside one section, edits no bullet of the rule list, and changes no rule any caller depends on.
- No skill runs the pinned command. The budget is, in the engine's own words, "guidance, not a hard clamp"; the command is what settles a count once it is disputed, run by whoever disputes it. `roadmap-outline-deep` holds no `Bash` grant and gains none — it names the method's home and never executes it.

## Verification

Counts against a whitespace-normalized read of the named file, never a line-oriented `grep`.

- the seven bullets of the `**Rules for writing a contract line:**` list are byte-identical to HEAD, and `family` in `roadmap-engine/SKILL.md` is unchanged from HEAD — the paragraph adds neither a bullet nor that word
- the budget's own figures are unchanged → `Target ~600 characters (range 400–1000)` → 1
- the method keeps one home → taken across the whole of `roadmap-outline-deep/SKILL.md`: the command pinned in the engine → 0, and `code point` → 0. A Budget bullet that names the address and then restates the method gives it a second home while passing every shape count above
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly those two files and nothing else
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section
