🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D420 DevOps practice

# 📜 D420 DevOps practice

**Status:** ✅ decided

## Context

Step 19z of the technical interview (PLAN D35).

## Options

- GitOps with Argo CD, or pipelines pushing to clusters.
- Dev, QA, staging and production, or ephemeral stages then production.
- An on-call rota with runbooks as code, or best effort.

## Choice

Confirmed by the owner on 2026-11-12: GitOps with Argo CD; ephemeral dev and QA, a long-lived staging, production with
canary rollouts; an on-call rota of maintainers with runbooks as code.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The DevOps chapter's target design.

## Related

- [DevOps practice](../../../technical/operations/devops.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D419 CI/CD and the image registry](d419-ci-cd-and-registry.md) · ⬆️ [Up](README.md) ·
➡️ [D421 Infrastructure: fully CNCF compatible](d421-infrastructure-cncf.md)
