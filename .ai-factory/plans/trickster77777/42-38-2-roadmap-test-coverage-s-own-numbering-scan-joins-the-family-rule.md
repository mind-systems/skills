# Plan: 38.2 — `roadmap-test-coverage`'s own numbering scan joins the family rule

## Context
`src/skills/roadmap-test-coverage/SKILL.md` § "Layer 4 — Deep Research (parallel agents)" mints its own note numbers with `find .ai-factory/specs -name "[0-9][0-9]-*.md" | sort | tail -1` and "Extract highest two-digit prefix + 1. If none, start at `01`." — three defects in one definition site: the glob is blind to a third digit, `sort` is lexicographic (verified: widening the glob alone returns `99-…` over `126-…` in this repo's `specs/trickster77777/`), and `find` without a depth limit recurses every subdirectory into one numbering space while `note` numbers per-directory. This task rewrites that one site to the shape 38.1 already gave `note` (read any-length digit run, compare numerically, write four zero-padded digits `0001`–`9999`, stop at the bound naming the destination) and scopes the scan to the flat `.ai-factory/specs/` directory — before any parallel agent is spawned.

Ground truth read fresh — `src/skills/roadmap-test-coverage/SKILL.md`:
- The single definition site is the block opening "Determine next note number:" in Layer 4 — the fenced `mkdir -p` + `find` command, the sentence "Extract highest two-digit prefix + 1. If none, start at `01`.", and "Store as `$NEXT_NOTE_NUM`."
- The seven consumer sites (agent prompt's "Note to write:", "Write the following document to", "saved:" line; Layer 6 item 1's pointer; Layer 8's "Notes written" list and both handoff blocks) all carry the bare placeholder `.ai-factory/specs/<NN>-<slug>.md` with no width embedded — none needs touching; they inherit whatever `<NN>` becomes.
- `note`'s landed wording (the family shape to match, read from `src/skills/note/SKILL.md`): scan pattern `` `^[0-9]+-.*\.md$` `` read as an integer and compared numerically; `<NN>` "zero-padded four-digit sequence number (`0001`, `0002`, `0003` …)"; default "start at `0001`"; bound "Numbers run `0001` through `9999`. When the highest number the scan finds is `9999` or greater, … writes nothing … reports that the numbering bound is reached, naming `<destination>`"; report form `Numbering bound reached: <destination> already holds 9999 — nothing written.`
- Frontmatter `allowed-tools` grants `Bash(find *)` and `Bash(mkdir *)`; a pipeline whose command string starts with `find` stays inside that grant, so no tool grant changes.
- Verified on this machine (macOS BSD tools): `find .ai-factory/specs/trickster77777 -maxdepth 1 -name "[0-9]*-*.md" -exec basename {} \; | sort -n | tail -1` returns `126-test-coverage-numbering-joins-the-family-rule.md` where the old `| sort | tail -1` returns `99-…`. On the flat `.ai-factory/specs/` (no numbered files) it prints nothing — the empty-directory case.

Assumptions pinned so the implementer does not invent them:
- The destination stays the flat `.ai-factory/specs/` — the same path every one of the seven consumer sites names. The named-roadmap `<slug>/` subdirectory contradiction is recorded in the spec as unowned by this phase and is **not** repaired here; do not redirect the scan or the writes into a subdirectory.
- `note` is not loaded, not called, and not edited. The `loads:` field stays `test-philosophy roadmap-engine`. The parallel structure — one `$NEXT_NOTE_NUM` computed once, each `Explore` agent handed its own number in the prompt template — is untouched; nothing serialises the agents.
- Reading and writing are two rules: the scan reads a leading digit run of any length (mixed widths exist and every one must count toward the maximum); the writer emits exactly four zero-padded digits. Do not narrow the read side to four digits.
- The bound predicate is transcribed with the "or greater" clause, as in `note`: when the highest number the scan finds is `9999` or greater, Layer 4 writes nothing and reports the bound, naming `.ai-factory/specs/`. The stop happens at the computation of `$NEXT_NOTE_NUM`, i.e. before "Launch one `Explore` agent per area".
- The placeholder `<NN>` keeps its name; only its definition changes.
- `find -name` globs cannot express `+`, so the shell filter is the looser `[0-9]*-*.md` (leading digit, anything, hyphen) and the prose states the exact rule `^[0-9]+-.*\.md$`, as `note` does; `sort -n` parses the leading digit run as the integer, which is the numeric comparison the spec asks for. Portable across BSD and GNU `sort`.
- No file under `.ai-factory/specs/` is renamed or renumbered.
- `aif-plan` stays untouched (dormant carrier, out of the active set).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the one definition site in Layer 4

- [x] **Scope the scan to one directory and make it read any-length prefixes numerically**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In § "Layer 4 — Deep Research (parallel agents)", replace the fenced block under "Determine next note number:" with:
  ```bash
  mkdir -p .ai-factory/specs
  find .ai-factory/specs -maxdepth 1 -name "[0-9]*-*.md" -exec basename {} \; | sort -n | tail -1
  ```
  Three changes, each load-bearing: `-maxdepth 1` scopes the scan to the flat `.ai-factory/specs/` directory only — the same directory every note this skill writes names — so subdirectories (named-roadmap spec folders) are never counted; `"[0-9]*-*.md"` widens the glob past two digits; `-exec basename {} \;` + `sort -n` compares the leading digit run as an integer, so `126-…` outranks `99-…`. Keep the command string starting with `find` (the `Bash(find *)` grant). Do not add `-regex`/`-E` (non-portable between BSD and GNU `find`).

- [x] **Widen the extraction rule for reading and set the write width and default to four digits** (depends on the previous task)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Replace the sentence "Extract highest two-digit prefix + 1. If none, start at `01`." with prose in the same terse register, stating both rules as two rules: the scan counts files whose name matches `` `^[0-9]+-.*\.md$` `` — a leading run of digits of any length — and the highest prefix is the numerically largest parsed integer, never the last name in string order; `$NEXT_NOTE_NUM` is that integer + 1, written with exactly four zero-padded digits (`0001`–`9999`) regardless of how small it is; if no numbered file exists, start at `0001`. Say in one clause that the four-digit width governs only what this skill writes — existing names of any width are still read. Keep "Store as `$NEXT_NOTE_NUM`." Do not write the phrase "two-digit" anywhere in the rewritten text.

- [x] **Declare the bound and stop before any agent is spawned** (depends on the previous task)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Immediately after "Store as `$NEXT_NOTE_NUM`." and before "Launch one `Explore` agent per area…", add one short paragraph (prose, no new heading): numbers run `0001` through `9999`; when the highest number the scan finds is `9999` or greater, Layer 4 launches no agent and writes nothing — instead it stops the pipeline here and reports that the numbering bound is reached, naming the destination, in the form `Numbering bound reached: .ai-factory/specs/ already holds 9999 — nothing written.` (mirroring `note`'s report line). State explicitly that the stop is at this point — `$NEXT_NOTE_NUM` is computed once, before the parallel launch, so no agent is ever spawned part-way. Do not touch the agent prompt template, the "single message (parallel)" instruction, or Critical Rule 3/6.

### Verify the file as a whole

- [x] **Whole-file checks** (depends on all previous tasks)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  After the edits: `grep -n '\[0-9\]\[0-9\]\|two-digit\|start at `01`' src/skills/roadmap-test-coverage/SKILL.md` returns nothing; `grep -n 'maxdepth 1' …` hits exactly once (Layer 4); `grep -c '0001' …` ≥ 1 and `grep -n '9999' …` hits only the Layer 4 bound paragraph; `grep -c '\.ai-factory/specs/<NN>-<slug>\.md' …` is unchanged from before the edit (the seven consumer sites untouched); the frontmatter (`loads:`, `allowed-tools`) is byte-identical to before; the file stays under 500 lines. Run the new command once against `.ai-factory/specs/trickster77777` (substituting the path) and confirm it returns the `126-…` name, and once against the flat `.ai-factory/specs` and confirm it prints nothing. `grep -rn '\[0-9\]\[0-9\]' src/skills src/commands` must now hit only `src/skills/aif-plan/SKILL.md`.
