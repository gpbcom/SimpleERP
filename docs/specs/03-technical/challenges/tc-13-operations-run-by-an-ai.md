🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🛟 TC-13 Hosted operations helped by an AI

# 🛟 TC-13 Hosted operations helped by an AI

**Status:** ✅ listed for the technical interviews

## Challenge

Let the support assistant read a customer's namespace, take masked screenshots and propose fixes that a maintainer
approves, and manage domains, DNS, certificates and mail records through providers' APIs.

## Raised by

- [F20 Hosted support assistant (hosted edition)](../../02-functional/f20-hosted-support-assistant/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md)

## Why it is hard

- Read access to a cluster is powerful: it must be narrow, audited and never reach secrets.
- A wrong DNS change breaks a customer's mail.
- Breaches must be handled within legal deadlines.

## Already decided

- [D388](../../06-decisions/vision/d388-hosted-edition-open-core.md) Hosted edition: closed services around the open
  core
- [D393](../../06-decisions/f20-hosted-support-assistant/d393-hosted-support-assistant-coverage.md) Hosted support
  assistant: access and approvals

## Options to weigh

- A read-only service account per namespace, and fixes as approved, scripted runbooks.
- DNS changes as plans, checked and reversible.
- Masking at the log pipeline, not in the AI assistant.

## Settled in

- 19f Security ([chapter](../../../technical/security/security.md))
- 19h Observability ([chapter](../../../technical/operations/observability.md))
- 19j CI/CD and deployment ([chapter](../../../technical/infrastructure/deployment.md))
- Then the technical capabilities: [T9 Install, backups and updates](../t09-install-backups-and-updates/README.md).

## Questions for the interview

- Which fixes may be scripted for approval in the first version?
- Who is on call for the hosted edition?

---

⬅️ [TC-12 Code written by an AI, running in production](tc-12-generated-code-in-production.md) · ⬆️ [Up](README.md) ·
➡️ [TC-14 Planning and calculation engines](tc-14-planning-and-calculation-engines.md)
