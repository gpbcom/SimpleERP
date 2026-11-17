🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-05 Run the site](README.md) › 🖥️ S-F18-18 Audience

# 🖥️ S-F18-18 Audience

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Measure audience and search ranking.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-05 step 1, U12 | desktop | ![FL-F18-05 step 1, U12, light](../../images/05-run-the-site/u12-marketing/1-audience-desktop-light.png) | ![FL-F18-05 step 1, U12, dark](../../images/05-run-the-site/u12-marketing/1-audience-desktop-dark.png) |
| FL-F18-05 step 1, U12 | phone | ![FL-F18-05 step 1, U12, light](../../images/05-run-the-site/u12-marketing/1-audience-phone-light.png) | ![FL-F18-05 step 1, U12, dark](../../images/05-run-the-site/u12-marketing/1-audience-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-18-audience-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-18-audience-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-18-audience-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-18-audience-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-18-audience-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-18-audience-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-18-audience-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-18-audience-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: visits, top pages, search ranking and advice, within consent.
- Empty: "No visit measured yet".
- Loading: the frame and titles show at once with placeholder rows for the figures; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: Figures last loaded stay visible with their date. Nothing else is queued: D38 keeps only today's schedule,
  time and intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F18-11 Audience figure](../../data/e-f18-11-audience-figure.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-11 Audience figure | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U12 | `u12-marketing/s-f18-18-audience-e-f18-11-audience-figure-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F18-05 Run the site](../../flows/fl-f18-05-run-the-site.md)

## Open questions

None.

---

⬅️ [S-F18-17 Languages](../01-build-the-site/s-f18-17-languages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-19 Shop link](../01-build-the-site/s-f18-19-shop-link.md)
