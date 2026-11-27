🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-04 Test and publish](README.md) › 🖥️ S-F18-14 Checks

# 🖥️ S-F18-14 Checks

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Run the automatic checks.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-04 step 2, U12 | desktop | ![FL-F18-04 step 2, U12, light](../../images/04-test-and-publish/u12-marketing/2-checks-desktop-light.png) | ![FL-F18-04 step 2, U12, dark](../../images/04-test-and-publish/u12-marketing/2-checks-desktop-dark.png) |
| FL-F18-04 step 2, U12 | phone | ![FL-F18-04 step 2, U12, light](../../images/04-test-and-publish/u12-marketing/2-checks-phone-light.png) | ![FL-F18-04 step 2, U12, dark](../../images/04-test-and-publish/u12-marketing/2-checks-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-14-checks-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-14-checks-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-14-checks-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-14-checks-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-14-checks-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-14-checks-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-14-checks-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-14-checks-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: each check with its result and report.
- Empty: "No check run yet".
- Loading: the frame and titles show at once with placeholder rows for the checks; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: reports are read-only.
- Offline: not available offline: checks run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-10 Publication check report](../../data/e-f18-10-publication-check-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-10 Publication check report | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U12, U48 | `u12-marketing/s-f18-14-checks-e-f18-10-publication-check-report-recorded-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f18-14-checks-e-f18-10-publication-check-report-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F18-04 Test and publish](../../flows/fl-f18-04-test-and-publish.md)

## Open questions

None.

---

⬅️ [S-F18-13 Preview](s-f18-13-preview.md) · ⬆️ [Up](README.md) · ➡️ [S-F18-15 Publication](s-f18-15-publication.md)
