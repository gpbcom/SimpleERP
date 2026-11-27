🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) ›
🛟 F20 Hosted support assistant (hosted edition)

# 🛟 F20 Hosted support assistant (hosted edition)

**Status:** ✅ specified

Build step: 10. Hosted edition services.

## Summary

In the hosted edition, a support assistant that talks a problem through with a customer who may not be technical, reads
the customer's own Kubernetes namespace and screenshots when needed, explains the cause in plain words, and fixes only
with a SimpleERP maintainer's yes
([D393](../../06-decisions/f20-hosted-support-assistant/d393-hosted-support-assistant-coverage.md)). A closed hosted
service around the open product ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)).

## Scope

- **Talk:** plain-words chat, clarifying questions, screenshots, how-to answers, request tracking.
- **Diagnose and fix:** read the namespace, explain, propose, approve, apply, verify, restore.
- **Incidents:** escalation, status page, proactive alerts, security incidents and breaches.
- **Govern:** rights, masking, quality, plans, exports.
- **Keep customers informed:** maintenance notices, release notes, written incident reports, service credits, French and
  English, NIS2 facts, employees' help on the phone and from the screen (D477).

## Personas

[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U01 Employee](../../01-users/personas/u01-employee.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U48 Hosting engineer](../../01-users/personas/u48-hosting-engineer.md).

## Out of scope

- Support of the customer's own customers: F16.
- Self-hosted installations: their IT provider runs support (D388).
- Any change not approved by a maintainer.

## Technical capabilities used

- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md) (cluster, backups)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md) (documentation)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 10, Hosted edition services, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Feature factory (hosted edition)](../f19-feature-factory/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Onboarding and module activation](../f21-onboarding-and-modules/README.md)
