# Plan: 38.1 — the numbering scan sees past ninety-nine

## Context
`src/skills/note/SKILL.md` states its numbering scan as the glob `[0-9][0-9]-*.md` at four sites and its width as "zero-padded two-digit" once; the glob cannot see a third leading digit, so in `.ai-factory/specs/trickster77777/` (19 two-digit files, real top `126-…`) it would propose `100`, which already exists. This task rewrites `note` so the scan reads a leading run of digits of any length, compares numerically, writes new names with exactly four zero-padded digits (`0001` … `9999`, empty-directory default `0001`), and at a destination already holding `9999` writes nothing and reports the bound with the destination named.

Ground truth read fresh — the five sites in `src/skills/note/SKILL.md`, addressed by the text that opens them:
1. § "Hooks (caller inputs)", **Destination directory** bullet: "the `mkdir -p`, the `[0-9][0-9]-*.md` numbering scan, and the final path."
2. § "Step 3: Save Note to File", the `<NN>` bullet under **Note file path**: "`<NN>` is a zero-padded two-digit sequence number (`01`, `02`, `03` …)".
3. Same section, the determination sentence: "To determine `<NN>`, find the highest existing `NN` prefix among files matching `[0-9][0-9]-*.md` in `<destination>` and add 1. If no numbered files exist yet, start at `01`."
4. Same section, **Folder style** paragraph: "reuse that same `[0-9][0-9]-*.md` scan to read the 1–2 most recent (highest-numbered) sibling files".
5. § "Note File Handling", first bullet: "`<NN>` determined by scanning existing `[0-9][0-9]-*.md` files per-directory in `<destination>` and incrementing the highest".

Assumptions pinned here so the implementer does not invent them:
- The placeholder name `<NN>` stays `<NN>`. It is a symbol callers resolve by name (`roadmap-engine` "`<NN>` scanned against the destination in play", `architect-editor-engine` "`.ai-factory/notes/<NN>-architect-buffer.md`", `docs/philosophy/multiuser-roadmaps.md`); only its *definition* inside `note` changes width. Renaming it would ripple through every caller and is not asked for.
- Reading and writing are two rules and are worded as two rules: the scan reads any-length digit runs (names of mixed width already exist and every one must count toward the maximum); the writer emits exactly four digits.
- The bound predicate is one sentence, transcribed verbatim into the skill by task 3: **when the highest number the scan finds is `9999` or greater, `note` writes nothing.** "Or greater" is deliberate — a hand-made five-digit name must also stop the writer rather than yield `10000`. The stop comes before composing a body: no `mkdir -p`, no `Write`, no folder-style sibling reads for a file that will not be written.
- No file on disk is renamed or back-filled; the task changes how `note` reads the shelf, not what is on it.
- `roadmap-test-coverage` (own hand-rolled scan, closed by 38.2) and `aif-plan` (dormant, not in `active/`) are not touched. `task-rescue` carries no scan of its own but quotes the old glob while describing `note`'s destination hook; that quote becomes a false description of the engine the moment `note` changes, and is corrected in place (one home per fact — the caller points, it does not copy).
- `allowed-tools` in `note`'s frontmatter (`Read Write Bash(ls *) Bash(mkdir *) Glob`) already covers listing the directory; the numeric comparison is done by the agent over the listed names, so no tool grant changes.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the scan, the width, and the bound in `note`

- [x] **Define the scan once, as a leading run of digits, and make every site name that one scan**
  Files: `src/skills/note/SKILL.md`
  In § "Hooks (caller inputs)", **Destination directory** bullet (site 1), replace the literal `[0-9][0-9]-*.md` with a description of the widened scan, stated once as the home of the rule: files whose name begins with a run of one or more digits followed by a hyphen and ends in `.md` — write the pattern as `` `^[0-9]+-.*\.md$` `` (a leading run of digits of any length, then `-`), and say in the same clause that the run is read as an integer and compared numerically, never as a string, so `100-…` ranks above `99-…`. Keep "Numbering stays **per-directory** (scan the chosen directory only)" unchanged. Keep the bullet's register (one dense bullet, second person absent, present tense). After this edit, `grep -n '\[0-9\]\[0-9\]' src/skills/note/SKILL.md` must hit only sites 3, 4, 5 until the next tasks clear them.

