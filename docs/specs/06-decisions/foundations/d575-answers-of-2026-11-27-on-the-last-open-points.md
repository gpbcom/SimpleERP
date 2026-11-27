🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D575 The owner's answers of 2026-11-27 on the last open points

# 📜 D575 The owner's answers of 2026-11-27 on the last open points

**Status:** ✅ decided

## Context

After [D572](d572-proposals-confirmed-in-bulk.md), [D573](d573-precedence-between-spec-pages.md) and
[D574](d574-lawyer-review-before-launch.md), 12 points were still open in the specifications: product values that only
the owner could set, standards and mailbox providers' rules that had been put on the lawyer's list although no law sets
them, France-pack rules that the product pages said were "written later", and a few values of the France country pack
that disagreed with their sources. A 13th came up the same day, once the cinema rule was read: what the product does
while a cinema's ticketing system has no CNC approval recorded.

## Options

- Leave each point open, as a question for a later round.
- Put every point on the lawyer's list of [D574](d574-lawyer-review-before-launch.md).
- Answer each point now, on the owner's word for product values and from official texts for legal values.

## Choice

The owner answers each point now, on 2026-11-27: points 1 to 12 at 16:40, point 13 at 17:08:

| # | Point | The owner's answer |
|---|---|---|
| 1 | The SMS marketing window of [UC-F5-09](../../02-functional/f05-social-media/use-cases/05-benchmark-additions/uc-f05-09-send-sms-campaigns.md) | 8:00 to 20:00, never on Sundays or public holidays: a **product default held in the country pack**, taken from the SMS operators' code of conduct (AF2M), not a law. The company may narrow it |
| 2 | Standards (ISO/IEC, such as ISO/IEC 17065), the VSME sustainability standard and the mailbox providers' bulk-sender rules | **Product references, not lawyer items**: they leave the lawyer's list and their pages cite them as design references |
| 3 | The retention of the voluntary VSME report, [E-F8-25](../../02-functional/f08-accounting/data/e-f08-25-sustainability-report.md) | **10 years**, like the accounting records and the management report (Code de commerce L123-22) |
| 4 | The 13 product pages saying a France-pack rule "is written later" | **Write those France-pack rules now**, from official texts; what cannot be read goes on the lawyer's list (D574) |
| 5 | The connector rights and costs review of [UC-F24-20](../../02-functional/f24-integrations-hub/use-cases/04-run-and-control/uc-f24-20-control-the-rights-and-costs-of-connectors.md) | **Quarterly** by default; the company may make it more frequent |
| 6 | The titles of [BR-SC08-17](../../08-sectors/sc08-non-profit/business-rules/br-sc08-17-aid-per-position-follows-the-approval.md) and [BR-SC20-18](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-18-civil-records-are-corrected-only-by-a-margin-note.md) | **Kept**, with no change of their file names |
| 7 | A care act needs a valid prescription with acts left, [BR-SC04-20](../../08-sectors/sc04-home-care/business-rules/br-sc04-20-care-acts-need-a-prescription.md) | **Kept as the product rule** |
| 8 | Payment after a quote signed at the customer's home, [BR-SC19-20](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-20-a-quote-signed-on-site-carries-the-withdrawal-notice.md) | **Follow the law**: no payment for 7 days after a contract signed at the customer's home (Code de la consommation L221-10), the urgent-repair exception kept (L221-28); the 14-day withdrawal right stays |
| 9 | The health sheet of a camp registration, [E-SC18-15](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-15-camp-registration.md) | It **carries the same lawyer item** as [UC-SC18-19](../../08-sectors/sc18-sports-and-fitness/use-cases/05-facilities-events-camps-and-rentals/uc-sc18-19-run-holiday-camps.md), linked to it and reviewed once |
| 10 | The driver-document reminder of [UC-SC07-04](../../08-sectors/sc07-transport/use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md) | **60 days before the expiry** by default, editable by the company |
| 11 | Four France-pack rules missing: removal quotes, conflicts of interest in foundations, refurbished products, the veterinary dispensing register | **Write them**, from official texts; what cannot be read goes on the lawyer's list (D574) |
| 12 | Values of the France country pack that disagree with their sources: CR-FR-181 (cinema VAT rate), CR-FR-156 (values and dates), CR-FR-222 ("Enforced by" still says "statement"), CR-FR-260 and CR-FR-248 (a "corrected from" left), and [D537](../f18-hosted-websites-and-domains/d537-benchmark-gaps-f18-hosted-websites-and-domains.md) (an F18 screen named "Accessibility statement") | **Fix them from official sources**, and list every changed value for the owner |
| 13 | The CNC approval of a cinema's computerised ticketing system ([BR-SC16-17](../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-17-box-office-figures-are-reported-to-the-cnc.md), [UC-SC16-22](../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-22-run-a-cinema.md)), asked on 2026-11-27 at 17:08 | **Block until approved**: the cinema module sells no ticket until the company has recorded the CNC approval number of its ticketing system and the declaration of its delivery and installation (Code du cinéma et de l'image animée L212-32, [CR-FR-248](../../10-country-packs/france/events/cr-fr-248-cinema-box-office.md)) |

