🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D563 Benchmark gaps of SC19 Trades and home services

# 📜 D563 Benchmark gaps of SC19 Trades and home services

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found that the
industry packages of other suites cover trades and home services (maintenance contracts, interventions, home-services
credit, installations with labels) and that SC19 did not exist. Home trades carry many duties: legal yearly check-ups,
the home-services tax credit with its advance, labels and grants, insurance and warranties, refrigerant handling, price
information for call-outs and the withdrawal right for quotes signed at home.

## Options

- G16 Maintenance contracts: contracts that list the legal check-up of each equipment, or a yearly price with no
  equipment list.
- G16 Maintenance contracts: visits generated before each legal due date, or visits typed one by one.
- G16 Maintenance contracts: check-ups recorded on the phone with a certificate, or paper forms entered later.
- G16 Maintenance contracts: renewals and index clauses followed at the notice date, or contracts that renew unseen.
- G16 On-site intervention: the nearest qualified technician proposed, or a dispatcher who picks by memory.
- G16 On-site intervention: reports with time, place and photos, or free-text notes.
- G16 On-site intervention: parts taken from the van's stock at use, or parts counted at the end of the week.
- G16 On-site intervention: signature and invoice on the spot, or invoices sent days later.
- G16 Home-services tax credit: household contracts that mark each service eligible or not, or one price for everything.
- G16 Home-services tax credit: recurring visits planned by the contract's frequency, or a calendar kept by hand.
- G16 Home-services tax credit: yearly certificates from the amounts paid, or certificates typed from the invoices.
- G16 Home-services tax credit: the immediate advance with the household's consent, or the household advancing the
  credit.
- G16 Installations and labels: installations as ordered steps with the grant check before works, or one project line.
- G16 Installations and labels: grant files with the label checked at signature, or grants chased after the works.
- G16 Installations and labels: label evidence with its audits planned, or a certificate in a drawer.
- G16 Installations and labels: refrigerant and grid records checked against the certificate, or paper registers.
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone: an on-call rota with the surcharge
  shown before dispatch, or surcharges announced on the invoice.
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone: insurance certificates checked on
  every quote and warranties delivered, or certificates sent on request.
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone: a counted stock for each van
  against a standard load, or one shared warehouse stock.
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone: quotes signed on the phone with the
  withdrawal notice, or paper quotes signed at home.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC19 Trades and home services is a new sector with five flows, FL-SC19-01 to FL-SC19-05, and twenty use cases, each with
its screen, its rule and, for fifteen of them, its entity and its list. The owner confirmed the scope in the
benchmark-gaps interviews of 2026-11-14, answering "Trades and home services" (G16), then, in the sector interview,
"Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone" (G195) and "All home trades
(Recommended)" (G196): plumbing, heating and air conditioning, electricity, solar, locksmiths, handymen, cleaning and
gardening, each a trade option of the sector pack that a company switches on. The owner chose "Block by block" for the
SC19 pages and "Full depth now" (G26). Each legal duty is written in plain words and marked until the
France-pack rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G16 | Maintenance contracts | UC-SC19-01: contracts list the legal yearly check-ups | "Maintenance contracts" |
| G16 | Maintenance contracts | UC-SC19-02: visits planned before the legal due date | "Maintenance contracts" |
| G16 | Maintenance contracts | UC-SC19-03: check-ups recorded with a certificate for the customer | "Maintenance contracts" |
| G16 | Maintenance contracts | UC-SC19-04: renewals follow the notice and index clauses | "Maintenance contracts" |
| G16 | On-site intervention | UC-SC19-05: the nearest qualified technician is proposed | "On-site intervention" |
| G16 | On-site intervention | UC-SC19-06: reports carry time, place and photos | "On-site intervention" |
| G16 | On-site intervention | UC-SC19-07: parts used lower the van's stock | "On-site intervention" |
| G16 | On-site intervention | UC-SC19-08: the invoice follows the signed report | "On-site intervention" |
| G16 | Home-services tax credit | UC-SC19-09: only eligible services carry the tax credit | "Home-services tax credit" |
| G16 | Home-services tax credit | UC-SC19-10: visits follow the contract's frequency | "Home-services tax credit" |
| G16 | Home-services tax credit | UC-SC19-11: certificates list paid amounts only | "Home-services tax credit" |
| G16 | Home-services tax credit | UC-SC19-12: the advance needs the customer's consent | "Home-services tax credit" |
| G16 | Installations and labels | UC-SC19-13: works start after the grant file is filed | "Installations and labels" |
| G16 | Installations and labels | UC-SC19-14: grants need the label at signature | "Installations and labels" |
| G16 | Installations and labels | UC-SC19-15: label audits are planned before expiry | "Installations and labels" |
| G16 | Installations and labels | UC-SC19-16: refrigerant handling needs a certified technician | "Installations and labels" |
| G195 | Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone | UC-SC19-17: call-out surcharges are shown before dispatch | "Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone" |
| G195 | Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone | UC-SC19-18: works start only with a valid insurance certificate | "Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone" |
| G195 | Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone | UC-SC19-19: each van is counted at every reload | "Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone" |
| G195 | Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone | UC-SC19-20: a quote signed on site carries the withdrawal notice | "Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC19 Trades and home
services").

