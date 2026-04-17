# Incident response

1. Declare — open `Ops incident` issue, pick severity.
2. Stabilize — SEV-1: roll back first (see `rollback.md`); SEV-2/3: gather logs.
3. Investigate — `docker logs`, `gh run list --status failure`, `kubectl describe pod` (K3s).
4. Resolve — patch, test, deploy, verify.
5. Post-mortem within 48h. Blameless.
