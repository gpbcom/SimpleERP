🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-16 An instalment plan replaces the due date

# 📏 BR-F6-16 An instalment plan replaces the due date

**Status:** ✅ specified

## Statement

An accepted instalment plan sums to the balance it covers; reminders follow its dates; a missed instalment resumes
reminders on the whole remaining balance after the grace days.

## Why

Customers keep their word; the company keeps track.

## Examples

| Case | Result |
|---|---|
| 3 x 1,400 EUR for 4,200 EUR | Accepted |
| Missed, 7 days pass | Reminders resume |

## Applies to

- [UC-F6-23 Agree an instalment plan](../use-cases/08-collect-and-settle/uc-f06-23-agree-an-instalment-plan.md)

## Exceptions

None.

## Configurable

Grace days (default: 7).

## Open questions

None.

---

⬅️ [BR-F6-15 A pro-forma is not an invoice](br-f06-15-a-pro-forma-is-not-an-invoice.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-17](br-f06-17-a-dispute-pauses-reminders-on-what-is-disputed.md)
