🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-07 Vouchers keep their legal validity period

# 📏 BR-SC17-07 Vouchers keep their legal validity period

**Status:** ✅ specified

## Statement

A voucher keeps the validity period the law sets: the salon cannot set a shorter period, cannot refuse a voucher while
it is valid, and extends it only with a recorded reason. A voucher past its end date is Expired and no longer accepted.

## Why

A voucher that expires too early or is refused while valid is a consumer complaint. The owner asked for gift vouchers
([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)). The minimum validity
is a value of the France pack, written later.

## Examples

| Case | Result |
|---|---|
| Voucher sold 2026-11-21 with a legal validity of one year | valid to 2027-11-21 at least |
| Validity set to six months | refused by the screen |
| Voucher offered the day after its end date | refused |
| Manager extends with a reason | accepted and recorded |
| Partial use of 32 on 50 | balance 18 |

## Applies to

- [UC-SC17-07](../use-cases/02-packages-and-memberships/uc-sc17-07-sell-and-redeem-gift-vouchers.md)
- [E-SC17-06 Gift voucher](../data/e-sc17-06-gift-voucher.md)
- [E-SC17-06 Gift voucher](../data/e-sc17-06-gift-voucher.md)

## Exceptions

None.

## Configurable

The validity above the legal minimum and the kinds of voucher, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-06 Membership dues stop at cancellation](br-sc17-06-membership-dues-stop-at-cancellation.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC17-08 Balances are shown before each sale](br-sc17-08-balances-are-shown-before-each-sale.md)
