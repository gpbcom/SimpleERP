🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-04 No-show fees follow the published terms

# 📏 BR-SC17-04 No-show fees follow the published terms

**Status:** ✅ specified

## Statement

A no-show fee or a kept deposit is allowed only if the deposit and cancellation terms were shown and accepted by the
customer before the booking was confirmed, and the customer cancelled later than the free cancellation time or did not
come. A visit cancelled by the salon always refunds the deposit.

## Why

Charging a fee the customer was never told about is unfair and can be refused by the customer's bank. The owner asked
for deposits and no-show fees ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).
The consumer rules come from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| Cancel 30 hours before, free until 24 hours | deposit refunded |
| Cancel 3 hours before | deposit kept |
| Salon cancels | deposit refunded in full |
| Terms not shown at booking | the fee is blocked |
| Manager waives the fee | deposit refunded, reason recorded |

## Applies to

- [UC-SC17-04](../use-cases/01-book-staff-and-cabins/uc-sc17-04-take-deposits-and-charge-no-shows.md)
- [E-SC17-03 Booking deposit](../data/e-sc17-03-booking-deposit.md)
- [E-SC17-02 Salon booking](../data/e-sc17-02-salon-booking.md)

## Exceptions

A customer who could not come for a documented reason (illness) may have the fee waived by the manager.

## Configurable

The services that need a deposit, the amount, the free cancellation time and the fee, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-03 Desk bookings send the same confirmation](br-sc17-03-desk-bookings-send-the-same-confirmation.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC17-05 Sessions are used oldest first](br-sc17-05-sessions-are-used-oldest-first.md)
