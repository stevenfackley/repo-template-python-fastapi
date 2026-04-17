---
description: Local smoke test.
---

1. `docker compose ps | grep {{PROJECT_NAME}}` (up? if not, `docker compose up -d --build`).
2. Curl `/health` → expect 200.
3. Curl `/` → expect 200.
4. Tail last 20 log lines.
