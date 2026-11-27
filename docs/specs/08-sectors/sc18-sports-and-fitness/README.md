🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🏋️ SC18 Sports and fitness

# 🏋️ SC18 Sports and fitness

**Status:** ✅ specified

Interviewed on 2026-11-14 as a new sector: D562 (the owner's answers of 2026-11-14: G15 and the sector interview G193
and G194).

## Summary

What sports clubs, gyms, studios and leisure centres add: memberships with dues by direct debit and door access, classes
with waiting lists and coach planning, federation licences, medical certificates, teams and competitions, personal
training, and the four areas the owner added (courts and facilities, tournaments and events, holiday camps, equipment
rental). ([D562](../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md))

## Profile

Associative sports clubs and commercial gyms, fitness and yoga studios, tennis and padel clubs and leisure centres, from
one section to a multi-site club. Both organisations are covered: the association with its licences and competitions,
and the gym with its contracts and access (D562).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U53 Coach](../../01-users/personas/u53-coach.md),
[U31 Treasurer](../../01-users/personas/u31-treasurer.md), [U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F4 Meetings](../../02-functional/f04-meetings/README.md): appointments and calendars.
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md): events and ticketing for tournaments,
  consent and customer messages.
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): customers, subscriptions, invoices
  and dues.
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): equipment, rental items and orders.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): direct debits, deposits and the books.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): coaches, shifts and qualifications.
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md): the till of the club shop and the bar.
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): coaches' pay inputs.

## Technical capabilities used

- [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)
- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (the sector pack)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (the AI assistant)
- [T8 RAG platform](../../03-technical/t08-rag-platform/README.md)
- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md)
- [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack's rules)

## Use cases

- [UC-SC18-01](use-cases/01-memberships-and-access/uc-sc18-01-sell-a-membership.md)
- [UC-SC18-02](use-cases/01-memberships-and-access/uc-sc18-02-collect-dues-by-direct-debit.md)
- [UC-SC18-03](use-cases/01-memberships-and-access/uc-sc18-03-control-access-at-the-door.md)
- [UC-SC18-04](use-cases/01-memberships-and-access/uc-sc18-04-freeze-or-cancel-a-membership.md)
- [UC-SC18-05](use-cases/02-classes-and-waiting-lists/uc-sc18-05-publish-the-class-timetable.md)
- [UC-SC18-06 Book a class](use-cases/02-classes-and-waiting-lists/uc-sc18-06-book-a-class.md)
- [UC-SC18-07](use-cases/02-classes-and-waiting-lists/uc-sc18-07-handle-the-waiting-list.md)
- [UC-SC18-08 Plan coaches](use-cases/02-classes-and-waiting-lists/uc-sc18-08-plan-coaches.md)
- [UC-SC18-09](use-cases/03-licences-and-competitions/uc-sc18-09-issue-federation-licences.md)
- [UC-SC18-10](use-cases/03-licences-and-competitions/uc-sc18-10-check-medical-certificates.md)
- [UC-SC18-11](use-cases/03-licences-and-competitions/uc-sc18-11-run-teams-and-competitions.md)
- [UC-SC18-12 Record results](use-cases/03-licences-and-competitions/uc-sc18-12-record-results.md)
- [UC-SC18-13](use-cases/04-personal-training/uc-sc18-13-sell-coaching-packages.md)
- [UC-SC18-14](use-cases/04-personal-training/uc-sc18-14-plan-a-training-programme.md)
- [UC-SC18-15 Follow progress](use-cases/04-personal-training/uc-sc18-15-follow-progress.md)
- [UC-SC18-16](use-cases/04-personal-training/uc-sc18-16-ask-the-assistant-about-the-club.md)
- [UC-SC18-17](use-cases/05-facilities-events-camps-and-rentals/uc-sc18-17-book-courts-and-facilities.md)
- [UC-SC18-18](use-cases/05-facilities-events-camps-and-rentals/uc-sc18-18-run-tournaments-and-events.md)
- [UC-SC18-19](use-cases/05-facilities-events-camps-and-rentals/uc-sc18-19-run-holiday-camps.md)
- [UC-SC18-20](use-cases/05-facilities-events-camps-and-rentals/uc-sc18-20-rent-out-equipment.md)

## Contents

|  | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | 🔄 |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | 🔄 |
| 🎁 |  | [Sector pack](sector-pack.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Beauty and wellness](../sc17-beauty-and-wellness/README.md) · ⬆️ [Up](../README.md)