## Decided by

The owner, on 2026-11-27.

## Consequences

- Point 1: [UC-F5-09](../../02-functional/f05-social-media/use-cases/05-benchmark-additions/uc-f05-09-send-sms-campaigns.md)
  states the window as a default of the pack the company may narrow, cites the AF2M code of conduct as a design
  reference, and leaves the lawyer's list.
- Point 2: the lawyer items whose reason was a standard or a mailbox provider's rule became design references, with no
  marker, outside the country pack:
  [UC-F5-16](../../02-functional/f05-social-media/use-cases/06-audiences-consent-and-journeys/uc-f05-16-keep-emails-delivered.md)
  (Gmail, Yahoo and Microsoft bulk-sender rules),
  [UC-F12-21](../../02-functional/f12-manufacturing/use-cases/10-people-and-tools/uc-f12-21-calibrate-measuring-equipment.md)
  (ISO 9001:2015, 7.1.5),
  [UC-F12-24](../../02-functional/f12-manufacturing/use-cases/12-quality-engineering/uc-f12-24-run-an-fmea.md)
  (IEC 60812),
  [UC-F12-25](../../02-functional/f12-manufacturing/use-cases/12-quality-engineering/uc-f12-25-monitor-a-process-with-control-charts.md)
  (ISO 7870-2),
  [UC-F8-28](../../02-functional/f08-accounting/use-cases/09-pay-analyse-and-report/uc-f08-28-prepare-the-sustainability-report.md)
  and
  [UC-F7-24](../../02-functional/f07-purchasing-and-stock/use-cases/09-compliance-and-carbon/uc-f07-24-measure-the-carbon-of-purchases.md)
  (EFRAG VSME),
  [UC-F1-18](../../02-functional/f01-administration/use-cases/11-team-delegation-and-access-review/uc-f01-18-run-an-access-review-campaign.md)
  (ISO/IEC 27001:2022, A 5.18) and
  [UC-SC03-18](../../08-sectors/sc03-services/use-cases/06-staffing-agencies-and-certification/uc-sc03-18-run-certification-audits.md)
  (NF EN ISO/IEC 17065). Each of these pages is now `✅ specified`. A standard is never again a reason for the marker
  of [D574](d574-lawyer-review-before-launch.md).
- Point 3: [E-F8-25](../../02-functional/f08-accounting/data/e-f08-25-sustainability-report.md) keeps the report 10
  years and leaves the lawyer's list.
