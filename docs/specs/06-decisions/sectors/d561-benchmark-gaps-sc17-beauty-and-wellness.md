🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D561 Benchmark gaps of SC17 Beauty and wellness

# 📜 D561 Benchmark gaps of SC17 Beauty and wellness

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found that industry
packages cover beauty and wellness salons, and that the specifications had no sector for them (G14). The owner confirmed
the new sector in the block-by-block interview with the answer "Beauty and wellness", then answered the sector
interview: the extra areas G191 "Loyalty and referrals, Client file with photos, Regulated care records, Chair and cabin
rental" and the staff model G192 "Both models (Recommended)", that is employees and independent renters side by side.
Several duties are legal (cosmetics safety and batch tracing, the declaration of tattoo, piercing and laser, hygiene
training and aftercare, the health data and photos of client files, the validity of gift vouchers, chair rental and
disguised employment, the sharing of tips).

## Options

- G14 Staff and cabin booking: services, staff skills and cabins as bookable resources, or one calendar per person with
  no place.
- G14 Staff and cabin booking: online booking limited to skilled staff and free cabins, or an open request form the
  salon answers.
- G14 Staff and cabin booking: desk bookings with the same rules and confirmation, or free notes in a diary.
- G14 Staff and cabin booking: deposits and no-show fees with terms shown before booking, or no deposit.
- G14 Packages and memberships: packages taken oldest first, or one balance of sessions with no order.
- G14 Packages and memberships: memberships billed as subscriptions with included services, or discounts only.
- G14 Packages and memberships: vouchers built on the shared gift card with the legal validity, or a free voucher code.
- G14 Packages and memberships: balances shown before each sale, or balances read in each list.
- G14 Salon retail and stock: retail through the certified till only, or a separate sale sheet.
- G14 Salon retail and stock: back-bar use recorded per service from a recipe, or stock counted only at inventory.
- G14 Salon retail and stock: orders from each salon's own minimum, or one company-wide minimum.
- G14 Salon retail and stock: a safety record per batch with recall tracing, or the supplier's sheet kept on paper.
- G14 Commissions and tips: commission plans by sale date for employees, or a flat rate by hand.
- G14 Commissions and tips: tips shared by a posted rule, or tips shared informally.
- G14 Commissions and tips: targets seen by the person and the manager, or targets seen by all.
- G14 Commissions and tips: an AI assistant within the asker's rights, or reports only.
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals: chair and cabin
  rental with the renter's own bookings and invoices, or employees only.
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals: care records with
  consent, batches and aftercare, or a booking note.
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals: a client file
  with photos kept only with consent, or notes with no photos.
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals: points and
  referrals on the shared loyalty rules, or a salon-only card.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC17 Beauty and wellness is the seventeenth sector, with five flows and twenty use cases, each with its screen, its rule
