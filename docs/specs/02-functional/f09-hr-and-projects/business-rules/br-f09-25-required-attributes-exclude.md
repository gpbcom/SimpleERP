🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-25 Required attributes exclude a candidate

# 📏 BR-F9-25 Required attributes exclude a candidate

**Status:** 🔄 draft (GH-2 step S4b, from VD-27, VD-28, VD-29 / D509, D510, D511)

## Statement

A person is offered for a work request or an operation only when they hold every attribute it requires, verified and
current; a person missing one is excluded, with the missing attribute as the reason, and the preferred attributes only
rank the people left.

## Why

- The owner's decisions VD-27 to VD-29
  [D509](../../../06-decisions/f09-hr-and-projects/d509-four-attribute-families-for-scheduling.md),
  [D510](../../../06-decisions/f09-hr-and-projects/d510-attributes-chosen-per-request-type-adjustable-per-request.md),
  [D511](../../../06-decisions/f09-hr-and-projects/d511-required-or-preferred-attributes-legal-ones-always-required.md):
  - scheduling may use four families of attributes: degrees and qualifications; skills and languages; place and travel;
    person and contract;
  - a configurator selects them per request type
    ([E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)), each one required or
    preferred with a weight; the planner may add or relax one on a single request, logged (BR-F9-34);
  - legal requirements are always required (BR-F9-26).
- One mechanism instead of one per domain. These rules are requirements on it, each set on a request type or an
  operation:

  | Rule | Request type or operation | Requirement |
  |---|---|---|
  | [BR-F12-17](../../f12-manufacturing/business-rules/br-f12-17-operators-sign-in-only-where-qualified.md) | Operation: sign in at a work centre | The work centre's qualifications |
  | [BR-SC05-13](../../../08-sectors/sc05-manufacturing/business-rules/br-sc05-13-operators-qualified-for-the-operation.md) | Operation: start a manufacturing operation | The operation's qualification |
  | [BR-F9-17](br-f09-17-mandatory-trainings-must-be-current-for-the-work-that-needs-them.md) | Any request type or operation needing a training | The mandatory training, current |
  | [BR-F9-22](br-f09-22-rounds-respect-travel-skills-continuity-and-working-time.md) | Request types of round visits | The visit's skills |
  | [BR-SC03-13](../../../08-sectors/sc03-services/business-rules/br-sc03-13-skills-kept-current.md) | Request type: staffing of an engagement | Skills and certifications at their level |
  | [BR-SC04-06](../../../08-sectors/sc04-home-care/business-rules/br-sc04-06-carers-match-the-needs.md) | Request type: home-care visit | The care plan's skills and qualifications |
  | [BR-SC07-05](../../../08-sectors/sc07-transport/business-rules/br-sc07-05-drivers-qualified-and-current.md) | Request type: trip | Licence, driver card, training |
  | [BR-SC07-09](../../../08-sectors/sc07-transport/business-rules/br-sc07-09-dangerous-goods-checked.md) | Request type: dangerous-goods trip | Dangerous-goods training |
  | [BR-SC12-07](../../../08-sectors/sc12-education-and-training/business-rules/br-sc12-07-quality-evidence-kept.md) | Request type: training session | The trainer's skills |

## Examples

| Case | Result |
|---|---|
| A visit whose request type requires the nursing qualification | Carers without it are excluded: "not eligible: qualification missing" |
| A request type that prefers English, weight 3 | Nobody is excluded; English speakers rank higher |
| A forklift job requiring CACES; a candidate's expired last week | Excluded: "not eligible: CACES expired" (BR-F9-27) |
| Maximum travel required, 45 minutes; a home 70 minutes away | Excluded: "not eligible: too far" |
| Nobody left after the exclusions | The work request is Blocked, with each person's reason; the planner decides: subcontract, move the window, train, refuse |
| The planner relaxes "Spanish" on one request | Spanish no longer excludes anyone for that request; logged with the reason (BR-F9-34) |

## Applies to

- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-34](../use-cases/12-schedule-customer-requests/uc-f09-34-run-the-automatic-scheduling.md)
- [UC-F9-35 Re-plan after a change](../use-cases/12-schedule-customer-requests/uc-f09-35-re-plan-after-a-change.md)
- [UC-F2-30](../../f02-no-code-configuration/use-cases/12-set-up-request-types/uc-f02-30-set-up-a-request-type.md)
- [E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)
- [E-F16-12 Work request](../../f16-customer-support-agents/data/e-f16-12-work-request.md)
- [E-F9-28 Assignment proposal](../data/e-f09-28-assignment-proposal.md)
- [E-F9-01 Employee record](../data/e-f09-01-employee-record.md)
- [E-F9-12 Qualification](../data/e-f09-12-certification.md)
- [E-F9-29 Degree](../data/e-f09-29-degree.md)

## Exceptions

A required attribute that is not a legal one may be relaxed by the planner on a single request, with a reason
(BR-F9-34). A legal one never is (BR-F9-26).

## Configurable

Yes:
- per request type, by a configurator: which attributes count, each required or preferred, and the weights (UC-F2-30);
- per work request, by the planner: one attribute added or relaxed, logged.

## Open questions

None.

---

⬅️ [BR-F9-24 No work without vigilance documents](br-f09-24-no-work-without-vigilance-documents.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F9-26 Legal requirements are never relaxed](br-f09-26-legal-requirements-never-relaxed.md)
