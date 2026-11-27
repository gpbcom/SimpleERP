🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🛟 [Decisions: F20 Hosted support assistant (hosted edition)](README.md) ›
📜 D539 Benchmark gaps of F20 Hosted support assistant

# 📜 D539 Benchmark gaps of F20 Hosted support assistant

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four support
features that F20 did not cover: calls with a human engineer, consented screen sharing, a monthly health report and
support in more languages. F20 already diagnoses, fixes and reports incidents with the AI assistant and engineers; these
add the personal and the periodic sides of hosted support.

## Options

- G103 Book an engineer: calls booked inside the plan's times, or requests answered in writing only.
- G104 Consented screen sharing: a time-limited, recorded access granted by the customer, or no access beyond the
  namespace readings.
- G105 Monthly health report: a monthly report of technical figures with no personal data, or reports on request only.
- G106 More support languages: more support languages at the same times, or French and English only.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F20 gets four use cases in one new flow, FL-F20-08, each with its screen and its rule, and three entities with their
lists; the languages have no entity of their own, since they are a setting of the company and a catalogue of the support
team. The AI assistant's own rights of D393 are unchanged: the engineer's access is a separate, consented one. All at
full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G103 | Book an engineer | UC-F20-29: calls that follow the plan's times | "Book an engineer" |
| G104 | Consented screen sharing | UC-F20-30: access that ends at its time limit and is audited | "Consented screen sharing" |
| G105 | Monthly health report | UC-F20-31: reports that contain no personal data | "Monthly health report" |
| G106 | More support languages | UC-F20-32: service times that are the same in every supported language | "More support languages" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F20 Hosted support
assistant").

## Consequences

- G103 Book an engineer:
  [UC-F20-29](../../02-functional/f20-hosted-support-assistant/use-cases/08-engineers-sharing-and-reports/uc-f20-29-book-a-call-with-an-engineer.md),
  [S-F20-29](../../02-functional/f20-hosted-support-assistant/screens/08-engineers-sharing-and-reports/s-f20-29-engineer-booking.md)
  and
  [BR-F20-20](../../02-functional/f20-hosted-support-assistant/business-rules/br-f20-20-calls-follow-the-plans-times.md),
  with [E-F20-19](../../02-functional/f20-hosted-support-assistant/data/e-f20-19-engineer-call.md) Engineer call and its
  list [S-F20-L19](../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l19-engineer-calls.md).
- G104 Consented screen sharing:
  [UC-F20-30](../../02-functional/f20-hosted-support-assistant/use-cases/08-engineers-sharing-and-reports/uc-f20-30-share-the-screen-or-a-time-limited-view.md),
  [S-F20-30](../../02-functional/f20-hosted-support-assistant/screens/08-engineers-sharing-and-reports/s-f20-30-consented-access.md)
  and
  [BR-F20-21](../../02-functional/f20-hosted-support-assistant/business-rules/br-f20-21-access-ends-at-its-time-limit-and-is-audited.md),
  with [E-F20-20](../../02-functional/f20-hosted-support-assistant/data/e-f20-20-access-grant.md) Access grant and its
  list [S-F20-L20](../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l20-access-grants.md).
- G105 Monthly health report:
  [UC-F20-31](../../02-functional/f20-hosted-support-assistant/use-cases/08-engineers-sharing-and-reports/uc-f20-31-read-the-monthly-health-report.md),
  [S-F20-31](../../02-functional/f20-hosted-support-assistant/screens/08-engineers-sharing-and-reports/s-f20-31-health-report.md)
  and
  [BR-F20-22](../../02-functional/f20-hosted-support-assistant/business-rules/br-f20-22-reports-contain-no-personal-data.md),
  with [E-F20-21](../../02-functional/f20-hosted-support-assistant/data/e-f20-21-health-report.md) Health report and its
  list [S-F20-L21](../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l21-health-reports.md).
- G106 More support languages:
  [UC-F20-32](../../02-functional/f20-hosted-support-assistant/use-cases/08-engineers-sharing-and-reports/uc-f20-32-get-support-in-more-languages.md),
  [S-F20-32](../../02-functional/f20-hosted-support-assistant/screens/08-engineers-sharing-and-reports/s-f20-32-support-languages.md)
  and
  [BR-F20-23](../../02-functional/f20-hosted-support-assistant/business-rules/br-f20-23-service-times-are-the-same-in-every-supported-language.md).
- Drawn in
  [FL-F20-08](../../02-functional/f20-hosted-support-assistant/flows/fl-f20-08-engineers-sharing-and-reports.md)
  Engineers, screen sharing, reports and languages.

## Related

- [FL-F20-08](../../02-functional/f20-hosted-support-assistant/flows/fl-f20-08-engineers-sharing-and-reports.md)
- [D393 Hosted support assistant: access and approvals](d393-hosted-support-assistant-coverage.md)
- [D394 F20 use cases](d394-f20-use-cases.md)
- [D477](d477-f20-gaps-and-improvements.md)
- [BR-F20-04](../../02-functional/f20-hosted-support-assistant/business-rules/br-f20-04-fixes-need-a-maintainer-yes.md)
- [BR-F20-11](../../02-functional/f20-hosted-support-assistant/business-rules/br-f20-11-response-times-per-plan.md)

---

⬅️ [D538 Benchmark gaps of F19 Feature factory](../f19-feature-factory/d538-benchmark-gaps-f19-feature-factory.md) ·
⬆️ [Up](README.md) · ➡️ [D540](../f21-onboarding-and-modules/d540-benchmark-gaps-f21-onboarding-and-modules.md)
