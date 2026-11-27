🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › ⚖️ F15 Legal assistant

# ⚖️ F15 Legal assistant

**Status:** ✅ specified

Build step: 6. HR and projects, and the legal assistant (Proposed).

## Summary

A legal assistant in the AI assistant panel (F3) that answers on the law of each enabled country, France first, for
employees, managers, HR, the owner and accountants, and on the technical rules and standards of the company's sector
([D28](../../06-decisions/foundations/d28-legal-assistant.md),
[D190](../../06-decisions/f15-legal-assistant/d190-legal-assistant-askers.md)). It answers for the person's real
situation from the ERP's data, within their rights, and warns on its own where it sees a legal risk, unless warnings are
turned off.

## Scope

- **Employees, own rights:** leave, working time, overtime, notice, training, sick leave.
- **Managers and HR, the company's duties:** thresholds, staff representatives (CSE), mandatory registers and displays,
  hiring and dismissal procedures, health and safety.
- **Owner, commercial and tax rules:** Code de commerce, Code général des impôts, invoicing and payment terms.
- **Accountants, tax and social rules:** contributions, tax questions (U05, U08).
- **Sector technical rules and standards:** for each activity sector SimpleERP can be configured for (08-sectors),
  documented in [Sector technical standards](../../05-non-functional/sector-technical-standards.md).
- **Real situation:** contract, seniority, collective agreement, company size and sector, from the ERP's data the asker
  may see, listed in the answer; "general answer only" always offered
  ([D191](../../06-decisions/f15-legal-assistant/d191-legal-answers-from-erp-data.md)).
- **French sources:** the codes, collective agreements, official guidance, case law
  ([D192](../../06-decisions/f15-legal-assistant/d192-legal-sources-france.md)).
- **Warnings:** on by default, can be turned off; then on demand only
  ([D193](../../06-decisions/f15-legal-assistant/d193-legal-warnings-on-by-default.md)).
- **Compliance and company records:** the compliance calendar, contracts' renewal and notice dates, the approval of the
  accounts and registers, data-subject requests and the AI uses inventory, confidence and the lawyer hand-off, the
  catalogue of warning triggers (D472).

## Personas

[U01 Employee](../../01-users/personas/u01-employee.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U06 HR](../../01-users/personas/u06-hr.md),
[U08 External accountant](../../01-users/personas/u08-external-accountant.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md).

## Out of scope

- Legal advice: answers inform and cite; they never replace a lawyer, and say when to consult one (05-non-functional,
  legal advice limits).
- Questions on the company's own data without a legal angle: the AI assistant (F3).
- Building the corpora: T11.

## Technical capabilities used

- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md)
- [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 6, HR and projects, and the legal assistant, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)) (Proposed): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | 🔄 |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | 🔄 |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Plugin store](../f14-plugin-store/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Customer support agents](../f16-customer-support-agents/README.md)
