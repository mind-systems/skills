# 55.7 — a retype decided and its costs unnamed

**Project:** tradeoxy_core
**Date:** 2026-09-23
**Stopped at:** planned:3
**Elapsed before the rescue:** 2654

The task takes the hand-rolled pair — check the form, then canonicalise — off every door at once and puts one constructor per transport in its place. The first plan did exactly that: three constructors, twenty-one route parameters, six sites across three sockets, two gRPC doors, the proto comments, the indicator-params branch — and a note saying no documentation moves.

The first reading found five defects, one of them real: the task adds four client-visible refusals on a surface where the documentation states outright that the message text is the contract, while declaring that no documentation moves. The other four were plan hygiene — a residue sweep blind to the residue it exists to catch, a dependency pointing at the neighbouring door instead of the real one, two enumerations short by an item each, and a fixture branding an identifier into a type the task itself makes unreachable. The second plan closed all five on the merits.

The second reading found seven more, and the first came from another level: retyping the request body's two id fields into a branded type flips their schema from string to object, because this repository's build runs a plugin that resolves an intersection to `Object` and consults its own factory ahead of the reflection the plan relied on. Beside it, the same field starts answering a refusal where the request previously reached the database and failed as the database fails — an improvement, unnamed. The remaining five were hygiene again, including a sweep specified to a zero it cannot reach. The third plan closed all seven.

The third reading found five more, and three of them were the same decision opened one layer deeper. The gate the plan added to protect against the object schema is specified to a state a correct implementation cannot produce: the plugin emits `Object` either way, and the string appears only further down, in the rendered schema. Deleting the door's hand guard changes the refusal's text and strips the field's name from it — while the spec, in the very paragraph ordering that deletion, states the text is unchanged. And beneath both, the project's own rule, the one the task exists to satisfy, demands in its first sentence the opposite of what the task does to the request body.

No reading returned to what the previous one had closed. Every plan closed what was found in it and introduced nothing of its own. The findings did not repeat; they deepened, one layer at a time, around a single undecided place.

> The spec decided that a request body's field is retyped to the branded type and named not one of that decision's costs — not that the project's own rule demands the plain string in its first sentence, not that the build renders such a field as an object instead of a string, and not that deleting the hand guard at the same door changes the refusal text the spec declares unchanged.

**Root-cause category:** specification gap, compounded by a rule that contradicts itself. **Recurring signal:** no finding repeated verbatim; what repeated was one decision's unnamed costs, surfacing one round apart, and three attempts in three rounds to write a verification gate that cannot do its job. **Scope was not the problem** — the wide mechanical surface converged on the first pass and was never reopened.

## What was done

The user ruled the model rather than the symptom: JSON carries a string, a DTO carries a string, the logic object carries the project's own type, and a value that does not parse is an ordinary parse failure. That deleted about a third of the spec — the transform beside the matcher, the transform-order argument, the non-string guard, the four-hundred-versus-five-hundred case, the explicit schema type on both properties, and the build-output gate — leaving the DTO's form check as a bare matcher in the shape of its neighbour, and leaving the door's two existing construction calls exactly where they were: they are the construction.

The same ruling settled the documentary half in the opposite direction from the reading that raised it. A malformed id is not contract material, so the repair was not to add the four refusal sentences a reading demanded but to remove the refusal prose already there: two clauses in the REST section, and the two form-refusal texts from the socket namespace's own contract list, which now names three messages, all of them meaning. The project's rule was repaired where it contradicted itself, and the contract line brought onto the same ruling.

One sentence went into the spec that the two earlier rescues of this task's predecessor had each paid for in their own way: no artifact of this task predicts or audits a tool's own output, and no check exists whose only job is to confirm an instruction was carried out. The predecessor's first rescue found a sweep pinned by its trigger and never its closure; its second found a plan enumerating which files the compiler would break; this one found three gates in three rounds. The same shape, three times, now stated where a planner reads it.

The repair went to spec and plan depth. The superseded reading had already reached the next open task, whose future lint message named the DTO's form check as a way to construct the type — a developer following that advice would add the decorator and still hold a string; repaired there too. The three readings were deleted; the plan was kept and edited — its documentary task removed, its DTO, schema and coverage tasks re-derived against the ruling — and the planning session kept, so the run resumes at the reading of the plan.
