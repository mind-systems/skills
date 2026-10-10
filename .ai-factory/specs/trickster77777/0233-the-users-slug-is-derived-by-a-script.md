# 83.1 — the user's slug is derived by a script

## What is true now

`src/skills/roadmap-engine/SKILL.md`, § "Named roadmaps", holds the derivation only as prose, in the paragraph **Slug derivation**: "the local-part of `git config user.email`, lowercased, every non-alphanumeric run collapsed to a single hyphen (`john.doe@example.com` → `john-doe`); fallback — slugified `user.name` when email is unset." Each agent that resolves "my roadmap" carries that sentence out itself. The skill has no `scripts/` directory.

The orchestrator derives the slug in running code, `_derive_identity_slug` in `orchestrator/orchestrator/main.py`: it takes the text before the first `@` of the git email, lowercases it, collapses every run of characters outside `a-z` and `0-9` to one hyphen, and trims hyphens from both ends; when the email is unset, or its slug comes out empty, it applies the same steps to the whole git name; when both give nothing, it has no slug. The paragraph above trims no hyphens and falls back only when the email is unset.

`docs/philosophy/multiuser-roadmaps.md` states the same derivation — edge hyphens trimmed, the `user.name` fallback when the email is absent or its slug comes out empty.

`src/skills/observe-logs/scripts/query-loki.sh` is a skill's helper script, executable, and `observe-logs` invokes it by a path relative to its own directory.

## What must be true after

`src/skills/roadmap-engine/scripts/user-slug.sh` exists, executable like `query-loki.sh`. Run in a git working directory, it derives the slug as the orchestrator's code does: it reads `git config user.email` as git resolves it there, takes the text before the first `@`, lowercases it, collapses every run of characters outside `a-z` and `0-9` to one hyphen and trims hyphens from both ends; when the email is unset, or its slug comes out empty, it applies the same steps to the whole of `git config user.name`. It prints the bare slug as exactly one line to standard output, nothing else, and exits zero:

```
<user-slug>
```

where `<user-slug>` stands for the derived slug, so `john.doe@example.com` prints `john-doe`. When neither value yields a slug, it prints nothing to standard output, says on standard error why no slug could be derived, and exits with status `2`; no other failure of the script uses `2`. The identity is that of the repository the script runs in, `git config` in its working directory, so a repository-local identity wins over the global one.

The script's callers read the bare slug: the hook of 83.3, which puts the label `The user's slug: ` before it, an agent that finds no such line, and the orchestrator's code.

The script is the one home of the derivation in the skills' text: no skill states how the slug is derived, the engine's paragraph being as 83.2 leaves it. The orchestrator calling the same script is its liaison's to take up.

## What breaks on contact

**Rule:** a text breaks on this change if it states the derivation of the user's slug as a rule for an agent to carry out beside the script.

**Sweep:**
```
grep -rn "local-part" src docs CLAUDE.md
grep -rn "slugified" src docs CLAUDE.md
grep -n "scripts/" CLAUDE.md
```

**Finding.** The search for `local-part` returns the engine's paragraph, which 83.2 rewrites; the registry's slug entry in `docs/reserved-words.md`, which names the local-part of the git email and stays true; and the lines of `docs/philosophy/multiuser-roadmaps.md` that describe the name derived from the git email and the owner line, which stay true, the behaviour being the same and only who derives it moving. The engine's `> Owner: <full email>` check compares the full email and is untouched. The search for `slugified` returns the engine's paragraph alone. The governing doc and the script agree: each trims edge hyphens, falls back to `user.name` when the email is absent or its slug comes out empty. In `CLAUDE.md`, `scripts/` appears as the repository's `compare-sources.sh` directory and as a skill's optional helpers, "e.g. `design_system.py`"; both stay true with a skill that gains a `scripts/` directory, and nothing there reads false.
