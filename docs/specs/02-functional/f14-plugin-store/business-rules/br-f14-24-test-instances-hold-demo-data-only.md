🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-24 Test instances hold demo data only

# 📏 BR-F14-24 Test instances hold demo data only

**Status:** 🔄 waiting for the owner

## Statement

A test instance holds demo data only: it is created from a sector example company, and any import or connection that
would bring real people's or real companies' data into it is refused.

## Why

A publisher is outside the company and must never see a customer's records, and a test environment is not a place for
personal data ([CR-FR-050](../../../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md)). The owner
asked for publisher test instances
([D533](../../../06-decisions/f14-plugin-store/d533-benchmark-gaps-f14-plugin-store.md)).

## Examples

| Case | Result |
|---|---|
| A new instance from the services example | created with invented people only |
| A CSV of real customers imported | refused |
| A connection to a real bank | refused |
| A plugin's own generated test data | allowed, it holds no real person |
| An instance past its end date | removed with its data |

## Applies to

- [UC-F14-29](../use-cases/08-trials-instances-and-partners/uc-f14-29-get-a-publisher-test-instance.md)
- [E-F14-22 Test instance](../data/e-f14-22-test-instance.md)
- [E-F14-01 Store listing](../data/e-f14-01-store-listing.md)

## Exceptions

None.

## Configurable

The limit of running instances and the duration, by the SimpleERP maintainer team.

## Open questions

None.

---

⬅️ [BR-F14-23](br-f14-23-rollback-restores-the-previous-version-and-data.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-25](br-f14-25-a-trial-ends-with-a-purchase-or-a-clean-uninstall.md)