- [x] **Change the width claim and the determination rule to four digits with a `0001` default** (depends on the previous task)
  Files: `src/skills/note/SKILL.md`
  In § "Step 3: Save Note to File":
  1. Site 2 — rewrite the `<NN>` bullet so it says `<NN>` is a zero-padded **four-digit** sequence number (`0001`, `0002`, `0003` …), and adds that the width governs only what `note` writes — existing names of any width are still read.
  2. Site 3 — rewrite the determination sentence in the same two-clause shape it has now: *find* — the highest existing prefix among files matching the scan defined in the hooks section (name it as "the numbering scan from the Destination directory hook" or repeat the `^[0-9]+-` form; do not reintroduce the two-digit glob), parsed as an integer and compared numerically, plus 1; *default* — "If no numbered files exist yet, start at `0001`." State that the result is written with exactly four zero-padded digits regardless of how small it is.
  Keep the sentence about `<destination>` defaulting to `.ai-factory/notes/` and the `<slug>` bullet untouched.

- [x] **Declare the bound: at `9999` write nothing and report the destination** (depends on the previous task)
  Files: `src/skills/note/SKILL.md`
  Immediately after the determination sentence (site 3) in § "Step 3: Save Note to File", add one short paragraph (prose, no new heading) stating: numbers run `0001` through `9999`; when the highest number the scan finds is `9999` or greater, `note` writes nothing — no `mkdir -p`, no file, no sibling reads — and reports that the numbering bound is reached, naming `<destination>`, instead of proposing `10000` or a number already taken. This is the one predicate from the Context section; write it with the "or greater" clause, not the bare `9999`. Then in § "Step 4: Report", add a second report form beneath the existing "Note saved:" block for this case, e.g. a fenced block reading `Numbering bound reached: <destination> already holds 9999 — nothing written.` Keep the existing "Note saved:" block and its trailing `<destination>` default sentence unchanged. In § "Important Rules", Rule 5 ("By default, always create a new file") gets one appended clause naming the bound as its only exception — a destination already at `9999` or above produces no file. Do not add a bound to the frontmatter `description:`.

- [x] **Make folder style pick its siblings by numeric order over the same scan** (depends on the first task)
  Files: `src/skills/note/SKILL.md`
  In § "Step 3: Save Note to File", **Folder style** paragraph (site 4), replace "reuse that same `[0-9][0-9]-*.md` scan" with a reference to the same scan defined in the hooks section, and make explicit that "most recent (highest-numbered)" is decided over the parsed integer — the 1–2 siblings with the numerically highest prefixes, so a name with a longer prefix outranks any shorter-prefixed one (`100-…` ranks above `99-…`). Do not use the phrase "two-digit" anywhere in the rewritten paragraph — the whole-file verification below greps it out. Everything else in the paragraph — precedence, guards, "at most 2 sibling reads" — stays word-for-word.

- [x] **Point the "Note File Handling" restatement at the rule instead of copying it** (depends on the previous tasks)
  Files: `src/skills/note/SKILL.md`
  In § "Note File Handling", first bullet (site 5), remove the second copy of the glob and the two-digit determination: the bullet says `<NN>` is the four-digit number determined by the per-directory numbering scan in Step 3 (bounded at `9999`), and nothing more — one home for the rule, the bullet a pointer. Keep the `<slug>` bullet and the lead-in sentence unchanged.
  Verification for the whole file after this task: `grep -n '\[0-9\]\[0-9\]\|two-digit\|start at `01`' src/skills/note/SKILL.md` returns nothing; `grep -c '0001' src/skills/note/SKILL.md` ≥ 2 (width bullet and default); `grep -n '9999' src/skills/note/SKILL.md` hits exactly four places — Step 3 (bound paragraph), Step 4 (bound report form), Important Rules Rule 5 (the exception clause), and Note File Handling (the pointer) — none of them stray; the placeholder `<NN>` still appears unchanged in the path templates; body stays under 500 lines; frontmatter untouched.

### Correct the one caller that quotes the old glob

- [x] **Drop the literal glob from `task-rescue`'s description of `note`'s destination hook** (depends on the `note` edits)
  Files: `src/skills/task-rescue/SKILL.md`
  In the paragraph opening "**All three of `note`'s hooks are supplied**", the *destination directory* bullet reads "it drives `note`'s `mkdir -p`, its per-directory `[0-9][0-9]-*.md` numbering scan, and the final path." Replace the quoted glob with plain words — "its per-directory numbering scan" — so the caller names the mechanism without copying its pattern; the sentence two lines below ("`note`'s own mechanics — numbering, `mkdir -p`, folder style — are not restated here") already commits the file to that. No other change in `task-rescue`. After the edit, `grep -rn '\[0-9\]\[0-9\]' src/skills src/commands` must hit only `src/skills/aif-plan/SKILL.md` and `src/skills/roadmap-test-coverage/SKILL.md` — the two carriers this task leaves alone by contract.
