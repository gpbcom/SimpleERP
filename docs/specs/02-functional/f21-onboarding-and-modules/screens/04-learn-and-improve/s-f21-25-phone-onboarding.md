🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-04 Learn and improve](README.md) › 🖥️ S-F21-25 Phone onboarding

# 🖥️ S-F21-25 Phone onboarding

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Walk an employee through the first sign-in on the phone.

## Entry points

The invitation link opened on a phone.

## Wireframe

```text
Welcome, Sophie            Step 3 of 5
-------------------------------------------------------------------------------
Two-factor: [Use an authenticator app]
                                         [Continue]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-04 step 7, U01 | desktop | ![FL-F21-04 step 7, U01, light](../../images/04-learn-and-improve/u01-employee/7-phone-onboarding-desktop-light.png) | ![FL-F21-04 step 7, U01, dark](../../images/04-learn-and-improve/u01-employee/7-phone-onboarding-desktop-dark.png) |
| FL-F21-04 step 7, U01 | phone | ![FL-F21-04 step 7, U01, light](../../images/04-learn-and-improve/u01-employee/7-phone-onboarding-phone-light.png) | ![FL-F21-04 step 7, U01, dark](../../images/04-learn-and-improve/u01-employee/7-phone-onboarding-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-25-phone-onboarding-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-25-phone-onboarding-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-25-phone-onboarding-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-25-phone-onboarding-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-25-phone-onboarding-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-25-phone-onboarding-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-25-phone-onboarding-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-25-phone-onboarding-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Step | E-F21-01 step | number | no | yes |
| Profile, password | F1 user | text | yes | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Continue | footer | employee | next step |

## States

- Normal: one step per screen with progress.
- Empty: never empty: starts at step 1.
- Loading: the frame and titles show at once with placeholder rows for the step; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an expired link.
- Read-only: done steps are read-only.
- Offline: The current step stays on screen; each step is saved only online. Nothing else is queued: D38 keeps only
  today's schedule, time and intervention records offline; a banner says the connection is lost and the actions come
  back with it.

Shown entities (VD-15): [E-F21-01 Onboarding progress](../../data/e-f21-01-onboarding-progress.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-01 Onboarding progress | Done | Badge "Done"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f21-25-phone-onboarding-e-f21-01-onboarding-progress-done-{desktop,phone}-{light,dark}.png` |
| E-F21-01 Onboarding progress | Closed | Badge "Closed"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f21-25-phone-onboarding-e-f21-01-onboarding-progress-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-13 Stepper](../../../../04-ux/design-system/components/c-13-stepper.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F21-04 Learn and improve](../../flows/fl-f21-04-learn-and-improve.md)

## Open questions

None.

---

⬅️ [S-F21-24 Languages](../01-first-run/s-f21-24-languages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-26 Expert booking](../06-experts-cutover-and-parallel-run/s-f21-26-expert-booking.md)
