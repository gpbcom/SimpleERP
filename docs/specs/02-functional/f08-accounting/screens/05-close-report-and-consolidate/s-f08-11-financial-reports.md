🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-05 Close, report and consolidate](README.md) › 🖥️ S-F8-11 Financial reports

# 🖥️ S-F8-11 Financial reports

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Read financial reports.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-05 step 2, U13 | desktop | ![FL-F8-05 step 2, U13, light](../../images/05-close-report-and-consolidate/u13-owner/2-reports-desktop-light.png) | ![FL-F8-05 step 2, U13, dark](../../images/05-close-report-and-consolidate/u13-owner/2-reports-desktop-dark.png) |
| FL-F8-05 step 2, U13 | phone | ![FL-F8-05 step 2, U13, light](../../images/05-close-report-and-consolidate/u13-owner/2-reports-phone-light.png) | ![FL-F8-05 step 2, U13, dark](../../images/05-close-report-and-consolidate/u13-owner/2-reports-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-11-financial-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-11-financial-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-11-financial-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-11-financial-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-11-financial-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-11-financial-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-11-financial-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-11-financial-reports-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Read financial reports, as the wireframe shows.
- Empty: No entry yet for the period, with Change the period.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-03 Journal entry](../../data/e-f08-03-journal-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-03 Journal entry | Draft | Badge "Draft"; a new record starts here; next: Posted (UC-F8-02); fields editable within the role | U05, U08, U13 | `u05-accounting/s-f08-11-financial-reports-e-f08-03-journal-entry-draft-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-11-financial-reports-e-f08-03-journal-entry-draft-desktop-{light,dark}.png`, `u13-owner/s-f08-11-financial-reports-e-f08-03-journal-entry-draft-{desktop,phone}-{light,dark}.png` |
| E-F8-03 Journal entry | Posted | Badge "Posted"; next: Reversed (UC-F8-02); fields editable within the role | U05, U08, U13 | `u05-accounting/s-f08-11-financial-reports-e-f08-03-journal-entry-posted-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-11-financial-reports-e-f08-03-journal-entry-posted-desktop-{light,dark}.png`, `u13-owner/s-f08-11-financial-reports-e-f08-03-journal-entry-posted-{desktop,phone}-{light,dark}.png` |
| E-F8-03 Journal entry | Reversed | Badge "Reversed"; final: read-only, no next state; the history shows how it got here | U05, U08, U13 | `u05-accounting/s-f08-11-financial-reports-e-f08-03-journal-entry-reversed-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-11-financial-reports-e-f08-03-journal-entry-reversed-desktop-{light,dark}.png`, `u13-owner/s-f08-11-financial-reports-e-f08-03-journal-entry-reversed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F8-05 Close, report and consolidate](../../flows/fl-f08-05-close-report-and-consolidate.md)

## Open questions

None.

---

⬅️ [S-F8-10 Closing](s-f08-10-closing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-12 Expenses](../02-purchase-to-pay/s-f08-12-expenses.md)
