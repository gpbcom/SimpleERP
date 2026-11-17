🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 🗄️ Data retention

# 🗄️ Data retention

**Status:** ✅ specified

## Requirement

- A leaver's business records stay, with their name; their private AI assistant history is deleted at deactivation;
  meeting recordings follow the meetings' retention rule (F4). See
  [D75](../06-decisions/f01-administration/d75-leavers-personal-data.md).

- Every entity is kept for the period of its kind, as the retention schedule below says
  ([D446](../06-decisions/security-and-compliance/d446-privacy-specified.md)).

## Retention schedule

A country rule, where it exists, sets the value; the defaults below apply where none does.

| Kind of record | Examples | Kept | Source |
|---|---|---|---|
| Accounting records and supporting documents | Entries, invoices, bank lines (F6 to F8) | 10 years from the year's close | [CR-FR-002](../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md) |
| Till data | Receipts, sessions (F10) | 6 years | [CR-FR-029](../10-country-packs/france/point-of-sale/cr-fr-029-till-data-kept-six-years.md) |
| Payslips | Payslips (F13) | The employer's copy 5 years; electronic payslips available 50 years from issue | [CR-FR-182](../10-country-packs/france/payroll/cr-fr-182-payslip.md), D445 |
| HR records | Employees, register, working time, candidates (F9) | Register 5 years after departure; working time 1 year; candidates 2 years after the last contact | [CR-FR-047](../10-country-packs/france/labour/cr-fr-047-hr-records-retention.md) |
| Customers, prospects, contacts | Contacts, leads (F5, F6) | 3 years after the last contact | [CR-FR-052](../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md) |
| Meeting audio and video | Recordings (F4) | Deleted once the transcript is checked, 7 days by default | [CR-FR-052](../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md) |
| Call recordings, when switched on | Recordings, scorecards (F4, D449) | (Proposed) 6 months; analysis reports 1 year | [CR-FR-207](../10-country-packs/france/data-protection/cr-fr-207-call-recording-proportionate.md) |
| Assistant conversations | Conversations (F3) | 12 months unused | [CR-FR-052](../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md) |
| Health records | Patient records (SC09) | (Proposed) as the health-practice rules say, the period to read | [CR-FR-131](../10-country-packs/france/health-practice/cr-fr-131-medical-record-access.md), [CR-FR-055](../10-country-packs/france/data-protection/cr-fr-055-health-data-hosting.md) |
| Audit trail | Audit entries (T3) | (Proposed) as long as the records they trace; personal data separable | REQ-T03-03 |
| Logs, metrics and traces | Observability (T9) | (Proposed) 13 months | - |
| Connector runs | Runs (T12) | (Proposed) 13 months | E-T12-04 |
| Backups | Backups (T9) | Self-hosted 30 days; hosted and IT providers 30 days daily, 12 months monthly | D24, D444 |
| Every other record | Any entity with no row above | (Proposed) while the company uses it, deleted with the company (REQ-T01-07); personal data erasable on request where no legal period applies | D446 |

## Measures

- Each entity's Retention section points to this schedule.
- (Proposed) Deletion jobs run daily per company; what they deleted is counted in the audit trail, never the content.
- (Proposed) A legal hold suspends deletion for the records it names, with its reason and end.

## Country pack

The legal values this page relies on, from the France country pack (D293):

- [CR-FR-002 Accounting records kept 10 years](../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md)
- [CR-FR-052 Personal data kept no longer than needed](../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md)
- [CR-FR-207 Call recording at work kept proportionate](../10-country-packs/france/data-protection/cr-fr-207-call-recording-proportionate.md)

## Open questions

None beyond the (Proposed) values above, listed under Waiting for the owner.

---

⬅️ [Privacy and GDPR](privacy-gdpr.md) · ⬆️ [Up](README.md) · ➡️ [Observability](observability.md)
