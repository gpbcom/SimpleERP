🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏭 F19 Feature factory (hosted edition)

# 🏭 F19 Feature factory (hosted edition)

**Status:** ✅ specified

Build step: 10. Hosted edition services (Proposed).

## Summary

In the hosted edition, a chatbot that builds new features: the customer describes a need, approves a specification and a
quote of 300 EUR a month excluding VAT, the factory generates a plugin that is tested, reviewed and signed, tried on a
copy, then installed; a promoted feature becomes available to every hosted customer and earns its promoter 50 % of its
price as a credit ([D389](../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md),
[D390](../../06-decisions/f19-feature-factory/d390-feature-price-and-promotion-credit.md)). A closed hosted service
around the open product ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)).

## Scope

- **Order:** describe, specify, quote.
- **Build:** generation in the sandbox, checks, review and signing, upgrades.
- **Use:** try on a copy, install, changes, defects, cancellation.
- **Promote:** terms, review, hosted store, withdrawal.
- **Bill:** invoices with VAT, credits, the board.
- **Commitments:** delivery dates and delays, refunds when acceptance fails, source handover under AGPL, security and
  privacy review, postings and payment follow-up (D476).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U07 Administrator](../../01-users/personas/u07-administrator.md),
[U48 Hosting engineer](../../01-users/personas/u48-hosting-engineer.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md).

## Out of scope

- Changing the core per customer (D389).
- Payouts to customers: the share is a credit only (D390).
- Self-hosted installations: the factory is a hosted service (D388).

## Technical capabilities used

- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md)
- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md) (copies, upgrades)

## Build step

Step 10, Hosted edition services, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)) (Proposed): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Hosted websites and domains (hosted edition)](../f18-hosted-websites-and-domains/README.md) ·
⬆️ [Up](../README.md) · ➡️ [Hosted support assistant (hosted edition)](../f20-hosted-support-assistant/README.md)
