🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-05 Keep the catalogue](README.md) › 🖥️ S-F24-18 Yearly review

# 🖥️ S-F24-18 Yearly review

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Review the list of 50 every year.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-05 step 1, U47 | desktop | ![FL-F24-05 step 1, U47, light](../../images/05-keep-the-catalogue/u47-simple-erp-maintainer/1-review-desktop-light.png) | ![FL-F24-05 step 1, U47, dark](../../images/05-keep-the-catalogue/u47-simple-erp-maintainer/1-review-desktop-dark.png) |
| FL-F24-05 step 1, U47 | phone | ![FL-F24-05 step 1, U47, light](../../images/05-keep-the-catalogue/u47-simple-erp-maintainer/1-review-phone-light.png) | ![FL-F24-05 step 1, U47, dark](../../images/05-keep-the-catalogue/u47-simple-erp-maintainer/1-review-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-18-yearly-review-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-18-yearly-review-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-18-yearly-review-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-18-yearly-review-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-18-yearly-review-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-18-yearly-review-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-18-yearly-review-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-18-yearly-review-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the list with market data and proposals.
- Empty: never empty.
- Loading: the frame and titles show at once with placeholder rows for the list; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the published list is read-only.
- Offline: not available offline: the review is online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F24-15 Connector catalogue review](../../data/e-f24-15-connector-catalogue-review.md),
[E-F24-01 Connector](../../data/e-f24-01-connector.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-15 Connector catalogue review | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f24-18-yearly-review-e-f24-15-connector-catalogue-review-active-{desktop,phone}-{light,dark}.png` |
| E-F24-01 Connector | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f24-18-yearly-review-e-f24-01-connector-active-{desktop,phone}-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F24-05 Keep the catalogue](../../flows/fl-f24-05-keep-the-catalogue.md)

## Open questions

None.

---

⬅️ [S-F24-17 Disconnect](../04-run-and-control/s-f24-17-disconnect.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-19 Requests](s-f24-19-requests.md)
