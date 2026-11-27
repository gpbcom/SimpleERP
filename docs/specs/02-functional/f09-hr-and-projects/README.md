🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 👥 F9 HR and projects

# 👥 F9 HR and projects

**Status:** ✅ specified

Build step: 6. HR and projects, and the legal assistant.

## Summary

People and work: employees, recruitment, time, attendance, appraisals and skills, workplace services, shifts,
timesheets, projects and field service, covering every HR feature of the benchmark and French duties
([D285](../../06-decisions/f09-hr-and-projects/d285-activity-drafts-opt-in.md) to
[D289](../../06-decisions/f09-hr-and-projects/d289-hr-coverage.md)).

## Scope

- **Employees:** records, departments, org chart, contracts, documents, equipment, onboarding and offboarding plans,
  self-service (D288).
- **French duties:** register, DPAE, career-path interviews (every 4 years, review every 8), health visits, displays,
  BDESE (D287).
- **Recruitment:** jobs, career site, boards, sourcing and campaigns (D235), LinkedIn sourcing through Unipile with
  ranked profiles and outreach sequences (D518), pipeline, AI CV reading, AI voice pre-screening, interviews (F4),
  offers, e-signature, referrals.
- **Time:** time off (accruals, approvals, holidays, mandatory and blackout days), attendance (kiosk, badge, PIN, phone,
  location at check-in only, D286), overtime, timesheets (opt-in activity drafts, D285).
- **Growth:** appraisals (self, manager, 360), goals, skills, certifications with reminders, eLearning.
- **Workplace:** fleet, approvals, lunch, visitors.
- **Work:** shifts and auto-planning, projects (tasks, milestones, Gantt, profitability, customer sharing), field
  service (map, worksheets, signatures, offline).
- **Gaps and improvements round ([D466](../../06-decisions/f09-hr-and-projects/d466-f09-gaps-and-improvements.md),
  2026-11-12):** the equality index and pay transparency, a whistleblowing channel, the training plan with OPCO funding,
  work accidents and the occupational risk assessment, capacity planning across projects, rounds and route optimisation
  (shared capability, [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md)), UC-F9-03 split per duty
  with disability employment (OETH), engagement surveys and exit interviews, the customer's project view, and
  subcontractors and freelancers on projects.

## Personas

[U06 HR](../../01-users/personas/u06-hr.md), [U01 Employee](../../01-users/personas/u01-employee.md),
[U02 Manager](../../01-users/personas/u02-manager.md), [U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U09 Customer](../../01-users/personas/u09-customer.md),
[U16 Office worker](../../01-users/personas/u16-office-worker.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U45 Payroll officer](../../01-users/personas/u45-payroll-officer.md),
[U38 Training coordinator](../../01-users/personas/u38-training-coordinator.md),
[U27 Quality manager](../../01-users/personas/u27-quality-manager.md),
[U24 Engagement manager](../../01-users/personas/u24-engagement-manager.md),
[U25 Care coordinator](../../01-users/personas/u25-care-coordinator.md),
[U29 Dispatcher](../../01-users/personas/u29-dispatcher.md), [U26 Carer](../../01-users/personas/u26-carer.md),
[U30 Driver](../../01-users/personas/u30-driver.md),
[U42 Sales representative](../../01-users/personas/u42-sales-representative.md),
[U10 Supplier](../../01-users/personas/u10-supplier.md).

## Out of scope

- Payroll computation: F13 (F9 feeds it).
- Expenses: F8 (UC-F8-12).
- Interview capture: F4 (UC-F4-13).

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (URSSAF, job boards, sourcing)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md) (HR privacy)

## Build step

Step 6, HR and projects, and the legal assistant, of the [roadmap](../../00-vision/roadmap/roadmap.md)
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
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Accounting](../f08-accounting/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Point of sale (plugin)](../f10-point-of-sale/README.md)