and, where it has one, its entity and its list. All at full depth now. The staff model is "Both models (Recommended)"
(G192): employees paid with commissions and tips, and independents who rent a chair and keep their own bookings and
invoices, side by side in one salon. Each legal duty is written in plain words and marked until the
France-pack rule is written; no article is quoted.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G14 | Staff and cabin booking | UC-SC17-01: services, staff skills and cabins set up as bookable resources | "Staff and cabin booking" |
| G14 | Staff and cabin booking | UC-SC17-02: online slots only where a skilled person and a cabin are free | "Staff and cabin booking" |
| G14 | Staff and cabin booking | UC-SC17-03: desk bookings send the same confirmation | "Staff and cabin booking" |
| G14 | Staff and cabin booking | UC-SC17-04: deposits and no-show fees from terms shown before booking | "Staff and cabin booking" |
| G14 | Packages and memberships | UC-SC17-05: packages of sessions used oldest first | "Packages and memberships" |
| G14 | Packages and memberships | UC-SC17-06: memberships billed as subscriptions that stop at cancellation | "Packages and memberships" |
| G14 | Packages and memberships | UC-SC17-07: vouchers with their legal validity period | "Packages and memberships" |
| G14 | Packages and memberships | UC-SC17-08: balances shown before each sale | "Packages and memberships" |
| G14 | Salon retail and stock | UC-SC17-09: retail sales through the certified till | "Salon retail and stock" |
| G14 | Salon retail and stock | UC-SC17-10: back-bar use lowers stock per service | "Salon retail and stock" |
| G14 | Salon retail and stock | UC-SC17-11: orders from each salon's minimum stock | "Salon retail and stock" |
| G14 | Salon retail and stock | UC-SC17-12: a safety record and batch per product | "Salon retail and stock" |
| G14 | Commissions and tips | UC-SC17-13: commissions from the plan in force on the sale date | "Commissions and tips" |
| G14 | Commissions and tips | UC-SC17-14: tips shared by the posted rule | "Commissions and tips" |
| G14 | Commissions and tips | UC-SC17-15: targets seen by the staff member and the manager | "Commissions and tips" |
| G14 | Commissions and tips | UC-SC17-16: an AI assistant within the asker's rights | "Commissions and tips" |
| G191 | Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals | UC-SC17-17: chair and cabin rental, renters keep their own bookings and invoices | "Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals" |
| G191 | Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals | UC-SC17-18: care records need the declared activity and consent | "Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals" |
| G191 | Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals | UC-SC17-19: photos kept only with the client's consent | "Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals" |
| G191 | Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals | UC-SC17-20: points and referrals on the shared loyalty rules | "Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC17 Beauty and wellness
(new)").

## Consequences

- G14 Staff and cabin booking:
  [UC-SC17-01](../../08-sectors/sc17-beauty-and-wellness/use-cases/01-book-staff-and-cabins/uc-sc17-01-set-up-services-staff-and-cabins.md),
  [S-SC17-01](../../08-sectors/sc17-beauty-and-wellness/screens/01-book-staff-and-cabins/s-sc17-01-salon-setup.md) and
  [BR-SC17-01](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-01-a-booking-needs-a-free-staff-member-and-cabin.md),
  with [E-SC17-01](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-01-cabin.md) Cabin and its list
  [S-SC17-L01](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l01-cabins.md).
- G14 Staff and cabin booking:
  [UC-SC17-02](../../08-sectors/sc17-beauty-and-wellness/use-cases/01-book-staff-and-cabins/uc-sc17-02-let-customers-book-online.md),
  [S-SC17-02](../../08-sectors/sc17-beauty-and-wellness/screens/01-book-staff-and-cabins/s-sc17-02-online-booking.md)
  and
  [BR-SC17-02](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-02-online-slots-follow-staff-skills.md),
  with [E-SC17-02](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-02-salon-booking.md) Salon booking and its list
  [S-SC17-L02](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l02-salon-bookings.md).
- G14 Staff and cabin booking:
  [UC-SC17-03](../../08-sectors/sc17-beauty-and-wellness/use-cases/01-book-staff-and-cabins/uc-sc17-03-book-at-the-desk.md),
  [S-SC17-03](../../08-sectors/sc17-beauty-and-wellness/screens/01-book-staff-and-cabins/s-sc17-03-desk-booking.md) and
  [BR-SC17-03](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-03-desk-bookings-send-the-same-confirmation.md).
- G14 Staff and cabin booking:
  [UC-SC17-04](../../08-sectors/sc17-beauty-and-wellness/use-cases/01-book-staff-and-cabins/uc-sc17-04-take-deposits-and-charge-no-shows.md),
  [S-SC17-04](../../08-sectors/sc17-beauty-and-wellness/screens/01-book-staff-and-cabins/s-sc17-04-deposits-and-no-shows.md)
  and
  [BR-SC17-04](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-04-no-show-fees-follow-the-published-terms.md),
  with [E-SC17-03](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-03-booking-deposit.md) Booking deposit and its
  list [S-SC17-L03](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l03-booking-deposits.md).
- G14 Packages and memberships:
  [UC-SC17-05](../../08-sectors/sc17-beauty-and-wellness/use-cases/02-packages-and-memberships/uc-sc17-05-sell-packages-and-prepaid-sessions.md),
  [S-SC17-05](../../08-sectors/sc17-beauty-and-wellness/screens/02-packages-and-memberships/s-sc17-05-packages.md) and
  [BR-SC17-05](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-05-sessions-are-used-oldest-first.md),
  with [E-SC17-04](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-04-session-package.md) Session package and its
  list [S-SC17-L04](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l04-session-packages.md).
