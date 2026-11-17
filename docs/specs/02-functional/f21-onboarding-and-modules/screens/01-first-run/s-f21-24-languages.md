🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-01 First run](README.md) › 🖥️ S-F21-24 Languages

# 🖥️ S-F21-24 Languages

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Set the company's default language and each user's own.

## Entry points

Guide, About you; the user's profile.

## Wireframe

```text
Languages
-------------------------------------------------------------------------------
Company default: [Français v]
My language:     [English v]
Legal documents: French (country pack)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-01 step 7, U13 | desktop | ![FL-F21-01 step 7, U13, light](../../images/01-first-run/u13-owner/7-languages-desktop-light.png) | ![FL-F21-01 step 7, U13, dark](../../images/01-first-run/u13-owner/7-languages-desktop-dark.png) |
| FL-F21-01 step 7, U13 | phone | ![FL-F21-01 step 7, U13, light](../../images/01-first-run/u13-owner/7-languages-phone-light.png) | ![FL-F21-01 step 7, U13, dark](../../images/01-first-run/u13-owner/7-languages-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-24-languages-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-24-languages-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-24-languages-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-24-languages-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-24-languages-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-24-languages-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f21-24-languages-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f21-24-languages-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Company default | E-F21-16 | list | yes (owner) | yes |
| My language | E-F21-16 | list | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Save | footer | owner, user | language applied |

## States

- Normal: the two choices and the legal note.
- Empty: never empty: a default is always set.
- Loading: the frame and titles show at once with placeholder rows for the languages; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a language without translation, with a notice.
- Read-only: users cannot change the company default.
- Offline: The languages last loaded stay visible; changing them needs the network. Nothing else is queued: D38 keeps
  only today's schedule, time and intervention records offline; a banner says the connection is lost and the actions
  come back with it.

Shown entities (VD-15): [E-F21-16 Language setting](../../data/e-f21-16-language-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-16 Language setting | Set | Badge "Set"; a new record starts here; next: Changed (UC-F21-24); fields editable within the role | U01, U13 | `u01-employee/s-f21-24-languages-e-f21-16-language-setting-set-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f21-24-languages-e-f21-16-language-setting-set-{desktop,phone}-{light,dark}.png` |
| E-F21-16 Language setting | Changed | Badge "Changed"; next: Set (UC-F21-24); fields editable within the role | U01, U13 | `u01-employee/s-f21-24-languages-e-f21-16-language-setting-changed-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f21-24-languages-e-f21-16-language-setting-changed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone and desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F21-01 First run](../../flows/fl-f21-01-first-run.md)

## Open questions

None.

---

⬅️ [S-F21-23 Invite your accountant](../03-team-and-data/s-f21-23-invite-your-accountant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-25 Phone onboarding](../04-learn-and-improve/s-f21-25-phone-onboarding.md)
