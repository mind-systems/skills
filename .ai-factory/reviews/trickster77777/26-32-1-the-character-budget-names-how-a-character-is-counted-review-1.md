# Review — 32.1 the character budget names how a character is counted (round 1)

Scope reviewed: `git diff HEAD` — `src/skills/roadmap-engine/SKILL.md` (+2), `src/skills/roadmap-outline-deep/SKILL.md` (+2/-1). Both files read in full around the change; task spec `.ai-factory/specs/trickster77777/107-character-budget-names-its-method.md` and the plan read as the contract.

## What the change does

`roadmap-engine` gains one paragraph at line 107, immediately under the `**Rules for writing a contract line:**` list, naming the counting method and pinning the command. `roadmap-outline-deep`'s **Budget** bullet gains one sentence addressing that paragraph by its home instead of restating it.

## Verification performed

Counts taken by the method the spec names — the whole file read and whitespace-normalized (`tr '\n' ' '`), never a line-oriented `grep` — and lengths by the pinned command itself.

- Seven bullets of the rule list byte-identical to HEAD: the engine diff has **zero** removed lines; the only hunk is a pure insertion. ✓
- `family` in `roadmap-engine/SKILL.md`: 2 occurrences, and 2 at HEAD — unchanged; the new paragraph adds neither a bullet nor that word. ✓
- `Target ~600 characters (range 400–1000)` → exactly 1. ✓ `~200–500` in outline-deep unchanged. ✓
- Method has one home: across the whole of `roadmap-outline-deep/SKILL.md`, `code point` → 0 and `python3` → 0. ✓
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly the two files. Nothing written under `active/` (both are symlinks into `src/skills/`, so the edits are already live). ✓
- The two `description:` blocks carrying `~600-char` (`roadmap-engine`, `roadmap-decompose`) and `docs/reserved-words.md:24` untouched, per the guard. ✓
- No frontmatter change: `loads: roadmap-engine note` and `allowed-tools:` on outline-deep, `loads: note` on the engine, all as at HEAD. No new skill, no new edge, no new grant. ✓
- The pinned command runs as written: `printf 'тест — тире\n' | python3 -c "import sys;print(len(sys.stdin.read().rstrip('\n')))"` → `11`. The `"` and `'\n'` landed literally in the file (nothing expanded on the way in), and the double-quoted `\n` survives the shell to reach Python as an escape. ✓
- Paragraph framing: one blank line at 106 and one at 108, so it is a paragraph under the list, not an eighth bullet and not a continuation. ✓ No trailing whitespace introduced (`git diff --check` clean). ✓
- `§ "Counting characters"` is addressable: the paragraph sits under `## Roadmap File Format`, and its bold lead-in is the same kind of anchor the file's existing `§ "Spec destination"` reference already targets. ✓

## Findings

### 1. The pointer sentence in the Budget bullet attaches to the wrong clause (correctness of reference)

`src/skills/roadmap-outline-deep/SKILL.md:103-104`. The sentence was appended at the very end of the bullet:

```
  whatever the preamble sheds. Prose that is neither the gate nor that distillation
  is dropped deliberately, not relocated. This is `roadmap-engine`'s "Roadmap File
  Format" § "Counting characters" — do not restate its mechanics here.
```

`This is` takes the immediately preceding sentence as its antecedent, and that sentence is the drop-don't-relocate rule about shed prose — not a count of anything. The thing whose method actually lives in the engine, `**~200–500 characters**`, is four sentences earlier at the head of the bullet.

The shape the spec told the implementation to copy does not have this problem. In the Step 1 analogue (`:63`), `This is …` sits directly against the sentence it addresses:

```
  `.ai-factory/specs/<slug>/` for a named roadmap, flat `.ai-factory/specs/` for the
  default roadmap. This is `roadmap-engine`'s "Named roadmaps" § "Spec destination"
  routed through `note`'s destination hook — do not restate its mechanics here, …
```

Failure scenario: an agent compressing a preamble reads the Budget bullet top to bottom and parses the closing sentence as *the deliberate-dropping discipline is homed in the engine* — a rule that does not exist there. It follows the address, finds a paragraph about counting code points, and is left with two readings of one sentence and no statement anywhere that `~200–500` is code points. That is precisely the miss this task exists to close: the budget still does not name its method to a reader who stops at the figure. The section title `Counting characters` is the only thing currently disambiguating, and it is doing that work against the sentence's own grammar.

Fix, minimal and inside the same bullet: move the pointer so it lands against the figure rather than after the shed-prose rule — e.g. attach it to the first sentence (`… down to **~200–500 characters**, counted per `roadmap-engine`'s "Roadmap File Format" § "Counting characters" — do not restate its mechanics here — keeping the phase's gate and its `Phase note:` pointer.`), or keep it in final position but give it an explicit subject rather than `This` (`The character count is `roadmap-engine`'s "Roadmap File Format" § "Counting characters" — do not restate its mechanics here.`). Either keeps `~200–500` unmoved, restates no mechanics, and adds no count.

## Note, not a finding

`rstrip('\n')` strips *every* trailing newline, not just one. On the single-line input these budgets are measured against that is indistinguishable from stripping one, and the command is the spec's verbatim pinned text — implementing it as written is correct. Recorded only so a later reader does not mistake it for drift.
