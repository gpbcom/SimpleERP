🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-15](README.md) ›
🖥️ S-F9-43 Project risks

# 🖥️ S-F9-43 Project risks

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md): the register and the requests of
  their projects.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): the requests of their project and the risks shared with
  them, on a phone.

## Purpose

Keep a project's risk register and decide change requests.

## Entry points

HR and projects › Projects › a project › Risks and changes; the notification of a request to decide.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Warehouse extension          Risks and changes                          [Add a risk] [New request] |
| ------------------------------------------------------------------------------------------- |
| RISK                      PROB.  IMPACT  OWNER      ACTION                 REVIEW      STATE |
| Supplier delay            High   High    Valérie P. Second supplier asked  2026-12-01  Open |
| Ground survey late        Low    Medium  Marc D.    Book the survey now    2026-11-25  Open |
| CHANGE REQUEST                  COST     DAYS   DECIDER     STATE                           |
| Add a second floor              9 000    12     Fabrice L.  Submitted    [Approve] [Reject] |
| Risks open: 2   Requests waiting: 1                                                         |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f09-43-project-risks-empty-desktop-{light,dark}.png`,
`s-f09-43-project-risks-empty-phone-{light,dark}.png`, `s-f09-43-project-risks-loading-desktop-{light,dark}.png`,
`s-f09-43-project-risks-loading-phone-{light,dark}.png`, `s-f09-43-project-risks-offline-desktop-{light,dark}.png`,
`s-f09-43-project-risks-offline-phone-{light,dark}.png`, `s-f09-43-project-risks-read-only-desktop-{light,dark}.png`,
`s-f09-43-project-risks-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-15 step 4, U24 | desktop | ![FL-F9-15 step 4, U24, light](../../images/15-work-location-headcount-and-learning/u24-engagement-manager/4-project-risks-desktop-light.png) | ![FL-F9-15 step 4, U24, dark](../../images/15-work-location-headcount-and-learning/u24-engagement-manager/4-project-risks-desktop-dark.png) |
| FL-F9-15 step 4, U24 | desktop | ![FL-F9-15 step 4, U24, light](../../images/15-work-location-headcount-and-learning/u24-engagement-manager/4-project-risks-desktop-light.png) | ![FL-F9-15 step 4, U24, dark](../../images/15-work-location-headcount-and-learning/u24-engagement-manager/4-project-risks-desktop-dark.png) |
| FL-F9-15 step 4, U24 | phone | ![FL-F9-15 step 4, U24, light](../../images/15-work-location-headcount-and-learning/u24-engagement-manager/4-project-risks-phone-light.png) | ![FL-F9-15 step 4, U24, dark](../../images/15-work-location-headcount-and-learning/u24-engagement-manager/4-project-risks-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-43-project-risks-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-43-project-risks-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-43-project-risks-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-43-project-risks-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-43-project-risks-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-43-project-risks-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-43-project-risks-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-43-project-risks-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Risk | project risk line | text | yes | yes |
| Probability and impact | project risk line | low, medium, high | yes | yes |
| Owner and action | project risk line | user and text | yes | no |
| Request impact | E-F9-51 cost, days, date | money, number, date | draft only | yes |
| State | E-F9-51 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a risk | header | the engagement manager, the team | a risk on the register |
| New request | header | the engagement manager | a Draft request (UC-F9-46) |
| Submit | request | the engagement manager | the request is sent to the approver |
| Approve, Reject | request | the customer, the owner | the decision is recorded |
| Apply | request | the engagement manager | the project is changed |

## States

- Normal: the risk register ranked by exposure and the change requests with their decider and state.
- Empty: No risk and no request yet: a hint to add the first risk.
- Loading: The register as placeholders, then the requests.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); applying an
  unapproved request is refused
  ([BR-F9-45](../../business-rules/br-f09-45-a-change-request-applies-only-once-approved.md)).
- Read-only: a closed project, or a customer who may only read: shown, with no action but the decision.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-51 Change request](../../data/e-f09-51-change-request.md),
[E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md),
[E-F6-01 Customer record](../../../f06-customers-and-sales/data/e-f06-01-customer-record.md),
[E-F6-03 Quote](../../../f06-customers-and-sales/data/e-f06-03-quote.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-51 Change request | Draft | Badge "Draft"; a new record starts here; next: Submitted or Withdrawn (UC-F9-46); fields editable within the role | U24, U09 | `u24-engagement-manager/s-f09-43-project-risks-e-f09-51-change-request-draft-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-43-project-risks-e-f09-51-change-request-draft-phone-{light,dark}.png` |
| E-F9-51 Change request | Submitted | Badge "Submitted"; next: Approved or Rejected or Withdrawn (BR-F9-45, UC-F9-46); fields editable within the role | U24, U09 | `u24-engagement-manager/s-f09-43-project-risks-e-f09-51-change-request-submitted-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-43-project-risks-e-f09-51-change-request-submitted-phone-{light,dark}.png` |
| E-F9-51 Change request | Approved | Badge "Approved"; next: Applied (BR-F9-45); fields editable within the role | U24, U09 | `u24-engagement-manager/s-f09-43-project-risks-e-f09-51-change-request-approved-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-43-project-risks-e-f09-51-change-request-approved-phone-{light,dark}.png` |
| E-F9-51 Change request | Rejected | Badge "Rejected"; final state, read-only | U24, U09 | `u24-engagement-manager/s-f09-43-project-risks-e-f09-51-change-request-rejected-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-43-project-risks-e-f09-51-change-request-rejected-phone-{light,dark}.png` |
| E-F9-51 Change request | Applied | Badge "Applied"; final state, read-only | U24, U09 | `u24-engagement-manager/s-f09-43-project-risks-e-f09-51-change-request-applied-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-43-project-risks-e-f09-51-change-request-applied-phone-{light,dark}.png` |
| E-F9-51 Change request | Withdrawn | Badge "Withdrawn"; final state, read-only | U24, U09 | `u24-engagement-manager/s-f09-43-project-risks-e-f09-51-change-request-withdrawn-{desktop,phone}-{light,dark}.png`; `u09-customer/s-f09-43-project-risks-e-f09-51-change-request-withdrawn-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

On a phone, the customer sees one request at a time with its impact and the two decision buttons.

## Accessibility

Probability and impact are words; the decision buttons say what they do; keyboard: next row, approve, reject.

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

⬅️ [S-F9-42 Careers and succession](s-f09-42-careers-and-succession.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-44 Online courses](s-f09-44-online-courses.md)
