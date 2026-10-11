# 83.4 — the slug script's header names no caller

## What is true now

`src/skills/roadmap-engine/scripts/user-slug.sh` opens with a header comment whose second and third lines read:

```
# Derives the slug the way the pipeline does: the lowercased, hyphen-collapsed
# local-part of git user.email, falling back to git user.name.
```

The orchestrator runs this script to get the slug (`_resolve_roadmap_relpath` in `orchestrator/orchestrator/main.py` calls it and reads its exit code) and no longer derives the slug itself, so "the way the pipeline does" points back at the script. The orchestrator's review of its task that made the call raised it as a deferred observation (`orchestrator/.ai-factory/reviews/trickster77777/25-28-2-the-user-s-slug-comes-from-the-skills-script-review-1.md`).

## What must be true after

The header's second and third lines are replaced by these lines, the rest of the header standing:

```
# Derives the slug: the lowercased, hyphen-collapsed local-part of git
# user.email, falling back to git user.name.
```

Nothing else in the script changes.

## What breaks on contact

**Rule:** a text breaks on this change if it describes the script's derivation by reference to a caller.

**Sweep:**
```
grep -rn "pipeline does" src docs CLAUDE.md
grep -rn "hyphen-collapsed" src docs CLAUDE.md
grep -rn "local-part" src docs CLAUDE.md
```

**Finding.** The searches for `pipeline does` and `hyphen-collapsed` return the script's header alone, the target. The search for `local-part` returns the same header and two docs, `docs/reserved-words.md` and `docs/philosophy/multiuser-roadmaps.md`, each naming the local-part of `user.email` and referring to no caller; both stay true.
