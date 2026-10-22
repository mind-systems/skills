# 80.4 — § 5.6 states one moment for a pin

## What is true now

The skill is as 80.3 leaves it.

`src/skills/task-rescue/SKILL.md`, § "Step 5.6 — Pin disposed observations", opens by saying a rescue pins each deferred-observation entry it disposes of this session "at the moment it disposes of it", together with every sibling occurrence across that task's review files, by the grammar and dedup rule of `orchestrator-artifacts` § "6. Status-marker grammar". Its second paragraph scopes the pin to review files still on disk at pin time and ends: "A pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it." Its closing paragraph says a rescue disposes only of what it evaluates this session and leaves the rest unmarked for the resolution session.

The rescue now writes its report and waits for the user's word, so the judgment on an entry can be made in Step 3, before the word. The opening names the moment of the judgment and the second paragraph names the moment of the repair: § 5.6 states two moments for one pin.

## What must be true after

§ 5.6 states one moment for a pin, the one the second paragraph names: a pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it. The opening sentence carries that moment, and the sentence at the end of the second paragraph that says it again goes, so the moment is stated once. The pointer to the grammar, the sibling occurrences, the scope to review files still on disk and the closing paragraph stay as they are.

## What breaks on contact

**Rule:** a text breaks on this change if it names the moment of a pin as the moment of the judgment.

**Sweep:**
```
grep -n -i "moment" src/skills/task-rescue/SKILL.md
```

**Finding.** The search returns the opening of § 5.6 and the sentence at the end of its second paragraph, which are the targets above, and a phrase in § 5.7 about the moment of the report's first write, which is another matter and stays. Outside the skill, `orchestrator-artifacts` § "6. Status-marker grammar" says the resolution session writes a marker at the moment it disposes of an observation; that is the resolution session's own discipline, and it stays.
