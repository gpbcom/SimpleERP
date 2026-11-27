🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D546 Benchmark gaps of SC02 Retail

# 📜 D546 Benchmark gaps of SC02 Retail

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that retail suites handle and SC02 did not: bookshops under the fixed book price, made-to-order furniture, second-hand
buy-back and franchise networks. Three carry a legal duty (the discount cap, the police register, the disclosure before
a franchise agreement).

## Options

- G131 Book trade: a book price rule with the 5 % cap in the till, or manual discounts checked by the cashier.
- G132 Furniture orders: made-to-order orders with dates tied to the supplier's confirmation, or ordinary orders with a
  free date.
- G133 Second-hand buy-back: a purchase register written before payment, or purchases noted outside the system.
- G134 Franchise network: franchisees with agreements, statements and royalty invoices, or the stores of other companies
  handled as ordinary customers.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC02 gets four use cases in one new flow, FL-SC02-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G131 | Book trade | UC-SC02-16: book discounts capped at 5 % of the publisher's price | "Book trade" |
| G132 | Furniture orders | UC-SC02-17: promised dates that follow the supplier's confirmed lead time | "Furniture orders" |
| G133 | Second-hand buy-back | UC-SC02-18: every purchase from a person entered in the register | "Second-hand buy-back" |
| G134 | Franchise network | UC-SC02-19: royalties that follow the franchise agreement | "Franchise network" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC02 Retail").

## Consequences

- G131 Book trade:
  [UC-SC02-16](../../08-sectors/sc02-retail/use-cases/06-books-furniture-second-hand-franchise/uc-sc02-16-sell-books-under-the-fixed-price-law.md),
  [S-SC02-16](../../08-sectors/sc02-retail/screens/06-books-furniture-second-hand-franchise/s-sc02-16-book-trade.md) and
  [BR-SC02-16](../../08-sectors/sc02-retail/business-rules/br-sc02-16-book-discounts-never-exceed-5-of-the-publishers-price.md),
  with [E-SC02-13](../../08-sectors/sc02-retail/data/e-sc02-13-book-title.md) Book title and its list
  [S-SC02-L13](../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l13-book-titles.md).
- G132 Furniture orders:
  [UC-SC02-17](../../08-sectors/sc02-retail/use-cases/06-books-furniture-second-hand-franchise/uc-sc02-17-sell-made-to-order-furniture.md),
  [S-SC02-17](../../08-sectors/sc02-retail/screens/06-books-furniture-second-hand-franchise/s-sc02-17-furniture-orders.md)
  and
  [BR-SC02-17](../../08-sectors/sc02-retail/business-rules/br-sc02-17-dates-follow-the-suppliers-confirmed-lead-time.md),
  with [E-SC02-14](../../08-sectors/sc02-retail/data/e-sc02-14-furniture-order.md) Furniture order and its list
  [S-SC02-L14](../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l14-furniture-orders.md).
- G133 Second-hand buy-back:
  [UC-SC02-18](../../08-sectors/sc02-retail/use-cases/06-books-furniture-second-hand-franchise/uc-sc02-18-buy-back-second-hand-goods.md),
  [S-SC02-18](../../08-sectors/sc02-retail/screens/06-books-furniture-second-hand-franchise/s-sc02-18-second-hand.md)
  and
  [BR-SC02-18](../../08-sectors/sc02-retail/business-rules/br-sc02-18-every-purchase-from-a-person-enters-the-police-register.md),
  with [E-SC02-15](../../08-sectors/sc02-retail/data/e-sc02-15-second-hand-purchase.md) Second-hand purchase and its
  list [S-SC02-L15](../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l15-second-hand-purchases.md).
- G134 Franchise network:
  [UC-SC02-19](../../08-sectors/sc02-retail/use-cases/06-books-furniture-second-hand-franchise/uc-sc02-19-run-a-franchise-network.md),
  [S-SC02-19](../../08-sectors/sc02-retail/screens/06-books-furniture-second-hand-franchise/s-sc02-19-franchise-network.md)
  and [BR-SC02-19](../../08-sectors/sc02-retail/business-rules/br-sc02-19-royalties-follow-the-franchise-agreement.md),
  with [E-SC02-16](../../08-sectors/sc02-retail/data/e-sc02-16-franchisee.md) Franchisee and its list
  [S-SC02-L16](../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l16-franchisees.md).
- Drawn in [FL-SC02-06](../../08-sectors/sc02-retail/flows/fl-sc02-06-books-furniture-second-hand-franchise.md) Books,
  furniture, second-hand and franchise.

## Related

- [FL-SC02-06](../../08-sectors/sc02-retail/flows/fl-sc02-06-books-furniture-second-hand-franchise.md)
- [D320 Retail sector coverage](d320-retail-sector-coverage.md)
- [D322 SC02 use cases](d322-sc02-use-cases.md)
- [U23 Store manager](../../01-users/personas/u23-store-manager.md)

---

⬅️ [D545 Benchmark gaps of SC01 Construction](d545-benchmark-gaps-sc01-construction.md) · ⬆️ [Up](README.md) ·
➡️ [D547 Benchmark gaps of SC03 Services](d547-benchmark-gaps-sc03-services.md)
