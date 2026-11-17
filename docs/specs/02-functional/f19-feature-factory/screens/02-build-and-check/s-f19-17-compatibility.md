🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-02 Build and check](README.md) › 🖥️ S-F19-17 Compatibility

# 🖥️ S-F19-17 Compatibility

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Keep features working across upgrades.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-02 step 4, U48 | desktop | ![FL-F19-02 step 4, U48, light](../../images/02-build-and-check/u48-hosting-engineer/4-upgrades-desktop-light.png) | ![FL-F19-02 step 4, U48, dark](../../images/02-build-and-check/u48-hosting-engineer/4-upgrades-desktop-dark.png) |
| FL-F19-02 step 4, U48 | phone | ![FL-F19-02 step 4, U48, light](../../images/02-build-and-check/u48-hosting-engineer/4-upgrades-phone-light.png) | ![FL-F19-02 step 4, U48, dark](../../images/02-build-and-check/u48-hosting-engineer/4-upgrades-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-17-compatibility-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-17-compatibility-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-17-compatibility-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-17-compatibility-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-17-compatibility-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-17-compatibility-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-17-compatibility-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-17-compatibility-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: features with their test results on the next version.
- Empty: "No feature to test".
- Loading: the frame and titles show at once with placeholder rows for the results; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: results are read-only.
- Offline: not available offline: tests run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-05 Feature check report](../../data/e-f19-05-feature-check-report.md),
[E-F19-04 Generated plugin version](../../data/e-f19-04-generated-plugin-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-05 Feature check report | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U48 | `u48-hosting-engineer/s-f19-17-compatibility-e-f19-05-feature-check-report-recorded-{desktop,phone}-{light,dark}.png` |
| E-F19-04 Generated plugin version | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U48 | `u48-hosting-engineer/s-f19-17-compatibility-e-f19-04-generated-plugin-version-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-02 Build and check](../../flows/fl-f19-02-build-and-check.md)

## Open questions

None.

---

⬅️ [S-F19-16 Invoices](../05-bill-and-credit/s-f19-16-invoices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-18 Withdrawal](../04-promote/s-f19-18-withdrawal.md)
