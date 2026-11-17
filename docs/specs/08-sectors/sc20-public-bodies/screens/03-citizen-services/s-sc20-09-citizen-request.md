🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-03 Citizen services](README.md) › 🖥️ S-SC20-09 Citizen request

# 🖥️ S-SC20-09 Citizen request

**Status:** 🔄 waiting for the owner

## Personas

- [U56 Citizen](../../../../01-users/personas/u56-citizen.md): my requests, their state and the answer, on the phone.
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md): the queue of requests to route and answer.

## Purpose

Receive a citizen's request, acknowledge it with its deadline and follow it to the answer.

## Entry points

Public bodies › Citizen requests; the portal's request button.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Request R-8412: Pothole on rue Haute                    State: Received   [Acknowledge]          |
| Type: Road defect     Received: 3 Mar 09:12     Deadline: 18 Mar     Department: Roads           |
| Citizen: M. Roux       Documents: photo (1)      Missing: none                                   |
| Message: Deep pothole near number 14                                                             |
| [Route] [Ask for a document] [Answer] [Pass to another authority]                                |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-03 step 1, U56 | phone | ![FL-SC20-03 step 1, U56, light](../../images/03-citizen-services/u56-citizen/1-citizen-request-phone-light.png) | ![FL-SC20-03 step 1, U56, dark](../../images/03-citizen-services/u56-citizen/1-citizen-request-phone-dark.png) |
| Error E1, U56 | phone | ![Error E1, U56, light](../../images/03-citizen-services/u56-citizen/e1-the-request-is-incomplete-phone-light.png) | ![Error E1, U56, dark](../../images/03-citizen-services/u56-citizen/e1-the-request-is-incomplete-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc20-09-citizen-request-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc20-09-citizen-request-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc20-09-citizen-request-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc20-09-citizen-request-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc20-09-citizen-request-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc20-09-citizen-request-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc20-09-citizen-request-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc20-09-citizen-request-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Type | E-SC20-08 type | list of request types | yes while Received | yes |
| Citizen | E-SC20-08 citizen | link | no | yes |
| Documents | E-SC20-08 documents | list | yes | yes by type |
| Deadline | E-SC20-08 deadline | date | no | yes |
| Department | E-SC20-08 department | link | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Acknowledge | header | office worker | the acknowledgement with the deadline is sent |
| Ask for a document | header | office worker | the request becomes Incomplete |
| Answer | header | department | the answer is sent and the request closed |

## States

- Normal: the requests with type, citizen, received date, deadline, department and state.
- Empty: No request yet, with New request for a citizen at the counter.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a document
  missing, no way to answer the citizen, with the request named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-08 Citizen request](../../data/e-sc20-08-citizen-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-08 Citizen request | Received | Badge "Received"; a new record starts here; next: Acknowledged or Incomplete (BR-SC20-09); fields editable within the role | U56, U16 | `u56-citizen/s-sc20-09-citizen-request-e-sc20-08-citizen-request-received-phone-{light,dark}.png`, `u16-office-worker/s-sc20-09-citizen-request-e-sc20-08-citizen-request-received-{desktop,phone}-{light,dark}.png` |
| E-SC20-08 Citizen request | Acknowledged | Badge "Acknowledged"; next: Answered (UC-SC20-09); fields editable within the role | U56, U16 | `u56-citizen/s-sc20-09-citizen-request-e-sc20-08-citizen-request-acknowledged-phone-{light,dark}.png`, `u16-office-worker/s-sc20-09-citizen-request-e-sc20-08-citizen-request-acknowledged-{desktop,phone}-{light,dark}.png` |
| E-SC20-08 Citizen request | Incomplete | Badge "Incomplete"; next: Acknowledged (BR-SC20-09); fields editable within the role | U56, U16 | `u56-citizen/s-sc20-09-citizen-request-e-sc20-08-citizen-request-incomplete-phone-{light,dark}.png`, `u16-office-worker/s-sc20-09-citizen-request-e-sc20-08-citizen-request-incomplete-{desktop,phone}-{light,dark}.png` |
| E-SC20-08 Citizen request | Answered | Badge "Answered"; next: Closed (UC-SC20-09); fields editable within the role | U56, U16 | `u56-citizen/s-sc20-09-citizen-request-e-sc20-08-citizen-request-answered-phone-{light,dark}.png`, `u16-office-worker/s-sc20-09-citizen-request-e-sc20-08-citizen-request-answered-{desktop,phone}-{light,dark}.png` |
| E-SC20-08 Citizen request | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U56, U16 | `u56-citizen/s-sc20-09-citizen-request-e-sc20-08-citizen-request-closed-phone-{light,dark}.png`, `u16-office-worker/s-sc20-09-citizen-request-e-sc20-08-citizen-request-closed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC20-03 Citizen services](../../flows/fl-sc20-03-citizen-services.md)

## Open questions

None.

---

⬅️ [S-SC20-08 Public contract](../02-public-procurement/s-sc20-08-public-contract.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-10 Hall booking](s-sc20-10-hall-booking.md)
