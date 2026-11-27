🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-05 Keep the catalogue](README.md) › 🖥️ S-F24-25 Icon library

# 🖥️ S-F24-25 Icon library

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Purpose

Keep each integration's logo with its brand terms and dark variant.

## Entry points

Maintainer space, Catalogue, Icons.

## Wireframe

```text
Icon library     Filter: [no logo] [no dark variant]          312 connectors
-------------------------------------------------------------------------------
Connector    Light    Dark    Terms checked   State
HubSpot      [logo]   [logo]  2026-11-12      approved
Teamtailor   -        -       -               category icon (ATS)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-05 step 3, U47 | desktop | ![FL-F24-05 step 3, U47, light](../../images/05-keep-the-catalogue/u47-simpleerp-maintainer/3-icon-library-desktop-light.png) | ![FL-F24-05 step 3, U47, dark](../../images/05-keep-the-catalogue/u47-simpleerp-maintainer/3-icon-library-desktop-dark.png) |
| FL-F24-05 step 3, U47 | phone | ![FL-F24-05 step 3, U47, light](../../images/05-keep-the-catalogue/u47-simpleerp-maintainer/3-icon-library-phone-light.png) | ![FL-F24-05 step 3, U47, dark](../../images/05-keep-the-catalogue/u47-simpleerp-maintainer/3-icon-library-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-25-icon-library-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-25-icon-library-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-25-icon-library-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-25-icon-library-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-25-icon-library-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-25-icon-library-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-25-icon-library-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-25-icon-library-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Connector | E-F24-12 connector | name | no | yes |
| Light, dark | E-F24-12 file, dark variant | SVG or PNG | yes | light yes |
| Terms | E-F24-12 brand terms | link | yes | yes |
| State | E-F24-12 | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Upload | row | maintainer | checked and approved |
| Withdraw | row | maintainer | category icon used |

## States

- Normal: connectors with logos and states.
- Empty: "Every connector has its logo".
- Loading: the frame and titles show at once with placeholder rows for the icons; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a refused file with the reason.
- Read-only: other roles do not see the library.
- Offline: not available offline: the library is on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F24-12 Integration icon](../../data/e-f24-12-integration-icon.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-12 Integration icon | Proposed | Badge "Proposed"; a new record starts here; next: Approved (UC-F24-21); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f24-25-icon-library-e-f24-12-integration-icon-proposed-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Approved | Badge "Approved"; next: Replaced or Withdrawn (UC-F24-01, UC-F24-27); fields editable within the role | U47 | `u47-simpleerp-maintainer/s-f24-25-icon-library-e-f24-12-integration-icon-approved-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Replaced | Badge "Replaced"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f24-25-icon-library-e-f24-12-integration-icon-replaced-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simpleerp-maintainer/s-f24-25-icon-library-e-f24-12-integration-icon-withdrawn-{desktop,phone}-{light,dark}.png` |

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

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F24-05 Keep the catalogue](../../flows/fl-f24-05-keep-the-catalogue.md)

## Open questions

None.

---

⬅️ [S-F24-24 My connections](../07-employees-and-their-tools/s-f24-24-my-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-26 AI connector builder](../08-ai-connectors-suites-and-warehouse/s-f24-26-ai-connector-builder.md)
