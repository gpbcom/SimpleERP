🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › ⚖️ [SC11 Professional firms](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC11-17 Brokers keep their ORIAS registration current

# 📏 BR-SC11-17 Brokers keep their ORIAS registration current

**Status:** 🔄 waiting for the owner

## Statement

A policy is placed only while the brokerage's registration, its professional-liability insurance and its financial
guarantee are current on the day. The registration status is checked at each placement, and the manager is warned before
it ends.

## Why

Placing policies without a valid registration is an offence and leaves clients unprotected. The owner asked for
insurance brokers ([D555](../../../06-decisions/sectors/d555-benchmark-gaps-sc11-professional-firms.md)). The
France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Registration valid until 2027-02-28, policy placed 2026-11-14 | placed |
| Registration ended on 2026-10-31 | refused |
| Liability insurance proof expired | refused |
| Registration ends in 40 days | placed, manager warned |
| Renewal of the registration filed | the new end date is recorded |

## Applies to

- [UC-SC11-22](../use-cases/07-notaries-brokers-officers-and-auditors/uc-sc11-22-run-an-insurance-brokerage.md)
- [E-SC11-17 Policy](../data/e-sc11-17-policy.md)
- [E-SC11-01 Client identity](../data/e-sc11-01-client-identity.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-242 Insurance brokers and ORIAS](../../../10-country-packs/france/professional-firms/cr-fr-242-insurance-brokers-orias.md)

## Exceptions

None.

## Configurable

The warning delay before the registration ends (60 days by default), by the manager.

## Open questions

None.

---

⬅️ [BR-SC11-16](br-sc11-16-client-funds-are-held-at-the-state-deposit-bank.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC11-18 Fees follow the regulated tariff](br-sc11-18-fees-follow-the-regulated-tariff.md)
