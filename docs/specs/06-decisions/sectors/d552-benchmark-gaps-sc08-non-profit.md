🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D552 Benchmark gaps of SC08 Non-profit

# 📜 D552 Benchmark gaps of SC08 Non-profit

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that non-profit suites handle and SC08 did not: grant-making foundations, work-integration enterprises, federations of
clubs and peer-to-peer fundraising. Each carries a duty (no vote with a conflict, aid following the approval, dues
following the headcount, funds paid only to the association).

## Options

- G155 Grant-making foundations: applications with a committee vote that excludes conflicted members, or a spreadsheet
  of applications outside the system.
- G156 Work-integration (IAE): pathways with the approval checked before each aid claim, or the pathway kept as notes on
  the employee record.
- G157 Federations: member organisations with dues from their headcount, or flat dues per club.
- G158 Peer-to-peer fundraising: supporter pages whose gifts go only to the association, or collections run outside the
  association's accounts.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC08 gets four use cases in one new flow, FL-SC08-07, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G155 | Grant-making foundations | UC-SC08-21: committee votes that exclude members with a conflict | "Grant-making foundations" |
| G156 | Work-integration (IAE) | UC-SC08-22: aid per position that follows the approval | "Work-integration (IAE)" |
| G157 | Federations | UC-SC08-23: dues that follow each club's headcount | "Federations" |
| G158 | Peer-to-peer fundraising | UC-SC08-24: funds that go to the association, never the page owner | "Peer-to-peer fundraising" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC08 Non-profit").

## Consequences

- G155 Grant-making foundations:
  [UC-SC08-21](../../08-sectors/sc08-non-profit/use-cases/07-foundations-integration-and-federations/uc-sc08-21-give-grants-as-a-foundation.md),
  [S-SC08-21](../../08-sectors/sc08-non-profit/screens/07-foundations-integration-and-federations/s-sc08-21-grant-making.md)
  and [BR-SC08-16](../../08-sectors/sc08-non-profit/business-rules/br-sc08-16-members-with-a-conflict-do-not-vote.md),
  with [E-SC08-16](../../08-sectors/sc08-non-profit/data/e-sc08-16-grant-application.md) Grant application and its list
  [S-SC08-L16](../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l16-grant-applications.md).
- G156 Work-integration (IAE):
  [UC-SC08-22](../../08-sectors/sc08-non-profit/use-cases/07-foundations-integration-and-federations/uc-sc08-22-run-a-work-integration-enterprise.md),
  [S-SC08-22](../../08-sectors/sc08-non-profit/screens/07-foundations-integration-and-federations/s-sc08-22-work-integration.md)
  and [BR-SC08-17](../../08-sectors/sc08-non-profit/business-rules/br-sc08-17-aid-per-position-follows-the-approval.md),
  with [E-SC08-17](../../08-sectors/sc08-non-profit/data/e-sc08-17-integration-pathway.md) Integration pathway and its
  list [S-SC08-L17](../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l17-integration-pathways.md).
- G157 Federations:
  [UC-SC08-23](../../08-sectors/sc08-non-profit/use-cases/07-foundations-integration-and-federations/uc-sc08-23-run-a-federation-of-member-clubs.md),
  [S-SC08-23](../../08-sectors/sc08-non-profit/screens/07-foundations-integration-and-federations/s-sc08-23-federation.md)
  and [BR-SC08-18](../../08-sectors/sc08-non-profit/business-rules/br-sc08-18-dues-follow-each-clubs-headcount.md), with
  [E-SC08-18](../../08-sectors/sc08-non-profit/data/e-sc08-18-member-organisation.md) Member organisation and its list
  [S-SC08-L18](../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l18-member-organisations.md).
- G158 Peer-to-peer fundraising:
  [UC-SC08-24](../../08-sectors/sc08-non-profit/use-cases/07-foundations-integration-and-federations/uc-sc08-24-let-supporters-fundraise-for-us.md),
  [S-SC08-24](../../08-sectors/sc08-non-profit/screens/07-foundations-integration-and-federations/s-sc08-24-peer-fundraising.md)
  and
  [BR-SC08-19](../../08-sectors/sc08-non-profit/business-rules/br-sc08-19-funds-go-to-the-association-never-the-page-owner.md),
  with [E-SC08-19](../../08-sectors/sc08-non-profit/data/e-sc08-19-fundraising-page.md) Fundraising page and its list
  [S-SC08-L19](../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l19-fundraising-pages.md).
- Drawn in [FL-SC08-07](../../08-sectors/sc08-non-profit/flows/fl-sc08-07-foundations-integration-and-federations.md)
  Foundations, integration, federations, peer fundraising.

## Related

- [FL-SC08-07](../../08-sectors/sc08-non-profit/flows/fl-sc08-07-foundations-integration-and-federations.md)
- [D338 Non-profit sector coverage](d338-non-profit-sector-coverage.md)
- [D340 SC08 use cases](d340-sc08-use-cases.md)
- [U31 Treasurer](../../01-users/personas/u31-treasurer.md)

---

⬅️ [D551 Benchmark gaps of SC07 Transport](d551-benchmark-gaps-sc07-transport.md) · ⬆️ [Up](README.md) ·
➡️ [D553 Benchmark gaps of SC09 Health practices](d553-benchmark-gaps-sc09-health-practices.md)
