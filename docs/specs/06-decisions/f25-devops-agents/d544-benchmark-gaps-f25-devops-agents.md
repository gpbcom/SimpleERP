🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🤖 [Decisions: F25 DevOps agents (hosted edition)](README.md) › 📜 D544 Benchmark gaps of F25 DevOps agents

# 📜 D544 Benchmark gaps of F25 DevOps agents

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four
product-side features that F25 did not cover: a public roadmap, a beta programme, credits for confirmed bug reports and
a customer-facing changelog. F25 already takes reports and requests, prepares the work, lets maintainers approve and
tells the requester; these show the customers where the product goes and reward their help.

## Options

- G123 Public roadmap: a roadmap of accepted tickets only, or no public roadmap.
- G124 Beta programme: a beta on a sandbox copy only, or betas on live data.
- G125 Bug-report credits: credits for confirmed, non-duplicate reports only, or no reward for reports.
- G126 Customer-facing changelog: a changelog of the installed modules only, or the full release notes for everyone.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F25 gets four use cases in one new flow, FL-F25-07, each with its screen and its rule, and three entities with their
lists; the changelog has no entity of its own, since it reads the release notes the maintainers already write. All at
full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G123 | Public roadmap | UC-F25-25: a public roadmap that shows accepted tickets only | "Public roadmap" |
| G124 | Beta programme | UC-F25-26: a beta programme that runs on a sandbox copy only | "Beta programme" |
| G125 | Bug-report credits | UC-F25-27: credits for confirmed, non-duplicate reports only | "Bug-report credits" |
| G126 | Customer-facing changelog | UC-F25-28: a changelog that shows installed modules only | "Customer-facing changelog" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F25 DevOps agents").

## Consequences

- G123 Public roadmap:
  [UC-F25-25](../../02-functional/f25-devops-agents/use-cases/07-roadmap-beta-and-credits/uc-f25-25-read-the-public-roadmap.md),
  [S-F25-25](../../02-functional/f25-devops-agents/screens/07-roadmap-beta-and-credits/s-f25-25-public-roadmap.md) and
  [BR-F25-18](../../02-functional/f25-devops-agents/business-rules/br-f25-18-the-roadmap-shows-accepted-tickets-only.md),
  with [E-F25-16](../../02-functional/f25-devops-agents/data/e-f25-16-roadmap-item.md) Roadmap item and its list
  [S-F25-L16](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l16-roadmap-items.md).
- G124 Beta programme:
  [UC-F25-26](../../02-functional/f25-devops-agents/use-cases/07-roadmap-beta-and-credits/uc-f25-26-join-the-beta-programme.md),
  [S-F25-26](../../02-functional/f25-devops-agents/screens/07-roadmap-beta-and-credits/s-f25-26-beta-programme.md) and
  [BR-F25-19](../../02-functional/f25-devops-agents/business-rules/br-f25-19-betas-run-on-a-sandbox-copy-only.md), with
  [E-F25-17](../../02-functional/f25-devops-agents/data/e-f25-17-beta-enrolment.md) Beta enrolment and its list
  [S-F25-L17](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l17-beta-enrolments.md).
- G125 Bug-report credits:
  [UC-F25-27](../../02-functional/f25-devops-agents/use-cases/07-roadmap-beta-and-credits/uc-f25-27-receive-credits-for-confirmed-reports.md),
  [S-F25-27](../../02-functional/f25-devops-agents/screens/07-roadmap-beta-and-credits/s-f25-27-report-credits.md) and
  [BR-F25-20](../../02-functional/f25-devops-agents/business-rules/br-f25-20-credits-go-to-confirmed-non-duplicate-reports-only.md),
  with [E-F25-18](../../02-functional/f25-devops-agents/data/e-f25-18-report-credit.md) Report credit and its list
  [S-F25-L18](../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l18-report-credits.md).
- G126 Customer-facing changelog:
  [UC-F25-28](../../02-functional/f25-devops-agents/use-cases/07-roadmap-beta-and-credits/uc-f25-28-follow-the-changelog-of-my-modules.md),
  [S-F25-28](../../02-functional/f25-devops-agents/screens/07-roadmap-beta-and-credits/s-f25-28-module-changelog.md) and
  [BR-F25-21](../../02-functional/f25-devops-agents/business-rules/br-f25-21-the-changelog-shows-installed-modules-only.md).
- Drawn in [FL-F25-07](../../02-functional/f25-devops-agents/flows/fl-f25-07-roadmap-beta-and-credits.md) Roadmap, beta,
  credits and changelog.

## Related

- [FL-F25-07](../../02-functional/f25-devops-agents/flows/fl-f25-07-roadmap-beta-and-credits.md)
- [D432 DevOps agents](d432-devops-agents-coverage.md)
- [D434 Maintainers approve agents' work](d434-maintainer-approval-label.md)
- [D482](d482-f25-gaps-and-improvements.md)
- [BR-F25-15](../../02-functional/f25-devops-agents/business-rules/br-f25-15-vulnerabilities-handled-under-the-cra.md)

---

⬅️ [D543 Benchmark gaps of F24 Integrations hub](../f24-integrations-hub/d543-benchmark-gaps-f24-integrations-hub.md) ·
⬆️ [Up](README.md) ·
➡️ [D545 Benchmark gaps of SC01 Construction](../sectors/d545-benchmark-gaps-sc01-construction.md)
