🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) ›
🧾 TC-05 Records that must never change, and those that must be erased

# 🧾 TC-05 Records that must never change, and those that must be erased

**Status:** ✅ listed for the technical interviews

## Challenge

Keep posted entries, invoices, till data and the audit trail inalterable and continuously numbered for years, send
invoices through approved platforms, and still erase personal data when the law asks.

## Raised by

- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md)
- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md)
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md)
- [T3 Audit trail](../t03-audit-trail/README.md)

## Why it is hard

- Till software must be inalterable, secured, kept and archived, with closures (country pack, point of sale rules).
- Accounting records are kept ten years; personal data must be erased when no longer needed.
- Numbering must stay continuous across offline tills, several sites and restores from backup.

## Already decided

- [D293](../../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md) Capabilities take legal
  rules from the country pack

## Options to weigh

- Hash chains or signed journals per company and per till.
- Separating legal records from personal data so that erasure leaves the books whole.
- Archive formats and where the legal archive lives.

## Settled in

- 19c Storage ([chapter](../../../technical/data/storage.md))
- 19f Security ([chapter](../../../technical/security/security.md))
- 19k Backups, recovery and upgrades ([chapter](../../../technical/operations/operations.md))
- Then the technical capabilities: [T3 Audit trail](../t03-audit-trail/README.md).

## Questions for the interview

- Is a till certification (NF525 or the publisher's attestation) in the first version's scope for every install?
- How is continuity proved after a restore?

---

⬅️ [TC-04 The country pack as a versioned rule engine](tc-04-country-pack-rule-engine.md) · ⬆️ [Up](README.md) ·
➡️ [TC-06 Offline devices and synchronisation](tc-06-offline-devices-and-sync.md)
