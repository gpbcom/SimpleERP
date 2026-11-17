🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D528 Benchmark gaps of F9 HR and projects

# 📜 D528 Benchmark gaps of F9 HR and projects

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the HR, learning and project features of the
benchmarked suites and offered each gap as an option
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F9 HR and projects").

## Options

- Take each gap as a use case of F9 in a new flow, or leave it out.
- Where a gap overlaps an existing use case, extend that use case or add a new one.

## Choice

The owner selected all five gaps; each becomes a use case of F9, drawn in
[FL-F9-15 Work location, headcount, careers and learning](../../02-functional/f09-hr-and-projects/flows/fl-f09-15-work-location-headcount-and-learning.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G59 | [UC-F9-43 Declare remote-work days](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-43-declare-remote-work-days.md) | "Remote-work days" |
| G60 | [UC-F9-44 Plan headcount against budget](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-44-plan-headcount-against-budget.md) | "Headcount planning" |
| G61 | [UC-F9-45 Plan careers and successors](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-45-plan-careers-and-successors.md) | "Careers and succession" |
| G62 | [UC-F9-46 Log project risks and change requests](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-46-log-project-risks-and-change-requests.md) | "Project risks and changes" |
| G08 | [UC-F9-47 Publish and sell online courses](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-47-publish-and-sell-online-courses.md) | "Sell online courses" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "Block by block").

## Consequences

- Use cases
  [UC-F9-43 Declare remote-work days](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-43-declare-remote-work-days.md)
  to
  [UC-F9-47 Publish and sell online courses](../../02-functional/f09-hr-and-projects/use-cases/15-work-location-headcount-and-learning/uc-f09-47-publish-and-sell-online-courses.md),
  screens
  [S-F9-40 Work location](../../02-functional/f09-hr-and-projects/screens/15-work-location-headcount-and-learning/s-f09-40-work-location.md)
  to
  [S-F9-44 Online courses](../../02-functional/f09-hr-and-projects/screens/15-work-location-headcount-and-learning/s-f09-44-online-courses.md),
  rules
  [BR-F9-42 Remote-work allowances follow the agreement](../../02-functional/f09-hr-and-projects/business-rules/br-f09-42-remote-work-allowances-follow-the-agreement.md)
  to
  [BR-F9-46 Certificates follow a passed assessment](../../02-functional/f09-hr-and-projects/business-rules/br-f09-46-certificates-follow-a-passed-assessment.md),
  entities [E-F9-48 Work location day](../../02-functional/f09-hr-and-projects/data/e-f09-48-work-location-day.md) to
  [E-F9-52 Online course](../../02-functional/f09-hr-and-projects/data/e-f09-52-online-course.md) and their lists
  [S-F9-L48 Work location days](../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l48-work-location-days.md)
  to [S-F9-L52 Online courses](../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l52-online-courses.md).
- The tax and social treatment of the remote-work allowance, the information to give employees on succession
  planning and the training-provider rules each need a France pack rule, written later.
- A project risk is a line of the project's register, not an entity of its own.

## Related

- [FL-F9-15 Work location, headcount, careers and learning](../../02-functional/f09-hr-and-projects/flows/fl-f09-15-work-location-headcount-and-learning.md)
- [D458 F1 Administration: gaps and improvements](../f01-administration/d458-f01-gaps-and-improvements.md)
- [Interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)

---

⬅️ [D527 Benchmark gaps of F8 Accounting](../f08-accounting/d527-benchmark-gaps-f08-accounting.md) ·
⬆️ [Up](README.md) ·
➡️ [D529 Benchmark gaps of F10 Point of sale](../f10-point-of-sale/d529-benchmark-gaps-f10-point-of-sale.md)
