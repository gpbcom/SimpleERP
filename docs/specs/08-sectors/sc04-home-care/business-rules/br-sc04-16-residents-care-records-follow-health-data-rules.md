🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-16 Residents' care records follow health-data rules

# 📏 BR-SC04-16 Residents' care records follow health-data rules

**Status:** 🔄 waiting for the owner

## Statement

A resident's care record is health data: it is hosted by an approved health-data host, readable only by the carers of
that resident and the coordinator, and every reading is logged with who and why. A relative reads only what the resident
or their representative shares.

## Why

A care record tells the most private facts about a person; a leak harms the resident and exposes the home. The owner
asked for community care ([D548](../../../06-decisions/sectors/d548-benchmark-gaps-sc04-home-care.md)). The
care-home contract rule is written later.

## Examples

| Case | Result |
|---|---|
| Carer of room 12 reads the record of room 12 | allowed and logged |
| Carer of another floor reads it | refused and logged |
| A son asks for the record | he sees only what his father shares |
| Coordinator exports the record for the doctor | allowed, logged, with the reason |

## Applies to

- [UC-SC04-16](../use-cases/06-care-homes-cesu-and-nursing/uc-sc04-16-run-a-care-home.md)
- [E-SC04-14 Resident](../data/e-sc04-14-resident.md)
- [E-SC04-06 Care log entry](../data/e-sc04-06-care-log-entry.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-256 Care-home resident contract](../../../10-country-packs/france/home-care/cr-fr-256-care-home-resident-contract.md)

## Exceptions

Emergency access by the on-call carer, logged and reviewed the next day.

## Configurable

The roles that read care records, by the coordinator within the sector pack.

## Open questions

None.

---

⬅️ [BR-SC04-15 Records kept no longer than needed](br-sc04-15-records-kept-no-longer-than-needed.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC04-17](br-sc04-17-cesu-vouchers-are-reconciled-with-the-issuer.md)