- G14 Packages and memberships:
  [UC-SC17-06](../../08-sectors/sc17-beauty-and-wellness/use-cases/02-packages-and-memberships/uc-sc17-06-run-memberships.md),
  [S-SC17-06](../../08-sectors/sc17-beauty-and-wellness/screens/02-packages-and-memberships/s-sc17-06-salon-memberships.md)
  and
  [BR-SC17-06](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-06-membership-dues-stop-at-cancellation.md),
  with [E-SC17-05](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-05-salon-membership.md) Salon membership and
  its list [S-SC17-L05](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l05-salon-memberships.md).
- G14 Packages and memberships:
  [UC-SC17-07](../../08-sectors/sc17-beauty-and-wellness/use-cases/02-packages-and-memberships/uc-sc17-07-sell-and-redeem-gift-vouchers.md),
  [S-SC17-07](../../08-sectors/sc17-beauty-and-wellness/screens/02-packages-and-memberships/s-sc17-07-gift-vouchers.md)
  and
  [BR-SC17-07](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-07-vouchers-keep-their-legal-validity-period.md),
  with [E-SC17-06](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-06-gift-voucher.md) Gift voucher and its list
  [S-SC17-L06](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l06-gift-vouchers.md).
- G14 Packages and memberships:
  [UC-SC17-08](../../08-sectors/sc17-beauty-and-wellness/use-cases/02-packages-and-memberships/uc-sc17-08-follow-customer-balances.md),
  [S-SC17-08](../../08-sectors/sc17-beauty-and-wellness/screens/02-packages-and-memberships/s-sc17-08-customer-balances.md)
  and
  [BR-SC17-08](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-08-balances-are-shown-before-each-sale.md).
- G14 Salon retail and stock:
  [UC-SC17-09](../../08-sectors/sc17-beauty-and-wellness/use-cases/03-salon-retail-and-stock/uc-sc17-09-sell-products-at-the-desk.md),
  [S-SC17-09](../../08-sectors/sc17-beauty-and-wellness/screens/03-salon-retail-and-stock/s-sc17-09-salon-retail.md) and
  [BR-SC17-09](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-09-retail-sales-go-through-the-certified-till.md).
- G14 Salon retail and stock:
  [UC-SC17-10](../../08-sectors/sc17-beauty-and-wellness/use-cases/03-salon-retail-and-stock/uc-sc17-10-record-products-used-in-services.md),
  [S-SC17-10](../../08-sectors/sc17-beauty-and-wellness/screens/03-salon-retail-and-stock/s-sc17-10-back-bar.md) and
  [BR-SC17-10](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-10-back-bar-use-lowers-stock-per-service.md),
  with [E-SC17-07](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-07-product-use.md) Product use and its list
  [S-SC17-L07](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l07-product-uses.md).
- G14 Salon retail and stock:
  [UC-SC17-11](../../08-sectors/sc17-beauty-and-wellness/use-cases/03-salon-retail-and-stock/uc-sc17-11-replenish-the-salon.md),
  [S-SC17-11](../../08-sectors/sc17-beauty-and-wellness/screens/03-salon-retail-and-stock/s-sc17-11-salon-replenishment.md)
  and
  [BR-SC17-11](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-11-orders-follow-minimum-stock-per-salon.md).
- G14 Salon retail and stock:
  [UC-SC17-12](../../08-sectors/sc17-beauty-and-wellness/use-cases/03-salon-retail-and-stock/uc-sc17-12-keep-cosmetics-safety-records.md),
  [S-SC17-12](../../08-sectors/sc17-beauty-and-wellness/screens/03-salon-retail-and-stock/s-sc17-12-cosmetics-safety.md)
  and
  [BR-SC17-12](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-12-products-keep-their-safety-sheet-and-batch.md),
  with [E-SC17-08](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-08-safety-record.md) Safety record and its list
  [S-SC17-L08](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l08-safety-records.md).
