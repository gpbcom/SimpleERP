🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D547 Benchmark gaps of SC03 Services

# 📜 D547 Benchmark gaps of SC03 Services

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four situations
that services suites handle and SC03 did not: staffing agencies, marketing agencies with media rebilling, certification
bodies and tender answer libraries. Two carry a legal or scheme duty (the signature delay of temporary-work contracts,
the surveillance of certificates).

## Options

- G135 Staffing agencies: assignment contracts with a signature deadline, or consultants' staffing records used for
  temporary workers.
- G136 Marketing agencies: proofs with recorded approvals and media rebilled at cost plus a fee, or approvals by email
  and a lump-sum invoice.
- G137 Certification bodies: certificates with surveillance dates that lapse, or audits billed as ordinary engagements.
- G138 Tender answer library: an answer library with review dates, or documents of past tenders copied by hand.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC03 gets four use cases in one new flow, FL-SC03-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked until its rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G135 | Staffing agencies | UC-SC03-16: assignment contracts signed in two working days | "Staffing agencies" |
| G136 | Marketing agencies | UC-SC03-17: media rebilled at cost plus the agreed fee | "Marketing agencies" |
| G137 | Certification bodies | UC-SC03-18: certificates that lapse without their surveillance audit | "Certification bodies" |
| G138 | Tender answer library | UC-SC03-19: library answers that carry their review date | "Tender answer library" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC03 Services").

## Consequences

- G135 Staffing agencies:
  [UC-SC03-16](../../08-sectors/sc03-services/use-cases/06-staffing-agencies-and-certification/uc-sc03-16-place-temporary-workers.md),
  [S-SC03-16](../../08-sectors/sc03-services/screens/06-staffing-agencies-and-certification/s-sc03-16-staffing-assignments.md)
  and
  [BR-SC03-16](../../08-sectors/sc03-services/business-rules/br-sc03-16-assignment-contracts-are-signed-in-two-working-days.md),
  with [E-SC03-17](../../08-sectors/sc03-services/data/e-sc03-17-assignment-contract.md) Assignment contract and its
  list [S-SC03-L17](../../08-sectors/sc03-services/screens/00-lists/s-sc03-l17-assignment-contracts.md).
- G136 Marketing agencies:
  [UC-SC03-17](../../08-sectors/sc03-services/use-cases/06-staffing-agencies-and-certification/uc-sc03-17-get-creative-work-approved-and-rebill-media.md),
  [S-SC03-17](../../08-sectors/sc03-services/screens/06-staffing-agencies-and-certification/s-sc03-17-agency-approvals.md)
  and
  [BR-SC03-17](../../08-sectors/sc03-services/business-rules/br-sc03-17-media-are-rebilled-at-cost-plus-the-agreed-fee.md),
  with [E-SC03-18](../../08-sectors/sc03-services/data/e-sc03-18-creative-proof.md) Creative proof and its list
  [S-SC03-L18](../../08-sectors/sc03-services/screens/00-lists/s-sc03-l18-creative-proofs.md).
- G137 Certification bodies:
  [UC-SC03-18](../../08-sectors/sc03-services/use-cases/06-staffing-agencies-and-certification/uc-sc03-18-run-certification-audits.md),
  [S-SC03-18](../../08-sectors/sc03-services/screens/06-staffing-agencies-and-certification/s-sc03-18-certification-audits.md)
  and
  [BR-SC03-18](../../08-sectors/sc03-services/business-rules/br-sc03-18-certificates-lapse-without-their-surveillance-audit.md),
  with [E-SC03-19](../../08-sectors/sc03-services/data/e-sc03-19-certificate.md) Certificate and its list
  [S-SC03-L19](../../08-sectors/sc03-services/screens/00-lists/s-sc03-l19-certificates.md).
- G138 Tender answer library:
  [UC-SC03-19](../../08-sectors/sc03-services/use-cases/06-staffing-agencies-and-certification/uc-sc03-19-answer-a-tender-from-the-answer-library.md),
  [S-SC03-19](../../08-sectors/sc03-services/screens/06-staffing-agencies-and-certification/s-sc03-19-answer-library.md)
  and [BR-SC03-19](../../08-sectors/sc03-services/business-rules/br-sc03-19-library-answers-carry-their-review-date.md),
  with [E-SC03-20](../../08-sectors/sc03-services/data/e-sc03-20-answer.md) Answer and its list
  [S-SC03-L20](../../08-sectors/sc03-services/screens/00-lists/s-sc03-l20-answers.md).
- Drawn in [FL-SC03-06](../../08-sectors/sc03-services/flows/fl-sc03-06-staffing-agencies-and-certification.md)
  Staffing, agencies, certification and tender library.

## Related

- [FL-SC03-06](../../08-sectors/sc03-services/flows/fl-sc03-06-staffing-agencies-and-certification.md)
- [D323 Services sector coverage](d323-services-sector-coverage.md)
- [D325 SC03 use cases](d325-sc03-use-cases.md)
- [U24 Engagement manager](../../01-users/personas/u24-engagement-manager.md)

---

⬅️ [D546 Benchmark gaps of SC02 Retail](d546-benchmark-gaps-sc02-retail.md) · ⬆️ [Up](README.md) ·
➡️ [D548 Benchmark gaps of SC04 Home care](d548-benchmark-gaps-sc04-home-care.md)
