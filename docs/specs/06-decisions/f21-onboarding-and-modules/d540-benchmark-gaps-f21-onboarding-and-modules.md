🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🧭 [Decisions: F21 Onboarding and module activation](README.md) › 📜 D540 Benchmark gaps of F21 Onboarding and modules

# 📜 D540 Benchmark gaps of F21 Onboarding and modules

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four onboarding
features that F21 did not cover: sessions with an implementation expert, a planned go-live cutover, a parallel run of
the old and the new tools, and a set-up proposed from last year's documents. F21 already has the first-run guide, the
imports and the migration from a named tool; these complete the human, the dated and the checked sides.

## Options

- G107 Book an expert: expert sessions quoted before booking, or self-service help only.
- G108 Go-live cutover: a go-live that waits for a complete checklist, or a go-live at the administrator's discretion.
- G109 Parallel run: a parallel run whose differences are explained before the old tool stops, or a cutover with the
  opening balances check only.
- G110 Set up from documents: settings proposed from documents and confirmed by a person, or the guide's questions only.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F21 gets four use cases in one new flow, FL-F21-06, each with its screen and its rule, and three entities with their
lists; the set-up from documents has no entity of its own, since it writes the existing company profile and progress
records after confirmation. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G107 | Book an expert | UC-F21-26: paid sessions quoted before booking | "Book an expert" |
| G108 | Go-live cutover | UC-F21-27: go-live that waits for a complete checklist | "Go-live cutover" |
| G109 | Parallel run | UC-F21-28: differences explained before the old tool stops | "Parallel run" |
| G110 | Set up from documents | UC-F21-29: settings proposed from documents and confirmed by a person | "Set up from documents" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F21 Onboarding and
modules").

## Consequences

- G107 Book an expert:
  [UC-F21-26](../../02-functional/f21-onboarding-and-modules/use-cases/06-experts-cutover-and-parallel-run/uc-f21-26-book-an-implementation-expert.md),
  [S-F21-26](../../02-functional/f21-onboarding-and-modules/screens/06-experts-cutover-and-parallel-run/s-f21-26-expert-booking.md)
  and
  [BR-F21-17](../../02-functional/f21-onboarding-and-modules/business-rules/br-f21-17-paid-sessions-are-quoted-before-booking.md),
  with [E-F21-19](../../02-functional/f21-onboarding-and-modules/data/e-f21-19-expert-session.md) Expert session and its
  list [S-F21-L19](../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l19-expert-sessions.md).
- G108 Go-live cutover:
  [UC-F21-27](../../02-functional/f21-onboarding-and-modules/use-cases/06-experts-cutover-and-parallel-run/uc-f21-27-run-the-go-live-cutover.md),
  [S-F21-27](../../02-functional/f21-onboarding-and-modules/screens/06-experts-cutover-and-parallel-run/s-f21-27-cutover.md)
  and
  [BR-F21-18](../../02-functional/f21-onboarding-and-modules/business-rules/br-f21-18-go-live-waits-for-a-complete-checklist.md),
  with [E-F21-20](../../02-functional/f21-onboarding-and-modules/data/e-f21-20-cutover-plan.md) Cutover plan and its
  list [S-F21-L20](../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l20-cutover-plans.md).
- G109 Parallel run:
  [UC-F21-28](../../02-functional/f21-onboarding-and-modules/use-cases/06-experts-cutover-and-parallel-run/uc-f21-28-run-old-and-new-tools-in-parallel.md),
  [S-F21-28](../../02-functional/f21-onboarding-and-modules/screens/06-experts-cutover-and-parallel-run/s-f21-28-parallel-run.md)
  and
  [BR-F21-19](../../02-functional/f21-onboarding-and-modules/business-rules/br-f21-19-differences-are-explained-before-the-old-tool-stops.md),
  with [E-F21-21](../../02-functional/f21-onboarding-and-modules/data/e-f21-21-parallel-run.md) Parallel run and its
  list [S-F21-L21](../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l21-parallel-runs.md).
- G110 Set up from documents:
  [UC-F21-29](../../02-functional/f21-onboarding-and-modules/use-cases/06-experts-cutover-and-parallel-run/uc-f21-29-set-up-from-last-years-documents.md),
  [S-F21-29](../../02-functional/f21-onboarding-and-modules/screens/06-experts-cutover-and-parallel-run/s-f21-29-setup-from-documents.md)
  and
  [BR-F21-20](../../02-functional/f21-onboarding-and-modules/business-rules/br-f21-20-settings-proposed-from-documents-are-confirmed-by-a-person.md).
- Drawn in
  [FL-F21-06](../../02-functional/f21-onboarding-and-modules/flows/fl-f21-06-experts-cutover-and-parallel-run.md)
  Experts, cutover, parallel run and set-up from documents.

## Related

- [FL-F21-06](../../02-functional/f21-onboarding-and-modules/flows/fl-f21-06-experts-cutover-and-parallel-run.md)
- [D395 Onboarding and one-click modules](d395-onboarding-and-modules-coverage.md)
- [D396 F21 use cases](d396-f21-use-cases.md)
- [D478](d478-f21-gaps-and-improvements.md)
- [BR-F21-13](../../02-functional/f21-onboarding-and-modules/business-rules/br-f21-13-opening-balances-match-last-years-fec.md)
- [BR-F21-12](../../02-functional/f21-onboarding-and-modules/business-rules/br-f21-12-migrations-read-the-old-tools-known-formats.md)

---

⬅️ [D539](../f20-hosted-support-assistant/d539-benchmark-gaps-f20-hosted-support-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [D541](../f22-unified-cost-management/d541-benchmark-gaps-f22-unified-cost-management.md)