- G14 Commissions and tips:
  [UC-SC17-13](../../08-sectors/sc17-beauty-and-wellness/use-cases/04-commissions-and-tips/uc-sc17-13-set-commission-plans.md),
  [S-SC17-13](../../08-sectors/sc17-beauty-and-wellness/screens/04-commissions-and-tips/s-sc17-13-commission-plans.md)
  and
  [BR-SC17-13](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-13-commissions-follow-the-plan-in-force-on-the-sale-date.md),
  with [E-SC17-09](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-09-commission-plan.md) Salon commission plan
  and its list [S-SC17-L09](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l09-commission-plans.md).
- G14 Commissions and tips:
  [UC-SC17-14](../../08-sectors/sc17-beauty-and-wellness/use-cases/04-commissions-and-tips/uc-sc17-14-share-tips.md),
  [S-SC17-14](../../08-sectors/sc17-beauty-and-wellness/screens/04-commissions-and-tips/s-sc17-14-salon-tips.md) and
  [BR-SC17-14](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-14-tips-are-shared-per-the-posted-rule.md),
  with [E-SC17-10](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-10-tip.md) Tip and its list
  [S-SC17-L10](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l10-tips.md).
- G14 Commissions and tips:
  [UC-SC17-15](../../08-sectors/sc17-beauty-and-wellness/use-cases/04-commissions-and-tips/uc-sc17-15-follow-staff-targets.md),
  [S-SC17-15](../../08-sectors/sc17-beauty-and-wellness/screens/04-commissions-and-tips/s-sc17-15-staff-targets.md) and
  [BR-SC17-15](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-15-targets-are-seen-by-the-staff-member-and-the-manager.md).
- G14 Commissions and tips:
  [UC-SC17-16](../../08-sectors/sc17-beauty-and-wellness/use-cases/04-commissions-and-tips/uc-sc17-16-ask-the-assistant-about-the-salon.md),
  [S-SC17-16](../../08-sectors/sc17-beauty-and-wellness/screens/04-commissions-and-tips/s-sc17-16-salon-assistant.md)
  and
  [BR-SC17-16](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-16-answers-follow-the-askers-rights.md).
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals:
  [UC-SC17-17](../../08-sectors/sc17-beauty-and-wellness/use-cases/05-rentals-care-records-and-loyalty/uc-sc17-17-rent-chairs-and-cabins-to-independents.md),
  [S-SC17-17](../../08-sectors/sc17-beauty-and-wellness/screens/05-rentals-care-records-and-loyalty/s-sc17-17-chair-rental.md)
  and
  [BR-SC17-17](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-17-renters-keep-their-own-bookings-and-invoices.md),
  with [E-SC17-11](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-11-rental-contract.md) Rental contract and its
  list [S-SC17-L11](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l11-rental-contracts.md).
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals:
  [UC-SC17-18](../../08-sectors/sc17-beauty-and-wellness/use-cases/05-rentals-care-records-and-loyalty/uc-sc17-18-keep-regulated-care-records.md),
  [S-SC17-18](../../08-sectors/sc17-beauty-and-wellness/screens/05-rentals-care-records-and-loyalty/s-sc17-18-regulated-care.md)
  and
  [BR-SC17-18](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-18-tattoo-piercing-and-laser-need-the-declared-activity-and-consent.md),
  with [E-SC17-12](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-12-care-record.md) Regulated care record and
  its list [S-SC17-L12](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l12-care-records.md).
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals:
  [UC-SC17-19](../../08-sectors/sc17-beauty-and-wellness/use-cases/05-rentals-care-records-and-loyalty/uc-sc17-19-keep-the-client-file-with-photos.md),
  [S-SC17-19](../../08-sectors/sc17-beauty-and-wellness/screens/05-rentals-care-records-and-loyalty/s-sc17-19-client-file.md)
  and
  [BR-SC17-19](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-19-photos-are-kept-only-with-the-clients-consent.md),
  with [E-SC17-13](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-13-client-file.md) Salon client file and its
  list [S-SC17-L13](../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l13-client-files.md).
