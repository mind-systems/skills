# Re-review — 32.1 the character budget names how a character is counted (round 2)

Scope: `git status` + `git diff HEAD`. Both changed files re-read from disk this pass, not from session memory. Contract read as: task spec `.ai-factory/specs/trickster77777/107-character-budget-names-its-method.md` and the plan.

Diff now: `src/skills/roadmap-engine/SKILL.md` (+2), `src/skills/roadmap-outline-deep/SKILL.md` (+6/-5). The engine blob is unchanged since round 1 (`965d33e..23e1062` both passes); only the Budget bullet moved.

## Verdicts on round-1 findings

### 1. The pointer sentence in the Budget bullet attaches to the wrong clause — **Fixed**

Current content of the cited location, `src/skills/roadmap-outline-deep/SKILL.md:99-104`, read fresh:

```
- **Budget** — rewrite the phase preamble down to **~200–500 characters**, counted
  per `roadmap-engine`'s "Roadmap File Format" § "Counting characters" — do not
  restate its mechanics here — keeping the phase's gate and its `Phase note:`
  pointer. The note states what is not yet as the docs say, per Step 1's template —
  it is a short distillation, not a home for whatever the preamble sheds. Prose that
  is neither the gate nor that distillation is dropped deliberately, not relocated.
```

The dangling `This is …` is gone. `counted per …` now sits directly against `**~200–500 characters**`, so the reference modifies the figure it is about, and the refusal to restate is carried in a paired-em-dash aside. The shed-prose rule (`dropped deliberately, not relocated`) is back to closing the bullet with nothing hanging off it. The fix took the first of the two remedies the round-1 review offered and moved nothing else: `~200–500` is byte-identical, and the three trailing sentences are the round-1 text re-wrapped, not rewritten (`git diff` shows only rewrap plus the inserted clause).

The address it names resolves: `**Counting characters:**` sits at `roadmap-engine/SKILL.md:107`, between `## Roadmap File Format` (line 77) and `## Roadmap maintenance flow` (line 124) — the `§` target is real and correctly attributed. Its shape matches the file's one existing engine-address at `:63` (`… "Named roadmaps" § "Spec destination" … — do not restate its mechanics here`): engine named, place named in straight double quotes, restatement refused, same `§` glyph.

## Full re-verification

All counts taken by the method the spec pins — whole file read and whitespace-normalized (`tr '\n' ' '`), never line-oriented `grep` — and lengths by the pinned command itself.

- Method keeps one home: across the whole of `roadmap-outline-deep/SKILL.md`, `code point` → 0, `python3` → 0, `rstrip` → 0. The bullet names the address and stops. ✓
- `~200–500 characters` → exactly 1, unchanged. ✓
- Engine: `Target ~600 characters (range 400–1000)` → exactly 1. ✓
- Engine: `family` → 2, and 2 at HEAD (`git show HEAD:…`) — unchanged; the paragraph adds neither a bullet nor that word. ✓
- Seven bullets of `**Rules for writing a contract line:**` byte-identical to HEAD: the engine hunk is a pure insertion, zero removed lines, framed by one blank line at 106 and one at 108 — a paragraph under the list, not an eighth bullet, not a continuation. ✓
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly the two files. Nothing under `active/` (both are symlinks into `src/skills/`, so the edits are already live in the working set). ✓
- No frontmatter change on either file: zero `+`/`-` lines touching `name:`, `description:`, `loads:`, `allowed-tools:`. No new skill, no new `loads:` edge, no new tool grant; `roadmap-outline-deep` still holds no `Bash` grant and executes nothing. ✓
- The two `description:` blocks carrying `~600-char` (`roadmap-engine`, `roadmap-decompose`) and `docs/reserved-words.md:24` untouched, per the guard that keeps the number-as-vocabulary out of scope. ✓
- No verification step anywhere gained a count. ✓
- The pinned command runs as written from the file: `printf 'тест — тире\n' | python3 -c "import sys;print(len(sys.stdin.read().rstrip('\n')))"` → `11` for eleven characters. The `"` and `'\n'` are literal in the file; the double-quoted `\n` survives the shell and reaches Python as an escape. ✓
- `git diff --check` clean — no trailing whitespace, no whitespace errors. Dash glyphs in the rewritten bullet are the file's own (4 em dashes, 1 en dash in `200–500`), matching neighbouring prose. ✓

## New issues

None. The round-2 edit is confined to one bullet, changes no number, states no mechanics a second time, and leaves every rule any of the engine's callers depends on untouched.

REVIEW_PASS
