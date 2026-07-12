# Plan: roadmap-prune: default-pair sweep never deletes stem subdirectories

## Context
Close the cross-developer deletion hazard on the default-pair side of `roadmap-prune`'s Step 5 sweep: on a repo that also holds `.ai-factory/roadmaps/`, a default-pair prune must delete only the flat regular files under `plans/`/`plan-reviews/`/`reviews/` (and flat `test-runs/` in tests mode), sparing every developer's per-roadmap stem subdirectories — while a solo repo (`roadmaps/` absent) keeps today's whole-dir `rm -rf` byte-for-byte.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Scope the default-pair sweep

- [x] **Task 1: Split the default-pair branch by `roadmaps/` presence**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 5, item 2, rewrite the **Default pair** bullet (currently: "`rm -rf` the three flat dirs directly under `<target repo root>/.ai-factory/`: `plans/`, `plan-reviews/`, `reviews/`"). Per spec 51 §Change, make the deletion conditional on `.ai-factory/roadmaps/` under the target repo root:
  - `roadmaps/` absent (solo repo) → today's whole-dir `rm -rf` of `plans/`, `plan-reviews/`, `reviews/`, byte-stable (keep the current phrasing verbatim for this branch).
  - `roadmaps/` present → delete only the regular files directly under each of the three dirs (`find <dir> -maxdepth 1 -type f -delete` or equivalent), preserving the per-roadmap stem subdirectories (`plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/`).
  State that this mirrors, on the default side, the per-stem protection the Named-roadmap branch already gives — "never a sibling stem's subdirectory," now protected from both sides. Do not touch the Named-roadmap bullet (already correct) or item 1 (spec-tag capture) / item 3 (`rm -f` spec paths).
  **Shared lead-in (review F1):** the item-2 stem — "Determine the sweep scope … then `rm -rf`:" (SKILL.md:277–278) — is a single deletion verb enclosing **both** the Default-pair and Named-roadmap sub-bullets. If the `roadmaps/`-present case is expressed with `find … -delete`, that hard-asserted `rm -rf` stem contradicts the nested `find`. Keep the two coupled: when a `find`-based branch is introduced, soften the shared lead-in to a verb-neutral form (e.g. "then delete:"); leave it as "then `rm -rf`:" only if the file-only sweep is expressed with an `rm`-based equivalent — the same coupling Task 3 applies to `allowed-tools`.

- [x] **Task 2: Apply the same file-only rule to flat `test-runs/` in tests mode**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 5, the `test-runs/` paragraph (the one ending "…the swept dir is flat `test-runs/` for the default pair and `test-runs/<stem>/` for a named test roadmap"). Extend the default-pair case so that when `roadmaps/` is present, the flat `test-runs/` sweep also deletes only the regular files directly under it (`-maxdepth 1 -type f`), preserving `test-runs/<stem>/` subdirs; when `roadmaps/` is absent, the whole-dir `rm -rf` of flat `test-runs/` stays byte-stable. Keep the `<name>-tests`→`<stem>` derivation and the named-test-roadmap case unchanged.

- [x] **Task 3: Reconcile the `Bash(rm *)` grant with the new `find` deletion**
  Files: `src/skills/roadmap-prune/SKILL.md`
  If — and only if — Tasks 1–2 introduce a literal `find … -delete` invocation into the skill body, add `Bash(find *)` to the frontmatter `allowed-tools` line (currently `Read Write Edit Bash(git *) Bash(rm *) Glob Grep Skill`) so the file-only deletion runs pre-approved. If the implementer phrases the file-only sweep with an `rm`-based equivalent instead (still covered by `Bash(rm *)`), leave `allowed-tools` byte-stable. Do not remove `Bash(rm *)` — the solo-repo whole-dir branch still uses it.

### Phase 2: Report wording

- [x] **Task 4: Confirm Step 8 report wording still matches the sweep** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  Per spec 51 §Files ("Step-8 report wording follows if it enumerates the swept dirs"), re-read Step 8's summary sentence ("List the dirs swept in Step 5 — the flat three dirs …"). The swept **dirs** are unchanged (still `plans/`, `plan-reviews/`, `reviews/`, plus flat `test-runs/`); only what is deleted inside them narrows. If the existing wording implies whole-dir removal in a way that now misreads on a multiuser default-pair prune, adjust it minimally to say the flat files within those dirs were swept; otherwise leave Step 8 byte-stable. Do not expand the report beyond the dir/spec-file enumeration it already produces.
