🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D564 Benchmark gaps of SC20 Public bodies

# 📜 D564 Benchmark gaps of SC20 Public bodies

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found a public
institution package in another suite (public accounting, procurement, citizen services, public-sector pay) and SC20 did
not exist. French local bodies carry strict duties: the authorising officer and the public accountant are kept apart,
expenditure is committed before it is ordered, acts become enforceable only once published and transmitted, the civil
registry is corrected only by margin notes, and permits have legal delays.

## Options

- G17 Public accounting M57: a budget voted by chapter that caps the credits, or a budget kept in a spreadsheet.
- G17 Public accounting M57: a commitment before every order, or orders placed and recorded afterwards.
- G17 Public accounting M57: payment orders and revenue titles signed by the authorising officer, or one person who
  orders and pays.
- G17 Public accounting M57: batches sent to the public accountant in the national format, or files re-keyed by the
  treasury.
- G17 Public buyer procurement: tender files whose procedure follows the thresholds, or procedures chosen by habit.
- G17 Public buyer procurement: publication in the legal media with the minimum deadline, or an ad on the website only.
- G17 Public buyer procurement: bids scored on the published criteria, or an award decided without a sheet.
- G17 Public buyer procurement: contracts followed with the legal payment term, or invoices paid when seen.
- G17 Citizen services portal: requests acknowledged with a deadline, or requests by email with no tracking.
- G17 Citizen services portal: halls booked at the council's rates with the capacity checked, or a paper diary.
- G17 Citizen services portal: online payment through the public treasury's channel, or payment at the counter only.
- G17 Citizen services portal: decisions posted and transmitted with their dates, or decisions pinned up without a
  record.
- G17 Public-sector HR and pay: grades and steps kept with the statute, or pay grids in a spreadsheet.
- G17 Public-sector HR and pay: pay computed from the index number and the point value, or typed amounts.
- G17 Public-sector HR and pay: contributions by each employee's pension scheme, or one rate for all.
- G17 Public-sector HR and pay: the AI assistant answering from the asker's rights with sources, or figures asked of the
  staff.
- G197 Council meetings, Civil registry, Planning permits, Public assets: council meetings with convocation, quorum,
  votes and transmission, or minutes typed afterwards.
- G197 Council meetings, Civil registry, Planning permits, Public assets: a civil registry corrected only by margin
  notes, or editable records.
- G197 Council meetings, Civil registry, Planning permits, Public assets: permit requests followed against their legal
  delay, or a list checked from time to time.
- G197 Council meetings, Civil registry, Planning permits, Public assets: an asset register depreciated under M57 and
  agreed with the accountant, or a yearly spreadsheet.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC20 Public bodies is a new sector with five flows, FL-SC20-01 to FL-SC20-05, and twenty use cases, each with its
