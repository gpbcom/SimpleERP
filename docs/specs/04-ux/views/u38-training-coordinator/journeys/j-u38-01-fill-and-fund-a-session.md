🏠 [Specs](../../../../README.md) › 🎨 [UX](../../../README.md) › 🪟 [Views](../../README.md) ›
🧑‍🏫 [Training coordinator: app shell and home](../README.md) › 🧭 [Journeys](README.md) ›
🧭 J-U38-01 Fill and fund a session

# 🧭 J-U38-01 Fill and fund a session

**Status:** ✅ specified

## Persona

[U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)

## Goal

Full sessions with every learner funded, and a quality file ready for the audit.

## Journey

Satisfaction at each step, from 1 (painful) to 5 (effortless): these scores are drawn from the
specs and confirmed by the owner (D572).

```mermaid
journey
  title Fill and fund a session
  section FL-SC12-01 Offer and sessions
    Plans the session with trainer and room: 4: U38
  section FL-SC12-02 Enrol and fund
    Enrols learners with quotes and agreements: 4: U38
    Gets the funding: 3: U38
  section FL-SC12-03 Deliver and assess
    Collects satisfaction: 4: U38
  section FL-SC12-04 Quality and reports
    Files the evidence in the Qualiopi file: 5: U38
```

## Flowchart

The same steps; each problem is the first error flow of the step's use case (once per use case), shown with the error
message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)).

```mermaid
flowchart TD
  S1["1. Plans the session with trainer and room"]
  S1 -- problem --> E1["Trainer not qualified: not proposed."]
  E1 -. fixed .-> S1
  S2["2. Enrols learners with quotes and agreements"]
  S2 -- problem --> E2["Session full: waiting list."]
  E2 -. fixed .-> S2
  S1 -- done --> S2
  S3["3. Gets the funding"]
  S3 -- problem --> E3["Refused: learner told."]
  E3 -. fixed .-> S3
  S2 -- done --> S3
  S4["4. Collects satisfaction"]
  S4 -- problem --> E4["Low score: action."]
  E4 -. fixed .-> S4
  S3 -- done --> S4
  S5["5. Files the evidence in the Qualiopi file"]
  S5 -- problem --> E5["Evidence missing: listed."]
  E5 -. fixed .-> S5
  S4 -- done --> S5
```

## Steps

| Step | Screen | Use case | What the persona does | What the system does |
|---|---|---|---|---|
| 1 | [S-SC12-02 Sessions](../../../../08-sectors/sc12-education-and-training/screens/01-offer-and-sessions/s-sc12-02-sessions.md) | [UC-SC12-02 Plan sessions with trainers and rooms](../../../../08-sectors/sc12-education-and-training/use-cases/01-offer-and-sessions/uc-sc12-02-plan-sessions-with-trainers-and-rooms.md) | Plans the session with trainer and room | Proposes only qualified trainers; opens enrolment. |
| 2 | [S-SC12-03 Enrolment](../../../../08-sectors/sc12-education-and-training/screens/02-enrol-and-fund/s-sc12-03-enrolment.md) | [UC-SC12-03 Enrol learners with quotes and agreements](../../../../08-sectors/sc12-education-and-training/use-cases/02-enrol-and-fund/uc-sc12-03-enrol-learners-with-quotes-and-agreements.md) | Enrols learners with quotes and agreements | Sends the quote and the agreement to sign; keeps a waiting list when full. |
| 3 | [S-SC12-04 Funding](../../../../08-sectors/sc12-education-and-training/screens/02-enrol-and-fund/s-sc12-04-funding.md) | [UC-SC12-04 Get funding](../../../../08-sectors/sc12-education-and-training/use-cases/02-enrol-and-fund/uc-sc12-04-get-funding.md) | Gets the funding | Records the funder's decision and splits the price. |
| 4 | [S-SC12-09 Satisfaction](../../../../08-sectors/sc12-education-and-training/screens/03-deliver-and-assess/s-sc12-09-satisfaction.md) | [UC-SC12-09 Collect satisfaction](../../../../08-sectors/sc12-education-and-training/use-cases/03-deliver-and-assess/uc-sc12-09-collect-satisfaction.md) | Collects satisfaction | Sends the survey and analyses the answers. |
| 5 | [S-SC12-12 Quality file](../../../../08-sectors/sc12-education-and-training/screens/04-quality-and-reports/s-sc12-12-quality-file.md) | [UC-SC12-12 Keep the Qualiopi evidence file](../../../../08-sectors/sc12-education-and-training/use-cases/04-quality-and-reports/uc-sc12-12-keep-the-qualiopi-evidence-file.md) | Files the evidence in the Qualiopi file | Lists missing evidence and prepares the audit. |

This persona's images of these flows (D120):
[FL-SC12-01 Offer and sessions](../../../../08-sectors/sc12-education-and-training/images/01-offer-and-sessions/u38-training-coordinator/README.md),
[FL-SC12-02 Enrol and fund](../../../../08-sectors/sc12-education-and-training/images/02-enrol-and-fund/u38-training-coordinator/README.md),
[FL-SC12-03 Deliver and assess](../../../../08-sectors/sc12-education-and-training/images/03-deliver-and-assess/u38-training-coordinator/README.md),
[FL-SC12-04 Quality and reports](../../../../08-sectors/sc12-education-and-training/images/04-quality-and-reports/u38-training-coordinator/README.md).

## Open questions

None.

---

⬆️ [Up](README.md)
