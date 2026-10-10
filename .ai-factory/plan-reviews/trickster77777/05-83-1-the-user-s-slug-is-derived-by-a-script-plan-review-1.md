## Code Review Summary

**Files Reviewed:** 1 plan (+ task spec `0233`, `orchestrator/orchestrator/main.py` `_derive_identity_slug` / `_git_config_value`, `src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/roadmap-engine/SKILL.md`, the sweep targets)
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` lists `scripts/` as a skill's directory for executable helpers (Python, Bash). `active/skills/roadmap-engine` is a directory symlink to `src/skills/roadmap-engine`, so the new `scripts/user-slug.sh` resolves through `~/.claude/skills/roadmap-engine/scripts/user-slug.sh` with no new symlink. 83.3's hook depends on that path.
- **Rules** — WARN: `.ai-factory/RULES.md` is absent (the file is optional).
- **Roadmap** — OK. Task 83.1 in `.ai-factory/roadmaps/trickster77777.md` matches the plan title. The contract line and spec `0233` match the plan's scope. The plan defers the engine paragraph to 83.2 and the hook to 83.3, which matches the boundaries of those tasks' contract lines.
- **Sweep pre-check** — I ran the spec's sweep now. `local-part` hits `roadmap-engine/SKILL.md` § "Named roadmaps", `docs/reserved-words.md` (slug entry) and `docs/philosophy/multiuser-roadmaps.md`. `slugified` hits the engine paragraph alone. This is exactly the spec's § "What breaks on contact" finding, so the plan's expected result is right.

### Critical Issues

**1. The proposed slugify pipeline gives a different result from the orchestrator's code when a value contains a newline, and then breaks the "exactly one line" contract.** (plan § "Create `user-slug.sh`" → **Slugify**)

The plan's pipeline is `tr 'A-Z' 'a-z' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//'`. `sed` works line by line, so a newline is never part of `[^a-z0-9]+`. It passes through unchanged, and the `^`/`$` trims run on each line separately. Git does store and return values with embedded newlines. I verified this: `git config user.name $'Ann\nLee'` is written as `name = Ann\nLee`, and `git config user.name` prints `Ann⏎Lee⏎`. Command substitution removes only the trailing newline. The results for this case:

- Python `_slugify("Ann\nLee")` → `ann-lee`
- the plan's pipeline → `ann⏎lee`. That is two lines on stdout, which breaks the spec's "prints the bare slug as exactly one line" and the plan's claim that it matches the orchestrator step for step. It would also put a newline into the label the 83.3 hook prints.

The input is rare, but the fix costs one stage and makes the pipeline simpler. Do the collapse with `tr`, which treats newline as an ordinary byte, and keep `sed` only for the edge trim:

```bash
printf '%s' "$1" | LC_ALL=C tr 'A-Z' 'a-z' | LC_ALL=C tr -cs 'a-z0-9' '-' | LC_ALL=C sed -E 's/^-+//; s/-+$//'
```

I ran this here with bash 3.2.57 and BSD tr/sed. Results: `Ann⏎Lee` → `ann-lee`, `--John..Doe--` → `john-doe`, `Ünïcödé Name` → `n-c-d-name`. All three match Python. Please also add a fixture to the contact check, e.g. name `$'Ann\nLee'` with no email → `ann-lee`, exactly one line.

A side note on the plan's wording: "a non-ASCII run collapses to one hyphen, the same as Python's `re.sub` after `.lower()` does" is true except for a few code points that Python's Unicode `.lower()` maps into ASCII. For example, KELVIN SIGN U+212A lowercases to `k`. Byte-wise `tr` cannot reproduce that, and nobody puts such characters in a git identity, so no code change is needed. Please soften the sentence so it does not claim exact parity there.

### Positive Notes
- The order of derivation matches `_derive_identity_slug` exactly. The email local-part is taken via `${email%%@*}` (the same as `split("@", 1)[0]`). If that slug is empty, the code falls back to the whole name, and if both are empty there is no slug. This is the behaviour the spec's § "What is true now" says the current engine prose gets wrong.
- Treating a non-zero exit or an empty value as unset mirrors `_git_config_value`. I checked whitespace-only values. Python's `.strip()` and the bash path end with the same outcome, because the slug comes out empty either way and the code falls through to the name.
- Exit `2` stays reserved for the no-slug case. Checking `command -v git` up front and exiting `1` keeps git absence apart from that case. Capturing with `|| email=""` correctly stops `set -e` from firing on an unset key.
- The plan states the bash 3.2 constraint explicitly. It fits this machine, which runs `GNU bash, version 3.2.57`.
- The contact-check fixtures isolate the developer's global identity with `GIT_CONFIG_GLOBAL`/`GIT_CONFIG_SYSTEM` (git 2.50 here, so both are supported). The local-overrides-global case covers the spec's "repository-local identity wins" requirement.
- The comment discipline (no plan-layer citations) is stated up front, and the plan does not touch the engine paragraph, which belongs to 83.2.