## Consequences

- G16 Maintenance contracts:
  [UC-SC19-01](../../08-sectors/sc19-trades-and-home-services/use-cases/01-maintenance-contracts/uc-sc19-01-sell-a-maintenance-contract.md),
  [S-SC19-01](../../08-sectors/sc19-trades-and-home-services/screens/01-maintenance-contracts/s-sc19-01-maintenance-contract.md)
  and
  [BR-SC19-01](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-01-contracts-list-the-legal-yearly-check-ups.md),
  with [E-SC19-01](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-01-maintenance-contract.md) Maintenance
  contract and its list
  [S-SC19-L01](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l01-maintenance-contracts.md).
- G16 Maintenance contracts:
  [UC-SC19-02](../../08-sectors/sc19-trades-and-home-services/use-cases/01-maintenance-contracts/uc-sc19-02-generate-recurring-visits.md),
  [S-SC19-02](../../08-sectors/sc19-trades-and-home-services/screens/01-maintenance-contracts/s-sc19-02-recurring-visits.md)
  and
  [BR-SC19-02](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-02-visits-are-planned-before-the-legal-due-date.md),
  with [E-SC19-02](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-02-planned-visit.md) Planned visit and its
  list [S-SC19-L02](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l02-planned-visits.md).
- G16 Maintenance contracts:
  [UC-SC19-03](../../08-sectors/sc19-trades-and-home-services/use-cases/01-maintenance-contracts/uc-sc19-03-record-legal-check-ups.md),
  [S-SC19-03](../../08-sectors/sc19-trades-and-home-services/screens/01-maintenance-contracts/s-sc19-03-legal-check-ups.md)
  and
  [BR-SC19-03](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-03-certificates-are-given-to-the-customer.md),
  with [E-SC19-03](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-03-check-up-certificate.md) Check-up
  certificate and its list
  [S-SC19-L03](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l03-check-up-certificates.md).
- G16 Maintenance contracts:
  [UC-SC19-04](../../08-sectors/sc19-trades-and-home-services/use-cases/01-maintenance-contracts/uc-sc19-04-renew-and-index-contracts.md),
  [S-SC19-04](../../08-sectors/sc19-trades-and-home-services/screens/01-maintenance-contracts/s-sc19-04-contract-renewal.md)
  and
  [BR-SC19-04](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-04-renewals-follow-the-notice-and-index-clauses.md).
- G16 On-site intervention:
  [UC-SC19-05](../../08-sectors/sc19-trades-and-home-services/use-cases/02-on-site-intervention/uc-sc19-05-dispatch-an-intervention.md),
  [S-SC19-05](../../08-sectors/sc19-trades-and-home-services/screens/02-on-site-intervention/s-sc19-05-dispatch.md) and
  [BR-SC19-05](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-05-the-nearest-qualified-technician-is-proposed.md),
  with [E-SC19-04](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-04-intervention.md) Intervention and its
  list [S-SC19-L04](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l04-interventions.md).
- G16 On-site intervention:
  [UC-SC19-06](../../08-sectors/sc19-trades-and-home-services/use-cases/02-on-site-intervention/uc-sc19-06-report-on-site-with-photos.md),
  [S-SC19-06](../../08-sectors/sc19-trades-and-home-services/screens/02-on-site-intervention/s-sc19-06-site-report.md)
  and
  [BR-SC19-06](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-06-reports-carry-time-place-and-photos.md),
  with [E-SC19-05](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-05-site-report.md) Site report and its
  list [S-SC19-L05](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l05-site-reports.md).
- G16 On-site intervention:
  [UC-SC19-07](../../08-sectors/sc19-trades-and-home-services/use-cases/02-on-site-intervention/uc-sc19-07-record-parts-used.md),
  [S-SC19-07](../../08-sectors/sc19-trades-and-home-services/screens/02-on-site-intervention/s-sc19-07-parts-used.md)
  and
  [BR-SC19-07](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-07-parts-used-lower-the-vans-stock.md).
