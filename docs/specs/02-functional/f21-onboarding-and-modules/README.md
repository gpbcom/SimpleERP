🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🧭 F21 Onboarding and module activation

# 🧭 F21 Onboarding and module activation

**Status:** ✅ specified

Build step: 2. Platform.

## Summary

The first-run path of a company, for a person who is not technical: an interactive, step-by-step guide in plain words
with the AI assistant at every step, sector templates and demo data, and a module catalogue where each functional
capability is switched on or off in one click, its dependencies explained and its data kept
([D395](../../06-decisions/f21-onboarding-and-modules/d395-onboarding-and-modules-coverage.md)).

## Scope

- **First run:** welcome, the company, a template, identity, VAT and bank, the legal check.
- **Modules:** the catalogue, one click on or off, dependencies, each module's short guide, hosted prices.
- **Team and data:** invitations, imports, connections.
- **Learn:** demo data, the checklist, tours, first sign-in of employees, provider templates, onboarding figures.
- **Migration and people:** migration from named tools, opening balances checked against the FEC, the external
  accountant's invitation, languages, onboarding on the phone (D478).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U07 Administrator](../../01-users/personas/u07-administrator.md),
[U01 Employee](../../01-users/personas/u01-employee.md),
[U11 IT provider administrator](../../01-users/personas/u11-provider-admin.md),
[U48 Hosting engineer](../../01-users/personas/u48-hosting-engineer.md).

## Out of scope

- The administration screens: F1 (its guided set-up becomes F21's steps).
- Configuration beyond the guide (fields, workflows): F2.

## Technical capabilities used

- [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md)
- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (modules as plugins)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack)
- [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

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

⬅️ [Hosted support assistant (hosted edition)](../f20-hosted-support-assistant/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Unified platform cost management](../f22-unified-cost-management/README.md)
