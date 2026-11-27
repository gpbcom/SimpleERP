🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-10 People and tools](README.md) › 🖥️ S-F12-27 Work instructions

# 🖥️ S-F12-27 Work instructions

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)

## Purpose

Edit, version and publish work instructions, and see acknowledgements.

## Entry points

Manufacturing › Instructions.

## Wireframe

```text
+------------------------------------------------------------------+
| Op 20 Assembly   v4 (2026-11-10)  previous v3   [Edit] [Publish]  |
| Changed: torque 22 Nm -> 24 Nm                                    |
| [image] [video]                                                   |
| Acknowledged: Paul 11-11 06:02, Lea 11-11 14:05   Waiting: Hugo   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-10 step 3, U21 | desktop | ![FL-F12-10 step 3, U21, light](../../images/10-people-and-tools/u21-production-planner/3-work-instructions-desktop-light.png) | ![FL-F12-10 step 3, U21, dark](../../images/10-people-and-tools/u21-production-planner/3-work-instructions-desktop-dark.png) |
| FL-F12-10 step 3, U21 | phone | ![FL-F12-10 step 3, U21, light](../../images/10-people-and-tools/u21-production-planner/3-work-instructions-phone-light.png) | ![FL-F12-10 step 3, U21, dark](../../images/10-people-and-tools/u21-production-planner/3-work-instructions-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-27-work-instructions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-27-work-instructions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-27-work-instructions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-27-work-instructions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-27-work-instructions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-27-work-instructions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-27-work-instructions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-27-work-instructions-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Version, content, acknowledgements | E-F12-22 | content |

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | planner | New version |
| Acknowledge | operator | On the tablet |

## States

- Normal: edit, version and publish work instructions, and see acknowledgements.
- Empty: no instruction yet: Write the first version.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: published versions; operators read.
- Offline: The tablet keeps the versions loaded at the shift's start; acknowledgements made offline sync in order,
  [UC-F12-26](../../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md).

Shown entities (VD-15): [E-F12-22 Work instruction version](../../data/e-f12-22-work-instruction-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-22 Work instruction version | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F12-28); fields editable within the role | U21 | `u21-production-planner/s-f12-27-work-instructions-e-f12-22-work-instruction-version-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-22 Work instruction version | Published | Badge "Published"; next: Superseded (UC-F12-28); fields editable within the role | U21 | `u21-production-planner/s-f12-27-work-instructions-e-f12-22-work-instruction-version-published-{desktop,phone}-{light,dark}.png` |
| E-F12-22 Work instruction version | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U21 | `u21-production-planner/s-f12-27-work-instructions-e-f12-22-work-instruction-version-superseded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the acknowledgement on the tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-10 People and tools](../../flows/fl-f12-10-people-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-26 Work in progress](../05-subcontracting-and-costs/s-f12-26-work-in-progress.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-28 Energy](../13-energy-passport-and-work-in-progress/s-f12-28-energy.md)
