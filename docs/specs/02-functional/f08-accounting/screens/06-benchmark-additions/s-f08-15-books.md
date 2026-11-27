🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-06 Benchmark additions](README.md) › 🖥️ S-F8-15 Books

# 🖥️ S-F8-15 Books

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Keep several books.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-06 step 1, U05 | desktop | ![FL-F8-06 step 1, U05, light](../../images/06-benchmark-additions/u05-accounting/1-books-desktop-light.png) | ![FL-F8-06 step 1, U05, dark](../../images/06-benchmark-additions/u05-accounting/1-books-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-15-books-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-15-books-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-15-books-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-15-books-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-15-books-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-15-books-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-15-books-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-15-books-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Keep several books, as the wireframe shows.
- Empty: No second book yet for the period, with Add a book.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-13 Book](../../data/e-f08-13-book.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-13 Book | Closed | Badge "Closed"; a new record starts here; next: Refused (UC-F8-15); fields editable within the role | U05, U08 | `u05-accounting/s-f08-15-books-e-f08-13-book-closed-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-15-books-e-f08-13-book-closed-desktop-{light,dark}.png` |
| E-F8-13 Book | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05, U08 | `u05-accounting/s-f08-15-books-e-f08-13-book-refused-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-15-books-e-f08-13-book-refused-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F8-06 Benchmark additions](../../flows/fl-f08-06-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F8-14 Accountant workspace](../01-set-up-and-post/s-f08-14-accountant-workspace.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-16 Revenue schedules](s-f08-16-revenue-schedules.md)
