🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-15](README.md) ›
🖥️ S-F9-42 Careers and succession

# 🖥️ S-F9-42 Careers and succession

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md): all plans.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): the plans of their team.

## Purpose

Name successors for key positions with their readiness and gaps, and follow career wishes.

## Entry points

HR and projects › Careers and succession; Appraisals › a career wish; the AI assistant
([BR-F3-34](../../../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Careers and succession      Works director              Holder: Marc D.      Vacancy risk: high |
| ------------------------------------------------------------------------------------------- |
| SUCCESSOR        READINESS            GAPS                         ACTION                   |
| Sonia M.         1 to 2 years         Budget management            Course 2027-02 [Edit]    |
| Julien R.        3 years or more      Site experience over 5 years  Project lead 2027 [Edit] |
| [Add a successor]   [Suggest with the AI assistant]   Next review: 2027-11-30   State: Active |
| Career wishes: 3 to read   Plans without a ready successor: 2                               |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)):
`s-f09-42-careers-and-succession-empty-desktop-{light,dark}.png`,
`s-f09-42-careers-and-succession-loading-desktop-{light,dark}.png`,
`s-f09-42-careers-and-succession-offline-desktop-{light,dark}.png`,
`s-f09-42-careers-and-succession-read-only-desktop-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-15 step 3, U06 | desktop | ![FL-F9-15 step 3, U06, light](../../images/15-work-location-headcount-and-learning/u06-hr/3-careers-and-succession-desktop-light.png) | ![FL-F9-15 step 3, U06, dark](../../images/15-work-location-headcount-and-learning/u06-hr/3-careers-and-succession-desktop-dark.png) |
| FL-F9-15 step 3, U06 | desktop | ![FL-F9-15 step 3, U06, light](../../images/15-work-location-headcount-and-learning/u06-hr/3-careers-and-succession-desktop-light.png) | ![FL-F9-15 step 3, U06, dark](../../images/15-work-location-headcount-and-learning/u06-hr/3-careers-and-succession-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-42-careers-and-succession-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-42-careers-and-succession-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-42-careers-and-succession-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-42-careers-and-succession-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-42-careers-and-succession-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-42-careers-and-succession-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-42-careers-and-succession-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-42-careers-and-succession-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Position and holder | E-F9-50 position and holder | text | no | yes |
| Successors | E-F9-50 successors and readiness | list | yes | no |
| Gaps and actions | E-F9-50 gaps and actions | list | yes | no |
| Vacancy risk | E-F9-50 vacancy risk | choice | yes | yes |
| State | E-F9-50 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a successor | list | HR, the line | a successor with a readiness level |
| Suggest | header | HR | the AI assistant proposes successors with reasons, flagged as AI |
| Activate | header | HR | the plan becomes Active (UC-F9-45) |
| Review | header | HR | the plan goes under review, then is confirmed |
| Close | header | HR | the plan is Closed |

## States

- Normal: the key position, its holder, its successors with readiness, gaps and actions.
- Empty: No plan for this position: a hint to add the first successor or to start a recruitment.
- Loading: The position, then the successors and their skills.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a plan the user
  may not read says so ([BR-F9-44](../../business-rules/br-f09-44-successor-lists-are-seen-by-hr-and-the-line.md)).
- Read-only: a closed plan, or a role that may only read: shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-50 Succession plan](../../data/e-f09-50-succession-plan.md),
[E-F9-49 Position](../../data/e-f09-49-position.md), [E-F9-01 Employee record](../../data/e-f09-01-employee-record.md),
[E-F9-12 Qualification](../../data/e-f09-12-certification.md), [E-F9-11 Appraisal](../../data/e-f09-11-appraisal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-50 Succession plan | Draft | Badge "Draft"; a new record starts here; next: Active or Closed (UC-F9-45); fields editable within the role | U06, U02 | `u06-hr/s-f09-42-careers-and-succession-e-f09-50-succession-plan-draft-desktop-{light,dark}.png`; `u02-manager/s-f09-42-careers-and-succession-e-f09-50-succession-plan-draft-{desktop,phone}-{light,dark}.png` |
| E-F9-50 Succession plan | Active | Badge "Active"; next: Under review or Closed (UC-F9-45); fields editable within the role | U06, U02 | `u06-hr/s-f09-42-careers-and-succession-e-f09-50-succession-plan-active-desktop-{light,dark}.png`; `u02-manager/s-f09-42-careers-and-succession-e-f09-50-succession-plan-active-{desktop,phone}-{light,dark}.png` |
| E-F9-50 Succession plan | Under review | Badge "Under review"; next: Active (UC-F9-45); fields editable within the role | U06, U02 | `u06-hr/s-f09-42-careers-and-succession-e-f09-50-succession-plan-under-review-desktop-{light,dark}.png`; `u02-manager/s-f09-42-careers-and-succession-e-f09-50-succession-plan-under-review-{desktop,phone}-{light,dark}.png` |
| E-F9-50 Succession plan | Closed | Badge "Closed"; final state, read-only | U06, U02 | `u06-hr/s-f09-42-careers-and-succession-e-f09-50-succession-plan-closed-desktop-{light,dark}.png`; `u02-manager/s-f09-42-careers-and-succession-e-f09-50-succession-plan-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Readiness is a word, not a colour; keyboard: next successor, edit, activate.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-15 Work location, headcount, careers and learning](../../flows/fl-f09-15-work-location-headcount-and-learning.md)

## Open questions

None.

---

⬅️ [S-F9-41 Headcount plan](s-f09-41-headcount-plan.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-43 Project risks](s-f09-43-project-risks.md)
