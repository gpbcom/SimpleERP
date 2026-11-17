🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-05 Duties and records](README.md) › 🖥️ S-F15-07 Compliance calendar

# 🖥️ S-F15-07 Compliance calendar

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md), who assigns and reviews
- [U06 Human resources](../../../../01-users/personas/u06-hr.md), who sees and completes the HR duties
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md), who sees and completes the tax and accounting
  duties

## Purpose

Show the company's dated legal duties with their owners, due dates, sources and proofs.

## Entry points

The owner's home card "Legal duties"; reminders; Legal menu, Calendar.

## Wireframe

```text
Compliance calendar      [Month] [List]   Filter: owner, family    3 due, 1 overdue
-------------------------------------------------------------------------------
Due          Duty                                   Owner        Status
2027-01-31   Update the single risk assessment     HR           planned
2026-11-30   Display the working hours             HR           overdue
2027-06-30   Approve the 2026 accounts             Owner        planned
-------------------------------------------------------------------------------
[Duty panel] source CR-FR-076, owner, proof, [Mark done] [Ask the assistant]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-05 step 1, U13 | desktop | ![FL-F15-05 step 1, U13, light](../../images/05-duties-and-records/u13-owner/1-compliance-calendar-desktop-light.png) | ![FL-F15-05 step 1, U13, dark](../../images/05-duties-and-records/u13-owner/1-compliance-calendar-desktop-dark.png) |
| FL-F15-05 step 1, U13 | phone | ![FL-F15-05 step 1, U13, light](../../images/05-duties-and-records/u13-owner/1-compliance-calendar-phone-light.png) | ![FL-F15-05 step 1, U13, dark](../../images/05-duties-and-records/u13-owner/1-compliance-calendar-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/05-duties-and-records/u13-owner/e1-compliance-calendar-refused-desktop-light.png) | ![Error E1, U13, dark](../../images/05-duties-and-records/u13-owner/e1-compliance-calendar-refused-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/05-duties-and-records/u13-owner/e1-compliance-calendar-refused-phone-light.png) | ![Error E1, U13, dark](../../images/05-duties-and-records/u13-owner/e1-compliance-calendar-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-07-compliance-calendar-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-07-compliance-calendar-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-07-compliance-calendar-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-07-compliance-calendar-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-07-compliance-calendar-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-07-compliance-calendar-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-07-compliance-calendar-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-07-compliance-calendar-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Duty | E-F15-05 title | text | no | yes |
| Source | E-F15-05 source | rule or article link | no | yes |
| Due date | E-F15-05 due date | date | yes (owner) | yes |
| Owner | E-F15-05 owner | user | yes (owner) | yes |
| Status | E-F15-05 status | planned, done, overdue | no | yes |
| Proof | E-F15-05 proof | file | yes | to mark done |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Assign | duty panel | owner | owner set and told |
| Mark done | duty panel | owner of the duty | done with proof, next occurrence planned |
| Ask the AI assistant | duty panel | any viewer | answer citing the source |
| Export | header | owner | iCalendar or CSV |

## States

- Normal: a month or list view of duties with status colours and text, filters by owner and family.
- Empty: "No duty generated yet": shown until the law pack is installed and the company's size and sector are set, with
  links to them.
- Loading: the frame and titles show at once with placeholder rows for the duties; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a duty marked done without proof, refused; a site with no law pack, listed as not covered.
- Read-only: HR, accounting and the external accountant see and complete their own duties; only the owner assigns.
- Offline: The owner's phone shows the duties last loaded with their date; marking done needs the network. Nothing else
  is queued: D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is
  lost and the actions come back with it.

Shown entities (VD-15): [E-F15-01 Law pack](../../data/e-f15-01-law-pack.md),
[E-F15-05 Compliance duty](../../data/e-f15-05-compliance-duty.md),
[E-F15-14 Corporate filing](../../data/e-f15-14-corporate-filing.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-01 Law pack | Scheduled | Badge "Scheduled"; a new record starts here; no other state; fields editable within the role | U05, U06, U13 | `u05-accounting/s-f15-07-compliance-calendar-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u06-hr/s-f15-07-compliance-calendar-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png`, `u13-owner/s-f15-07-compliance-calendar-e-f15-01-law-pack-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Planned | Badge "Planned"; a new record starts here; next: Done or Overdue (UC-F15-07); fields editable within the role | U05, U06, U13 | `u05-accounting/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-planned-desktop-{light,dark}.png`, `u06-hr/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-planned-desktop-{light,dark}.png`, `u13-owner/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-planned-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U05, U06, U13 | `u05-accounting/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-done-desktop-{light,dark}.png`, `u06-hr/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-done-desktop-{light,dark}.png`, `u13-owner/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-done-{desktop,phone}-{light,dark}.png` |
| E-F15-05 Compliance duty | Overdue | Badge "Overdue"; next: Done (UC-F15-07); fields editable within the role | U05, U06, U13 | `u05-accounting/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-overdue-desktop-{light,dark}.png`, `u06-hr/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-overdue-desktop-{light,dark}.png`, `u13-owner/s-f15-07-compliance-calendar-e-f15-05-compliance-duty-overdue-{desktop,phone}-{light,dark}.png` |
| E-F15-14 Corporate filing | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U06, U13 | `u05-accounting/s-f15-07-compliance-calendar-e-f15-14-corporate-filing-active-desktop-{light,dark}.png`, `u06-hr/s-f15-07-compliance-calendar-e-f15-14-corporate-filing-active-desktop-{light,dark}.png`, `u13-owner/s-f15-07-compliance-calendar-e-f15-14-corporate-filing-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the owner reads and marks done on a phone (D34).

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-05 Duties and records](../../flows/fl-f15-05-duties-and-records.md)

## Open questions

None.

---

⬅️ [S-F15-06 Standards register](../04-set-up-the-legal-assistant/s-f15-06-standards-register.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-08 Contracts](s-f15-08-contracts.md)
