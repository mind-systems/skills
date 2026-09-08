# The character budget names how a character is counted

## Current state (grounded, read fresh)

Two budgets in this family are stated in characters. `src/skills/roadmap-engine/SKILL.md` § "Rules for writing a contract line" reads "Target ~600 characters (range 400–1000)". `src/skills/roadmap-outline-deep/SKILL.md`'s **Budget** bullet reads "rewrite the phase preamble down to ~200–500 characters". Neither names how the count is taken. These two are the only length budgets in the repository, but the `~600` figure is named again in two `description:` blocks — `roadmap-engine`'s own and `roadmap-decompose`'s, both reading "a ~600-char contract line" — where it carries the vocabulary and not the rule, and so takes no unit and no method.

The environment defaults against them. `LANG`, `LC_ALL` and `LC_CTYPE` are all unset, so `wc -m` counts bytes; `awk`'s `length` counts bytes on this platform whatever the locale. Measured on the line `тест — тире`, eleven characters: bare `wc -m` returns 22, `LC_ALL=en_US.UTF-8 wc -m` returns 12 — the trailing newline counted — and a code-point count returns 11. `en_US.UTF-8` is installed here, so the locale-forced `wc -m` is available — but on that same line it returns 12 for eleven characters, counting the trailing newline the rule excludes, so it cannot be the pinned command without an off-by-one correction every caller has to remember. `awk`'s `length` returns 21 on that line with the locale forced and without it alike, confirming it never leaves bytes.

The cost is not hypothetical. A contract line of 991 characters was reported as 995 by `awk`, and eight separate measurements this session reported bytes as characters before being caught and redone.

`roadmap-outline-deep` declares `loads: roadmap-engine`, so a rule stated in the engine already reaches it; what it lacks is a sentence at its own budget naming where that rule lives.

## The change

1. `src/skills/roadmap-engine/SKILL.md` gains one short paragraph immediately below the `**Rules for writing a contract line:**` bullet list — a paragraph under the list, never a bullet inside it: the rule governs every budget in this family, and a bullet under that heading would scope it to contract lines alone. It states that every budget in this family is counted in Unicode code points with the trailing newline excluded, and pins the command that yields them here:

   ```
   python3 -c "import sys;print(len(sys.stdin.read().rstrip('\n')))"
   ```

   The numbers themselves — `~600`, `400–1000` — do not change, and no bullet of that list is edited.

2. `src/skills/roadmap-outline-deep/SKILL.md`'s **Budget** bullet names `roadmap-engine` as the home of that method, in the shape this same file already uses twice for the engine's rules: the engine named, its section named in quotes, and the restatement explicitly refused — as in "This is `roadmap-engine`'s "Named roadmaps" § "Spec destination" routed through `note`'s destination hook — do not restate its mechanics here". It restates neither the method nor the command, and `~200–500` does not change.

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

## Verification

Counts against a whitespace-normalized read of the named file, never a line-oriented `grep`.

- `roadmap-engine/SKILL.md` states the unit and pins the command in a paragraph below the `**Rules for writing a contract line:**` list, never as a bullet inside it → `code point` ≥ 1, the pinned command verbatim → 1, and the list's seven bullets byte-identical to HEAD
- the pinned command proves itself on a line of known length → run on the eleven-code-point line `тест — тире` it returns 11
- the budget's own figures are unchanged → `Target ~600 characters (range 400–1000)` → 1
- `roadmap-outline-deep/SKILL.md`'s **Budget** bullet carries all three parts of the shape → `roadmap-engine` named → 1, the place in the engine that holds the method named in quotes → 1, and the restatement explicitly refused → 1; `~200–500` → 1, and the command pinned in the engine appears in this file → 0
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly those two files and nothing else
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section
