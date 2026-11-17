🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-04 Test and publish](README.md) › 🖥️ S-F18-15 Publication

# 🖥️ S-F18-15 Publication

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Approve, publish and roll back.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-04 step 3, U13 | desktop | ![FL-F18-04 step 3, U13, light](../../images/04-test-and-publish/u13-owner/3-publish-desktop-light.png) | ![FL-F18-04 step 3, U13, dark](../../images/04-test-and-publish/u13-owner/3-publish-desktop-dark.png) |
| FL-F18-04 step 3, U13 | phone | ![FL-F18-04 step 3, U13, light](../../images/04-test-and-publish/u13-owner/3-publish-phone-light.png) | ![FL-F18-04 step 3, U13, dark](../../images/04-test-and-publish/u13-owner/3-publish-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-15-publication-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-15-publication-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-15-publication-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-15-publication-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-15-publication-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-15-publication-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-15-publication-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-15-publication-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: versions with the checks' result, publish and roll back.
- Empty: "Not published yet".
- Loading: the frame and titles show at once with placeholder rows for the versions; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: marketing publishes only when granted.
- Offline: not available offline: publication runs online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F18-01 Hosted website](../../data/e-f18-01-hosted-website.md),
[E-F18-10 Publication check report](../../data/e-f18-10-publication-check-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-01 Hosted website | New | Badge "New"; a new record starts here; next: Live (UC-F18-13); fields editable within the role | U13 | `u13-owner/s-f18-15-publication-e-f18-01-hosted-website-new-{desktop,phone}-{light,dark}.png` |
| E-F18-01 Hosted website | Live | Badge "Live"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f18-15-publication-e-f18-01-hosted-website-live-{desktop,phone}-{light,dark}.png` |
| E-F18-10 Publication check report | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f18-15-publication-e-f18-10-publication-check-report-recorded-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F18-14 Checks](s-f18-14-checks.md) · ⬆️ [Up](README.md) · ➡️ [S-F18-16 Editor](s-f18-16-editor.md)
