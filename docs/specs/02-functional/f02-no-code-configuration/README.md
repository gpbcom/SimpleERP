🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🔧 F2 No-code configuration

# 🔧 F2 No-code configuration

**Status:** ✅ specified

Build step: 2. Platform.

## Summary

What a company changes in SimpleERP without a developer: fields, statuses and forms, new record types, document and
email templates, and workflows. See [D94](../../06-decisions/f02-no-code-configuration/d94-f2-scope.md).

## Scope

- **Fields, statuses and forms:** custom fields on existing records (such as "site manager" on a quote), custom statuses
  and their order, the layout of forms.
- **New record types:** whole new kinds of records with their list and form, such as "Vehicles" for a transport company
  or "Interventions" for home care.
- **Document and email templates:** the look and wording of quotes, invoices, delivery notes and emails.
- **Workflows and automations:** simple "when, if, then" rules and a visual flow designer
  ([D95](../../06-decisions/f02-no-code-configuration/d95-rules-and-visual-workflows.md)), with approval chains and
  actions (notify, assign, change status, call a webhook).
- **Who:** the administrator and users with the Configurator role
  ([D96](../../06-decisions/f02-no-code-configuration/d96-configurator-role.md)).
- **Safety:** draft, preview with real data, publish; every version kept and can be rolled back
  ([D97](../../06-decisions/f02-no-code-configuration/d97-draft-preview-publish.md)).
- **Benchmark additions (D300):** live spreadsheets and dashboards, a documents workspace, e-signature requests,
  building with plain language, a sandbox copy of the company.
- **Gaps and improvements round ([D459](../../06-decisions/f02-no-code-configuration/d459-f02-gaps-and-improvements.md),
  2026-11-12):** kanban, calendar, map, Gantt and timeline views; the shared booking engine (any record type can be
  booked, [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md)); portals for any record type and
  offline phone forms; impact analysis, rule test cases, pack upgrade merge and the unused-configuration report;
  field-level rights and validation, translations, and one approval engine.

## Personas

- [U07 Administrator](../../01-users/personas/u07-administrator.md)
- [U02 Manager](../../01-users/personas/u02-manager.md), with the Configurator role, for their department
- [U16 Office worker](../../01-users/personas/u16-office-worker.md), with the Configurator role, for templates
- [U13 Owner](../../01-users/personas/u13-owner.md), with the Configurator role, in small companies
- [U12 Marketing and communication](../../01-users/personas/u12-marketing.md), with the Configurator role, for templates
- [U03 Sales](../../01-users/personas/u03-sales.md)
- [U05 Accounting](../../01-users/personas/u05-accounting.md)
- [U06 Human resources](../../01-users/personas/u06-hr.md)
- [U11 IT provider administrator](../../01-users/personas/u11-provider-admin.md)

See [D98](../../06-decisions/f02-no-code-configuration/d98-who-configures.md).
- [U22 Site manager](../../01-users/personas/u22-site-manager.md)
- [U28 Hotel receptionist](../../01-users/personas/u28-hotel-receptionist.md)
- [U33 Medical secretary](../../01-users/personas/u33-medical-secretary.md)
- [U38 Training coordinator](../../01-users/personas/u38-training-coordinator.md)
- [U43 Event producer](../../01-users/personas/u43-event-producer.md)
- [U09 Customer](../../01-users/personas/u09-customer.md)
- [U14 Field worker](../../01-users/personas/u14-field-worker.md)
- [U26 Carer](../../01-users/personas/u26-carer.md)
- [U30 Driver](../../01-users/personas/u30-driver.md)

## Out of scope

- Code: plugins (T4, F14) are written by developers.
- Users, roles and connections: [F1](../f01-administration/README.md).

## Technical capabilities used

- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md) (the Configurator role)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md) (versions)
- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (record types and plugins share one model)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md) (custom fields and record types appear in the
  API; webhook actions)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

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
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Administration](../f01-administration/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Assistant](../f03-assistant/README.md)
