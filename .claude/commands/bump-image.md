---
description: Redeploy prod from a given commit (the image ref is set at deploy time, not in compose).
argument-hint: "<git-sha>"
---

`docker-compose.prod.yml` uses `image: ${IMAGE_REF}`; `deploy-ec2-ssh` supplies it at deploy time. There is no tag to edit in the repo.

1. Verify the commit exists: `git rev-parse --verify $ARGUMENTS^{commit}`.
2. Show the command, do not run it without confirmation: `gh workflow run deploy-prod.yml -f ref=$ARGUMENTS` (rebuilds and deploys that ref).
3. For an instant rollback to an already-pushed digest, follow `docs/runbooks/rollback.md` instead.
