---
description: Commit all changes as "Roadmap update" — amend if the last commit is an unpushed "Roadmap update", else make a new one. Nothing else.
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git log *) Bash(git merge-base *)
---

Run exactly this, then say nothing else:

```sh
git add -A && \
if [ "$(git log -1 --pretty=%s)" = "Roadmap update" ] && ! git merge-base --is-ancestor HEAD @{u} 2>/dev/null; then \
  git commit --amend --no-edit; \
else \
  git commit -m "Roadmap update"; \
fi
```

Do not push, do not change the message.
