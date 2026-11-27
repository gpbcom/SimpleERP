🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🧰 F14 Plugin store

# 🧰 F14 Plugin store

**Status:** ✅ specified

Build step: 7. Plugins and the plugin store.

## Summary

Finding, installing, buying and publishing plugins and sector packs: the store, permissions, updates, licences, reviews,
the publisher portal with automated checks, security review and signing, prices, payouts, seller reporting, private
stores, withdrawals, refunds and moderation, covering everything the benchmark offers
([D368](../../06-decisions/f14-plugin-store/d368-plugin-store-coverage.md)).

## Scope

- **Install:** browse, install with permissions, compatible updates, uninstall with export.
- **Buy:** support and update plans, reviews, refunds; no seats and no enforced licence check
  ([D443](../../06-decisions/vision/d443-paid-plugins-sell-support-updates-hosting.md)).
- **Publish:** submission, automated checks, security review, signing, releases.
- **Money:** prices, payouts, seller reporting, VAT.
- **Operate:** private stores, withdrawals, moderation and transparent ranking.
- **Supply chain and lifecycle:** bill of materials and licence checks, end of life and take-over, beta channel, staged
  rollout and rollback, translations and support terms (D471).

## Personas

[U46 Plugin publisher](../../01-users/personas/u46-plugin-publisher.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U11 IT provider administrator](../../01-users/personas/u11-provider-admin.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U05 Accounting](../../01-users/personas/u05-accounting.md).

## Out of scope

- The plugin runtime itself: T4.
- The plugin SDK: step 19n.

## Technical capabilities used

- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (install, permissions, sandbox)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (payments)

## Build step

Step 7, Plugins and the plugin store, of the [roadmap](../../00-vision/roadmap/roadmap.md)
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

⬅️ [Payroll (plugin)](../f13-payroll/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Legal assistant](../f15-legal-assistant/README.md)
