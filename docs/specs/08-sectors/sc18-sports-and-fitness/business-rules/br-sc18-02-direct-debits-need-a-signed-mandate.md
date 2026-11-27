🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-02 Direct debits need a signed mandate

# 📏 BR-SC18-02 Direct debits need a signed mandate

**Status:** ✅ specified

## Statement

A direct debit is sent only for a member whose mandate is signed and Active on the debit date; a due with no active
mandate is left out of the file, and the member is told the amount and the date before each debit.

## Why

A debit without a signed mandate is refused by the bank and may be refunded to the member. The owner asked for clubs and
gyms ([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)). The formats are those of
[CR-FR-023](../../../10-country-packs/france/payments/cr-fr-023-sepa-formats.md); the advance delay is a value of the
France pack, written later.

## Examples

| Case | Result |
|---|---|
| Active mandate | the due is in the file |
| No mandate | left out and the member is contacted |
| Revoked mandate | no debit |
| Rejected debit | Unpaid, retried once |
| Change of bank | the old mandate is Revoked and the new one Active |

## Applies to

- [UC-SC18-02](../use-cases/01-memberships-and-access/uc-sc18-02-collect-dues-by-direct-debit.md)
- [E-SC18-02 Dues mandate](../data/e-sc18-02-dues-mandate.md)
- [E-SC18-02 Dues mandate](../data/e-sc18-02-dues-mandate.md)

## Exceptions

None.

## Configurable

The collection day, the advance notice and the number of retries, by the treasurer.

## Open questions

None.

---

⬅️ [BR-SC18-01 Contracts state the cancellation terms](br-sc18-01-contracts-state-the-cancellation-terms.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC18-03 Access needs a valid membership](br-sc18-03-access-needs-a-valid-membership.md)