screen, its rule and, for fifteen of them, its entity and its list. The owner confirmed the scope in the benchmark-gaps
interviews of 2026-11-14, answering "Public bodies" (G17), then, in the sector interview, "Council meetings, Civil
registry, Planning permits, Public assets" (G197) and "Local bodies (Recommended)" (G198): communes, groups of communes
and their public establishments such as social action centres and tourist offices, with the M57 accounting framework and
the heritage of M14 for assets carried over. The owner chose "Block by block" for the SC20 pages and "Full depth now"
(G26). Each legal duty is written in plain words and marked as proposed until its France-pack rule was written (the
rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G17 | Public accounting M57 | UC-SC20-01: expenditure stays within the voted credits | "Public accounting M57" |
| G17 | Public accounting M57 | UC-SC20-02: no order without a prior commitment | "Public accounting M57" |
| G17 | Public accounting M57 | UC-SC20-03: orders are signed by the authorising officer | "Public accounting M57" |
| G17 | Public accounting M57 | UC-SC20-04: files follow the public treasury format | "Public accounting M57" |
| G17 | Public buyer procurement | UC-SC20-05: the procedure follows the thresholds | "Public buyer procurement" |
| G17 | Public buyer procurement | UC-SC20-06: publication follows the legal media | "Public buyer procurement" |
| G17 | Public buyer procurement | UC-SC20-07: award follows the published criteria | "Public buyer procurement" |
| G17 | Public buyer procurement | UC-SC20-08: payments meet the legal payment term | "Public buyer procurement" |
| G17 | Citizen services portal | UC-SC20-09: requests are acknowledged with a deadline | "Citizen services portal" |
| G17 | Citizen services portal | UC-SC20-10: bookings follow the council's rates | "Citizen services portal" |
| G17 | Citizen services portal | UC-SC20-11: payments go to the public treasury's channel | "Citizen services portal" |
| G17 | Citizen services portal | UC-SC20-12: decisions are published to become enforceable | "Citizen services portal" |
| G17 | Public-sector HR and pay | UC-SC20-13: step changes follow the seniority rules | "Public-sector HR and pay" |
| G17 | Public-sector HR and pay | UC-SC20-14: pay follows the index points of the grade | "Public-sector HR and pay" |
| G17 | Public-sector HR and pay | UC-SC20-15: contributions follow the employee's scheme | "Public-sector HR and pay" |
| G17 | Public-sector HR and pay | UC-SC20-16: answers follow the asker's rights | "Public-sector HR and pay" |
| G197 | Council meetings, Civil registry, Planning permits, Public assets | UC-SC20-17: deliberations are sent to the prefecture to become enforceable | "Council meetings, Civil registry, Planning permits, Public assets" |
| G197 | Council meetings, Civil registry, Planning permits, Public assets | UC-SC20-18: civil records are corrected only by a margin note | "Council meetings, Civil registry, Planning permits, Public assets" |
| G197 | Council meetings, Civil registry, Planning permits, Public assets | UC-SC20-19: silence after the legal delay counts as the law says | "Council meetings, Civil registry, Planning permits, Public assets" |
| G197 | Council meetings, Civil registry, Planning permits, Public assets | UC-SC20-20: assets follow the M57 depreciation rules | "Council meetings, Civil registry, Planning permits, Public assets" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC20 Public bodies").

## Consequences

- G17 Public accounting M57:
  [UC-SC20-01](../../08-sectors/sc20-public-bodies/use-cases/01-public-accounting/uc-sc20-01-prepare-and-vote-the-budget.md),
  [S-SC20-01](../../08-sectors/sc20-public-bodies/screens/01-public-accounting/s-sc20-01-budget-vote.md) and
  [BR-SC20-01](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-01-expenditure-stays-within-voted-credits.md),
  with [E-SC20-01](../../08-sectors/sc20-public-bodies/data/e-sc20-01-budget.md) Budget and its list
  [S-SC20-L01](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l01-budgets.md).
- G17 Public accounting M57:
  [UC-SC20-02](../../08-sectors/sc20-public-bodies/use-cases/01-public-accounting/uc-sc20-02-commit-expenditure.md),
  [S-SC20-02](../../08-sectors/sc20-public-bodies/screens/01-public-accounting/s-sc20-02-commitments.md) and
  [BR-SC20-02](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-02-no-order-without-a-prior-commitment.md),
  with [E-SC20-02](../../08-sectors/sc20-public-bodies/data/e-sc20-02-commitment.md) Commitment and its list
  [S-SC20-L02](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l02-commitments.md).
- G17 Public accounting M57:
  [UC-SC20-03](../../08-sectors/sc20-public-bodies/use-cases/01-public-accounting/uc-sc20-03-issue-payment-orders-and-revenue-titles.md),
  [S-SC20-03](../../08-sectors/sc20-public-bodies/screens/01-public-accounting/s-sc20-03-orders-and-titles.md) and
  [BR-SC20-03](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-03-orders-are-signed-by-the-authorising-officer.md),
  with [E-SC20-03](../../08-sectors/sc20-public-bodies/data/e-sc20-03-payment-order.md) Payment order and its list
  [S-SC20-L03](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l03-payment-orders.md).
- G17 Public accounting M57:
  [UC-SC20-04](../../08-sectors/sc20-public-bodies/use-cases/01-public-accounting/uc-sc20-04-exchange-with-the-public-treasury.md),
  [S-SC20-04](../../08-sectors/sc20-public-bodies/screens/01-public-accounting/s-sc20-04-treasury-exchange.md) and
  [BR-SC20-04](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-04-files-follow-the-public-treasury-format.md),
  with [E-SC20-04](../../08-sectors/sc20-public-bodies/data/e-sc20-04-treasury-exchange.md) Treasury exchange and its
  list [S-SC20-L04](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l04-treasury-exchanges.md).
- G17 Public buyer procurement:
  [UC-SC20-05](../../08-sectors/sc20-public-bodies/use-cases/02-public-procurement/uc-sc20-05-prepare-a-tender-file.md),
  [S-SC20-05](../../08-sectors/sc20-public-bodies/screens/02-public-procurement/s-sc20-05-tender-file.md) and
  [BR-SC20-05](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-05-the-procedure-follows-the-thresholds.md),
  with [E-SC20-05](../../08-sectors/sc20-public-bodies/data/e-sc20-05-tender-file.md) Tender file and its list
  [S-SC20-L05](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l05-tender-files.md).
- G17 Public buyer procurement:
  [UC-SC20-06](../../08-sectors/sc20-public-bodies/use-cases/02-public-procurement/uc-sc20-06-publish-the-tender.md),
  [S-SC20-06](../../08-sectors/sc20-public-bodies/screens/02-public-procurement/s-sc20-06-tender-publication.md) and
  [BR-SC20-06](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-06-publication-follows-the-legal-media.md).
- G17 Public buyer procurement:
  [UC-SC20-07](../../08-sectors/sc20-public-bodies/use-cases/02-public-procurement/uc-sc20-07-analyse-bids-and-award.md),
  [S-SC20-07](../../08-sectors/sc20-public-bodies/screens/02-public-procurement/s-sc20-07-bid-analysis.md) and
  [BR-SC20-07](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-07-award-follows-the-published-criteria.md),
  with [E-SC20-06](../../08-sectors/sc20-public-bodies/data/e-sc20-06-bid.md) Bid and its list
  [S-SC20-L06](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l06-bids.md).
- G17 Public buyer procurement:
  [UC-SC20-08](../../08-sectors/sc20-public-bodies/use-cases/02-public-procurement/uc-sc20-08-follow-the-public-contract.md),
  [S-SC20-08](../../08-sectors/sc20-public-bodies/screens/02-public-procurement/s-sc20-08-public-contract.md) and
  [BR-SC20-08](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-08-payments-meet-the-legal-payment-term.md),
  with [E-SC20-07](../../08-sectors/sc20-public-bodies/data/e-sc20-07-public-contract.md) Public contract and its list
  [S-SC20-L07](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l07-public-contracts.md).
- G17 Citizen services portal:
  [UC-SC20-09](../../08-sectors/sc20-public-bodies/use-cases/03-citizen-services/uc-sc20-09-receive-a-citizens-request.md),
  [S-SC20-09](../../08-sectors/sc20-public-bodies/screens/03-citizen-services/s-sc20-09-citizen-request.md) and
  [BR-SC20-09](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-09-requests-are-acknowledged-with-a-deadline.md),
  with [E-SC20-08](../../08-sectors/sc20-public-bodies/data/e-sc20-08-citizen-request.md) Citizen request and its list
  [S-SC20-L08](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l08-citizen-requests.md).
- G17 Citizen services portal:
  [UC-SC20-10](../../08-sectors/sc20-public-bodies/use-cases/03-citizen-services/uc-sc20-10-book-halls-and-equipment.md),
  [S-SC20-10](../../08-sectors/sc20-public-bodies/screens/03-citizen-services/s-sc20-10-hall-booking.md) and
  [BR-SC20-10](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-10-bookings-follow-the-councils-rates.md),
  with [E-SC20-09](../../08-sectors/sc20-public-bodies/data/e-sc20-09-hall-booking.md) Hall booking and its list
  [S-SC20-L09](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l09-hall-bookings.md).
- G17 Citizen services portal:
  [UC-SC20-11](../../08-sectors/sc20-public-bodies/use-cases/03-citizen-services/uc-sc20-11-take-online-payments.md),
  [S-SC20-11](../../08-sectors/sc20-public-bodies/screens/03-citizen-services/s-sc20-11-public-payments.md) and
  [BR-SC20-11](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-11-payments-go-to-the-public-treasurys-channel.md).
- G17 Citizen services portal:
  [UC-SC20-12](../../08-sectors/sc20-public-bodies/use-cases/03-citizen-services/uc-sc20-12-publish-council-decisions.md),
  [S-SC20-12](../../08-sectors/sc20-public-bodies/screens/03-citizen-services/s-sc20-12-council-decisions.md) and
  [BR-SC20-12](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-12-decisions-are-published-to-become-enforceable.md),
  with [E-SC20-10](../../08-sectors/sc20-public-bodies/data/e-sc20-10-council-decision.md) Council decision and its list
  [S-SC20-L10](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l10-council-decisions.md).
- G17 Public-sector HR and pay:
  [UC-SC20-13](../../08-sectors/sc20-public-bodies/use-cases/04-public-hr-and-pay/uc-sc20-13-manage-grades-and-steps.md),
  [S-SC20-13](../../08-sectors/sc20-public-bodies/screens/04-public-hr-and-pay/s-sc20-13-grades-and-steps.md) and
  [BR-SC20-13](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-13-step-changes-follow-the-seniority-rules.md),
  with [E-SC20-11](../../08-sectors/sc20-public-bodies/data/e-sc20-11-grade.md) Grade and its list
  [S-SC20-L11](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l11-grades.md).
- G17 Public-sector HR and pay:
  [UC-SC20-14](../../08-sectors/sc20-public-bodies/use-cases/04-public-hr-and-pay/uc-sc20-14-compute-statutory-pay.md),
  [S-SC20-14](../../08-sectors/sc20-public-bodies/screens/04-public-hr-and-pay/s-sc20-14-statutory-pay.md) and
  [BR-SC20-14](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-14-pay-follows-the-index-points-of-the-grade.md).
- G17 Public-sector HR and pay:
  [UC-SC20-15](../../08-sectors/sc20-public-bodies/use-cases/04-public-hr-and-pay/uc-sc20-15-declare-public-sector-contributions.md),
  [S-SC20-15](../../08-sectors/sc20-public-bodies/screens/04-public-hr-and-pay/s-sc20-15-public-contributions.md) and
  [BR-SC20-15](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-15-contributions-follow-the-employees-scheme.md).
- G17 Public-sector HR and pay:
  [UC-SC20-16](../../08-sectors/sc20-public-bodies/use-cases/04-public-hr-and-pay/uc-sc20-16-ask-the-assistant-about-the-budget.md),
  [S-SC20-16](../../08-sectors/sc20-public-bodies/screens/04-public-hr-and-pay/s-sc20-16-budget-assistant.md) and
  [BR-SC20-16](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-16-answers-follow-the-askers-rights.md).
- G197 Council meetings, Civil registry, Planning permits, Public assets:
  [UC-SC20-17](../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-17-run-council-meetings-and-deliberations.md),
  [S-SC20-17](../../08-sectors/sc20-public-bodies/screens/05-council-registry-permits-and-assets/s-sc20-17-council-meetings.md)
  and
  [BR-SC20-17](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-17-deliberations-are-sent-to-the-prefecture-to-become-enforceable.md),
  with [E-SC20-12](../../08-sectors/sc20-public-bodies/data/e-sc20-12-deliberation.md) Deliberation and its list
  [S-SC20-L12](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l12-deliberations.md).
- G197 Council meetings, Civil registry, Planning permits, Public assets:
  [UC-SC20-18](../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-18-keep-the-civil-registry.md),
  [S-SC20-18](../../08-sectors/sc20-public-bodies/screens/05-council-registry-permits-and-assets/s-sc20-18-civil-registry.md)
  and
  [BR-SC20-18](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-18-civil-records-are-corrected-only-by-a-margin-note.md),
  with [E-SC20-13](../../08-sectors/sc20-public-bodies/data/e-sc20-13-civil-record.md) Civil record and its list
  [S-SC20-L13](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l13-civil-records.md).
- G197 Council meetings, Civil registry, Planning permits, Public assets:
  [UC-SC20-19](../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-19-instruct-planning-permits.md),
  [S-SC20-19](../../08-sectors/sc20-public-bodies/screens/05-council-registry-permits-and-assets/s-sc20-19-planning-permits.md)
  and
  [BR-SC20-19](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-19-silence-after-the-legal-delay-counts-as-the-law-says.md),
  with [E-SC20-14](../../08-sectors/sc20-public-bodies/data/e-sc20-14-permit-request.md) Permit request and its list
  [S-SC20-L14](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l14-permit-requests.md).
- G197 Council meetings, Civil registry, Planning permits, Public assets:
  [UC-SC20-20](../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-20-keep-the-public-assets-register.md),
  [S-SC20-20](../../08-sectors/sc20-public-bodies/screens/05-council-registry-permits-and-assets/s-sc20-20-public-assets.md)
  and
  [BR-SC20-20](../../08-sectors/sc20-public-bodies/business-rules/br-sc20-20-assets-follow-the-m57-depreciation-rules.md),
  with [E-SC20-15](../../08-sectors/sc20-public-bodies/data/e-sc20-15-public-asset.md) Public asset and its list
  [S-SC20-L15](../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l15-public-assets.md).
- Drawn in [FL-SC20-01](../../08-sectors/sc20-public-bodies/flows/fl-sc20-01-public-accounting.md) Public accounting.
- Drawn in [FL-SC20-02](../../08-sectors/sc20-public-bodies/flows/fl-sc20-02-public-procurement.md) Public procurement.
- Drawn in [FL-SC20-03](../../08-sectors/sc20-public-bodies/flows/fl-sc20-03-citizen-services.md) Citizen services.
- Drawn in [FL-SC20-04](../../08-sectors/sc20-public-bodies/flows/fl-sc20-04-public-hr-and-pay.md) Public-sector HR and
  pay.
- Drawn in [FL-SC20-05](../../08-sectors/sc20-public-bodies/flows/fl-sc20-05-council-registry-permits-and-assets.md)
  Council, civil registry, permits and assets.
- G17 the sector as a whole: the sector pages of SC20 with its README, regulatory, sector pack and open questions.
- G197 and G198: the four extra areas are
  [UC-SC20-17](../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-17-run-council-meetings-and-deliberations.md)
  to
  [UC-SC20-20](../../08-sectors/sc20-public-bodies/use-cases/05-council-registry-permits-and-assets/uc-sc20-20-keep-the-public-assets-register.md),
  and the bodies in scope are the local bodies.
- [D114](d114-sixteen-sectors.md) and the sector list are updated by the main session.
- The legal reading of 2026-11-27 corrected two duties of the context: a civil record is rectified by order of the
  tribunal president, or administratively for material errors, and binds once published on the registers, rather than
  by a margin note only ([CR-FR-260](../../10-country-packs/france/company/cr-fr-260-civil-registry.md)); the list of deliberations is posted
  within one week, not the minutes ([CR-FR-262](../../10-country-packs/france/company/cr-fr-262-deliberations-legality-check.md)).

## Related

- [FL-SC20-01](../../08-sectors/sc20-public-bodies/flows/fl-sc20-01-public-accounting.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [U54 Public finance officer](../../01-users/personas/u54-public-finance-officer.md)
- [U55 Elected official](../../01-users/personas/u55-elected-official.md)
- [U56 Citizen](../../01-users/personas/u56-citizen.md)

---

⬅️ [D563 Benchmark gaps of SC19 Trades and home services](d563-benchmark-gaps-sc19-trades-and-home-services.md) ·
⬆️ [Up](README.md) · ➡️ [D565 New personas U49 to U56](../foundations/d565-personas-u49-to-u56.md)
