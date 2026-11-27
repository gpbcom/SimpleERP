🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛒 [Decisions: F6 Customers and sales](README.md) ›
📜 D525 Benchmark gaps of F6 Customers and sales

# 📜 D525 Benchmark gaps of F6 Customers and sales

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found five features
that F6 had no use case for: a partner programme, several identifiers per company, frame contracts, solvency checks and
warranty claims. The new persona U51 Reseller partner works in the partner portal.

## Options

- G24 Partner programme: a partner programme for any company, or only a lead referral field.
- G47 Several identifiers: several checked identifiers per company, or one registration number.
- G48 Frame contracts: frame contracts with call-offs, or repeated quotes.
- G49 Solvency checks: solvency checks through a provider, or the customer's history only.
- G50 Warranty claims: warranty claims with the legal guarantee first, or the helpdesk alone.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F6 gets five use cases in one new flow, each with its screen, its rule, its entity and its list, at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G24 | Partner programme | UC-F6-27: a partner programme where forwarded leads leave their owner's pipeline | "Partner programme" |
| G47 | Several identifiers | UC-F6-28: several identifiers per company, checked per scheme | "Several identifiers" |
| G48 | Frame contracts | UC-F6-29: frame contracts whose call-offs never exceed the balance without approval | "Frame contracts" |
| G49 | Solvency checks | UC-F6-30: solvency checks, with terms above the limit needing a recent report | "Solvency checks" |
| G50 | Warranty claims | UC-F6-31: warranty claims under the legal conformity guarantee first | "Warranty claims" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F6 Customers and sales").

## Consequences

- G24 Partner programme:
  [UC-F6-27](../../02-functional/f06-customers-and-sales/use-cases/10-partners-contracts-and-warranties/uc-f06-27-run-a-partner-programme.md),
  [S-F6-24](../../02-functional/f06-customers-and-sales/screens/10-partners-contracts-and-warranties/s-f06-24-partner-programme.md)
  and
  [BR-F6-19](../../02-functional/f06-customers-and-sales/business-rules/br-f06-19-forwarded-leads-leave-their-owners-pipeline.md),
  with [E-F6-23](../../02-functional/f06-customers-and-sales/data/e-f06-23-partner.md) Partner and its list
  [S-F6-L23](../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l23-partners.md).
- G47 Several identifiers:
  [UC-F6-28](../../02-functional/f06-customers-and-sales/use-cases/10-partners-contracts-and-warranties/uc-f06-28-keep-several-identifiers-per-company.md),
  [S-F6-25](../../02-functional/f06-customers-and-sales/screens/10-partners-contracts-and-warranties/s-f06-25-company-identifiers.md)
  and
  [BR-F6-20](../../02-functional/f06-customers-and-sales/business-rules/br-f06-20-identifiers-are-checked-per-scheme.md),
  with [E-F6-24](../../02-functional/f06-customers-and-sales/data/e-f06-24-company-identifier.md) Company identifier and
  its list [S-F6-L24](../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l24-company-identifiers.md).
- G48 Frame contracts:
  [UC-F6-29](../../02-functional/f06-customers-and-sales/use-cases/10-partners-contracts-and-warranties/uc-f06-29-agree-a-frame-contract-and-call-off-orders.md),
  [S-F6-26](../../02-functional/f06-customers-and-sales/screens/10-partners-contracts-and-warranties/s-f06-26-frame-contracts.md)
  and
  [BR-F6-21](../../02-functional/f06-customers-and-sales/business-rules/br-f06-21-call-offs-never-exceed-the-balance-without-approval.md),
  with [E-F6-25](../../02-functional/f06-customers-and-sales/data/e-f06-25-frame-contract.md) Frame contract and its
  list [S-F6-L25](../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l25-frame-contracts.md).
- G49 Solvency checks:
  [UC-F6-30](../../02-functional/f06-customers-and-sales/use-cases/10-partners-contracts-and-warranties/uc-f06-30-check-a-customers-solvency.md),
  [S-F6-27](../../02-functional/f06-customers-and-sales/screens/10-partners-contracts-and-warranties/s-f06-27-solvency-check.md)
  and
  [BR-F6-22](../../02-functional/f06-customers-and-sales/business-rules/br-f06-22-terms-above-the-limit-need-a-recent-solvency-check.md),
  with [E-F6-26](../../02-functional/f06-customers-and-sales/data/e-f06-26-solvency-report.md) Solvency report and its
  list [S-F6-L26](../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l26-solvency-reports.md).
- G50 Warranty claims:
  [UC-F6-31](../../02-functional/f06-customers-and-sales/use-cases/10-partners-contracts-and-warranties/uc-f06-31-handle-a-warranty-claim.md),
  [S-F6-28](../../02-functional/f06-customers-and-sales/screens/10-partners-contracts-and-warranties/s-f06-28-warranty-claims.md)
  and
  [BR-F6-23](../../02-functional/f06-customers-and-sales/business-rules/br-f06-23-the-legal-conformity-guarantee-applies-first.md),
  with [E-F6-27](../../02-functional/f06-customers-and-sales/data/e-f06-27-warranty.md) Warranty and its list
  [S-F6-L27](../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l27-warranties.md).
- Drawn in [FL-F6-10](../../02-functional/f06-customers-and-sales/flows/fl-f06-10-partners-contracts-and-warranties.md)
  Partners, frame contracts and warranties.

## Related

- [FL-F6-10](../../02-functional/f06-customers-and-sales/flows/fl-f06-10-partners-contracts-and-warranties.md)
- [BR-F6-18](../../02-functional/f06-customers-and-sales/business-rules/br-f06-18-commissions-follow-paid-invoices.md)
- [U51 Reseller partner](../../01-users/personas/u51-reseller-partner.md)

---

⬅️ [D524 Benchmark gaps of F5 Social media and marketing](../f05-social-media/d524-benchmark-gaps-f05-social-media.md) ·
⬆️ [Up](README.md) · ➡️ [D526](../f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)