- G16 On-site intervention:
  [UC-SC19-08](../../08-sectors/sc19-trades-and-home-services/use-cases/02-on-site-intervention/uc-sc19-08-sign-and-invoice-on-the-spot.md),
  [S-SC19-08](../../08-sectors/sc19-trades-and-home-services/screens/02-on-site-intervention/s-sc19-08-sign-and-invoice.md)
  and
  [BR-SC19-08](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-08-the-invoice-follows-the-signed-report.md).
- G16 Home-services tax credit:
  [UC-SC19-09](../../08-sectors/sc19-trades-and-home-services/use-cases/03-home-services-tax-credit/uc-sc19-09-sell-cleaning-and-gardening-to-households.md),
  [S-SC19-09](../../08-sectors/sc19-trades-and-home-services/screens/03-home-services-tax-credit/s-sc19-09-household-services.md)
  and
  [BR-SC19-09](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-09-only-eligible-services-carry-the-tax-credit.md),
  with [E-SC19-06](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-06-household-contract.md) Household
  contract and its list
  [S-SC19-L06](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l06-household-contracts.md).
- G16 Home-services tax credit:
  [UC-SC19-10](../../08-sectors/sc19-trades-and-home-services/use-cases/03-home-services-tax-credit/uc-sc19-10-plan-recurring-household-visits.md),
  [S-SC19-10](../../08-sectors/sc19-trades-and-home-services/screens/03-home-services-tax-credit/s-sc19-10-household-visits.md)
  and
  [BR-SC19-10](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-10-visits-follow-the-contracts-frequency.md).
- G16 Home-services tax credit:
  [UC-SC19-11](../../08-sectors/sc19-trades-and-home-services/use-cases/03-home-services-tax-credit/uc-sc19-11-issue-the-tax-credit-certificate.md),
  [S-SC19-11](../../08-sectors/sc19-trades-and-home-services/screens/03-home-services-tax-credit/s-sc19-11-tax-credit-certificate.md)
  and
  [BR-SC19-11](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-11-certificates-list-paid-amounts-only.md).
- G16 Home-services tax credit:
  [UC-SC19-12](../../08-sectors/sc19-trades-and-home-services/use-cases/03-home-services-tax-credit/uc-sc19-12-use-the-immediate-advance.md),
  [S-SC19-12](../../08-sectors/sc19-trades-and-home-services/screens/03-home-services-tax-credit/s-sc19-12-immediate-advance.md)
  and
  [BR-SC19-12](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-12-the-advance-needs-the-customers-consent.md).
- G16 Installations and labels:
  [UC-SC19-13](../../08-sectors/sc19-trades-and-home-services/use-cases/04-installations-and-labels/uc-sc19-13-run-an-installation-project.md),
  [S-SC19-13](../../08-sectors/sc19-trades-and-home-services/screens/04-installations-and-labels/s-sc19-13-installation-project.md)
  and
  [BR-SC19-13](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-13-works-start-after-the-grant-file-is-filed.md),
  with [E-SC19-07](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-07-installation.md) Installation and its
  list [S-SC19-L07](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l07-installations.md).
- G16 Installations and labels:
  [UC-SC19-14](../../08-sectors/sc19-trades-and-home-services/use-cases/04-installations-and-labels/uc-sc19-14-file-grants-and-certificates.md),
  [S-SC19-14](../../08-sectors/sc19-trades-and-home-services/screens/04-installations-and-labels/s-sc19-14-installation-grants.md)
  and
  [BR-SC19-14](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-14-grants-need-the-label-at-signature.md),
  with [E-SC19-08](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-08-grant-file.md) Grant file and its list
  [S-SC19-L08](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l08-grant-files.md).
- G16 Installations and labels:
  [UC-SC19-15](../../08-sectors/sc19-trades-and-home-services/use-cases/04-installations-and-labels/uc-sc19-15-keep-the-rge-label-evidence.md),
  [S-SC19-15](../../08-sectors/sc19-trades-and-home-services/screens/04-installations-and-labels/s-sc19-15-rge-evidence.md)
  and
  [BR-SC19-15](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-15-label-audits-are-planned-before-expiry.md),
  with [E-SC19-09](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-09-label.md) Label and its list
  [S-SC19-L09](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l09-labels.md).
