# global CLAUDE.md: interface names declare their kind — mandatory at decomposition

## Current state

Live incident (tradeoxy): planning artifacts carried an abstraction name that read as neither interface nor class — the agent implementing it could not tell the kind from the name. The local fix landed in `tradeoxy_broker/.ai-factory/RULES.md` ("Protocol Naming: Protocol names must carry either an `I` prefix (`IPLRService`) or a `Protocol` suffix (`BrokerProtocol`) — no other form"), but nothing carries the concept across projects, and nothing binds **decomposition** to it: `roadmap-decompose`, `roadmap-decompose-skeleton` (whose skeleton lens is precisely where new interfaces are born), architect work-orders, and orchestrator planners all name new abstractions with no kind-marking rule anywhere in their loaded context.

## Change

One verbatim bullet appended to `src/global/CLAUDE.md` § "Planning workflow" (exact text — the contract):

> - **Interface names declare their kind.** When a planning artifact — a roadmap line, a spec, a skeleton, a work-order, a plan — names a new abstraction, the name carries the language's own interface marker (`I` prefix, `Protocol` suffix, or whatever form the language's convention uses), so a reader tells a contract from a class by the name alone. Where the project's rules pin a specific form, that form is mandatory.

The global file is the single home: it loads into every session of every project — chat planning, architect passes, and the orchestrator's headless agents alike — so every decomposition tier inherits the rule without any skill edit.

## Files & types

- edit `src/global/CLAUDE.md` — § "Planning workflow", +1 bullet

## Guards

- **Exact text above lands verbatim** — no rewording; existing section text byte-identical outside the insertion.
- **One home** — the rule enters no skill body: decompose/skeleton/agent-architect are not edited (the global file already reaches them); project `RULES.md` files keep their local, more specific forms and win by the rule's own last sentence.
- Nothing project-specific in the global file — `IPLRService`/tradeoxy examples stay in the spec, not in the bullet.

## Verification

- `grep -n "declare their kind" src/global/CLAUDE.md` → one hit in § Planning workflow; `git diff` shows only the insertion.
- Live: a decompose run that births a new abstraction names it with the language's marker (or the project's pinned form); a skeleton pass on a heavy task produces `I*`/`*Protocol`-marked contract names.
