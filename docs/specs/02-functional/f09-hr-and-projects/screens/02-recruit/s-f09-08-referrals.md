🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-02 Recruit](README.md) ›
🖥️ S-F9-08 Referrals

# 🖥️ S-F9-08 Referrals

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Run referrals.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-02 step 4, U01 | phone | ![FL-F9-02 step 4, U01, light](../../images/02-recruit/u01-employee/4-referrals-phone-light.png) | ![FL-F9-02 step 4, U01, dark](../../images/02-recruit/u01-employee/4-referrals-phone-dark.png) |
| FL-F9-02 step 4, U01 | desktop | ![FL-F9-02 step 4, U01, light](../../images/02-recruit/u01-employee/4-referrals-desktop-light.png) | ![FL-F9-02 step 4, U01, dark](../../images/02-recruit/u01-employee/4-referrals-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-08-referrals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-08-referrals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-08-referrals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-08-referrals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-08-referrals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-08-referrals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-08-referrals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-08-referrals-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run referrals, as the wireframe shows.
- Empty: No referral yet, with Refer someone.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-07 Applicant](../../data/e-f09-07-applicant.md),
[E-F9-36 Employee referral](../../data/e-f09-36-employee-referral.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-07 Applicant | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U06 | `u01-employee/s-f09-08-referrals-e-f09-07-applicant-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-08-referrals-e-f09-07-applicant-active-desktop-{light,dark}.png` |
| E-F9-36 Employee referral | Tracked | Badge "Tracked"; a new record starts here; next: Hired (UC-F9-08); fields editable within the role | U01, U06 | `u01-employee/s-f09-08-referrals-e-f09-36-employee-referral-tracked-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-08-referrals-e-f09-36-employee-referral-tracked-desktop-{light,dark}.png` |
| E-F9-36 Employee referral | Not counted | Badge "Not counted"; a new record can start here; final: read-only, no next state; the history shows how it got here | U01, U06 | `u01-employee/s-f09-08-referrals-e-f09-36-employee-referral-not-counted-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-08-referrals-e-f09-36-employee-referral-not-counted-desktop-{light,dark}.png` |
| E-F9-36 Employee referral | Hired | Badge "Hired"; final: read-only, no next state; the history shows how it got here | U01, U06 | `u01-employee/s-f09-08-referrals-e-f09-36-employee-referral-hired-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-08-referrals-e-f09-36-employee-referral-hired-desktop-{light,dark}.png` |

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

## Shown in

- [FL-F9-02 Recruit](../../flows/fl-f09-02-recruit.md)

## Open questions

None.

---

⬅️ [S-F9-07 Offer](s-f09-07-offer.md) · ⬆️ [Up](README.md) · ➡️ [S-F9-09 Time off](../03-time/s-f09-09-time-off.md)
