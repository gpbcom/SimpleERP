🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F14-03 Publish](README.md) ›
🖥️ S-F14-11 Releases

# 🖥️ S-F14-11 Releases

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md)

## Purpose

Publish versions and release notes.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-03 step 4, U46 | desktop | ![FL-F14-03 step 4, U46, light](../../images/03-publish/u46-plugin-publisher/4-release-desktop-light.png) | ![FL-F14-03 step 4, U46, dark](../../images/03-publish/u46-plugin-publisher/4-release-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-11-releases-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-11-releases-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-11-releases-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-11-releases-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-11-releases-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-11-releases-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-11-releases-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-11-releases-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: versions with their notes, reach and rollout.
- Empty: "No release yet".
- Loading: the frame and titles show at once with placeholder rows for the releases; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: published notes are read-only.
- Offline: not available offline: releases are published online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-03 Plugin version](../../data/e-f14-03-plugin-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-03 Plugin version | New | Badge "New"; a new record starts here; next: Submitted (UC-F14-08); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-11-releases-e-f14-03-plugin-version-new-desktop-{light,dark}.png` |
| E-F14-03 Plugin version | Submitted | Badge "Submitted"; next: Published (UC-F14-03); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-11-releases-e-f14-03-plugin-version-submitted-desktop-{light,dark}.png` |
| E-F14-03 Plugin version | Published | Badge "Published"; next: Approved (UC-F14-10); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-11-releases-e-f14-03-plugin-version-published-desktop-{light,dark}.png` |
| E-F14-03 Plugin version | Approved | Badge "Approved"; next: Signed (UC-F14-10); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-11-releases-e-f14-03-plugin-version-approved-desktop-{light,dark}.png` |
| E-F14-03 Plugin version | Running | Badge "Running"; final: read-only, no next state; the history shows how it got here | U46 | `u46-plugin-publisher/s-f14-11-releases-e-f14-03-plugin-version-running-desktop-{light,dark}.png` |

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

- [FL-F14-03 Publish](../../flows/fl-f14-03-publish.md)

## Open questions

None.

---

⬅️ [S-F14-10 Security review](s-f14-10-security-review.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-12 Pricing](../04-money-and-taxes/s-f14-12-pricing.md)
