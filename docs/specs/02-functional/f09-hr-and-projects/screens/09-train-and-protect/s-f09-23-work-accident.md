🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-09 Train and protect](README.md) › 🖥️ S-F9-23 Work accident

# 🖥️ S-F9-23 Work accident

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Report a work accident and declare it within 48 hours.

## Entry points

HR › Work accidents; Report an accident on the phone.

## Wireframe

```text
Phone (manager)
  Who [Paul Morel v]  When [11-12 10:30]  Where [Lyon 3]
  What happened [Fall from a ladder        ]
  Witnesses [Hugo]  First aid [yes]   [Photo] [Send]
HR (desktop)
| Paul Morel  11-12 10:30  declare before 11-14 10:30  [Declare] |
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-09 step 2, U02 | desktop | ![FL-F9-09 step 2, U02, light](../../images/09-train-and-protect/u02-manager/2-work-accident-desktop-light.png) | ![FL-F9-09 step 2, U02, dark](../../images/09-train-and-protect/u02-manager/2-work-accident-desktop-dark.png) |
| FL-F9-09 step 2, U02 | phone | ![FL-F9-09 step 2, U02, light](../../images/09-train-and-protect/u02-manager/2-work-accident-phone-light.png) | ![FL-F9-09 step 2, U02, dark](../../images/09-train-and-protect/u02-manager/2-work-accident-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-23-work-accident-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-23-work-accident-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-23-work-accident-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-23-work-accident-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-23-work-accident-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-23-work-accident-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-23-work-accident-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-23-work-accident-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Employee, when, where, what, declaration, leave | E-F9-23 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Send | managers | HR alerted |
| Declare | HR | Declaration sent |

## States

- Normal: report a work accident and declare it within 48 hours.
- Empty: no accident this year: "No accident recorded".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: declared accidents; health details only for HR.
- Offline: The report can be filled offline on the phone and is sent when the network is back,
  [UC-F2-22](../../../f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md);
  the 48-hour clock starts when HR receives it.

Shown entities (VD-15): [E-F9-23 Work accident](../../data/e-f09-23-work-accident.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-23 Work accident | Active | Badge "Active"; a new record starts here; next: Closed (UC-F9-26); fields editable within the role | U02, U06 | `u02-manager/s-f09-23-work-accident-e-f09-23-work-accident-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-23-work-accident-e-f09-23-work-accident-active-desktop-{light,dark}.png` |
| E-F9-23 Work accident | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U02, U06 | `u02-manager/s-f09-23-work-accident-e-f09-23-work-accident-closed-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-23-work-accident-e-f09-23-work-accident-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Report on a phone; declare on desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-09 Train and protect](../../flows/fl-f09-09-train-and-protect.md)

## Open questions

None.

---

⬅️ [S-F9-22 Training plan](s-f09-22-training-plan.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-24 Risk assessment](s-f09-24-risk-assessment.md)
