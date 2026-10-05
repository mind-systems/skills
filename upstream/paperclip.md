# paperclip

URL: https://github.com/paperclipai/paperclip
Counterparts: none

Why we follow it: an open-source control plane that runs a team of AI agents as a company: an org chart, goals, heartbeats, budgets and approval gates, with the work and its history kept in its own database. Read for the team and orchestration direction, not diffed.

## 2026-10-05

Last seen: `1c07b59` (2026-10-04)

Heading:
- agent companies that run 24/7: hire any agent behind an adapter ("If it can receive a heartbeat, it's hired"), goals carried into tasks as goal ancestry, delegation along an org chart, budgets with automatic pause, approval gates, a dashboard and a phone;
- chat connectors;
- an org-wide skill library.

Converges with us:
- a team of agents toward one goal;
- persistent sessions continued by session id per agent and task (`--resume`, or ACP);
- a wake that arrives with its reason and the new comments inline ("Wake Payload" / "Resume Delta");
- a recovery wake when a run ends without a final disposition;
- file memory the agent keeps itself (a PARA skill).

Diverges:
- planning, tasks, reviews and history live in its Postgres, not in the repository beside the code;
- roles and job descriptions (we dropped roles when agents in roles grew fanatical and pressed each other);
- one central registry against links held by each head;
- autonomy braked by money (budgets) rather than by an operator that removes work;
- it never reaches an open interactive session, only processes it spawns;
- its runs override the user's Claude settings (`.claude/settings.local.json`, `dontAsk`; `dangerouslySkipPermissions` by default on the CLI engine).

Taken: nothing. Worth remembering: waking a head is `claude -p --resume <session-id>` with a wake payload (our `address.md` already holds the id); atomic checkout by one conditional update ("Never retry a 409"); coalesced wakes.
