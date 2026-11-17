🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-05 Duties and records](README.md) › 🖥️ S-F15-09 Company records

# 🖥️ S-F15-09 Company records

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md), who holds and signs decisions
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md), who prepares accounts and filings

## Purpose

Prepare and keep the company's decisions, register and filings, and its beneficial-owner declaration.

## Entry points

Legal menu, Company records; the "approve the accounts" duty.

## Wireframe

```text
Company records                       Legal form: SAS, sole shareholder
-------------------------------------------------------------------------------
Register   Date         Body               Subject                       State
14         2027-06-20   sole shareholder   approval of the 2026 accounts registered
13         2026-06-18   sole shareholder   approval of the 2025 accounts registered
-------------------------------------------------------------------------------
Beneficial owners: 2 declared, last update 2026-02-01        [Declare a change]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-05 step 3, U13 | desktop | ![FL-F15-05 step 3, U13, light](../../images/05-duties-and-records/u13-owner/3-company-records-desktop-light.png) | ![FL-F15-05 step 3, U13, dark](../../images/05-duties-and-records/u13-owner/3-company-records-desktop-dark.png) |
| FL-F15-05 step 3, U13 | phone | ![FL-F15-05 step 3, U13, light](../../images/05-duties-and-records/u13-owner/3-company-records-phone-light.png) | ![FL-F15-05 step 3, U13, dark](../../images/05-duties-and-records/u13-owner/3-company-records-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-09-company-records-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-09-company-records-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-09-company-records-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-09-company-records-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-09-company-records-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-09-company-records-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-09-company-records-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-09-company-records-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Register number | E-F15-07 register number | number | no | yes |
| Date | E-F15-07 date | date | yes | yes |
| Body | E-F15-07 body | list | yes | yes |
| Resolutions | E-F15-07 resolutions | text | yes | yes |
| Minutes | E-F15-07 minutes | signed PDF | yes | yes |
| Filings | E-F15-07 filings | list | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Prepare a decision | header | external accountant, owner | draft with resolutions |
| Attach signed minutes | decision | owner | decision numbered in the register |
| Record a filing | decision | external accountant | receipt attached, duty done |
| Declare a change | beneficial owners | owner | declaration duty created |

## States

- Normal: the register of decisions, the filings and the beneficial owners.
- Empty: "No decision recorded yet": shown for a new company, with the first duties from the calendar.
- Loading: the frame and titles show at once with placeholder rows for the decisions; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: minutes not signed, the decision not numbered.
- Read-only: accounting reads; a registered decision is read-only.
- Offline: not available offline: records are kept on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-05 Compliance duty](../../data/e-f15-05-compliance-duty.md),
[E-F15-07 Corporate decision](../../data/e-f15-07-corporate-decision.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-05 Compliance duty | Planned | Badge "Planned"; a new record starts here; next: Done or Overdue (UC-F15-07); fields editable within the role | U08, U13 | `u08-external-accountant/s-f15-09-company-records-e-f15-05-compliance-duty-planned-desktop-{light,dark}.png`, `u13-owner/s-f15-09-company-records-e-f15-05-compliance-duty-planned-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U08, U13 | `u08-external-accountant/s-f15-09-company-records-e-f15-05-compliance-duty-done-desktop-{light,dark}.png`, `u13-owner/s-f15-09-company-records-e-f15-05-compliance-duty-done-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Overdue | Badge "Overdue"; next: Done (UC-F15-07); fields editable within the role | U08, U13 | `u08-external-accountant/s-f15-09-company-records-e-f15-05-compliance-duty-overdue-desktop-{light,dark}.png`, `u13-owner/s-f15-09-company-records-e-f15-05-compliance-duty-overdue-{desktop,phone}-{light,dark}.png` |
| E-F15-07 Corporate decision | Prepared | Badge "Prepared"; a new record starts here; next: Held (UC-F15-09); fields editable within the role | U08, U13 | `u08-external-accountant/s-f15-09-company-records-e-f15-07-corporate-decision-prepared-desktop-{light,dark}.png`, `u13-owner/s-f15-09-company-records-e-f15-07-corporate-decision-prepared-{desktop,phone}-{light,dark}.png` |
| E-F15-07 Corporate decision | Held | Badge "Held"; next: Registered (UC-F15-09); fields editable within the role | U13 | `u13-owner/s-f15-09-company-records-e-f15-07-corporate-decision-held-{desktop,phone}-{light,dark}.png` |
| E-F15-07 Corporate decision | Registered | Badge "Registered"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f15-09-company-records-e-f15-07-corporate-decision-registered-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-05 Duties and records](../../flows/fl-f15-05-duties-and-records.md)

## Open questions

None.

---

⬅️ [S-F15-08 Contracts](s-f15-08-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-10 Privacy and AI register](../06-privacy-and-ai-duties/s-f15-10-privacy-and-ai-register.md)
