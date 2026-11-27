🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-09 Train and protect](README.md) › 🖥️ S-F9-22 Training plan

# 🖥️ S-F9-22 Training plan

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Purpose

Plan trainings with their funding and follow attendance and certificates.

## Entry points

HR › Training plan.

## Wireframe

```text
+------------------------------------------------------------------+
| Training plan 2027   Budget 24,000   OPCO 14,500   CPF 3,200       |
| Course                 Trainees  Date    Cost   Funding   Status  |
| Driver continuous      6         01-18   4,200  OPCO 3,000 agreed |
| First aid              8         02-03   1,600  company   planned |
| Mandatory expiring in 90 days: 3                 [Plan them]      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-09 step 1, U06 | desktop | ![FL-F9-09 step 1, U06, light](../../images/09-train-and-protect/u06-hr/1-training-plan-desktop-light.png) | ![FL-F9-09 step 1, U06, dark](../../images/09-train-and-protect/u06-hr/1-training-plan-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/09-train-and-protect/u06-hr/e1-training-plan-refused-desktop-light.png) | ![Error E1, U06, dark](../../images/09-train-and-protect/u06-hr/e1-training-plan-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-22-training-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-22-training-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-22-training-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-22-training-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-22-training-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-22-training-plan-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-22-training-plan-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-22-training-plan-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Course, trainees, cost, funding, status | E-F9-22 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Request funding | HR | Sent to the OPCO |
| Record attendance | HR, trainer | Certificates |

## States

- Normal: plan trainings with their funding and follow attendance and certificates.
- Empty: no plan yet: Start from the needs.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: past sessions.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F9-22 Training session](../../data/e-f09-22-training-session.md),
[E-F9-12 Qualification](../../data/e-f09-12-certification.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-22 Training session | Planned | Badge "Planned"; a new record starts here; next: Closed or Held (UC-F9-25); fields editable within the role | U06 | `u06-hr/s-f09-22-training-plan-e-f09-22-training-session-planned-desktop-{light,dark}.png` |
| E-F9-22 Training session | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f09-22-training-plan-e-f09-22-training-session-closed-desktop-{light,dark}.png` |
| E-F9-22 Training session | Held | Badge "Held"; next: Closed (UC-F9-25); fields editable within the role | U06 | `u06-hr/s-f09-22-training-plan-e-f09-22-training-session-held-desktop-{light,dark}.png` |
| E-F9-12 Qualification | To verify | Badge "To verify"; a new record starts here; next: Verified or Rejected (UC-F9-33, BR-F9-27); fields editable within the role | U06 | `u06-hr/s-f09-22-training-plan-e-f09-12-certification-to-verify-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Verified | Badge "Verified"; a new record starts here; next: Expired (UC-F12-22); fields editable within the role | U06 | `u06-hr/s-f09-22-training-plan-e-f09-12-certification-verified-desktop-{light,dark}.png` |
| E-F9-12 Qualification | Expired | Badge "Expired"; next: To verify (UC-F9-33); fields editable within the role | U06 | `u06-hr/s-f09-22-training-plan-e-f09-12-certification-expired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; attendance on a tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-09 Train and protect](../../flows/fl-f09-09-train-and-protect.md)

## Open questions

None.

---

⬅️ [S-F9-21 Whistleblowing](../07-fair-pay-and-speaking-up/s-f09-21-whistleblowing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-23 Work accident](s-f09-23-work-accident.md)
