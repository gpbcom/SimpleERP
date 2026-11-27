🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-03 Try, install and maintain](README.md) › 🖥️ S-F19-23 Ownership

# 🖥️ S-F19-23 Ownership

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Show a feature's licence and versions and hand over its source and data export.

## Entry points

The feature's page, Ownership; cancellation.

## Wireframe

```text
Gate booking, ownership             Licence: AGPL-3.0
-------------------------------------------------------------------------------
Version 1.2 signed 2026-12-09     [Download source]
Data export (after cancellation)  [Download]
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-03 step 6, U13 | desktop | ![FL-F19-03 step 6, U13, light](../../images/03-try-install-and-maintain/u13-owner/6-ownership-desktop-light.png) | ![FL-F19-03 step 6, U13, dark](../../images/03-try-install-and-maintain/u13-owner/6-ownership-desktop-dark.png) |
| FL-F19-03 step 6, U13 | phone | ![FL-F19-03 step 6, U13, light](../../images/03-try-install-and-maintain/u13-owner/6-ownership-phone-light.png) | ![FL-F19-03 step 6, U13, dark](../../images/03-try-install-and-maintain/u13-owner/6-ownership-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-23-ownership-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-23-ownership-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-23-ownership-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-23-ownership-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-23-ownership-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-23-ownership-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-23-ownership-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-23-ownership-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Licence | E-F19-13 licence | text | no | yes |
| Version | E-F19-13 version | text | no | yes |
| Source archive | E-F19-13 source archive | file | no | yes |
| Data export | E-F19-13 data export | file | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Download source | row | owner | archive given |
| Download export | row | owner | export given |

## States

- Normal: licence, versions and downloads.
- Empty: "Not signed yet": the source comes with the first signed version.
- Loading: the frame and titles show at once with placeholder rows for the versions; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a download that fails, retried.
- Read-only: administrators read.
- Offline: not available offline: downloads need the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-13 Code handover](../../data/e-f19-13-code-handover.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-13 Code handover | Available | Badge "Available"; a new record starts here; next: Downloaded (UC-F19-23); fields editable within the role | U13 | `u13-owner/s-f19-23-ownership-e-f19-13-code-handover-available-{desktop,phone}-{light,dark}.png` |
| E-F19-13 Code handover | Downloaded | Badge "Downloaded"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-23-ownership-e-f19-13-code-handover-downloaded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F19-03 Try, install and maintain](../../flows/fl-f19-03-try-install-and-maintain.md)

## Open questions

None.

---

⬅️ [S-F19-22 Refunds](../06-delivery-and-refunds/s-f19-22-refunds.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-24 Security and privacy](../02-build-and-check/s-f19-24-security-and-privacy.md)