- G191 Chair and cabin rental, Regulated care records, Client file with photos, Loyalty and referrals:
  [UC-SC17-20](../../08-sectors/sc17-beauty-and-wellness/use-cases/05-rentals-care-records-and-loyalty/uc-sc17-20-run-loyalty-and-referrals.md),
  [S-SC17-20](../../08-sectors/sc17-beauty-and-wellness/screens/05-rentals-care-records-and-loyalty/s-sc17-20-salon-loyalty.md)
  and
  [BR-SC17-20](../../08-sectors/sc17-beauty-and-wellness/business-rules/br-sc17-20-salon-points-follow-the-shared-loyalty-rules.md).
- Drawn in [FL-SC17-01](../../08-sectors/sc17-beauty-and-wellness/flows/fl-sc17-01-book-staff-and-cabins.md) Book staff
  and cabins.
- Drawn in [FL-SC17-02](../../08-sectors/sc17-beauty-and-wellness/flows/fl-sc17-02-packages-and-memberships.md) Packages
  and memberships.
- Drawn in [FL-SC17-03](../../08-sectors/sc17-beauty-and-wellness/flows/fl-sc17-03-salon-retail-and-stock.md) Salon
  retail and stock.
- Drawn in [FL-SC17-04](../../08-sectors/sc17-beauty-and-wellness/flows/fl-sc17-04-commissions-and-tips.md) Commissions
  and tips.
- Drawn in [FL-SC17-05](../../08-sectors/sc17-beauty-and-wellness/flows/fl-sc17-05-rentals-care-records-and-loyalty.md)
  Rentals, care records, client files and loyalty.
- G192 "Both models (Recommended)": the commission plans of
  [UC-SC17-13](../../08-sectors/sc17-beauty-and-wellness/use-cases/04-commissions-and-tips/uc-sc17-13-set-commission-plans.md)
  cover employees only, and
  [UC-SC17-17](../../08-sectors/sc17-beauty-and-wellness/use-cases/05-rentals-care-records-and-loyalty/uc-sc17-17-rent-chairs-and-cabins-to-independents.md)
  gives renters their own calendar, bookings and invoice series.
- The sector list of the specifications and [D114](d114-sixteen-sectors.md) are updated by the main session; this round
  adds the pages of the sector only.
- New entities relate to capability entities rather than replace them:
  [E-SC17-02](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-02-salon-booking.md) to
  [E-F2-18](../../02-functional/f02-no-code-configuration/data/e-f02-18-resource-booking.md),
  [E-SC17-05](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-05-salon-membership.md) to
  [E-F6-07](../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md),
  [E-SC17-06](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-06-gift-voucher.md) to
  [E-F10-10](../../02-functional/f10-point-of-sale/data/e-f10-10-loyalty-card-and-gift-card.md),
  [E-SC17-09](../../08-sectors/sc17-beauty-and-wellness/data/e-sc17-09-commission-plan.md) to
  [E-F6-18](../../02-functional/f06-customers-and-sales/data/e-f06-18-commission-plan-and-target.md).
- The legal reading of 2026-11-27: tips and service charges go in full to the staff in contact with customers
  (Code du travail L3244-1); the posted rule of G14 shares them among those staff only
  ([CR-FR-113](../../10-country-packs/france/labour/cr-fr-113-tips-sharing.md)).

## Related

- [FL-SC17-01](../../08-sectors/sc17-beauty-and-wellness/flows/fl-sc17-01-book-staff-and-cabins.md)
- [D114 Sixteen sectors](d114-sixteen-sectors.md)
- [U52 Beautician](../../01-users/personas/u52-beautician.md)
- [U23 Store manager](../../01-users/personas/u23-store-manager.md)
- [D553 Benchmark gaps of SC09 Health practices](d553-benchmark-gaps-sc09-health-practices.md)

---

⬅️ [D560 Benchmark gaps of SC16 Events and culture](d560-benchmark-gaps-sc16-events-and-culture.md) ·
⬆️ [Up](README.md) ·
➡️ [D562 Benchmark gaps of SC18 Sports and fitness](d562-benchmark-gaps-sc18-sports-and-fitness.md)