- Point 4: the France-pack rules written for the 13 pages, each linked from the page that applies it; a value no
  official text gives carries the marker of D574:
  - [CR-FR-263 Free trials of paid services](../../10-country-packs/france/consumer/cr-fr-263-free-trials-of-paid-services.md), for [UC-F14-30](../../02-functional/f14-plugin-store/use-cases/08-trials-instances-and-partners/uc-f14-30-try-a-paid-plugin-free.md);
  - [CR-FR-264 Capital increase decisions and subscriptions](../../10-country-packs/france/company/cr-fr-264-capital-increase.md), for [UC-F15-16](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-16-simulate-a-fundraising-dilution.md);
  - [CR-FR-265 Contract terms the law limits](../../10-country-packs/france/consumer/cr-fr-265-unfair-contract-terms.md), for [UC-F15-17](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-17-draft-a-contract-from-the-clause-library.md);
  - [CR-FR-266 Renewing trademarks, designs and patents](../../10-country-packs/france/digital/cr-fr-266-industrial-property-renewals.md), for [UC-F15-19](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-19-keep-the-companys-ip-portfolio.md);
  - [CR-FR-267 Provisions for litigation](../../10-country-packs/france/accounting/cr-fr-267-litigation-provisions.md), for [UC-F15-20](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-20-keep-the-litigation-register.md), [BR-F15-24](../../02-functional/f15-legal-assistant/business-rules/br-f15-24-a-probable-loss-gets-a-provision-proposal-in-f8.md);
  - [CR-FR-268 Tax deduction of provisions](../../10-country-packs/france/tax-and-vat/cr-fr-268-tax-deduction-of-provisions.md), for [BR-F15-24](../../02-functional/f15-legal-assistant/business-rules/br-f15-24-a-probable-loss-gets-a-provision-proposal-in-f8.md);
  - [CR-FR-269 Hosting user posts (notice and action)](../../10-country-packs/france/digital/cr-fr-269-hosting-user-posts.md), for [UC-F16-18](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-18-run-the-community-forum.md);
  - [CR-FR-270 Prepaid service packs](../../10-country-packs/france/consumer/cr-fr-270-prepaid-services.md), for [UC-F16-22](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-22-sell-prepaid-support-hours.md);
  - [CR-FR-271 General terms and prices for business buyers](../../10-country-packs/france/trade/cr-fr-271-terms-and-prices-for-businesses.md), for [BR-F19-21](../../02-functional/f19-feature-factory/business-rules/br-f19-21-fixed-price-changes-keep-their-price.md);
  - [CR-FR-272 VAT on advance payments for services](../../10-country-packs/france/tax-and-vat/cr-fr-272-vat-on-advance-payments-for-services.md), for [UC-F19-29](../../02-functional/f19-feature-factory/use-cases/07-catalogue-and-co-funding/uc-f19-29-co-fund-a-feature.md);
  - [CR-FR-273 Valuations the law requires](../../10-country-packs/france/company/cr-fr-273-valuations-required-by-law.md), for [UC-F23-34](../../02-functional/f23-what-if-simulation/use-cases/08-budgets-rolling-group-and-valuation/uc-f23-34-value-the-company.md);
  - [CR-FR-274 Transfers outside the EU to a cloud suite](../../10-country-packs/france/data-protection/cr-fr-274-transfers-to-cloud-suites.md), for [UC-F24-29](../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-29-connect-google-workspace-or-microsoft-365.md);
  - [CR-FR-275 Copying personal data for analytics](../../10-country-packs/france/data-protection/cr-fr-275-copying-personal-data-for-analytics.md), for [UC-F24-30](../../02-functional/f24-integrations-hub/use-cases/08-ai-connectors-suites-and-warehouse/uc-f24-30-export-data-to-a-warehouse.md).
- Point 11: the four new France-pack rules, each linked from the page that applies it:
  - [CR-FR-276 Removal quotes and delivery reserves](../../10-country-packs/france/transport/cr-fr-276-removal-quotes.md), for [BR-SC07-17](../../08-sectors/sc07-transport/business-rules/br-sc07-17-the-removal-quote-binds-once-signed.md), [UC-SC07-22](../../08-sectors/sc07-transport/use-cases/07-passengers-removals-courier-and-freight/uc-sc07-22-quote-and-run-house-removals.md);
  - [CR-FR-277 Conflicts of interest in associations and foundations](../../10-country-packs/france/non-profit/cr-fr-277-conflicts-of-interest-in-foundations.md), for [BR-SC08-16](../../08-sectors/sc08-non-profit/business-rules/br-sc08-16-members-with-a-conflict-do-not-vote.md);
  - [CR-FR-278 Refurbished products](../../10-country-packs/france/products/cr-fr-278-refurbished-products.md), for [BR-SC05-17](../../08-sectors/sc05-manufacturing/business-rules/br-sc05-17-every-refurbished-unit-is-graded-and-tested.md);
  - [CR-FR-279 Veterinary medicines dispensing register](../../10-country-packs/france/health-practice/cr-fr-279-veterinary-dispensing-register.md), for [BR-SC09-18](../../08-sectors/sc09-health-practices/business-rules/br-sc09-18-dispensed-medicines-enter-the-register.md).
