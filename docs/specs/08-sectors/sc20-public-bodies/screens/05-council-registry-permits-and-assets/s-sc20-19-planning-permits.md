🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-05 Council, civil registry, permits and assets](README.md) ›
🖥️ S-SC20-19 Planning permits

# 🖥️ S-SC20-19 Planning permits

**Status:** 🔄 waiting for the owner

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the requests, their clock,
  consultations and decision.
- [U56 Citizen](../../../../01-users/personas/u56-citizen.md): my permit request, with its state and delay, on the
  phone.

## Purpose

Instruct planning-permit requests inside their legal delay and notify the decision.

## Entry points

Public bodies › Planning permits; the portal's permit request.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Permit PC-2027-031: House extension, Garcia                   State: Instructed                  |
| Kind: Building permit   Filed: 3 Mar   Complete: 18 Mar   Delay: 2 months   Ends: 18 May         |
| Consultations: Heritage architect (asked 20 Mar), Roads (answered)                               |
| Days left: 41       Documents: plans, form, photos        Missing: none                          |
| [Ask for a document] [Consult] [Draft decision] [Notify]                                         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-05 step 3, U54 | desktop | ![FL-SC20-05 step 3, U54, light](../../images/05-council-registry-permits-and-assets/u54-public-finance-officer/3-planning-permits-desktop-light.png) | ![FL-SC20-05 step 3, U54, dark](../../images/05-council-registry-permits-and-assets/u54-public-finance-officer/3-planning-permits-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-19-planning-permits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-19-planning-permits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-19-planning-permits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-19-planning-permits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-19-planning-permits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-19-planning-permits-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-19-planning-permits-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-19-planning-permits-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind | E-SC20-14 kind | list of kinds of permit | yes while Filed | yes |
| Filed on | E-SC20-14 filed | date | no | yes |
| Complete on | E-SC20-14 complete | date | no | no |
| Delay ends | E-SC20-14 delay end | date | no | yes |
| Consultations | E-SC20-14 consultations | list of body and answer | yes | no |
| Decision | E-SC20-14 decision | granted, refused | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Ask for a document | header | instructing officer | the file becomes Incomplete |
| Consult | header | instructing officer | a body is consulted and the delay is updated |
| Notify | header | mayor or delegate | the decision is signed and notified |

## States

- Normal: the requests with kind, filing, completion, delay end, consultations, decision and state.
- Empty: No permit request yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  document asked too late, a delay passed, with the request named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-14 Permit request](../../data/e-sc20-14-permit-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-14 Permit request | Filed | Badge "Filed"; a new record starts here; next: Incomplete or Instructed (BR-SC20-19, UC-SC20-19); fields editable within the role | U54, U56 | `u54-public-finance-officer/s-sc20-19-planning-permits-e-sc20-14-permit-request-filed-desktop-{light,dark}.png`, `u56-citizen/s-sc20-19-planning-permits-e-sc20-14-permit-request-filed-phone-{light,dark}.png` |
| E-SC20-14 Permit request | Incomplete | Badge "Incomplete"; next: Filed (BR-SC20-19); fields editable within the role | U54, U56 | `u54-public-finance-officer/s-sc20-19-planning-permits-e-sc20-14-permit-request-incomplete-desktop-{light,dark}.png`, `u56-citizen/s-sc20-19-planning-permits-e-sc20-14-permit-request-incomplete-phone-{light,dark}.png` |
| E-SC20-14 Permit request | Instructed | Badge "Instructed"; next: Granted, Refused or Delay passed (UC-SC20-19, BR-SC20-19); fields editable within the role | U54, U56 | `u54-public-finance-officer/s-sc20-19-planning-permits-e-sc20-14-permit-request-instructed-desktop-{light,dark}.png`, `u56-citizen/s-sc20-19-planning-permits-e-sc20-14-permit-request-instructed-phone-{light,dark}.png` |
| E-SC20-14 Permit request | Granted | Badge "Granted"; final: read-only, no next state; the history shows how it got here | U54, U56 | `u54-public-finance-officer/s-sc20-19-planning-permits-e-sc20-14-permit-request-granted-desktop-{light,dark}.png`, `u56-citizen/s-sc20-19-planning-permits-e-sc20-14-permit-request-granted-phone-{light,dark}.png` |
| E-SC20-14 Permit request | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U54, U56 | `u54-public-finance-officer/s-sc20-19-planning-permits-e-sc20-14-permit-request-refused-desktop-{light,dark}.png`, `u56-citizen/s-sc20-19-planning-permits-e-sc20-14-permit-request-refused-phone-{light,dark}.png` |
| E-SC20-14 Permit request | Delay passed | Badge "Delay passed"; final: read-only, no next state; the history shows how it got here | U54, U56 | `u54-public-finance-officer/s-sc20-19-planning-permits-e-sc20-14-permit-request-delay-passed-desktop-{light,dark}.png`, `u56-citizen/s-sc20-19-planning-permits-e-sc20-14-permit-request-delay-passed-phone-{light,dark}.png` |

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

- [FL-SC20-05](../../flows/fl-sc20-05-council-registry-permits-and-assets.md)

## Open questions

None.

---

⬅️ [S-SC20-18 Civil registry](s-sc20-18-civil-registry.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-20 Public assets](s-sc20-20-public-assets.md)
