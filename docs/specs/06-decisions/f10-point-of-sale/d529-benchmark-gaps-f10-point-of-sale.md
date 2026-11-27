🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏪 [Decisions: F10 Point of sale (plugin)](README.md) ›
📜 D529 Benchmark gaps of F10 Point of sale

# 📜 D529 Benchmark gaps of F10 Point of sale

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the point-of-sale features of the benchmarked
suites and offered each gap as an option
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F10 Point of sale").

## Options

- Take each gap as a use case of F10 in a new flow, or leave it out.
- Where a gap overlaps an existing use case, extend that use case or add a new one.

## Choice

The owner selected all four gaps; each becomes a use case of F10, drawn in
[FL-F10-12 Takeaway, tap to pay, labels and layaway](../../02-functional/f10-point-of-sale/flows/fl-f10-12-takeaway-softpos-and-labels.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G63 | [UC-F10-29 Take online takeaway orders](../../02-functional/f10-point-of-sale/use-cases/12-takeaway-softpos-and-labels/uc-f10-29-take-online-takeaway-orders.md) | "Online takeaway" |
| G64 | [UC-F10-30 Take payment by tap on phone](../../02-functional/f10-point-of-sale/use-cases/12-takeaway-softpos-and-labels/uc-f10-30-take-payment-by-tap-on-phone.md) | "Tap to pay on phone" |
| G65 | [UC-F10-31 Update electronic shelf labels](../../02-functional/f10-point-of-sale/use-cases/12-takeaway-softpos-and-labels/uc-f10-31-update-electronic-shelf-labels.md) | "Electronic shelf labels" |
| G66 | [UC-F10-32 Hold an item with a deposit or park a sale](../../02-functional/f10-point-of-sale/use-cases/12-takeaway-softpos-and-labels/uc-f10-32-hold-an-item-with-a-deposit-or-park-a-sale.md) | "Layaway and parked sales" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "Block by block").

## Consequences

- Use cases
  [UC-F10-29 Take online takeaway orders](../../02-functional/f10-point-of-sale/use-cases/12-takeaway-softpos-and-labels/uc-f10-29-take-online-takeaway-orders.md)
  to
  [UC-F10-32 Hold an item with a deposit or park a sale](../../02-functional/f10-point-of-sale/use-cases/12-takeaway-softpos-and-labels/uc-f10-32-hold-an-item-with-a-deposit-or-park-a-sale.md),
  screens
  [S-F10-28 Online takeaway](../../02-functional/f10-point-of-sale/screens/12-takeaway-softpos-and-labels/s-f10-28-online-takeaway.md)
  to
  [S-F10-31 Layaway](../../02-functional/f10-point-of-sale/screens/12-takeaway-softpos-and-labels/s-f10-31-layaway.md),
  rules
  [BR-F10-23 Online orders stay within kitchen capacity](../../02-functional/f10-point-of-sale/business-rules/br-f10-23-online-orders-stay-within-kitchen-capacity.md)
  to
  [BR-F10-26 Layaway deposits are refunded per the shop's terms](../../02-functional/f10-point-of-sale/business-rules/br-f10-26-layaway-deposits-are-refunded-per-the-shops-terms.md),
  entities [E-F10-22 Takeaway order](../../02-functional/f10-point-of-sale/data/e-f10-22-takeaway-order.md),
  [E-F10-23 Shelf label](../../02-functional/f10-point-of-sale/data/e-f10-23-shelf-label.md) and
  [E-F10-24 Layaway](../../02-functional/f10-point-of-sale/data/e-f10-24-layaway.md) and their lists
  [S-F10-L22 Takeaway orders](../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l22-takeaway-orders.md) to
  [S-F10-L24 Layaways](../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l24-layaways.md).
- Tap to pay has no entity of its own: its payments are till payments and till log lines.
- The card-terminal rules for a phone and the consumer rules on deposits each need a France pack rule,
  written later.

## Related

- [FL-F10-12 Takeaway, tap to pay, labels and layaway](../../02-functional/f10-point-of-sale/flows/fl-f10-12-takeaway-softpos-and-labels.md)
- [D458 F1 Administration: gaps and improvements](../f01-administration/d458-f01-gaps-and-improvements.md)
- Interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)

---

⬅️ [D528 Benchmark gaps of F9 HR and projects](../f09-hr-and-projects/d528-benchmark-gaps-f09-hr-and-projects.md) ·
⬆️ [Up](README.md) ·
➡️ [D530 Benchmark gaps of F11 Online shop](../f11-online-shop/d530-benchmark-gaps-f11-online-shop.md)
