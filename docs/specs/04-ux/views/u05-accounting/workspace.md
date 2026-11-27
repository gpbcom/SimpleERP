🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧮 [Accounting: app shell and home](README.md) › 🧰 U05 Accounting: workspace

# 🧰 U05 Accounting: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U05 Accounting](../../../01-users/personas/u05-accounting.md) works with, embedded on their
[home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. (Proposed) The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F1-L18 API tokens](../../../02-functional/f01-administration/screens/00-lists/s-f01-l18-api-tokens.md) | Administration | Open: Active, Revoked | UC-F3-22 |
| [S-F2-L12 Spreadsheets](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l12-spreadsheets.md) | No-code configuration | All | UC-F2-12 |
| [S-F2-L13 Documents](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l13-documents.md) | No-code configuration | Open: ToSort, ToValidate | UC-F2-13 |
| [S-F2-L31 Bulk operations](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l31-bulk-operations.md) | No-code configuration | Mine: run by | UC-F2-32 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04, UC-F3-16 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L15 Agents](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l15-agents.md) | Assistant | Open: Paused | UC-F3-10, UC-F3-11 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F3-L24 Agent templates](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l24-agent-templates.md) | Assistant | Mine: none, the templates belong to the product | UC-F3-21 |
| [S-F3-L25 Add-in connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l25-add-in-connections.md) | Assistant | Mine: user | UC-F3-22 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F6-28, UC-F6-30 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-F6-18 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F6-06, UC-F6-08, UC-F6-09, UC-F6-19 and more |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-F6-07, UC-F6-09 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-F6-10 |
| [S-F6-L10 Rate plan and meters](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l10-rate-plan-and-meters.md) | Customers and sales | All | UC-F6-16 |
| [S-F6-L12 Credit limits](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l12-credit-limits.md) | Customers and sales | All | UC-F6-18, UC-SC15-16 |
| [S-F6-L13 Public buyer settings](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l13-public-buyer-settings.md) | Customers and sales | All | UC-F6-19 |
| [S-F6-L14 Funder agreements](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l14-funder-agreements.md) | Customers and sales | Open: Active | UC-F6-20, UC-SC04-08, UC-SC12-04 |
| [S-F6-L15 Pro-forma invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l15-pro-forma-invoices.md) | Customers and sales | Open: Issued, Superseded | UC-F6-22 |
| [S-F6-L16 Instalment plans](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l16-instalment-plans.md) | Customers and sales | Open: Proposed, Accepted, Broken | UC-F6-23 |
| [S-F6-L17 Invoice disputes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l17-invoice-disputes.md) | Customers and sales | All | UC-F6-24 |
| [S-F6-L18 Commission plan and targets](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l18-commission-plan-and-targets.md) | Customers and sales | Open: Draft, Active | UC-F6-26 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Mine: rep | UC-SC14-19 |
| [S-F6-L21 Payment reminders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l21-payment-reminders.md) | Customers and sales | All | UC-F6-08, UC-F6-24 |
| [S-F6-L22 Formal notices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l22-formal-notices.md) | Customers and sales | All | UC-F6-08 |
| [S-F6-L24 Company identifiers](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l24-company-identifiers.md) | Customers and sales | All | UC-F6-28, UC-F6-30, UC-F8-38, UC-SC07-24 |
| [S-F6-L26 Solvency reports](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l26-solvency-reports.md) | Customers and sales | All | UC-F6-30 |
| [S-F7-L01 Supplier records](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l01-supplier-records.md) | Purchasing and stock | All | UC-F7-18 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | All | UC-F7-04 |
| [S-F7-L05 Supplier invoices](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l05-supplier-invoices.md) | Purchasing and stock | All | UC-F7-04, UC-F7-24 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F7-09, UC-F7-22 |
| [S-F7-L12 Landed costs](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l12-landed-costs.md) | Purchasing and stock | All | UC-F7-09 |
| [S-F7-L15 Supplier contracts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l15-supplier-contracts.md) | Purchasing and stock | Open: Draft, Active, Renewed | UC-F7-18 |
| [S-F7-L18 Eco-contribution scales](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l18-eco-contribution-scales.md) | Purchasing and stock | All | UC-F7-22 |
| [S-F7-L20 Emission factors](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l20-emission-factors.md) | Purchasing and stock | All | UC-F7-24, UC-F8-28 |
| [S-F7-L24 Periodic counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l24-periodic-counts.md) | Purchasing and stock | All | UC-F7-27 |
| [S-F8-L01 Accounts](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l01-accounts.md) | Accounting | All | UC-F8-01, UC-F8-11 |
| [S-F8-L02 Journals](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l02-journals.md) | Accounting | All | UC-F8-01, UC-F8-14 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | All | UC-F8-02, UC-F8-14, UC-F8-03, UC-F8-11 and more |
| [S-F8-L04 Bank lines](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l04-bank-lines.md) | Accounting | All | UC-F8-04, UC-F8-05, UC-F8-06, UC-F8-21 |
| [S-F8-L05 Reconciliation models](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l05-reconciliation-models.md) | Accounting | All | UC-F8-06 |
| [S-F8-L06 Tax returns](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l06-tax-returns.md) | Accounting | Open: Prepared, Validated, Filed | UC-F8-03, UC-F8-07, UC-F8-24 |
| [S-F8-L07 Fixed assets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l07-fixed-assets.md) | Accounting | All | UC-F8-08, UC-F8-22 |
| [S-F8-L08 Accounting budgets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l08-accounting-budgets.md) | Accounting | All | UC-F8-09 |
| [S-F8-L09 Expense claims](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l09-expense-claims.md) | Accounting | Mine: employee | UC-F8-12 |
| [S-F8-L10 Fiscal periods](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l10-fiscal-periods.md) | Accounting | All | UC-F8-01, UC-F8-10 |
| [S-F8-L12 Filing partners](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l12-filing-partners.md) | Accounting | All | UC-F8-07 |
| [S-F8-L13 Books](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l13-books.md) | Accounting | Open: Refused | UC-F8-15 |
| [S-F8-L14 Revenue schedules](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l14-revenue-schedules.md) | Accounting | All | UC-F8-16, UC-SC14-03 |
| [S-F8-L15 Company cards](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l15-company-cards.md) | Accounting | All | UC-F8-18 |
| [S-F8-L16 Budget plans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l16-budget-plans.md) | Accounting | Mine: drivers | UC-F8-19 |
| [S-F8-L17 Client money ledgers](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l17-client-money-ledgers.md) | Accounting | Open: Open | UC-F8-21, UC-SC10-05, UC-SC10-12, UC-SC11-07 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-F8-22, UC-SC12-19, UC-SC13-07 |
| [S-F8-L19 Dedicated funds](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l19-dedicated-funds.md) | Accounting | Open: Open | UC-F8-23 |
| [S-F8-L20 Volunteer contributions](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l20-volunteer-contributions.md) | Accounting | All | UC-F8-23 |
| [S-F8-L21 Corporate tax computations](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l21-corporate-tax-computations.md) | Accounting | Open: Draft, Filed | UC-F8-24 |
| [S-F8-L23 Doubtful debt provisions](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l23-doubtful-debt-provisions.md) | Accounting | All | UC-F8-26 |
| [S-F8-L24 Variance comments](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l24-variance-comments.md) | Accounting | All | UC-F8-27 |
| [S-F8-L25 Sustainability reports](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l25-sustainability-reports.md) | Accounting | All | UC-F8-28 |
| [S-F8-L26 Accountant requests](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l26-accountant-requests.md) | Accounting | Mine: assignee | UC-F8-29 |
| [S-F8-L27 FEC files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l27-fec-files.md) | Accounting | All | UC-F8-01, UC-F8-10, UC-F21-22 |
| [S-F8-L28 Payment runs](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l28-payment-runs.md) | Accounting | All | UC-F8-03, UC-F8-04 |
| [S-F8-L29 Entry annotations](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l29-entry-annotations.md) | Accounting | All | UC-F8-01, UC-F8-10 |
| [S-F8-L30 Analytic plans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l30-analytic-plans.md) | Accounting | All | UC-F8-09 |
| [S-F8-L31 Closing checklists](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l31-closing-checklists.md) | Accounting | All | UC-F8-10 |
| [S-F8-L33 Tax rates](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l33-tax-rates.md) | Accounting | All | UC-F8-01 |
| [S-F8-L34 Loans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l34-loans.md) | Accounting | All | UC-F8-30 |
| [S-F8-L35 Remittance slips](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l35-remittance-slips.md) | Accounting | All | UC-F8-31 |
| [S-F8-L36 Revaluation runs](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l36-revaluation-runs.md) | Accounting | All | UC-F8-32 |
| [S-F8-L39 Entry templates](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l39-entry-templates.md) | Accounting | All | UC-F8-35 |
| [S-F8-L40 Audit requests](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l40-audit-requests.md) | Accounting | All | UC-F8-36 |
| [S-F8-L41 Leases](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l41-leases.md) | Accounting | All | UC-F8-37 |
| [S-F8-L42 Peppol participants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l42-peppol-participants.md) | Accounting | All | UC-F8-38 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-SC04-11 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Open: Open, Closing, Posted | UC-F10-23 |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-24 |
| [S-F10-L05 Receipts](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l05-receipts.md) | Point of sale (plugin) | All | UC-F10-27 |
| [S-F10-L06 Closures](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l06-closures.md) | Point of sale (plugin) | All | UC-F10-18 |
| [S-F10-L07 Till archives](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l07-till-archives.md) | Point of sale (plugin) | All | UC-F10-18 |
| [S-F10-L15 Till event logs](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l15-till-event-logs.md) | Point of sale (plugin) | Mine: user | UC-F10-18 |
| [S-F10-L17 Cash movements](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l17-cash-movements.md) | Point of sale (plugin) | All | UC-F10-23 |
| [S-F10-L18 Card settlements](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l18-card-settlements.md) | Point of sale (plugin) | All | UC-F10-24 |
| [S-F10-L20 Tax-free forms](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l20-tax-free-forms.md) | Point of sale (plugin) | Open: Issued, Validated, Refunded | UC-F10-27 |
| [S-F11-L05 Checkouts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l05-checkouts.md) | Online shop (plugin) | All | UC-F11-21 |
| [S-F11-L16 Fraud checks](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l16-fraud-checks.md) | Online shop (plugin) | All | UC-F11-21 |
| [S-F11-L17 Chargebacks](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l17-chargebacks.md) | Online shop (plugin) | Open: Received | UC-F11-22 |
| [S-F12-L02 Work centres](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l02-work-centres.md) | Manufacturing (plugin) | All | UC-F12-12 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Open: Draft, Confirmed, InProgress | UC-F12-12, UC-F12-27 |
| [S-F12-L21 Work-in-progress valuations](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l21-work-in-progress-valuations.md) | Manufacturing (plugin) | All | UC-F12-27 |
| [S-F13-L06 Pay runs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l06-pay-runs.md) | Payroll (plugin) | All | UC-F13-34 |
| [S-F13-L08 Pay transfers](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l08-pay-transfers.md) | Payroll (plugin) | Mine: employee | UC-F13-09 |
| [S-F13-L11 Contribution payments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l11-contribution-payments.md) | Payroll (plugin) | All | UC-F13-12 |
| [S-F13-L12 Payroll entries](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l12-payroll-entries.md) | Payroll (plugin) | All | UC-F13-13 |
| [S-F13-L19 Garnishments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l19-garnishments.md) | Payroll (plugin) | Mine: employee | UC-F13-09 |
| [S-F13-L20 Pay advances](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l20-pay-advances.md) | Payroll (plugin) | Mine: employee | UC-F13-09 |
| [S-F13-L24 Payroll cost allocations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l24-payroll-cost-allocations.md) | Payroll (plugin) | Mine: employee | UC-F13-13, UC-F13-34 |
| [S-F13-L25 Analytic axis](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l25-analytic-axis.md) | Payroll (plugin) | All | UC-F13-34 |
| [S-F14-L08 Payouts](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l08-payouts.md) | Plugin store | Open: Sent, Reconciled, Held | UC-F14-13 |
| [S-F14-L09 Seller reports](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l09-seller-reports.md) | Plugin store | All | UC-F14-14 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01, UC-F15-13, UC-F15-07 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | Mine: shown to | UC-F15-01 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L05 Compliance duties](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l05-compliance-duties.md) | Legal assistant | Mine: owner | UC-F15-07 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L14 Corporate filings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l14-corporate-filings.md) | Legal assistant | All | UC-F15-07 |
| [S-F15-L21 Disputes](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l21-disputes.md) | Legal assistant | All | UC-F15-20 |
| [S-F19-L03 Feature subscriptions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l03-feature-subscriptions.md) | Feature factory (hosted edition) | All | UC-F19-19 |
| [S-F19-L08 Promotion credits](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l08-promotion-credits.md) | Feature factory (hosted edition) | All | UC-F19-15, UC-F19-19 |
| [S-F19-L09 Hosted invoices](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l09-hosted-invoices.md) | Feature factory (hosted edition) | All | UC-F19-15, UC-F19-16, UC-F19-25, UC-F19-22 |
| [S-F19-L11 Delivery commitments](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l11-delivery-commitments.md) | Feature factory (hosted edition) | Open: OnTime, Delayed, Late | UC-F19-19 |
| [S-F19-L12 Feature refunds](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l12-feature-refunds.md) | Feature factory (hosted edition) | All | UC-F19-19, UC-F19-22 |
| [S-F19-L15 Factory postings](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l15-factory-postings.md) | Feature factory (hosted edition) | All | UC-F19-15, UC-F19-16, UC-F19-25, UC-F19-26 |
| [S-F19-L16 Feature defects](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l16-feature-defects.md) | Feature factory (hosted edition) | All | UC-F19-22 |
| [S-F20-L12 Support plans](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l12-support-plans.md) | Hosted support assistant (hosted edition) | All | UC-F20-24 |
| [S-F20-L16 Service credits](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l16-service-credits.md) | Hosted support assistant (hosted edition) | All | UC-F20-24 |
| [S-F21-L15 Opening balance checks](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l15-opening-balance-checks.md) | Onboarding and module activation | All | UC-F21-22 |
| [S-F21-L21 Parallel runs](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l21-parallel-runs.md) | Onboarding and module activation | All | UC-F21-28 |
| [S-F22-L01 Cost periods](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l01-cost-periods.md) | Unified platform cost management | All | UC-F22-01, UC-F22-24 |
| [S-F22-L02 Metered call records](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l02-metered-call-records.md) | Unified platform cost management | Mine: user | UC-F22-01, UC-F22-03, UC-F22-13, UC-F22-14 and more |
| [S-F22-L03 Provider price lists](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l03-provider-price-lists.md) | Unified platform cost management | All | UC-F22-21 |
| [S-F22-L05 Hosted quotas](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l05-hosted-quotas.md) | Unified platform cost management | All | UC-F22-15 |
| [S-F22-L09 Allocation rules](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l09-allocation-rules.md) | Unified platform cost management | All | UC-F22-03, UC-F22-14 |
| [S-F22-L11 Forecasts](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l11-forecasts.md) | Unified platform cost management | All | UC-F22-12, UC-F22-19 |
| [S-F22-L12 Invoice matches](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l12-invoice-matches.md) | Unified platform cost management | All | UC-F22-13 |
| [S-F22-L13 Usage invoices](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l13-usage-invoices.md) | Unified platform cost management | All | UC-F22-15 |
| [S-F22-L14 Exchange rates](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l14-exchange-rates.md) | Unified platform cost management | All | UC-F22-01, UC-F22-21, UC-F22-13 |
| [S-F22-L15 Compute machines](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l15-compute-machines.md) | Unified platform cost management | Open: InService | UC-F22-01, UC-F22-14 |
| [S-F22-L16 Savings recommendations](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l16-savings-recommendations.md) | Unified platform cost management | All | UC-F22-24 |
| [S-F22-L20 SaaS subscriptions](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l20-saas-subscriptions.md) | Unified platform cost management | All | UC-F22-28 |
| [S-F23-L01 Baseline forecasts](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l01-baseline-forecasts.md) | What-if simulation and impact | All | UC-F23-01, UC-F23-24 |
| [S-F23-L02 Scenarios](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l02-scenarios.md) | What-if simulation and impact | Mine: owner | UC-F23-21 |
| [S-F23-L03 Scenario changes](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l03-scenario-changes.md) | What-if simulation and impact | All | UC-F23-04 |
| [S-F23-L04 Simulation runs](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l04-simulation-runs.md) | What-if simulation and impact | All | UC-F23-05 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-07, UC-F23-08, UC-F23-12 |
| [S-F23-L06 Sensitivities](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l06-sensitivities.md) | What-if simulation and impact | All | UC-F23-14 |
| [S-F23-L11 Goals](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l11-goals.md) | What-if simulation and impact | All | UC-F23-21, UC-F23-22 |
| [S-F23-L13 Driver accuracies](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l13-driver-accuracies.md) | What-if simulation and impact | Mine: driver | UC-F23-01, UC-F23-24 |
| [S-F23-L15 Budget contributions](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l15-budget-contributions.md) | What-if simulation and impact | All | UC-F23-31 |
| [S-F23-L16 Forecast versions](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l16-forecast-versions.md) | What-if simulation and impact | All | UC-F23-32 |
| [S-F24-L06 Sync jobs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l06-sync-jobs.md) | Integrations hub | All | UC-F24-31 |
| [S-F24-L14 E-invoicing registrations](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l14-e-invoicing-registrations.md) | Integrations hub | All | UC-F24-24 |
| [S-F24-L19 Firm syncs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l19-firm-syncs.md) | Integrations hub | All | UC-F24-31 |
| [S-SC01-L06 Progress bills](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l06-progress-bills.md) | Construction | Open: Draft, Sent | UC-SC01-13, UC-SC01-06 |
| [S-SC01-L12 Public tenders](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l12-public-tenders.md) | Construction | Open: Watching, Answered | UC-SC01-13 |
| [S-SC01-L15 Revision formulas](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l15-revision-formulas.md) | Construction | All | UC-SC01-16 |
| [S-SC03-L07 Billing proposals](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l07-billing-proposals.md) | Services | All | UC-SC03-06, UC-SC03-07, UC-SC03-14 |
| [S-SC03-L08 Milestones](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l08-milestones.md) | Services | All | UC-SC03-07 |
| [S-SC03-L09 Revenue positions](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l09-revenue-positions.md) | Services | All | UC-SC03-08 |
| [S-SC04-L08 Care invoices](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l08-care-invoices.md) | Home care | All | UC-SC04-08, UC-SC04-10 |
| [S-SC04-L09 Tax-credit certificates](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l09-tax-credit-certificates.md) | Home care | All | UC-SC04-09 |
| [S-SC04-L13 Immediate advance claims](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l13-immediate-advance-claims.md) | Home care | All | UC-SC04-10 |
| [S-SC05-L15 Bonded stocks](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l15-bonded-stocks.md) | Manufacturing | All | UC-SC05-16 |
| [S-SC06-L11 Tourist tax lines](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l11-tourist-tax-lines.md) | Restaurant and hospitality | All | UC-SC06-12 |
| [S-SC06-L12 Meal voucher payments](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l12-meal-voucher-payments.md) | Restaurant and hospitality | All | UC-SC06-13 |
| [S-SC07-L05 Consignment notes](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l05-consignment-notes.md) | Transport and logistics | All | UC-SC07-24 |
| [S-SC07-L10 Fuel and toll lines](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l10-fuel-and-toll-lines.md) | Transport and logistics | All | UC-SC07-10 |
| [S-SC07-L13 Transport invoice lines](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l13-transport-invoice-lines.md) | Transport and logistics | All | UC-SC07-13, UC-SC07-17, UC-SC07-15 |
| [S-SC07-L14 Client stocks](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l14-client-stocks.md) | Transport and logistics | All | UC-SC07-15 |
| [S-SC07-L17 Transport CO2 statements](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l17-transport-co2-statements.md) | Transport and logistics | All | UC-SC07-17 |
| [S-SC07-L21 Shipment files](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l21-shipment-files.md) | Transport and logistics | All | UC-SC07-24 |
| [S-SC09-L05 Care sheets](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l05-care-sheets.md) | Health practices | Open: Signed, Sent | UC-SC09-18 |
| [S-SC09-L06 Insurer returns](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l06-insurer-returns.md) | Health practices | All | UC-SC09-15 |
| [S-SC09-L10 Shared costs](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l10-shared-costs.md) | Health practices | All | UC-SC09-13, UC-SC09-15 |
| [S-SC09-L12 Locum agreements](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l12-locum-agreements.md) | Health practices | All | UC-SC09-16 |
| [S-SC10-L05 Client funds](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l05-client-funds.md) | Real estate | All | UC-SC10-05 |
| [S-SC10-L06 Fee scales](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l06-fee-scales.md) | Real estate | All | UC-SC10-06 |
| [S-SC10-L11 Landlord statements](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l11-landlord-statements.md) | Real estate | All | UC-SC10-12 |
| [S-SC10-L16 Co-ownerships](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l16-co-ownerships.md) | Real estate | All | UC-SC10-18 |
| [S-SC11-L07 Fee bills](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l07-fee-bills.md) | Professional firms | All | UC-SC11-19 |
| [S-SC11-L08 Trust movements](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l08-trust-movements.md) | Professional firms | All | UC-SC11-07 |
| [S-SC11-L14 Partner shares](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l14-partner-shares.md) | Professional firms | All | UC-SC11-19 |
| [S-SC12-L05 Training fundings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l05-training-fundings.md) | Education and training | All | UC-SC12-04 |
| [S-SC12-L10 Training invoices](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l10-training-invoices.md) | Education and training | All | UC-SC12-10 |
| [S-SC12-L13 Yearly training reports](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l13-yearly-training-reports.md) | Education and training | All | UC-SC12-13 |
| [S-SC12-L14 Students](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l14-students.md) | Education and training | All | UC-SC12-15 |
| [S-SC12-L18 School fees](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l18-school-fees.md) | Education and training | All | UC-SC12-19 |
| [S-SC13-L01 Plots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l01-plots.md) | Agriculture and food | All | UC-SC13-07 |
| [S-SC13-L02 Crop plans](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l02-crop-plans.md) | Agriculture and food | All | UC-SC13-18 |
| [S-SC13-L05 Animals](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l05-animals.md) | Agriculture and food | All | UC-SC13-07 |
| [S-SC13-L07 Machines](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l07-machines.md) | Agriculture and food | All | UC-SC13-18 |
| [S-SC13-L08 Seasonal contracts](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l08-seasonal-contracts.md) | Agriculture and food | All | UC-SC13-19 |
| [S-SC13-L10 Cooperative statements](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l10-cooperative-statements.md) | Agriculture and food | All | UC-SC13-11 |
| [S-SC13-L16 CAP aid declarations](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l16-cap-aid-declarations.md) | Agriculture and food | All | UC-SC13-07 |
| [S-SC14-L01 Software subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l01-software-subscriptions.md) | IT and software | Open: Trial, Active | UC-SC14-01 |
| [S-SC14-L02 Customer usage records](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l02-customer-usage-records.md) | IT and software | All | UC-SC14-02, UC-SC14-15 |
| [S-SC14-L14 Dunning cases](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l14-dunning-cases.md) | IT and software | All | UC-SC14-16 |
| [S-SC14-L15 Partner deals](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l15-partner-deals.md) | IT and software | All | UC-SC14-19 |
| [S-SC14-L18 Licence subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l18-licence-subscriptions.md) | IT and software | All | UC-SC14-23 |
| [S-SC14-L19 R&D projects](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l19-r-d-projects.md) | IT and software | All | UC-SC14-24 |
| [S-SC15-L02 Rebate rules](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l02-rebate-rules.md) | Wholesale and distribution | All | UC-SC15-02 |
| [S-SC15-L09 Import files](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l09-import-files.md) | Wholesale and distribution | All | UC-SC15-12 |
| [S-SC15-L10 Statistics returns](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l10-statistics-returns.md) | Wholesale and distribution | All | UC-SC15-13 |
| [S-SC16-L06 Performer declarations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l06-performer-declarations.md) | Events and culture | All | UC-SC16-04 |
| [S-SC16-L07 Ticket orders](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l07-ticket-orders.md) | Events and culture | Open: Refunded, Exchanged | UC-SC16-17 |
| [S-SC16-L15 Show declarations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l15-show-declarations.md) | Events and culture | All | UC-SC16-14, UC-SC16-15 |
| [S-SC16-L18 Ticket refunds](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l18-ticket-refunds.md) | Events and culture | All | UC-SC16-17 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[Education and training](../../../08-sectors/sc12-education-and-training/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[Feature factory (hosted edition)](../../../02-functional/f19-feature-factory/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Home care](../../../08-sectors/sc04-home-care/screens/00-lists/README.md),
[Hosted support assistant (hosted edition)](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Professional firms](../../../08-sectors/sc11-professional-firms/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Real estate](../../../08-sectors/sc10-real-estate/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[Unified platform cost management](../../../02-functional/f22-unified-cost-management/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U05 | desktop | ![Workspace, U05, light](mockups/workspace-desktop-light.png) | ![Workspace, U05, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U05 | phone | ![Workspace, U05, light](mockups/workspace-phone-light.png) | ![Workspace, U05, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
