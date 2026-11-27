🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🌐 [Decisions: F18 Hosted websites and domains (hosted edition)](README.md) ›
📜 D537 Benchmark gaps of F18 Hosted websites and domains

# 📜 D537 Benchmark gaps of F18 Hosted websites and domains

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four website
features that F18 did not cover: tests of two versions of a page, tracking of known visitors for sales, an accessibility
check with a published statement, and members-only pages. F18 already builds, publishes and checks sites with domains
and mail records; these add the measurement, the legal and the audience sides.

## Options

- G95 Page A/B tests: page tests that end at significance or an end date, or pages changed by opinion only.
- G96 Visitor tracking for sales: visitor tracking only with consent, or audience totals without any visit record.
- G97 Accessibility (EAA): an accessibility check with a published statement required for shop sites, or no
  accessibility follow-up.
- G98 Members-only pages: members-only pages that are never indexed, or public pages only.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F18 gets four use cases in one new flow, FL-F18-07, each with its screen, its rule, its entity and its list. Page tests
do not replace the tests of F5 on posts and emails, and visit records never replace the anonymous audience figures. All
at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G95 | Page A/B tests | UC-F18-28: page tests that end at significance or at their end date | "Page A/B tests" |
| G96 | Visitor tracking for sales | UC-F18-29: visits tracked only with consent | "Visitor tracking for sales" |
| G97 | Accessibility (EAA) | UC-F18-30: an accessibility check, and the accessibility information published for every shop site, on screen S-F18-30 Accessibility | "Accessibility (EAA)" |
| G98 | Members-only pages | UC-F18-31: members-only pages that are never indexed | "Members-only pages" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F18 Hosted websites and
domains").

## Consequences

- G95 Page A/B tests:
  [UC-F18-28](../../02-functional/f18-hosted-websites-and-domains/use-cases/07-tests-visitors-and-accessibility/uc-f18-28-a-b-test-a-page.md),
  [S-F18-28](../../02-functional/f18-hosted-websites-and-domains/screens/07-tests-visitors-and-accessibility/s-f18-28-page-ab-test.md)
  and
  [BR-F18-22](../../02-functional/f18-hosted-websites-and-domains/business-rules/br-f18-22-tests-end-at-significance-or-their-end-date.md),
  with [E-F18-20](../../02-functional/f18-hosted-websites-and-domains/data/e-f18-20-page-test.md) Page test and its list
  [S-F18-L20](../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l20-page-tests.md).
- G96 Visitor tracking for sales:
  [UC-F18-29](../../02-functional/f18-hosted-websites-and-domains/use-cases/07-tests-visitors-and-accessibility/uc-f18-29-track-known-visitors-for-sales.md),
  [S-F18-29](../../02-functional/f18-hosted-websites-and-domains/screens/07-tests-visitors-and-accessibility/s-f18-29-visitor-tracking.md)
  and
  [BR-F18-23](../../02-functional/f18-hosted-websites-and-domains/business-rules/br-f18-23-visits-are-tracked-only-with-consent.md),
  with [E-F18-21](../../02-functional/f18-hosted-websites-and-domains/data/e-f18-21-visit.md) Visit and its list
  [S-F18-L21](../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l21-visits.md).
- G97 Accessibility (EAA):
  [UC-F18-30 Check and declare accessibility](../../02-functional/f18-hosted-websites-and-domains/use-cases/07-tests-visitors-and-accessibility/uc-f18-30-check-and-declare-accessibility.md),
  the screen
  [S-F18-30 Accessibility](../../02-functional/f18-hosted-websites-and-domains/screens/07-tests-visitors-and-accessibility/s-f18-30-accessibility.md)
  and
  [BR-F18-24 An e-shop publishes its accessibility information](../../02-functional/f18-hosted-websites-and-domains/business-rules/br-f18-24-an-e-shop-publishes-its-accessibility-statement.md),
  with the entity
  [E-F18-22 Accessibility statement](../../02-functional/f18-hosted-websites-and-domains/data/e-f18-22-accessibility-statement.md),
  the page that holds the accessibility information the law asks for
  ([CR-FR-222](../../10-country-packs/france/digital/cr-fr-222-accessibility-statement.md)), and its list
  [S-F18-L22 Accessibility statements](../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l22-accessibility-statements.md)
  ([D575](../foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md)).
- G98 Members-only pages:
  [UC-F18-31](../../02-functional/f18-hosted-websites-and-domains/use-cases/07-tests-visitors-and-accessibility/uc-f18-31-publish-members-only-pages.md),
  [S-F18-31](../../02-functional/f18-hosted-websites-and-domains/screens/07-tests-visitors-and-accessibility/s-f18-31-members-pages.md)
  and
  [BR-F18-25](../../02-functional/f18-hosted-websites-and-domains/business-rules/br-f18-25-members-only-content-is-never-indexed.md),
  with [E-F18-23](../../02-functional/f18-hosted-websites-and-domains/data/e-f18-23-page-audience.md) Page audience and
  its list
  [S-F18-L23](../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l23-page-audiences.md).
- Drawn in
  [FL-F18-07](../../02-functional/f18-hosted-websites-and-domains/flows/fl-f18-07-tests-visitors-and-accessibility.md)
  A/B tests, visitors, accessibility and members.

## Related

- [FL-F18-07](../../02-functional/f18-hosted-websites-and-domains/flows/fl-f18-07-tests-visitors-and-accessibility.md)
- [D385 Hosted websites and domains coverage](d385-hosted-websites-coverage.md)
- [D386 A site is tested before it goes live](d386-website-publication-gate.md)
- [D475](d475-f18-gaps-and-improvements.md)
- [BR-F18-14](../../02-functional/f18-hosted-websites-and-domains/business-rules/br-f18-14-analytics-only-with-consent.md)
- [BR-F18-05](../../02-functional/f18-hosted-websites-and-domains/business-rules/br-f18-05-customer-approves-rollback-kept.md)

---

⬅️ [D536](../f17-competitive-analysis/d536-benchmark-gaps-f17-competitive-analysis.md) · ⬆️ [Up](README.md) ·
➡️ [D538 Benchmark gaps of F19 Feature factory](../f19-feature-factory/d538-benchmark-gaps-f19-feature-factory.md)
