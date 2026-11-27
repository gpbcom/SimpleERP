🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D558 Benchmark gaps of SC14 IT and software

# 📜 D558 Benchmark gaps of SC14 IT and software

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that IT service suites handle and SC14 did not: hardware resale and leasing, licence reselling, the research tax credit
and open-source sponsorship. Three carry a check against a document (the device's return, the distributor's statement,
the timesheet).

## Options

- G179 Hardware resale and leasing: devices followed by serial number until returned, or the lease invoiced from a fixed
  list outside the stock.
- G180 Licence reselling: seats compared with the distributor's statement before invoicing, or invoices sent first and
  corrected later.
- G181 Research tax credit: hours claimed only with approved timesheets, or a yearly estimate from the team.
- G182 Open-source sponsorship: tiers invoiced as subscriptions with their benefits, or sponsors kept in a list outside
  the invoicing.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC14 gets four use cases in one new flow, FL-SC14-07, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G179 | Hardware resale and leasing | UC-SC14-22: devices on lease until their return is scanned and checked | "Hardware resale and leasing" |
| G180 | Licence reselling | UC-SC14-23: seats billed that match the distributor's statement | "Licence reselling" |
| G181 | Research tax credit | UC-SC14-24: claimed hours backed by timesheet evidence | "Research tax credit" |
| G182 | Open-source sponsorship | UC-SC14-25: sponsor tiers invoiced like subscriptions | "Open-source sponsorship" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC14 IT and software").

## Consequences

- G179 Hardware resale and leasing:
  [UC-SC14-22](../../08-sectors/sc14-it-and-software/use-cases/07-hardware-licences-and-tax-credits/uc-sc14-22-resell-and-lease-it-hardware.md),
  [S-SC14-22](../../08-sectors/sc14-it-and-software/screens/07-hardware-licences-and-tax-credits/s-sc14-22-hardware-leasing.md)
  and
  [BR-SC14-16](../../08-sectors/sc14-it-and-software/business-rules/br-sc14-16-leased-devices-stay-listed-until-returned.md),
  with [E-SC14-17](../../08-sectors/sc14-it-and-software/data/e-sc14-17-leased-device.md) Leased device and its list
  [S-SC14-L17](../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l17-leased-devices.md).
- G180 Licence reselling:
  [UC-SC14-23](../../08-sectors/sc14-it-and-software/use-cases/07-hardware-licences-and-tax-credits/uc-sc14-23-resell-cloud-licences.md),
  [S-SC14-23](../../08-sectors/sc14-it-and-software/screens/07-hardware-licences-and-tax-credits/s-sc14-23-licence-reselling.md)
  and
  [BR-SC14-17](../../08-sectors/sc14-it-and-software/business-rules/br-sc14-17-seats-billed-match-the-distributors-statement.md),
  with [E-SC14-18](../../08-sectors/sc14-it-and-software/data/e-sc14-18-licence-subscription.md) Licence subscription
  and its list [S-SC14-L18](../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l18-licence-subscriptions.md).
- G181 Research tax credit:
  [UC-SC14-24](../../08-sectors/sc14-it-and-software/use-cases/07-hardware-licences-and-tax-credits/uc-sc14-24-claim-research-tax-credits.md),
  [S-SC14-24](../../08-sectors/sc14-it-and-software/screens/07-hardware-licences-and-tax-credits/s-sc14-24-research-tax-credit.md)
  and
  [BR-SC14-18](../../08-sectors/sc14-it-and-software/business-rules/br-sc14-18-claimed-hours-have-timesheet-evidence.md),
  with [E-SC14-19](../../08-sectors/sc14-it-and-software/data/e-sc14-19-r-d-project.md) R&D project and its list
  [S-SC14-L19](../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l19-r-d-projects.md).
- G182 Open-source sponsorship:
  [UC-SC14-25](../../08-sectors/sc14-it-and-software/use-cases/07-hardware-licences-and-tax-credits/uc-sc14-25-accept-open-source-sponsorship.md),
  [S-SC14-25](../../08-sectors/sc14-it-and-software/screens/07-hardware-licences-and-tax-credits/s-sc14-25-sponsorship.md)
  and
  [BR-SC14-19](../../08-sectors/sc14-it-and-software/business-rules/br-sc14-19-sponsor-tiers-are-invoiced-like-subscriptions.md),
  with [E-SC14-20](../../08-sectors/sc14-it-and-software/data/e-sc14-20-sponsorship.md) Sponsorship and its list
  [S-SC14-L20](../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l20-sponsorships.md).
- Drawn in [FL-SC14-07](../../08-sectors/sc14-it-and-software/flows/fl-sc14-07-hardware-licences-and-tax-credits.md)
  Hardware, licences, research tax credit and sponsorship.

## Related

- [FL-SC14-07](../../08-sectors/sc14-it-and-software/flows/fl-sc14-07-hardware-licences-and-tax-credits.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [U13 Owner](../../01-users/personas/u13-owner.md)

---

⬅️ [D557 Benchmark gaps of SC13 Agriculture and food](d557-benchmark-gaps-sc13-agriculture-and-food.md) ·
⬆️ [Up](README.md) ·
➡️ [D559 Benchmark gaps of SC15 Wholesale and distribution](d559-benchmark-gaps-sc15-wholesale-and-distribution.md)
