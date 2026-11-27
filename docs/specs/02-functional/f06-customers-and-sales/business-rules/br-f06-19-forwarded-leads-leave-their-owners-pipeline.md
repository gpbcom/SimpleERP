🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-19 Forwarded leads leave their owner's pipeline

# 📏 BR-F6-19 Forwarded leads leave their owner's pipeline

**Status:** ✅ specified

## Statement

A lead forwarded to a partner leaves its previous owner's pipeline and forecast at the moment it is forwarded and
belongs to the partner; it returns to the previous owner when the partner does not act within its tier's time or is
suspended; a lead has one owner at a time.

## Why

Two owners for one lead double the forecast and make the commission unclear. The owner asked for a partner programme for
any company ([D525](../../../06-decisions/f06-customers-and-sales/d525-benchmark-gaps-f06-customers-and-sales.md));
[BR-F6-18 Commissions follow paid invoices](br-f06-18-commissions-follow-paid-invoices.md) pays commissions only on paid
invoices.

## Examples

| Case | Result |
|---|---|
| A lead forwarded to Nord Distribution | it leaves Julien R.'s pipeline at once |
| No activity for 14 days, tier Gold | the lead returns to Julien R. |
| A lead already forwarded to another partner | the second forward is refused |
| A suspended partner with 5 open leads | the 5 return to their previous owners |
| A deal registered by two partners | the first registered keeps it for the protection period |

## Applies to

- [UC-F6-27](../use-cases/10-partners-contracts-and-warranties/uc-f06-27-run-a-partner-programme.md)
- [E-F6-23 Partner](../data/e-f06-23-partner.md)
- [E-F6-20 Lead](../data/e-f06-20-lead.md)
- [E-F6-02 Opportunity](../data/e-f06-02-opportunity.md)
- [E-F6-19 Commission line](../data/e-f06-19-commission-line.md)

## Exceptions

None.

## Configurable

Yes: the time before a lead returns and the protection period, per tier, by sales (defaults: 14 and 90 days).

## Open questions

None.

---

⬅️ [BR-F6-18 Commissions follow paid invoices](br-f06-18-commissions-follow-paid-invoices.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-20 Identifiers are checked per scheme](br-f06-20-identifiers-are-checked-per-scheme.md)