- Point 4 also covers the 39 other use cases that said a France-pack rule "is written later" (UC-F1-26, UC-F4-31,
  UC-F7-28 and 36 sector use cases of SC05 to SC18), found after the answer: each now links the existing rules that
  hold it, extended where needed (CR-FR-065, CR-FR-111), or one of these new rules:
  - [CR-FR-280 Personal data shared inside a group](../../10-country-packs/france/data-protection/cr-fr-280-personal-data-shared-inside-a-group.md);
  - [CR-FR-281 VAT on deposits for returnable packaging](../../10-country-packs/france/tax-and-vat/cr-fr-281-vat-on-returnable-packaging-deposits.md);
  - [CR-FR-282 Police form for foreign guests](../../10-country-packs/france/hospitality/cr-fr-282-police-form-for-foreign-guests.md);
  - [CR-FR-283 Health data outside care](../../10-country-packs/france/data-protection/cr-fr-283-health-data-outside-care.md);
  - [CR-FR-284 Sports licences and medical certificates](../../10-country-packs/france/non-profit/cr-fr-284-sports-licences-and-medical-certificates.md);
  - [CR-FR-285 Paid sports instructors](../../10-country-packs/france/labour/cr-fr-285-paid-sports-instructors.md);
  - [CR-FR-286 Appeals to public generosity](../../10-country-packs/france/non-profit/cr-fr-286-appeals-to-public-generosity.md);
  - [CR-FR-287 Health centres (centres de santé)](../../10-country-packs/france/health-practice/cr-fr-287-health-centres.md);
  - [CR-FR-288 Furnished tourist rentals](../../10-country-packs/france/real-estate/cr-fr-288-furnished-tourist-rentals.md);
  - [CR-FR-289 Closed-loop payment wristbands](../../10-country-packs/france/payments/cr-fr-289-closed-loop-payment-wristbands.md);
  - [CR-FR-290 Cosmetic products used and sold](../../10-country-packs/france/products/cr-fr-290-cosmetic-products.md);
  - [CR-FR-291 Commissions in pay](../../10-country-packs/france/payroll/cr-fr-291-commissions-in-pay.md).
- Point 8 is held by
  [CR-FR-036 Consumer withdrawal right](../../10-country-packs/france/consumer/cr-fr-036-withdrawal-right.md).
- Point 12: the corrected rules are in the [France country pack](../../10-country-packs/france/README.md). D537 now
  cites the screen
  [S-F18-30 Accessibility](../../02-functional/f18-hosted-websites-and-domains/screens/07-tests-visitors-and-accessibility/s-f18-30-accessibility.md)
  and the list
  [S-F18-L22 Accessibility statements](../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l22-accessibility-statements.md).
- Point 5: [UC-F24-20](../../02-functional/f24-integrations-hub/use-cases/04-run-and-control/uc-f24-20-control-the-rights-and-costs-of-connectors.md)
  is quarterly by default, with a shorter period the company may set. It is a review of rights and costs, apart from
  the yearly review of the default connector list ([D573](d573-precedence-between-spec-pages.md), point 10).
- Point 6: no page is renamed.
- Point 7: [BR-SC04-20](../../08-sectors/sc04-home-care/business-rules/br-sc04-20-care-acts-need-a-prescription.md)
  cites this decision for its count of acts.
- Point 8: [BR-SC19-20](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-20-a-quote-signed-on-site-carries-the-withdrawal-notice.md),
  [UC-SC19-20](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-20-quote-on-site-and-sign-on-the-phone.md)
  and the [SC19 regulatory page](../../08-sectors/sc19-trades-and-home-services/regulatory.md) state the 7-day payment
  ban and the urgent-repair exception; BR-SC19-20 leaves the lawyer's list.
- Point 9: [E-SC18-15](../../08-sectors/sc18-sports-and-fitness/data/e-sc18-15-camp-registration.md) carries the
  marker of D574 for the retention of the health sheet, linked to the same item of UC-SC18-19.
- Point 10: [UC-SC07-04](../../08-sectors/sc07-transport/use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md),
  [BR-SC07-05](../../08-sectors/sc07-transport/business-rules/br-sc07-05-drivers-qualified-and-current.md) and the
  [SC07 open questions](../../08-sectors/sc07-transport/open-questions.md) state the 60-day default.
- Point 13: [BR-SC16-17](../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-17-box-office-figures-are-reported-to-the-cnc.md)
  and [UC-SC16-22](../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-22-run-a-cinema.md)
  refuse every ticket sale of a cinema until its CNC approval number and the declaration date of the delivery and
  installation are recorded, in two new fields of
  [E-SC16-03 Venue room](../../08-sectors/sc16-events-and-culture/data/e-sc16-03-venue-room.md).
- The screens whose text follows these answers are redrawn by the screens work, as in
  [D573](d573-precedence-between-spec-pages.md).
- The [waiting list](../../09-waiting/README.md), the lawyer's checklist, is updated to match.

## Related

- [D572 The owner's proposals confirmed in bulk](d572-proposals-confirmed-in-bulk.md)
- [D573 Which page wins when two specification pages disagree](d573-precedence-between-spec-pages.md)
- [D574 Legal items no official source settles are reviewed by a lawyer before launch](d574-lawyer-review-before-launch.md)
- [France country pack](../../10-country-packs/france/README.md)

---

⬅️ [D574](d574-lawyer-review-before-launch.md) · ⬆️ [Up](README.md)
