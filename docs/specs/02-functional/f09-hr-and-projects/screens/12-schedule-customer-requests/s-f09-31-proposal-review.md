🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-12 Schedule customer requests](README.md) › 🖥️ S-F9-31 Proposal review

# 🖥️ S-F9-31 Proposal review

**Status:** ✅ specified

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) and
  [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md), as planners (D517): confirm,
  edit, override.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): reads the proposals and the overrides of their teams.

## Purpose

Show why the engine proposes a person for a work request, and let the planner confirm, adjust or override.

## Entry points

"Propose" or "Review" on the scheduling board (S-F9-30) or the work requests (S-F16-14); the notification "automatic
mode stopped".

## Wireframe

The route map follows [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md) for roles with the map right;
the travel minutes come from the route optimiser of
[S-F9-27 Rounds](../11-capacity-rounds-and-partners/s-f09-27-rounds.md).

```text
+-----------------------------------------------------------------------------------------------+
| WR-2207 Bathing help · Mme Roche, Villeurbanne · Tue 08:00-09:00 · 60 min           |
| Request type: Bathing help v3   Required: carer qualification   Preferred: French (4), zones (3)|
| [Adjust for this request]                                                                     |
|-----------------------------------------------------------------------------------------------|
| CANDIDATES                     SCORE  TRAVEL ADDED  WHY                                        |
| (o) Lea Martin       best      92     +6 min        usual carer, French, in her zone           |
| ( ) Marc Petit                 81     +14 min       French, in his zone                        |
| ( ) Sofia Morel                64     +22 min       outside her zone                           |
| EXCLUDED (4)                                                                                  |
|   Karim B.     not eligible: carer qualification                                              |
|   Nadia R.     not eligible: qualification to verify                                          |
|   Hugo L.      not eligible: medical restriction                                              |
|   Ines T.      absent                                                                          |
|-----------------------------------------------------------------------------------------------|
| [ map: Lea's round with the visit added, before and after ]                                   |
|                                    [Confirm Lea] [Choose another...] [Change the time] [Block] |
+-----------------------------------------------------------------------------------------------+
Choosing another than the best asks: "Reason for the override" [ text ] (required).
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-12 step 3, U25 | desktop | ![FL-F2-12 step 3, U25, light](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/3-proposal-review-desktop-light.png) | ![FL-F2-12 step 3, U25, dark](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/3-proposal-review-desktop-dark.png) |
| FL-F2-12 step 3, U25 | phone | ![FL-F2-12 step 3, U25, light](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/3-proposal-review-phone-light.png) | ![FL-F2-12 step 3, U25, dark](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/3-proposal-review-phone-dark.png) |
| Error E3, U25 | desktop | ![Error E3, U25, light](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/e3-a-planner-relaxes-a-legal-attribute-on-a-desktop-light.png) | ![Error E3, U25, dark](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/e3-a-planner-relaxes-a-legal-attribute-on-a-desktop-dark.png) |
| Error E3, U25 | phone | ![Error E3, U25, light](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/e3-a-planner-relaxes-a-legal-attribute-on-a-phone-light.png) | ![Error E3, U25, dark](../../../f02-no-code-configuration/images/12-set-up-request-types/u25-care-coordinator/e3-a-planner-relaxes-a-legal-attribute-on-a-phone-dark.png) |
| Error E1, U25 | desktop | ![Error E1, U25, light](../../images/12-schedule-customer-requests/u25-care-coordinator/e1-no-eligible-person-desktop-light.png) | ![Error E1, U25, dark](../../images/12-schedule-customer-requests/u25-care-coordinator/e1-no-eligible-person-desktop-dark.png) |
| Error E1, U25 | phone | ![Error E1, U25, light](../../images/12-schedule-customer-requests/u25-care-coordinator/e1-no-eligible-person-phone-light.png) | ![Error E1, U25, dark](../../images/12-schedule-customer-requests/u25-care-coordinator/e1-no-eligible-person-phone-dark.png) |
| Error E3, U25 | desktop | ![Error E3, U25, light](../../images/12-schedule-customer-requests/u25-care-coordinator/e3-a-legal-requirement-cannot-be-relaxed-desktop-light.png) | ![Error E3, U25, dark](../../images/12-schedule-customer-requests/u25-care-coordinator/e3-a-legal-requirement-cannot-be-relaxed-desktop-dark.png) |
| Error E3, U25 | phone | ![Error E3, U25, light](../../images/12-schedule-customer-requests/u25-care-coordinator/e3-a-legal-requirement-cannot-be-relaxed-phone-light.png) | ![Error E3, U25, dark](../../images/12-schedule-customer-requests/u25-care-coordinator/e3-a-legal-requirement-cannot-be-relaxed-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-31-proposal-review-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-31-proposal-review-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-31-proposal-review-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-31-proposal-review-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-31-proposal-review-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-31-proposal-review-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-31-proposal-review-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-31-proposal-review-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Work request | E-F16-12 | number, type, customer, place, window, duration | time within the window | yes |
| Attributes | E-F2-25, adjusted on E-F9-28 | required and preferred with weights | add or relax one, with a reason; legal ones locked | yes |
| Candidates | E-F9-28 candidates | name, score, travel added, why | choose one | yes |
| Excluded | E-F9-28 excluded | name and a short reason (BR-F9-29) | no | yes |
| Route | E-F9-26, E-T13-02 | map | no | for work at a place |
| Override reason | E-F9-28 override reason | text | yes | when the choice is not the best |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm | footer | planners | work request scheduled; visit added to the round |
| Choose another | candidates | planners | override with a required reason, logged (BR-F9-34) |
| Adjust for this request | header | planners | add or relax one attribute with a reason; legal ones refused (BR-F9-26) |
| Change the time | footer | planners | the proposal computed again |
| Block | footer | planners | work request blocked with a reason (subcontract, move the window, train, refuse) |

## States

- Normal: the proposal with its candidates, excluded and route.
- Empty: no candidate and no one excluded (no one in the team): "Nobody in this team works on Tuesday".
- Loading: "Computing the proposal" while the engine and the optimiser answer.
- Error: the error message pattern (D122); "Assign by hand" stays, logged as an override.
- Read-only: a proposal already confirmed or overridden; managers.
- Offline: not available offline.

Shown entities (VD-15): [E-F16-12 Work request](../../../f16-customer-support-agents/data/e-f16-12-work-request.md),
[E-F9-28 Assignment proposal](../../data/e-f09-28-assignment-proposal.md),
[E-F2-25 Request type](../../../f02-no-code-configuration/data/e-f02-25-request-type.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-12 Work request | Proposed | Badge "Proposed"; every action | U25, U29 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-proposed-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f16-12-work-request-proposed-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Blocked | Badge "Blocked"; the reasons counted; Change the time, Adjust | U25, U29, U02 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-31-proposal-review-e-f16-12-work-request-blocked-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Scheduled | Read-only; who confirmed, when, any override reason | U25, U29, U02 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-31-proposal-review-e-f16-12-work-request-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Waiting | Candidates selectable; Confirm | U25, U29 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-waiting-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-waiting-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Stopped | Banner "The automatic mode stopped here" with the problem; then as Waiting | U25, U29 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-stopped-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-stopped-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | No candidate | No candidate list; the excluded with reasons; Change the time, Adjust, Block | U25, U29 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-no-candidate-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-no-candidate-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Applied | Read-only; "Assigned by the automatic mode" | U25, U29, U02 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-applied-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-applied-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-31-proposal-review-e-f09-28-assignment-proposal-applied-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Confirmed | Read-only; "Confirmed by" | U25, U29, U02 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-confirmed-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-confirmed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-31-proposal-review-e-f09-28-assignment-proposal-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Overridden | Read-only; the reason shown | U25, U29, U02 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-overridden-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-overridden-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-31-proposal-review-e-f09-28-assignment-proposal-overridden-{desktop,phone}-{light,dark}.png` |
| E-F9-28 Assignment proposal | Superseded | Read-only; "Replaced by a newer proposal" with a link | U25, U29, U02 | `u25-care-coordinator/s-f09-31-proposal-review-e-f09-28-assignment-proposal-superseded-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f09-28-assignment-proposal-superseded-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-31-proposal-review-e-f09-28-assignment-proposal-superseded-{desktop,phone}-{light,dark}.png` |
| E-F2-25 Request type | Published | Read-only header; adjusted attributes tagged "this request only" | U25, U29 | `u25-care-coordinator/s-f09-31-proposal-review-e-f02-25-request-type-published-{desktop,phone}-{light,dark}.png`, `u29-dispatcher/s-f09-31-proposal-review-e-f02-25-request-type-published-{desktop,phone}-{light,dark}.png` |
| E-F2-25 Request type | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F16-16); fields editable within the role | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f02-25-request-type-draft-{desktop,phone}-{light,dark}.png` |
| E-F2-25 Request type | Retired | Badge "Retired"; next: Published (UC-F2-30); fields editable within the role | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f02-25-request-type-retired-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Drafted | Badge "Drafted"; a new record starts here; next: To confirm or Ready (UC-F16-16, BR-F16-13); fields editable within the role | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-drafted-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | To confirm | Badge "To confirm"; next: Ready (UC-F16-16); fields editable within the role | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-to-confirm-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Ready | Badge "Ready"; next: Proposed, Blocked or Cancelled (UC-F9-33, BR-F9-25, UC-F9-35); fields editable within the role | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-ready-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | In progress | Badge "In progress"; next: Done (BR-F9-06); fields editable within the role | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-12 Work request | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U25 | `u25-care-coordinator/s-f09-31-proposal-review-e-f16-12-work-request-done-{desktop,phone}-{light,dark}.png` |

The states are those of the entity drafts.

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone: the candidates as cards, the best first; the excluded folded; the map on a tab; the footer actions as a sticky
bar.

## Accessibility

The best candidate is said in words ("best"), not only by order or colour; the reasons are text; the override reason
field is announced as required.

## Components

- [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)
- [FL-F2-12 Set up request types](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md)

## Open questions

None.

---

⬅️ [S-F9-30 Scheduling board](s-f09-30-scheduling-board.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-32 Automatic scheduling settings](s-f09-32-automatic-scheduling-settings.md)
