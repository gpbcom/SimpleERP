🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🛟 [Decisions: F20 Hosted support assistant (hosted edition)](README.md) ›
📜 D393 Hosted support assistant: access and approvals

# 📜 D393 Hosted support assistant: access and approvals

**Status:** ✅ decided

## Context

The owner asked for a support chatbot that discusses an issue with the customer, with access to the Kubernetes
infrastructure, presented nicely for customers who may not be technical (PLAN D32).

## Options

- Reads and diagnoses; fixes need a yes.
- Read only.
- Full autonomy in the customer's namespace.

## Choice

Confirmed by the owner on 2026-11-12: the AI assistant talks in plain words, reads the customer's own namespace (status,
logs, metrics, events) through a narrow, audited service account, takes screenshots when needed, explains the cause
simply, and proposes a fix; every fix (restart, scale, roll back, renew a certificate, restore) is applied only after a
simple-ERP maintainer's yes (U47); anything else goes to a human engineer. Never another customer's data, never a
secret. A closed hosted service (D388).

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F20-02 to BR-F20-08; twenty use cases (D394).

Revised by D452 on 2026-11-12: the engineer who approves a fix is the hosting engineer (U48).

## Related

- [F20 Hosted support assistant](../../02-functional/f20-hosted-support-assistant/README.md)

---

⬅️ [D392 simple-ERP maintainer persona](../ux/d392-simple-erp-maintainer-persona.md) · ⬆️ [Up](README.md) ·
➡️ [D394 F20 use cases](d394-f20-use-cases.md)
