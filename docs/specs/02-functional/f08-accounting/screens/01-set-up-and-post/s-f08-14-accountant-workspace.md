🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-01 Set up and post](README.md) ›
🖥️ S-F8-14 Accountant workspace

# 🖥️ S-F8-14 Accountant workspace

**Status:** ✅ specified

## Personas

- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Work with the external accountant.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-01 step 3, U08 | desktop | ![FL-F8-01 step 3, U08, light](../../images/01-set-up-and-post/u08-external-accountant/3-accountant-workspace-desktop-light.png) | ![FL-F8-01 step 3, U08, dark](../../images/01-set-up-and-post/u08-external-accountant/3-accountant-workspace-desktop-dark.png) |
| Error E1, U08 | desktop | ![Error E1, U08, light](../../images/10-accountant-collaboration/u08-external-accountant/e1-accountant-workspace-refused-desktop-light.png) | ![Error E1, U08, dark](../../images/10-accountant-collaboration/u08-external-accountant/e1-accountant-workspace-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-14-accountant-workspace-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-14-accountant-workspace-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-14-accountant-workspace-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-14-accountant-workspace-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-14-accountant-workspace-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-14-accountant-workspace-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-14-accountant-workspace-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-14-accountant-workspace-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Work with the external accountant, as the wireframe shows.
- Empty: No question or document request yet for the period, with Ask the accountant.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-02 Journal](../../data/e-f08-02-journal.md),
[E-F8-03 Journal entry](../../data/e-f08-03-journal-entry.md),
[E-F8-26 Accountant request](../../data/e-f08-26-accountant-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-02 Journal | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05, U08 | `u05-accounting/s-f08-14-accountant-workspace-e-f08-02-journal-recorded-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-02-journal-recorded-desktop-{light,dark}.png` |
| E-F8-03 Journal entry | Draft | Badge "Draft"; a new record starts here; next: Posted (UC-F8-02); fields editable within the role | U01, U05, U08 | `u01-employee/s-f08-14-accountant-workspace-e-f08-03-journal-entry-draft-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-14-accountant-workspace-e-f08-03-journal-entry-draft-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-03-journal-entry-draft-desktop-{light,dark}.png` |
| E-F8-03 Journal entry | Reversed | Badge "Reversed"; final: read-only, no next state; the history shows how it got here | U01, U05, U08 | `u01-employee/s-f08-14-accountant-workspace-e-f08-03-journal-entry-reversed-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-14-accountant-workspace-e-f08-03-journal-entry-reversed-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-03-journal-entry-reversed-desktop-{light,dark}.png` |
| E-F8-26 Accountant request | Open | Badge "Open"; a new record starts here; next: Answered (UC-F8-29); fields editable within the role | U01, U05, U08 | `u01-employee/s-f08-14-accountant-workspace-e-f08-26-accountant-request-open-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-14-accountant-workspace-e-f08-26-accountant-request-open-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-26-accountant-request-open-desktop-{light,dark}.png` |
| E-F8-26 Accountant request | Answered | Badge "Answered"; next: Closed (UC-F8-29); fields editable within the role | U01, U05, U08 | `u01-employee/s-f08-14-accountant-workspace-e-f08-26-accountant-request-answered-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-14-accountant-workspace-e-f08-26-accountant-request-answered-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-26-accountant-request-answered-desktop-{light,dark}.png` |
| E-F8-26 Accountant request | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U05, U08 | `u05-accounting/s-f08-14-accountant-workspace-e-f08-26-accountant-request-closed-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-26-accountant-request-closed-desktop-{light,dark}.png` |
| E-F8-03 Journal entry | Posted | Badge "Posted"; next: Reversed (UC-F8-02); fields editable within the role | U01, U05, U08 | `u01-employee/s-f08-14-accountant-workspace-e-f08-03-journal-entry-posted-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-f08-14-accountant-workspace-e-f08-03-journal-entry-posted-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-14-accountant-workspace-e-f08-03-journal-entry-posted-desktop-{light,dark}.png` |

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

- [FL-F8-01 Set up and post](../../flows/fl-f08-01-set-up-and-post.md)
- [FL-F8-10 Accountant collaboration](../../flows/fl-f08-10-accountant-collaboration.md)

## Open questions

None.

---

⬅️ [S-F8-13 Consolidation](../05-close-report-and-consolidate/s-f08-13-consolidation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-15 Books](../06-benchmark-additions/s-f08-15-books.md)
