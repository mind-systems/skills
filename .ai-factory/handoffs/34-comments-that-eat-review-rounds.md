# Handoff — comments that eat review rounds

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

This comes from a working session on `tradeoxy_core` (2026-09-30), written by the architect holding buffer `130` there, at the user's request. **It is parked on purpose:** the user will not feed it to the skills yet — «когда разберёмся с коментариями в коде в ходе одной из будущих фаз, может какие то новые выводы сделаем». It records what was found and the questions left open; it proposes no rule. Its sibling is `33-counts-and-line-numbers-leak-into-specs.md` — the same waste, from numbers instead of prose. The files named here override this description wherever they disagree.

## 2. Why it matters — the orchestrator runs idle

The user: «Самое мерзкое даже не то, что они засоряют код, а забирают на себя ревью итерации, как и дебильные подсчёты. Оркестратор работает в пустую просто, месит воду в ступе.» The evidence in `tradeoxy_core`'s history:
- **55.9** (`4aeb19b`, spec `193`): the second code-review round existed for one comment alone — review 1 raised a LOW finding that the `SlotLoadState` doc «states an invariant as absolute that one pre-existing interleaving can break», repair «prose only»; round 2 confirmed «the only change anywhere in `src/` is the comment above; every executable line is byte-identical».
- **`ReplayOrderAxisRegistry`** (`ed6ecef`, spec `87`): three code-review rounds with zero behavioural findings — every actionable finding was about the class header's wording or its citation form.
- The same shape at the plan tier: a plan review spends its finding on a comment the plan intends to write (54.7.2, `80c6a84`: plan review 1 disproved the rationale a planned comment would carry).

## 3. How the prose gets there — five mechanisms, traced

`indicator-runtime.service.ts` is 1273 lines, 486 of them comments; `order-axis-context.ts` 61%, `eviction-policy.ts` 45%, `replay-order-axis-registry.ts` 42%, `replay-engine.ts` 40% (measured 2026-09-30).
1. **The spec's argument becomes a commissioned comment, and review tightens it.** Specs carry the *why*; the planner turns it into a deliverable — 54.7.2's plan: «Header comment for the method: the three arrival cases, why the fast case finds nothing, and why `{ async: true }` is load-bearing»; 55.9's plan dictates the doc comment near-verbatim, «state its limit precisely, because the next reader reasons from this sentence». The reviewer then checks every sentence like code, and each precision adds a qualifier. The reviewers were not nitpicking style — they held prose to ground truth, and caught real errors in it (a registry comment asserting the opposite of what the live runtime does).
2. **A skeleton task's deliverable is its doc comment** — no bodies exist, so the contract is written as a class doc, and it stays once the bodies land.
3. **A task's scope fence becomes a module header** — spec `31`'s «no DB, no cron, no NestJS providers… 13.2.2's concern» became `eviction-policy.ts`'s «No NestJS decorators, no DataSource, no cron…», with a neighbour's task key in production code.
4. **The tag purge left the argument behind** (34.6, `746eb3b`): plan-layer citations were removed from code; where no doc existed, the prose around them stayed. The user: «Мы запретили тэгать поверхность планирования и вместо этого целиком спеки начали переезжать в код.» Pre-ban pointers that survived in `proto/` partly dangle («note 50» no longer exists).
5. **The copy drifts** — the `SlotLoadState` essay retells `docs/indicators.md` § «Состояние загрузки слота» and already contradicts it.

## 4. The good example

The user's own Swift in `tradeoxy_broker`: `Order.swift` 9 comment lines of 329, `ProductionBroker.swift` none. Each comment says one non-obvious thing where the reader meets it, in one to three lines — «тут внимательный. Этот стоп фактический, а в индикаторе обычно триггерный». The user: «Я не имею ничего против коментариев, объясняющих код, сам их пишу».

## 5. Open questions — not answered here

- **How to fix it at all** — the user: «не понятно как это чинить вообще».
- **Teach, not forbid** — «Может тут не запрещать надо а научить писать коментарии.»
- **Teach whom** — «Но кого учить тоже вопрос..»: the spec author (the architect, who writes the *why* the planner carries), the planner (who commissions comments), or the reviewer (who spends rounds on prose); and whether the source is the specs or those prompts — «наши спеки или промпт планировщика и ревьювера — тот ещё вопрос».

## 6. Next step

None now. `tradeoxy_core`'s Phase 65 («Comments and test titles state what the code does now») takes the rotten comments as its work; what that cleanup teaches is to be added here before the user decides whether the skills change.
