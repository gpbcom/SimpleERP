🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-07 Schemes and special contracts](README.md) › 🖥️ S-F13-21 Schemes

# 🖥️ S-F13-21 Schemes

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md), who enrols and exempts
- [U06 Human resources](../../../../01-users/personas/u06-hr.md), who uploads forms and proofs

## Purpose

Enrol each employee in the mandatory health and provident schemes, or record their exemption with its proof.

## Entry points

Payroll menu, Schemes; the "new employee to enrol" notification; an employee's pay profile.

## Wireframe

```text
Schemes                                     [To set up 3] [Proofs lapsing 1]
-------------------------------------------------------------------------------
Employee         Health        Provident        Status       Since
Sophie Bernard   Mutuelle A    -                enrolled     2026-03-01
Karim Haddad     exempted      Executives A     enrolled     2025-09-01
Lucas Martin     ?             ?                to set up    2026-09-01   [Enrol]
-------------------------------------------------------------------------------
[Employee panel] scheme, start date, shares 24.00 / 36.00, [Record exemption]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-07 step 1, U45 | desktop | ![FL-F13-07 step 1, U45, light](../../images/07-schemes-and-special-contracts/u45-payroll-officer/1-schemes-desktop-light.png) | ![FL-F13-07 step 1, U45, dark](../../images/07-schemes-and-special-contracts/u45-payroll-officer/1-schemes-desktop-dark.png) |
| Error E1, U45 | desktop | ![Error E1, U45, light](../../images/07-schemes-and-special-contracts/u45-payroll-officer/e1-schemes-refused-desktop-light.png) | ![Error E1, U45, dark](../../images/07-schemes-and-special-contracts/u45-payroll-officer/e1-schemes-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-21-schemes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-21-schemes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-21-schemes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-21-schemes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-21-schemes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-21-schemes-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-21-schemes-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-21-schemes-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Employee | E-F13-17 employee | name | no | yes |
| Scheme | E-F13-17 scheme | name and insurer | yes | yes |
| Status | E-F13-17 status | enrolled, exempted, ended | yes | yes |
| Exemption reason | E-F13-17 exemption reason | list of the country pack | yes | if exempted |
| Proof | E-F13-17 proof | file | yes (HR, payroll) | if exempted |
| Shares | E-F13-17 shares | EUR per month | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Enrol | employee panel | payroll officer | memberships saved, enrolment sent to the insurer |
| Record exemption | employee panel | payroll officer | exemption saved, no deduction |
| Upload proof | employee panel | HR, payroll officer | proof attached |
| End membership | employee panel | payroll officer | membership ended at the date |

## States

- Normal: the list of employees with their health and provident status, filters "to set up" and "proofs lapsing".
- Empty: "No employee to enrol yet": shown before the first contract; a link opens payroll set-up to define the schemes.
- Loading: the frame and titles show at once with placeholder rows for the employees and their memberships; within 1
  second (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: an exemption reason outside the country pack's list, or an employee with neither membership nor exemption,
  highlighted in the list.
- Read-only: HR sees statuses and uploads proofs but cannot enrol or exempt; the employee sees only their own
  memberships.
- Offline: not available offline: payroll set-up is office work on a desktop. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-17 Scheme membership](../../data/e-f13-17-scheme-membership.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-17 Scheme membership | Enrolled | Badge "Enrolled"; a new record starts here; next: Ended (UC-F13-21); fields editable within the role | U06, U45 | `u06-hr/s-f13-21-schemes-e-f13-17-scheme-membership-enrolled-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-21-schemes-e-f13-17-scheme-membership-enrolled-desktop-{light,dark}.png` |
| E-F13-17 Scheme membership | Exempted | Badge "Exempted"; a new record starts here; next: Enrolled or Ended (UC-F13-21); fields editable within the role | U06, U45 | `u06-hr/s-f13-21-schemes-e-f13-17-scheme-membership-exempted-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-21-schemes-e-f13-17-scheme-membership-exempted-desktop-{light,dark}.png` |
| E-F13-17 Scheme membership | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f13-21-schemes-e-f13-17-scheme-membership-ended-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-21-schemes-e-f13-17-scheme-membership-ended-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop. On a tablet the employee panel opens over the list; not offered on a phone (payroll is desktop work, U45
devices).

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-07 Schemes and special contracts](../../flows/fl-f13-07-schemes-and-special-contracts.md)

## Open questions

None.

---

⬅️ [S-F13-20 Payroll assistant](../06-assistant/s-f13-20-payroll-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-22 Special contracts](s-f13-22-special-contracts.md)
