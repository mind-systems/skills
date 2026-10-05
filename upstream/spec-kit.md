# spec-kit

URL: https://github.com/github/spec-kit
Counterparts: none

Why we follow it: GitHub's spec-driven development toolkit, the earliest of the line: its first commit is 2025-08-21, and the user regards it as the forerunner of ai-factory and so of ours. No textual borrowing is credited or found; what is shared is the shape, spec → plan → tasks → implement. Read for direction, not diffed.

## 2026-10-05

Last seen: `ae5ade7` (2026-10-03, after v1.1.0)

Heading:
- from a fixed SDD pipeline to a platform: extensions, presets, workflows with approve/reject gates, catalogs, 38 agent integrations;
- "1.0.0 is now just a number… from stability to adaptability";
- bug-fix and idea-assessment processes beside SDD.

Converges with us:
- intent before implementation: "code serves specifications";
- `converge` is append-only, classifies findings as missing, partial, contradicts or unrequested, holds that "completion claims are not evidence", and writes nothing when converged; its "unrequested" is our task-has-a-source question asked after the build;
- a constraint is quoted verbatim into the task;
- `analyze` is strictly read-only;
- clarifications are recorded in the spec under the session date;
- a roadmap of specs, each entry with an id, intent, scope boundary, dependencies and status.

Diverges:
- law and numbers written ahead: a versioned constitution of "NON-NEGOTIABLE" principles whose conflicts are "automatically CRITICAL", success criteria that are "measurable" with numeric examples, checklists as "unit tests for requirements writing", capped loops and finding limits;
- tasks are one line each, with no per-task spec;
- the spec is not held after the code: "None is the default";
- the same architecture blind spot as `aif-architecture`: structure is folder options only, and "Complexity Tracking" lists a repository pattern as a violation to justify, a bias against abstraction, the cultural root of "never interface indirection".

Taken: nothing. Worth remembering: `converge`'s "unrequested" class and its write-nothing-when-converged rule.
