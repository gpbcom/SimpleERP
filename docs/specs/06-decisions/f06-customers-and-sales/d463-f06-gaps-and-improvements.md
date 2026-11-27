🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛒 [Decisions: F6 Customers and sales](README.md) ›
📜 D463 F6 Customers and sales: gaps and improvements

# 📜 D463 F6 Customers and sales: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F6 and the sectors that rely on it.

## Options

- **Credit limits and credit hold.** Absent from F6; only SC15 UC-16 specifies them (20 mentions). Standard in Odoo and
  ERPNext. Serves U05, SC15, SC07, SC01.
- **Commissions and sales targets.** Absent in F6 and F13. SC15 reps, SC14 resellers, SC02 staff targets and SC11 profit
  shares each re-invent them.
- **Multi-payer invoicing with caps.** Funder plus beneficiary: SC04 (APA/PCH), SC09 (third-party payment), SC12
  (OPCO/employer), SC08 grants. Ximi scores ✅ on E04.
- **Public buyers and Chorus Pro.** No mention in F6; only SC01 and F8 cite them, though SC04, SC12 and SC16 also bill
  public bodies.
- **Account hierarchy, activity timeline and email on the customer record.** Hierarchy, timeline and inbox are absent.
  Serves SC15 (chains), SC14.
- **Offline order taking on the road.** "Offline" is absent in F6. Serves SC15 UC-05, SC13.
- **Confirm the waiting proposals.** 30 items are still proposed: UC-F6-01 to 12 and all entities and screens.
- **More flows.** Only 5 flows for 16 use cases; fl-f06-04 subscriptions has 180 words; UC-F6-11 portal has 3 steps.
- **Instalment plans and disputed-invoice status.** A dispute should pause dunning (UC-F6-08).
- **Pro-forma invoices and periodic statement of account.** Both absent.
- **More reports.** Sales and margin per rep, territory and product (today: pipeline, win rate, DSO, aged balance, MRR).

## Choice

Confirmed by the owner on 2026-11-12:

- F6 Customers and sales: gaps: All four: credit limits and hold; public buyers and Chorus Pro; account hierarchy,
  timeline and emails; offline order taking
- F6 Customers and sales: improvements: All four: more and deeper flows; instalments and disputes; pro-forma and
  statements; sales reports
- F6 Customers and sales: proposals: "Confirm all of F6"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F6.
- F6's waiting proposals are confirmed (D457).

## Related

- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md)

---

⬅️ [D462 F5 Social media and marketing: gaps and improvements](../f05-social-media/d462-f05-gaps-and-improvements.md) ·
⬆️ [Up](README.md) · ➡️ [D464](../f07-purchasing-and-stock/d464-f07-gaps-and-improvements.md)
