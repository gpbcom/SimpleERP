🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-29 Audit exports carry the checksum chain

# 📏 BR-F1-29 Audit exports carry the checksum chain

**Status:** ✅ specified

## Statement

Every audit export and SIEM event carries its checksum and the previous one's, so that a missing or changed event shows.

## Why

An auditor or a SIEM must be able to prove the trail was not altered.

## Examples

| Case | Result |
|---|---|
| Export of 3 events | 3 events with their checksums |
| One event changed in the export file | The chain breaks at that event |

## Applies to

- [UC-F1-22 Search the audit trail and export it to a SIEM](../use-cases/13-security-and-audit/uc-f01-22-search-the-audit-trail-and-export-it-to-a-siem.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-28](br-f01-28-security-policies-never-lock-out-every-administrator.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-30](br-f01-30-a-closed-company-keeps-only-what-the-law-requires.md)