- G16 Installations and labels:
  [UC-SC19-16](../../08-sectors/sc19-trades-and-home-services/use-cases/04-installations-and-labels/uc-sc19-16-keep-refrigerant-and-grid-connection-records.md),
  [S-SC19-16](../../08-sectors/sc19-trades-and-home-services/screens/04-installations-and-labels/s-sc19-16-regulated-records.md)
  and
  [BR-SC19-16](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-16-refrigerant-handling-needs-a-certified-technician.md),
  with [E-SC19-10](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-10-regulated-record.md) Regulated record
  and its list
  [S-SC19-L10](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l10-regulated-records.md).
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone:
  [UC-SC19-17](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-17-run-the-emergency-on-call-service.md),
  [S-SC19-17](../../08-sectors/sc19-trades-and-home-services/screens/05-on-call-warranties-van-stock-and-site-quotes/s-sc19-17-on-call.md)
  and
  [BR-SC19-17](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-17-call-out-surcharges-are-shown-before-dispatch.md),
  with [E-SC19-11](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-11-on-call-rota.md) On-call rota and its
  list [S-SC19-L11](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l11-on-call-rotas.md).
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone:
  [UC-SC19-18](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-18-keep-builders-warranties-and-certificates.md),
  [S-SC19-18](../../08-sectors/sc19-trades-and-home-services/screens/05-on-call-warranties-van-stock-and-site-quotes/s-sc19-18-builders-warranties.md)
  and
  [BR-SC19-18](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-18-works-start-only-with-a-valid-insurance-certificate.md),
  with [E-SC19-12](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-12-warranty-certificate.md) Warranty
  certificate and its list
  [S-SC19-L12](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l12-warranty-certificates.md).
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone:
  [UC-SC19-19](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-19-keep-stock-in-each-van.md),
  [S-SC19-19](../../08-sectors/sc19-trades-and-home-services/screens/05-on-call-warranties-van-stock-and-site-quotes/s-sc19-19-van-stock.md)
  and
  [BR-SC19-19](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-19-each-van-is-counted-at-every-reload.md),
  with [E-SC19-13](../../08-sectors/sc19-trades-and-home-services/data/e-sc19-13-van-stock.md) Van stock and its list
  [S-SC19-L13](../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l13-van-stocks.md).
- G195 Emergency on-call, Builders' warranties, Van stock, Site quotes on the phone:
  [UC-SC19-20](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-20-quote-on-site-and-sign-on-the-phone.md),
  [S-SC19-20](../../08-sectors/sc19-trades-and-home-services/screens/05-on-call-warranties-van-stock-and-site-quotes/s-sc19-20-site-quotes.md)
  and
  [BR-SC19-20](../../08-sectors/sc19-trades-and-home-services/business-rules/br-sc19-20-a-quote-signed-on-site-carries-the-withdrawal-notice.md).
- Drawn in [FL-SC19-01](../../08-sectors/sc19-trades-and-home-services/flows/fl-sc19-01-maintenance-contracts.md)
  Maintenance contracts.
- Drawn in [FL-SC19-02](../../08-sectors/sc19-trades-and-home-services/flows/fl-sc19-02-on-site-intervention.md) On-site
  intervention.
- Drawn in [FL-SC19-03](../../08-sectors/sc19-trades-and-home-services/flows/fl-sc19-03-home-services-tax-credit.md)
  Home services tax credit.
- Drawn in [FL-SC19-04](../../08-sectors/sc19-trades-and-home-services/flows/fl-sc19-04-installations-and-labels.md)
  Installations and labels.
- Drawn in
  [FL-SC19-05](../../08-sectors/sc19-trades-and-home-services/flows/fl-sc19-05-on-call-warranties-van-stock-and-site-quotes.md)
  On-call, warranties, van stock and site quotes.
- G16 the sector as a whole: the sector pages of SC19 with its README, regulatory, sector pack and open questions.
- G195 and G196: the four extra areas are
  [UC-SC19-17](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-17-run-the-emergency-on-call-service.md)
  to
  [UC-SC19-20](../../08-sectors/sc19-trades-and-home-services/use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-20-quote-on-site-and-sign-on-the-phone.md),
  and each home trade is an option of the sector pack that a company switches on.
- [D114](d114-sixteen-sectors.md) and the sector list are updated by the main session.

## Related

- [FL-SC19-01](../../08-sectors/sc19-trades-and-home-services/flows/fl-sc19-01-maintenance-contracts.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [U13 Owner](../../01-users/personas/u13-owner.md)
- [U29 Dispatcher](../../01-users/personas/u29-dispatcher.md)
- [U14 Field worker](../../01-users/personas/u14-field-worker.md)

---

⬅️ [D562 Benchmark gaps of SC18 Sports and fitness](d562-benchmark-gaps-sc18-sports-and-fitness.md) ·
⬆️ [Up](README.md) · ➡️ [D564 Benchmark gaps of SC20 Public bodies](d564-benchmark-gaps-sc20-public-bodies.md)
