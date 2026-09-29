# 65.5 — the seed carries what a spec holds

## What is true now

This task is sequenced after 65.2, so `src/skills/agent-architect/templates/buffer-seed.md` is read here as spec 181 leaves it. Its `## Method` section holds a placeholder line in angle brackets, "A mistake as the pattern behind it and the reason that pattern holds, never the episode that revealed it.", and one bold-led entry, **Standing entry — the counts rule.**, whose body ends "ask which member is missing." The section that follows is `## Orientation`.

The seed says nothing of what a spec holds. The rule lives in two places, and a new buffer carries neither: `roadmap-engine`'s bold lead-in "**What a task spec holds:**" says a task spec holds what is true now, what must be true after, what breaks on contact, and nothing else, and that no clause is a check that the instruction was carried out, none is a position in the file, and none fences off a neighbour by name; `docs/what-a-task-carries.md` gives the reasons, chiefly that the orchestrator's reviewer already holds the spec and already checks, and that a planner turns each checking passage into a step of the plan.

The head re-reads its buffer all session and a skill is read once and fades; the user's ruling is "Скилл — рождает архитектора, буфер — его ПЗУ", and on this rule: "вот это правило — не ставить заборы для оркестратора — место ему в шаблоне буфера." The field showed the cost: an architect whose session held the engine's new text kept writing guard and acceptance sections into specs, from a habit its buffer kept.

## What must be true after

`## Method` gains a second standing entry, directly after the counts rule and before `## Orientation`, in the same shape, a bold lead-in and then the body, separated from the entry above by a blank line:

> **Standing entry — what a spec holds.** A spec states what is true now, what must be true after and what breaks on contact, and nothing else. It carries no check that the instruction was carried out: the orchestrator plans, builds and reviews on its own, and a check written into a spec comes back as plan steps and review rounds. It names no position in a file, only what the artifact must hold. It puts no fence around a neighbour; scope is what the task changes.

The entry points to no doc and no skill, and the counts-rule entry above it is as spec 181 pins it.

## What breaks on contact

**Rule:** a text breaks on this change if it reads the seed, or if it states what a spec holds in a way that disagrees with the new entry.

**Sweep:**
```
grep -rn "buffer-seed" src/ docs/ CLAUDE.md
grep -rn "What a task spec holds" src/ docs/ CLAUDE.md
grep -rn "and nothing else" src/skills src/commands
```

**Finding.** The first search reaches `agent-architect/SKILL.md`, in the founding passage, which reads the seed once and has a new buffer copy it whole, so the new entry reaches every buffer founded afterwards; the seed's own opening says the same. The editor holds no seed but reads the founded buffer whole, as its own working context, so it holds the entry too — the reach the ruling wants, and the one route by which a rule about how a spec is worded reaches whoever writes it. A buffer founded from an earlier seed holds neither this entry nor the counts rule's new form; those are records of what the seed said then and belong to their heads. No other skill, command or doc reads the seed.

The second search reaches `roadmap-engine`'s paragraph, which is the rule's home, and the walk of `command-pin-gaps` toward a spec's three parts, which cites that paragraph by name and restates none of it, so the entry cannot disagree with it. The entry agrees with the paragraph sentence by sentence. It names the same parts. It gives the same reason for no check that the paragraph gives, the review the orchestrator already runs, and adds the reason `docs/what-a-task-carries.md` states, that a check comes back as plan steps and review rounds. It states the position rule as the paragraph does, what the artifact must hold and never where to write it. It states the fence rule as the paragraph does, scope as what the task changes. The third search reaches that paragraph, the walk paragraph of `command-pin-gaps` where "this task and nothing else" describes what a run holds, and a sentence of `docs/paired-loop.md` on genres; the last two share the words and not the subject.
