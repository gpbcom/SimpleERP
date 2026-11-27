🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-05 Duties and records](README.md) › 🖥️ S-F15-08 Contracts

# 🖥️ S-F15-08 Contracts

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md), who decides renewals
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md), who records contracts

## Purpose

Keep the company's contracts with their terms, renewal kinds and last notice days.

## Entry points

Legal menu, Contracts; a partner's page; the "last notice day" reminder.

## Wireframe

```text
Contracts                                       [Add contract] [Import CSV]
-------------------------------------------------------------------------------
Contract                       Party          Ends         Last notice   Renewal
Kitchen maintenance            Froid Service  2026-12-31   2026-09-30    tacit
Premises lease (3-6-9)         SCI Port       2031-03-31   2028-09-30    term
Fleet insurance                Assur A        2027-01-01   notice unknown
-------------------------------------------------------------------------------
[Contract panel] document, term, notice, [Give notice] [Renew]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-05 step 2, U13 | desktop | ![FL-F15-05 step 2, U13, light](../../images/05-duties-and-records/u13-owner/2-contracts-desktop-light.png) | ![FL-F15-05 step 2, U13, dark](../../images/05-duties-and-records/u13-owner/2-contracts-desktop-dark.png) |
| FL-F15-05 step 2, U13 | phone | ![FL-F15-05 step 2, U13, light](../../images/05-duties-and-records/u13-owner/2-contracts-phone-light.png) | ![FL-F15-05 step 2, U13, dark](../../images/05-duties-and-records/u13-owner/2-contracts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-08-contracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-08-contracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-08-contracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-08-contracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-08-contracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-08-contracts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-08-contracts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-08-contracts-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contract, party | E-F15-06 title, party | text, link | yes | yes |
| Kind | E-F15-06 kind | list | yes | yes |
| Term end | E-F15-06 term end | date | yes | yes |
| Renewal | E-F15-06 renewal | tacit, explicit, none | yes | yes |
| Notice period | E-F15-06 notice period | duration | yes | no |
| Last notice day | E-F15-06 last notice day | date | no (computed) | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Add contract | header | owner, purchasing | document read, dates proposed |
| Give notice | contract panel | owner | letter attached, contract ends at its term |
| Renew | contract panel | owner | new term recorded |
| Import CSV | header | owner, purchasing | existing contracts loaded |

## States

- Normal: contracts sorted by last notice day with their renewal kind.
- Empty: "No contract recorded": invites to add one or import a list.
- Loading: the frame and titles show at once with placeholder rows for the contracts; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an unreadable document (fields entered by hand), or a notice period missing ("notice unknown").
- Read-only: accounting reads; ended contracts are read-only.
- Offline: not available offline: contract documents are read and stored on the server. D38 keeps only today's schedule,
  time and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every
  action is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-06 Contract record](../../data/e-f15-06-contract-record.md),
[E-F15-05 Compliance duty](../../data/e-f15-05-compliance-duty.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-06 Contract record | Active | Badge "Active"; a new record starts here; next: Notice given or Renewed (UC-F15-08); fields editable within the role | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-06-contract-record-active-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-06-contract-record-active-{desktop,phone}-{light,dark}.png` |
| E-F15-06 Contract record | Notice given | Badge "Notice given"; next: Ended (UC-F15-08); fields editable within the role | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-06-contract-record-notice-given-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-06-contract-record-notice-given-{desktop,phone}-{light,dark}.png` |
| E-F15-06 Contract record | Renewed | Badge "Renewed"; next: Active (BR-F15-12); fields editable within the role | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-06-contract-record-renewed-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-06-contract-record-renewed-{desktop,phone}-{light,dark}.png` |
| E-F15-06 Contract record | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-06-contract-record-ended-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-06-contract-record-ended-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Planned | Badge "Planned"; a new record starts here; next: Done or Overdue (UC-F15-07); fields editable within the role | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-05-compliance-duty-planned-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-05-compliance-duty-planned-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-05-compliance-duty-done-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-05-compliance-duty-done-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Overdue | Badge "Overdue"; next: Done (UC-F15-07); fields editable within the role | U04, U13 | `u04-purchasing/s-f15-08-contracts-e-f15-05-compliance-duty-overdue-desktop-{light,dark}.png`, `u13-owner/s-f15-08-contracts-e-f15-05-compliance-duty-overdue-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the owner answers reminders on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-05 Duties and records](../../flows/fl-f15-05-duties-and-records.md)

## Open questions

None.

---

⬅️ [S-F15-07 Compliance calendar](s-f15-07-compliance-calendar.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-09 Company records](s-f15-09-company-records.md)
