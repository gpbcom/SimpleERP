🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-17 CESU vouchers are reconciled with the issuer

# 📏 BR-SC04-17 CESU vouchers are reconciled with the issuer

**Status:** ✅ specified

## Statement

Vouchers are reconciled with the issuer batch by batch and voucher by voucher: each payment received is matched to the
vouchers it pays, and a difference is listed per voucher until every voucher is Reimbursed or Rejected with a reason.

## Why

The provider carries the vouchers as money owed until the issuer pays; an unreconciled difference is lost income. The
owner asked for CESU payments ([D548](../../../06-decisions/sectors/d548-benchmark-gaps-sc04-home-care.md)).
The France-pack rule is listed below.

## Examples

| Case | Result |
|---|---|
| Batch 432.00 EUR, payment 420.00 EUR | one voucher of 12.00 EUR listed as the difference |
| Payment 432.00 EUR | all vouchers Reimbursed |
| Voucher rejected as expired | Rejected with its reason |
| Voucher sent twice | the second is refused as already sent |

## Applies to

- [UC-SC04-17](../use-cases/06-care-homes-cesu-and-nursing/uc-sc04-17-accept-cesu-vouchers.md)
- [E-SC04-15 CESU voucher](../data/e-sc04-15-cesu-voucher.md)
- [E-SC04-08 Care invoice](../data/e-sc04-08-care-invoice.md)
- France-pack rule:
  [CR-FR-230 CESU vouchers](../../../10-country-packs/france/home-care/cr-fr-230-cesu-vouchers.md)

## Exceptions

None.

## Configurable

The days before the issuer's limit date at which a batch is warned (10 by default), by the coordinator.

## Open questions

None.

---

⬅️ [BR-SC04-16](br-sc04-16-residents-care-records-follow-health-data-rules.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC04-18 In agent mode the family is the employer](br-sc04-18-in-agent-mode-the-family-is-the-employer.md)
